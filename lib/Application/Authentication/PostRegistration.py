# <?php

# require_once(ROOT_DIR . 'lib/Application/Authentication/namespace.php');

# class PostRegistration implements IPostRegistration
# {
#     /**
#      * @var IWebAuthentication
#      */
#     protected $authentication;

#     /**
#      * @var IAccountActivation
#      */
#     protected $activation;

#     public function __construct(IWebAuthentication $authentication, IAccountActivation $activation)
#     {
#         $this->authentication = $authentication;
#         $this->activation = $activation;
#     }

#     public function HandleSelfRegistration(User $user, IRegistrationPage $page, ILoginContext $loginContext)
#     {
#         if ($user->StatusId() == AccountStatus::ACTIVE) {
#             Log::Debug('PostRegistration - Handling activate user %s', $user->EmailAddress());
#             $this->authentication->Login($user->EmailAddress(), $loginContext);
#             $page->Redirect(Pages::UrlFromId($user->Homepage()));
#         } else {
#             Log::Debug('PostRegistration - Handling pending user %s', $user->EmailAddress());
#             $this->activation->Notify($user);
#             $page->Redirect(Pages::ACTIVATION);
#         }
#     }
# }


# User class (Assuming you have a User class)

class User:
    def __init__(self, email_address: str, status_id: int, homepage: int):
        self.email_address = email_address
        self.status_id = status_id
        self.homepage = homepage

    def email_address(self) -> str:
        return self.email_address

    def status_id(self) -> int:
        return self.status_id

    def homepage(self) -> int:
        return self.homepage


# AccountStatus class (Assuming you have an AccountStatus class with static properties)

class AccountStatus:
    ACTIVE = 1
    PENDING = 2


# IWebAuthentication interface (Using abstract class)
from abc import ABC, abstractmethod

class IWebAuthentication(ABC):
    @abstractmethod
    def login(self, username: str, login_context: ILoginContext) -> None:
        pass


# IAccountActivation interface (Using abstract class)

class IAccountActivation(ABC):
    @abstractmethod
    def notify(self, user: User) -> None:
        pass


# IRegistrationPage interface (Using abstract class)

class IRegistrationPage(ABC):
    @abstractmethod
    def redirect(self, url: str) -> None:
        pass


# ILoginContext interface (Using abstract class)

class ILoginContext(ABC):
    @abstractmethod
    def get_data(self) -> LoginData:
        pass


# Pages class (Assuming you have a Pages class with static methods)

class Pages:
    @staticmethod
    def url_from_id(page_id: int) -> str:
        # Replace this with the actual implementation to get URL from the page_id
        return f"/page/{page_id}"


# PostRegistration class (Implementation of IPostRegistration interface)
class PostRegistration:
    def __init__(self, authentication: IWebAuthentication, activation: IAccountActivation):
        self.authentication = authentication
        self.activation = activation

    def handle_self_registration(self, user: User, page: IRegistrationPage, login_context: ILoginContext) -> None:
        if user.status_id() == AccountStatus.ACTIVE:
            print(f"PostRegistration - Handling activate user {user.email_address()}")
            self.authentication.login(user.email_address(), login_context)
            page.redirect(Pages.url_from_id(user.homepage()))
        else:
            print(f"PostRegistration - Handling pending user {user.email_address()}")
            self.activation.notify(user)
            page.redirect(Pages.url_from_id(Pages.ACTIVATION))


# LoginData class (Assuming you have a LoginData class)
class LoginData:
    pass

