# <?php

# require_once(ROOT_DIR . 'lib/external/random/random.php');

# class BookedStringHelper
# {
#     /**
#      * @static
#      * @param $haystack string
#      * @param $needle string
#      * @return bool
#      */
#     public static function StartsWith($haystack, $needle)
#     {
#         $length = strlen($needle ?? '');
#         return (substr($haystack ?? '', 0, $length) === $needle);
#     }

#     /**
#      * @static
#      * @param $haystack string
#      * @param $needle string
#      * @return bool
#      */
#     public static function EndsWith($haystack, $needle)
#     {
#         $length = strlen($needle);
#         if ($length == 0) {
#             return true;
#         }

#         $start  = $length * -1;
#         return (substr($haystack, $start) === $needle);
#     }

#     /**
#      * @static
#      * @param $haystack string
#      * @param $needle string
#      * @return bool
#      */
#     public static function Contains($haystack, $needle)
#     {
#         return strpos($haystack, $needle) !== false;
#     }

#     /**
#      * @return string
#      */
#     public static function Random($length = 50)
#     {
#         try {
#             $string = random_bytes(intval($length/2));
#             $string = bin2hex($string);
#         } catch (Exception $e) {
#             $string = uniqid(rand(), true);
#             Log::Error('Could not generate web service session token. %s', $e);
#         }
#         return $string;
#     }
# }

from fastapi import FastAPI
import secrets
import logging

app = FastAPI()
logger = logging.getLogger(__name__)

class BookedStringHelper:
    @staticmethod
    def starts_with(haystack: str, needle: str) -> bool:
        length = len(needle) if needle else 0
        return haystack[:length] == needle

    @staticmethod
    def ends_with(haystack: str, needle: str) -> bool:
        length = len(needle)
        if length == 0:
            return True
        return haystack[-length:] == needle

    @staticmethod
    def contains(haystack: str, needle: str) -> bool:
        return needle in haystack

    @staticmethod
    def random(length: int = 50) -> str:
        try:
            num_bytes = length // 2
            random_bytes = secrets.token_bytes(num_bytes)
            random_string = random_bytes.hex()
        except Exception as e:
            random_string = secrets.token_hex(num_bytes)  # Fallback
            logger.error('Could not generate web service session token. %s', e)
        return random_string

@app.get("/starts_with/")
def starts_with(haystack: str, needle: str):
    return {"result": BookedStringHelper.starts_with(haystack, needle)}

@app.get("/ends_with/")
def ends_with(haystack: str, needle: str):
    return {"result": BookedStringHelper.ends_with(haystack, needle)}

@app.get("/contains/")
def contains(haystack: str, needle: str):
    return {"result": BookedStringHelper.contains(haystack, needle)}

@app.get("/random_string/")
def random_string(length: int = 50):
    return {"random_string": BookedStringHelper.random(length)}


