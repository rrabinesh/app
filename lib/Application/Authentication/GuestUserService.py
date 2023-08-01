# <?php

# interface IGuestUserService
# {
#     /**
#      * @param string $email
#      * @return UserSession
#      */
#     public function CreateOrLoad($email);

#     /**
#      * @param $email
#      * @return bool
#      */
#     public function EmailExists($email);
# }

# class GuestUserService implements IGuestUserService
# {
#     /**
#      * @var IAuthentication
#      */
#     private $authentication;

#     /**
#      * @var IRegistration
#      */
#     private $registration;

#     public function __construct(IAuthentication $authentication, IRegistration $registration)
#     {
#         $this->authentication = $authentication;
#         $this->registration = $registration;
#     }

#     public function CreateOrLoad($email)
#     {
#         $user = $this->authentication->Login($email, new WebLoginContext(new LoginData()));
#         if ($user->IsLoggedIn()) {
#             Log::Debug('User already has account, skipping guest creation %s', $email);

#             return $user;
#         }

#         Log::Debug('Email address was not found, creating guest account %s', $email);

#         $currentLanguage = Resources::GetInstance()->CurrentLanguage;
#         $this->registration->Register($email, $email, 'Guest', 'Guest', Password::GenerateRandom(), null, $currentLanguage, null);
#         return $this->authentication->Login($email, new WebLoginContext(new LoginData(false, $currentLanguage)));
#     }

#     public function EmailExists($email)
#     {
#         $user = $this->authentication->Login($email, new WebLoginContext(new LoginData()));
#         return $user->IsLoggedIn();
#     }
# }

from fastapi import Depends

from authentication import AuthenticationService, LoginContext, LoginData
from registration import RegistrationService

class GuestUserService:

    def __init__(
        self, 
        auth_service: AuthenticationService = Depends(),
        registration_service: RegistrationService = Depends(),
    ):
        self.auth = auth_service
        self.registration = registration_service

    async def create_or_load(self, email: str):
        user = await self.auth.login(email, LoginContext(), LoginData())
        if user.is_logged_in:
            print(f"User {email} already exists, skipping creation")
            return user

        print(f"Creating new guest user {email}")        
        await self.registration.register(
            email=email,
            first_name="Guest",
            last_name="Guest",
            password=generate_password(), 
            language=get_current_language()
        )

        return await self.auth.login(email, LoginContext(), LoginData())

    async def email_exists(self, email: str) -> bool:
        user = await self.auth.login(email, LoginContext(), LoginData())
        return user.is_logged_in

