# <?php

# class WebServiceExpiration
# {
#     private static $SESSION_LENGTH_IN_MINUTES = 30;

#     public function __construct()
#     {
#         self::$SESSION_LENGTH_IN_MINUTES = Configuration::Instance()->GetKey(ConfigKeys::INACTIVITY_TIMEOUT, new IntConverter());
#     }

#     /**
#      * @param string $expirationTime
#      * @return bool
#      */
#     public static function IsExpired($expirationTime)
#     {
#         return Date::Parse($expirationTime, 'UTC')->LessThan(Date::Now());
#     }

#     /**
#      * @return string
#      */
#     public static function Create()
#     {
#         return Date::Now()->AddMinutes(self::$SESSION_LENGTH_IN_MINUTES)->ToUtc()->ToIso();
#     }
# }

from datetime import datetime, timedelta
from fastapi import FastAPI

app = FastAPI()

class WebServiceExpiration:
    def __init__(self):
        # Replace this with the actual implementation of getting the session length in minutes from the configuration
        self.session_length_in_minutes = 30

    @staticmethod
    def is_expired(expiration_time: str):
        return datetime.fromisoformat(expiration_time) < datetime.utcnow()

    def create(self):
        return (datetime.utcnow() + timedelta(minutes=self.session_length_in_minutes)).isoformat()
