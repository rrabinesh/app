# <?php

# class LoginTime
# {
#     /**
#      * @var null
#      * Only for testing
#      */
#     public static $Now = null;

#     private static $_format = 'Y-m-d H:i:s';

#     public static function Now()
#     {
#         if (empty(self::$Now)) {
#             return Date::Now()->ToDatabase();
#         } else {
#             return date(self::$_format, self::$Now);
#         }
#     }
# }


# login_time.py

from datetime import datetime

format_str = '%Y-%m-%d %H:%M:%S'

def get_login_time():
    # For testing purposes, you can set the desired time as a string in the format 'Y-m-d H:i:s'
    # For example: Now = '2023-07-26 12:34:56'
    # If Now is None, it will return the current time in the specified format.
    now = None  # Replace None with a specific time string for testing or set it to None for the current time
    if now:
        return now
    else:
        return datetime.now().strftime(format_str)
