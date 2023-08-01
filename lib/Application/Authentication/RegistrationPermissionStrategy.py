# <?php

# class RegistrationPermissionStrategy implements IRegistrationPermissionStrategy
# {
#     public function AddAccount(User $user)
#     {
#         $autoAssignCommand = new AutoAssignPermissionsCommand($user->Id());
#         ServiceLocator::GetDatabase()->Execute($autoAssignCommand);
#     }
# }

# class GuestReservationPermissionStrategy implements IRegistrationPermissionStrategy
# {
#     /**
#      * @var IRequestedResourcePage
#      */
#     private $page;

#     public function __construct(IRequestedResourcePage $page)
#     {
#         $this->page = $page;
#     }

#     public function AddAccount(User $user)
#     {
#         $autoAssignCommand = new AutoAssignGuestPermissionsCommand($user->Id(), $this->page->GetRequestedScheduleId());
#         ServiceLocator::GetDatabase()->Execute($autoAssignCommand);
#     }
# }


# User class (Assuming you have a User class)
class User:
    def __init__(self, user_id):
        self.user_id = user_id


# ServiceLocator class (Assuming you have a ServiceLocator class with GetDatabase method)
class ServiceLocator:
    @staticmethod
    def get_database():
        # Replace this with the actual implementation to get the Database instance
        return Database()


# Database class (Assuming you have a Database class with Execute method)
class Database:
    def execute(self, command):
        # Replace this with the actual implementation to execute the given command
        pass


# AutoAssignPermissionsCommand class (Assuming you have an AutoAssignPermissionsCommand class)
class AutoAssignPermissionsCommand:
    def __init__(self, user_id):
        self.user_id = user_id


# AutoAssignGuestPermissionsCommand class (Assuming you have an AutoAssignGuestPermissionsCommand class)
class AutoAssignGuestPermissionsCommand:
    def __init__(self, user_id, schedule_id):
        self.user_id = user_id
        self.schedule_id = schedule_id


# IRequestedResourcePage class (Assuming you have an IRequestedResourcePage class)
class IRequestedResourcePage:
    def get_requested_schedule_id(self):
        # Replace this with the actual implementation to get the requested schedule ID
        return 123  # Replace with the actual schedule ID


# RegistrationPermissionStrategy class (Implementation of IRegistrationPermissionStrategy interface)
class RegistrationPermissionStrategy:
    def add_account(self, user):
        auto_assign_command = AutoAssignPermissionsCommand(user.user_id)
        ServiceLocator.get_database().execute(auto_assign_command)


# GuestReservationPermissionStrategy class (Implementation of IRegistrationPermissionStrategy interface)
class GuestReservationPermissionStrategy:
    def __init__(self, page):
        self.page = page

    def add_account(self, user):
        auto_assign_command = AutoAssignGuestPermissionsCommand(user.user_id, self.page.get_requested_schedule_id())
        ServiceLocator.get_database().execute(auto_assign_command)


