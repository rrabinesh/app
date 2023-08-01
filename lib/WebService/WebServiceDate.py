# <?php

# class WebServiceDate
# {
#     /**
#      * @param string $dateString
#      * @param UserSession $session
#      * @return Date
#      */
#     public static function GetDate($dateString, UserSession $session)
#     {
#         try {
#             if (BookedStringHelper::Contains($dateString, 'T')) {
#                 return Date::ParseExact($dateString);
#             }

#             return Date::Parse($dateString, $session->Timezone);
#         } catch (Exception $ex) {
#             return Date::Now();
#         }
#     }
# }

from datetime import datetime

class WebServiceDate:
    @staticmethod
    def get_date(date_string: str, timezone: str) -> datetime:
        try:
            if 'T' in date_string:
                return datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S')

            # Here, you can implement the Date::Parse() equivalent functionality for parsing date strings
            # based on the provided timezone. Note that Python's datetime doesn't directly support timezones
            # in its standard library. You may need to use third-party libraries like pytz to handle timezones.

            # For simplicity, let's assume that the input date_string is already in the correct format and timezone.
            # In real-world applications, you should handle timezone conversion properly.

            return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

        except ValueError:
            # If the provided date_string is not in the expected format, return the current date and time.
            return datetime.now()


