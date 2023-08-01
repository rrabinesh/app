# <?php

# require_once(ROOT_DIR . 'Domain/Access/UserSessionRepository.php');
# require_once(ROOT_DIR . 'lib/Application/Authentication/namespace.php');

# interface IWebServiceAuthentication
# {
#     /**
#      * @abstract
#      * @param string $username
#      * @param string $password
#      * @return bool If user is valid
#      */
#     public function Validate($username, $password);

#     /**
#      * @abstract
#      * @param string $username
#      * @return WebServiceUserSession
#      */
#     public function Login($username);

#     /**
#      * @param string $publicUserId
#      * @param string $sessionToken
#      * @return void
#      */
#     public function Logout($publicUserId, $sessionToken);
# }

# class WebServiceAuthentication implements IWebServiceAuthentication
# {
#     private $authentication;
#     private $userSessionRepository;

#     /**
#      * @param IAuthentication $authentication
#      * @param IUserSessionRepository $userSessionRepository
#      */
#     public function __construct(IAuthentication $authentication, IUserSessionRepository $userSessionRepository)
#     {
#         $this->authentication = $authentication;
#         $this->userSessionRepository = $userSessionRepository;
#     }

#     /**
#      * @param string $username
#      * @param string $password
#      * @return bool If user is valid
#      */
#     public function Validate($username, $password)
#     {
#         return $this->authentication->Validate($username, $password);
#     }

#     /**
#      * @param string $username
#      * @return WebServiceUserSession
#      */
#     public function Login($username)
#     {
#         Log::Debug('Web Service Login with username: %s', $username);
#         $userSession = $this->authentication->Login($username, new WebServiceLoginContext());
#         if ($userSession->IsLoggedIn()) {
#             $webSession = WebServiceUserSession::FromSession($userSession);
#             $existingSession = $this->userSessionRepository->LoadBySessionToken($webSession->SessionToken);

#             if ($existingSession == null) {
#                 $this->userSessionRepository->Add($webSession);
#             } else {
#                 $this->userSessionRepository->Update($webSession);
#             }

#             return $webSession;
#         }

#         return new NullUserSession();
#     }

#     /**
#      * @param int $userId
#      * @param string $sessionToken
#      * @return void
#      */
#     public function Logout($userId, $sessionToken)
#     {
#         Log::Debug('Logout sessionToken: %s', $sessionToken);

#         $webSession = $this->userSessionRepository->LoadBySessionToken($sessionToken);
#         if ($webSession != null && $webSession->UserId == $userId) {
#             $this->userSessionRepository->Delete($webSession);
#             $this->authentication->Logout($webSession);
#         }
#     }
# }

# class WebServiceLoginContext implements ILoginContext
# {
#     /**
#      * @return LoginData
#      */
#     public function GetData()
#     {
#         return new LoginData(false, null);
#     }
# }


from pydantic import BaseModel
from typing import Optional

# Replace the following class with your actual implementation of WebServiceUserSession
class WebServiceUserSession(BaseModel):
    session_token: str
    user_id: int
    # Add other fields as needed


# IWebServiceAuthentication interface
class IWebServiceAuthentication:
    def Validate(self, username: str, password: str) -> bool:
        ...

    def Login(self, username: str) -> WebServiceUserSession:
        ...

    def Logout(self, user_id: int, session_token: str) -> None:
        ...


# WebServiceAuthentication class
class WebServiceAuthentication(IWebServiceAuthentication):
    def __init__(self, authentication: IAuthentication, user_session_repository: IUserSessionRepository):
        self.authentication = authentication
        self.user_session_repository = user_session_repository

    def Validate(self, username: str, password: str) -> bool:
        return self.authentication.Validate(username, password)

    def Login(self, username: str) -> WebServiceUserSession:
        # Log::Debug('Web Service Login with username: %s', $username);
        # Assume that WebServiceLoginContext is a class with specific fields
        user_session = self.authentication.Login(username, WebServiceLoginContext())
        if user_session.IsLoggedIn():
            web_session = WebServiceUserSession(
                session_token=user_session.SessionToken,
                user_id=user_session.UserId,
                # Add other fields as needed
            )

            existing_session = self.user_session_repository.LoadBySessionToken(web_session.session_token)
            if existing_session is None:
                self.user_session_repository.Add(web_session)
            else:
                self.user_session_repository.Update(web_session)

            return web_session

        return WebServiceUserSession()  # Returning an empty session object

    def Logout(self, user_id: int, session_token: str) -> None:
        # Log::Debug('Logout sessionToken: %s', $sessionToken);
        web_session = self.user_session_repository.LoadBySessionToken(session_token)
        if web_session is not None and web_session.user_id == user_id:
            self.user_session_repository.Delete(web_session)
            self.authentication.Logout(web_session)


# WebServiceLoginContext class
class WebServiceLoginContext:
    def GetData(self) -> LoginData:
        # Return a LoginData object (Assuming LoginData is a class with specific fields)
        return LoginData(False, None)  # You should replace this with the actual implementation



