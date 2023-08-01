# <?php

# require_once(ROOT_DIR . 'Domain/Access/UserSessionRepository.php');

# class WebServiceSecurity
# {
#     /**
#      * @var IUserSessionRepository
#      */
#     private $repository;

#     public function __construct(IUserSessionRepository $repository)
#     {
#         $this->repository = $repository;
#     }

#     public function HandleSecureRequest(IRestServer $server, $requireAdminRole = false)
#     {
#         $sessionToken = $server->GetHeader(WebServiceHeaders::SESSION_TOKEN);
#         $userId = $server->GetHeader(WebServiceHeaders::USER_ID);

#         Log::Debug('Handling secure request. url=%s, userId=%s, sessionToken=%s', $_SERVER['REQUEST_URI'], $userId, $sessionToken);

#         if (empty($sessionToken) || empty($userId)) {
#             Log::Debug('Empty token or userId');
#             return false;
#         }

#         $session = $this->repository->LoadBySessionToken($sessionToken);

#         if ($session != null && $session->IsExpired()) {
#             Log::Debug('Session is expired');
#             $this->repository->Delete($session);
#             return false;
#         }

#         if ($session == null || $session->UserId != $userId) {
#             Log::Debug('Session token does not match user session token');
#             return false;
#         }

#         if ($requireAdminRole && !$session->IsAdmin) {
#             Log::Debug('Route is limited to application administrators and this user is not an admin');
#             return false;
#         }

#         $session->ExtendSession();
#         $this->repository->Update($session);
#         $server->SetSession($session);

#         Log::Debug('Secure request was authenticated');

#         return true;
#     }
# }


from typing import Optional
from fastapi import Header, HTTPException, Depends

# Mock classes to represent the IUserSessionRepository and WebServiceUserSession
class IUserSessionRepository:
    def LoadBySessionToken(self, session_token: str):
        # Replace this with the actual implementation to load user session by session token
        pass

class WebServiceUserSession:
    def __init__(self, user_id, session_token, is_admin, is_expired):
        self.UserId = user_id
        self.SessionToken = session_token
        self.IsAdmin = is_admin
        self.IsExpired = is_expired

# Create a mock repository class that implements the IUserSessionRepository interface
class UserSessionRepository(IUserSessionRepository):
    def LoadBySessionToken(self, session_token: str):
        # Replace this with the actual database query to load user session by session token
        # Return the deserialized WebServiceUserSession if found, or None if not found
        pass

# Mock Log class
class Log:
    @staticmethod
    def Debug(message, *args):
        # Replace this with the actual logging implementation
        pass

# FastAPI Dependency for getting the User Session from the session token header
def get_user_session(session_token: Optional[str] = Header(None), repository: IUserSessionRepository = Depends(UserSessionRepository)):
    if session_token:
        session = repository.LoadBySessionToken(session_token)
        if session and not session.IsExpired:
            return session
    return None

# FastAPI Dependency for handling secure requests
def handle_secure_request(
    server: "IRestServer",
    session: WebServiceUserSession = Depends(get_user_session),
    require_admin_role: bool = False
):
    if not session:
        raise HTTPException(status_code=401, detail="Unauthorized")

    Log.Debug('Handling secure request. url=%s, userId=%s, sessionToken=%s', server.GetUrl(), session.UserId, session.SessionToken)

    if session.IsExpired:
        Log.Debug('Session is expired')
        # Perform cleanup or logout actions here if needed
        raise HTTPException(status_code=401, detail="Session is expired")

    if not session.UserId:
        Log.Debug('Empty user ID')
        raise HTTPException(status_code=401, detail="Unauthorized")

    if require_admin_role and not session.IsAdmin:
        Log.Debug('Route is limited to application administrators and this user is not an admin')
        raise HTTPException(status_code=403, detail="Forbidden")

    # Extend the session
    # Note: FastAPI doesn't have the concept of "extending" a session like PHP, but you can update the session in the database to prolong the expiration time if needed

    Log.Debug('Secure request was authenticated')

# FastAPI SecurityMiddleware to apply the security handling to all routes
# Note: Replace "IRestServer" with your FastAPI Request object type
class SecurityMiddleware:
    def __init__(self, app, require_admin_role=False):
        self.app = app
        self.require_admin_role = require_admin_role

    async def __call__(self, server: "IRestServer"):
        try:
            handle_secure_request(server, require_admin_role=self.require_admin_role)
            return await self.app(server)
        except HTTPException as exc:
            return exc
