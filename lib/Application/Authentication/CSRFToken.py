# <?php

# class CSRFToken
# {
#     /**
#      * @var string
#      */
#     public static $_Token;

#     /**
#      * @return string
#      */
#     public static function Create()
#     {
#         if (!empty(self::$_Token)) {
#             return self::$_Token;
#         }

#         return base64_encode(md5(BookedStringHelper::Random()));
#     }
# }




import base64
import hashlib
import secrets

class CSRFToken:
    _Token = None

    @staticmethod
    def Create() -> str:
        if CSRFToken._Token:
            return CSRFToken._Token

        random_bytes = secrets.token_bytes(32)
        csrf_token = base64.b64encode(hashlib.md5(random_bytes).digest()).decode()

        CSRFToken._Token = csrf_token
        return csrf_token


