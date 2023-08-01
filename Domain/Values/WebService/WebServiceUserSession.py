# <?php

# require_once(ROOT_DIR . 'lib/Server/UserSession.php');
# require_once(ROOT_DIR . 'Domain/Values/WebService/WebServiceExpiration.php');
# require_once(ROOT_DIR . 'Domain/Values/WebService/WebServiceSessionToken.php');

# class WebServiceUserSession extends UserSession
# {
#     public $SessionToken = '';
#     public $SessionExpiration = '';

#     public function __construct($id)
#     {
#         parent::__construct($id);
#         $this->SessionToken = WebServiceSessionToken::Generate();
#         $this->SessionExpiration = WebServiceExpiration::Create();
#     }

#     /**
#      * @param UserSession $session
#      * @return WebServiceUserSession
#      */
#     public static function FromSession(UserSession $session)
#     {
#         $webSession = new WebServiceUserSession($session->UserId);

#         $webSession->FirstName = $session->FirstName;
#         $webSession->LastName = $session->LastName;
#         $webSession->Email = $session->Email;
#         $webSession->Timezone = $session->Timezone;
#         $webSession->HomepageId = $session->HomepageId;
#         $webSession->IsAdmin = $session->IsAdmin;
#         $webSession->IsGroupAdmin = $session->IsGroupAdmin;
#         $webSession->IsResourceAdmin = $session->IsResourceAdmin;
#         $webSession->IsScheduleAdmin = $session->IsScheduleAdmin;
#         $webSession->LanguageCode = $session->LanguageCode;
#         $webSession->PublicId = $session->PublicId;
#         $webSession->ScheduleId = $session->ScheduleId;
#         $webSession->Groups = $session->Groups;
#         $webSession->AdminGroups = $session->AdminGroups;

#         return $webSession;
#     }

#     public function ExtendSession()
#     {
#         $this->SessionExpiration = WebServiceExpiration::Create();
#     }

#     /**
#      * @return bool
#      */
#     public function IsExpired()
#     {
#         return WebServiceExpiration::IsExpired($this->SessionExpiration);
#     }
# }

import uuid
from datetime import datetime, timedelta

class WebServiceExpiration:
    @staticmethod
    def create():
        # Set the session expiration to 1 hour from now (adjust as needed)
        return datetime.utcnow() + timedelta(hours=1)

    @staticmethod
    def is_expired(expiration):
        return datetime.utcnow() > expiration


class WebServiceUserSession:
    def __init__(self, user_id):
        self.id = user_id
        self.session_token = str(uuid.uuid4())  # Generate a random session token
        self.session_expiration = WebServiceExpiration.create()

    @classmethod
    def from_session(cls, user_session):
        web_session = cls(user_session.user_id)

        # Copy the relevant attributes from the original UserSession
        web_session.first_name = user_session.first_name
        web_session.last_name = user_session.last_name
        web_session.email = user_session.email
        web_session.timezone = user_session.timezone
        web_session.homepage_id = user_session.homepage_id
        web_session.is_admin = user_session.is_admin
        web_session.is_group_admin = user_session.is_group_admin
        web_session.is_resource_admin = user_session.is_resource_admin
        web_session.is_schedule_admin = user_session.is_schedule_admin
        web_session.language_code = user_session.language_code
        web_session.public_id = user_session.public_id
        web_session.schedule_id = user_session.schedule_id
        web_session.groups = user_session.groups
        web_session.admin_groups = user_session.admin_groups

        return web_session

    def extend_session(self):
        self.session_expiration = WebServiceExpiration.create()

    def is_expired(self):
        return WebServiceExpiration.is_expired(self.session_expiration)



