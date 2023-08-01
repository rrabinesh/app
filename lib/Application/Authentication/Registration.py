# <?php

# require_once(ROOT_DIR . 'Domain/namespace.php');
# require_once(ROOT_DIR . 'Domain/Access/namespace.php');
# require_once(ROOT_DIR . 'lib/Application/Reservation/ReservationEvents.php');

# class Registration implements IRegistration
# {
#     /**
#      * @var PasswordEncryption
#      */
#     private $passwordEncryption;

#     /**
#      * @var IUserRepository
#      */
#     private $userRepository;

#     /**
#      * @var IRegistrationNotificationStrategy
#      */
#     private $notificationStrategy;

#     /**
#      * @var IRegistrationPermissionStrategy
#      */
#     private $permissionAssignmentStrategy;

#     /**
#      * @var IGroupViewRepository
#      */
#     private $groupRepository;

#     public function __construct(
#         $passwordEncryption = null,
#         $userRepository = null,
#         $notificationStrategy = null,
#         $permissionAssignmentStrategy = null,
#         $groupRepository = null
#     ) {
#         $this->passwordEncryption = $passwordEncryption;
#         $this->userRepository = $userRepository;
#         $this->notificationStrategy = $notificationStrategy;
#         $this->permissionAssignmentStrategy = $permissionAssignmentStrategy;
#         $this->groupRepository = $groupRepository;

#         if ($passwordEncryption == null) {
#             $this->passwordEncryption = new PasswordEncryption();
#         }

#         if ($userRepository == null) {
#             $this->userRepository = new UserRepository();
#         }

#         if ($notificationStrategy == null) {
#             $this->notificationStrategy = new RegistrationNotificationStrategy();
#         }

#         if ($permissionAssignmentStrategy == null) {
#             $this->permissionAssignmentStrategy = new RegistrationPermissionStrategy();
#         }

#         if ($groupRepository == null) {
#             $this->groupRepository = new GroupRepository();
#         }
#     }

#     public function Register(
#         $username,
#         $email,
#         $firstName,
#         $lastName,
#         $password,
#         $timezone,
#         $language,
#         $homepageId,
#         $additionalFields = [],
#         $attributeValues = [],
#         $groups = null,
#         $acceptTerms = false
#     ) {
#         $homepageId = empty($homepageId) ? Pages::DEFAULT_HOMEPAGE_ID : $homepageId;
#         $encryptedPassword = $this->passwordEncryption->EncryptPassword($password);
#         $timezone = empty($timezone) ? Configuration::Instance()->GetKey(ConfigKeys::DEFAULT_TIMEZONE) : $timezone;

#         $attributes = new UserAttribute($additionalFields);

#         if ($this->CreatePending()) {
#             $user = User::CreatePending($firstName, $lastName, $email, $username, $language, $timezone, $encryptedPassword->EncryptedPassword(), $encryptedPassword->Salt(), $homepageId);
#         } else {
#             $user = User::Create($firstName, $lastName, $email, $username, $language, $timezone, $encryptedPassword->EncryptedPassword(), $encryptedPassword->Salt(), $homepageId);
#         }

#         $user->ChangeAttributes($attributes->Get(UserAttribute::Phone), $attributes->Get(UserAttribute::Organization), $attributes->Get(UserAttribute::Position));
#         $user->ChangeCustomAttributes($attributeValues);
#         $user->AcceptTerms($acceptTerms);

#         if ($groups != null) {
#             $user->WithGroups($groups);
#         }

#         if (Configuration::Instance()->GetKey(ConfigKeys::REGISTRATION_AUTO_SUBSCRIBE_EMAIL, new BooleanConverter())) {
#             foreach (ReservationEvent::AllEvents() as $event) {
#                 $user->ChangeEmailPreference($event, true);
#             }
#         }

#         $userId = $this->userRepository->Add($user);
#         if ($user->Id() != $userId) {
#             $user->WithId($userId);
#         }
#         $this->permissionAssignmentStrategy->AddAccount($user);
#         $this->notificationStrategy->NotifyAccountCreated($user, $password);

#         return $user;
#     }

#     /**
#      * @return bool
#      */
#     protected function CreatePending()
#     {
#         return Configuration::Instance()->GetKey(ConfigKeys::REGISTRATION_REQUIRE_ACTIVATION, new BooleanConverter());
#     }

#     public function UserExists($loginName, $emailAddress)
#     {
#         $userId = $this->userRepository->UserExists($emailAddress, $loginName);

#         return !empty($userId);
#     }

#     public function Synchronize(AuthenticatedUser $user, $insertOnly = false, $overwritePassword = true)
#     {
#         if ($this->UserExists($user->UserName(), $user->Email())) {
#             if ($insertOnly) {
#                 return;
#             }

#             $password = null;
#             $salt = null;

#             if ($overwritePassword) {
#                 $encryptedPassword = $this->passwordEncryption->EncryptPassword($user->Password());
#                 $password = $encryptedPassword->EncryptedPassword();
#                 $salt = $encryptedPassword->Salt();
#             }

#             $command = new UpdateUserFromLdapCommand($user->UserName(), $user->Email(), $user->FirstName(), $user->LastName(), $password, $salt, $user->Phone(), $user->Organization(), $user->Title());
#             ServiceLocator::GetDatabase()->Execute($command);

#             if ($this->GetUserGroups($user) != null) {
#                 $updatedUser = $this->userRepository->LoadByUsername($user->Username());
#                 $updatedUser->ChangeGroups($this->GetUserGroups($user));
#                 $this->userRepository->Update($updatedUser);
#             }
#         } else {
#             $defaultHomePageId = Configuration::Instance()->GetKey(ConfigKeys::DEFAULT_HOMEPAGE, new IntConverter());
#             $additionalFields = ['phone' => $user->Phone(), 'organization' => $user->Organization(), 'position' => $user->Title()];
#             $this->Register(
#                 $user->UserName(),
#                 $user->Email(),
#                 $user->FirstName(),
#                 $user->LastName(),
#                 $user->Password(),
#                 $user->TimezoneName(),
#                 $user->LanguageCode(),
#                 empty($defaultHomePageId) ? Pages::DEFAULT_HOMEPAGE_ID : $defaultHomePageId,
#                 $additionalFields,
#                 [],
#                 $this->GetUserGroups($user)
#             );
#         }
#     }

#     /**
#      * @param AuthenticatedUser $user
#      * @return null|UserGroup[]
#      */
#     private function GetUserGroups(AuthenticatedUser $user)
#     {
#         $userGroups = $user->GetGroups();

#         if (empty($userGroups)) {
#             return null;
#         }

#         $groupsToSync = [];
#         if ($userGroups != null) {
#             $lowercaseGroups = array_map('strtolower', $userGroups);

#             $groupsToSync = [];
#             $groups = $this->groupRepository->GetList()->Results();
#             /** @var GroupItemView $group */
#             foreach ($groups as $group) {
#                 if (in_array(strtolower($group->Name()), $lowercaseGroups)) {
#                     Log::Debug('Syncing group %s for user %s', $group->Name(), $user->Username());
#                     $groupsToSync[] = new UserGroup($group->Id(), $group->Name());
#                 } else {
#                     Log::Debug('User %s is not part of group %s, sync skipped', $group->Name(), $user->Username());
#                 }
#             }
#         }

#         return $groupsToSync;
#     }
# }

# class AdminRegistration extends Registration
# {
#     protected function CreatePending()
#     {
#         return false;
#     }
# }

# class GuestRegistration extends Registration
# {
#     protected function CreatePending()
#     {
#         return false;
#     }
# }

# User class (Assuming you have a User class)

class User:
    def __init__(self, first_name: str, last_name: str, email: str, username: str, language: str,
                 timezone: str, encrypted_password: str, salt: str, homepage_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.language = language
        self.timezone = timezone
        self.encrypted_password = encrypted_password
        self.salt = salt
        self.homepage_id = homepage_id
        self.attributes = {}
        self.custom_attributes = {}
        self.groups = []
        self.terms_accepted = False

    def add_attribute(self, attribute_type: str, value: str) -> None:
        self.attributes[attribute_type] = value

    def add_custom_attribute(self, attribute_name: str, value: str) -> None:
        self.custom_attributes[attribute_name] = value

    def with_groups(self, groups: List[str]) -> None:
        self.groups = groups

    def accept_terms(self, accepted: bool) -> None:
        self.terms_accepted = accepted


# PasswordEncryption class (Assuming you have a PasswordEncryption class with encrypt_password method)
# Replace this with your actual encryption implementation
class PasswordEncryption:
    def encrypt_password(self, password: str) -> Dict[str, str]:
        # Replace this with your actual encryption implementation
        encrypted_password = "encrypted_password"  # Replace with the encrypted password
        salt = "salt"  # Replace with the salt
        return {"encrypted_password": encrypted_password, "salt": salt}


# Pages class (Assuming you have a Pages class with static methods)
class Pages:
    DEFAULT_HOMEPAGE_ID = 1

    @staticmethod
    def url_from_id(page_id: int) -> str:
        # Replace this with the actual implementation to get URL from the page_id
        return f"/page/{page_id}"


# UserRepository class (Assuming you have a UserRepository class with add and user_exists methods)
# Replace this with your actual user repository implementation
class UserRepository:
    def add(self, user: User) -> int:
        # Replace this with the actual implementation to add a user to the repository and return the user ID
        return 123

    def user_exists(self, email: str, username: str) -> bool:
        # Replace this with the actual implementation to check if a user exists based on email and username
        return False


# GroupRepository class (Assuming you have a GroupRepository class with get_list method)
# Replace this with your actual group repository implementation
class GroupRepository:
    def get_list(self):
        # Replace this with the actual implementation to get a list of groups
        return []


# IRegistration interface (Using abstract class)
from abc import ABC, abstractmethod

class IRegistration(ABC):
    @abstractmethod
    def register(self, username, email, first_name, last_name, password, timezone, language, homepage_id,
                 additional_fields=None, attribute_values=None, groups=None, accept_terms=False) -> User:
        pass

    @abstractmethod
    def user_exists(self, login_name, email_address) -> bool:
        pass

    @abstractmethod
    def synchronize(self, user, insert_only=False, overwrite_password=True) -> None:
        pass


# Registration class (Implementation of IRegistration interface)
class Registration(IRegistration):
    def __init__(
        self,
        password_encryption: PasswordEncryption = None,
        user_repository: UserRepository = None,
        notification_strategy: "RegistrationNotificationStrategy" = None,
        permission_assignment_strategy: "RegistrationPermissionStrategy" = None,
        group_repository: GroupRepository = None
    ):
        self.password_encryption = password_encryption or PasswordEncryption()
        self.user_repository = user_repository or UserRepository()
        self.notification_strategy = notification_strategy or RegistrationNotificationStrategy()
        self.permission_assignment_strategy = permission_assignment_strategy or RegistrationPermissionStrategy()
        self.group_repository = group_repository or GroupRepository()

    def register(
        self,
        username,
        email,
        first_name,
        last_name,
        password,
        timezone,
        language,
        homepage_id,
        additional_fields=None,
        attribute_values=None,
        groups=None,
        accept_terms=False
    ) -> User:
        homepage_id = homepage_id or Pages.DEFAULT_HOMEPAGE_ID
        encrypted_password = self.password_encryption.encrypt_password(password)
        timezone = timezone or "UTC"

        user = User(first_name, last_name, email, username, language, timezone,
                    encrypted_password["encrypted_password"], encrypted_password["salt"], homepage_id)

        if self.create_pending():
            user.status_id = AccountStatus.PENDING
        else:
            user.status_id = AccountStatus.ACTIVE

        if additional_fields:
            for attribute_type, value in additional_fields.items():
                user.add_attribute(attribute_type, value)

        if attribute_values:
            for attribute_name, value in attribute_values.items():
                user.add_custom_attribute(attribute_name, value)

        user.accept_terms(accept_terms)

        if groups:
            user.with_groups(groups)

        # Code to add user to database/repository and other operations
        # Replace the following code with your actual implementation

        user_id = self.user_repository.add(user)
        user.id = user_id

        if groups:
            self.permission_assignment_strategy.add_account(user)

        self.notification_strategy.notify_account_created(user, password)

        return user

    def create_pending(self):
        # Replace this with your actual implementation for checking registration settings
        return False

    def user_exists(self, login_name, email_address):
        return self.user_repository.user_exists(email_address, login_name)

    def synchronize(self, user, insert_only=False, overwrite_password=True):
        # Replace this with your actual implementation for user synchronization
        pass


# AccountStatus class (Assuming you have an AccountStatus class with static properties)
class AccountStatus:
    ACTIVE = 1
    PENDING = 2


