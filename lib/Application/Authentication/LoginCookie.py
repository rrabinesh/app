# <?php

# require_once(ROOT_DIR . 'lib/Common/namespace.php');

# class LoginCookie extends Cookie
# {
#     public $UserID;
#     public $LastLogin;

#     public function __construct($userid, $lastLoginTime)
#     {
#         $this->UserID = $userid;
#         $this->LastLogin = $lastLoginTime;

#         parent::__construct(CookieKeys::PERSIST_LOGIN, sprintf('%s|%s', $userid, $lastLoginTime));
#     }

#     public static function FromValue($cookieValue)
#     {
#         $cookieParts = explode('|', $cookieValue);

#         if (count($cookieParts) == 2) {
#             return new LoginCookie($cookieParts[0], $cookieParts[1]);
#         }

#         return null;
#     }
# }
# LoginCookie class (Custom implementation)

class LoginCookie:
    def __init__(self, userid: str, last_login_time: str):
        self.UserID = userid
        self.LastLogin = last_login_time
        self.cookie_value = f"{userid}|{last_login_time}"

    @staticmethod
    def from_value(cookie_value: str) -> "LoginCookie":
        cookie_parts = cookie_value.split('|')

        if len(cookie_parts) == 2:
            return LoginCookie(cookie_parts[0], cookie_parts[1])

        return None


