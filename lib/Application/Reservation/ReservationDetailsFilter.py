# <?php

# class ReservationDetailsFilter
# {
#     /**
#      * @param Date|null $reservationStart
#      * @param Date|null $reservationEnd
#      * @return bool
#      */
#     public static function HideReservationDetails($reservationStart = null, $reservationEnd = null)
#     {
#         $hideReservationDetails = Configuration::Instance()->GetSectionKey(
#             ConfigSection::PRIVACY,
#             ConfigKeys::PRIVACY_HIDE_RESERVATION_DETAILS,
#             new LowerCaseConverter()
#         );
#         if ($hideReservationDetails == 'past' && $reservationEnd != null) {
#             return $reservationEnd->LessThan(Date::Now());
#         } elseif ($hideReservationDetails == 'future' && $reservationEnd != null) {
#             return $reservationEnd->GreaterThan(Date::Now());
#         } elseif ($hideReservationDetails == 'current' && $reservationStart != null) {
#             return $reservationStart->LessThan(Date::Now());
#         }

#         $converter = new BooleanConverter();
#         return $converter->Convert($hideReservationDetails);
#     }
# }


from enum import Enum
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

class ConfigSection(Enum):
    PRIVACY = 'privacy'

class ConfigKeys(Enum):
    PRIVACY_HIDE_RESERVATION_DETAILS = 'hide_reservation_details'

class LowerCaseConverter:
    def convert(self, value):
        return value.lower()

class BooleanConverter:
    def convert(self, value):
        return value.lower() == 'true'

class Date:
    # Define methods as needed
    @staticmethod
    def now():
        return datetime.now()

class ReservationDetailsFilter:
    @staticmethod
    def hide_reservation_details(reservation_start=None, reservation_end=None):
        hide_reservation_details = Configuration().instance().get_section_key(
            ConfigSection.PRIVACY,
            ConfigKeys.PRIVACY_HIDE_RESERVATION_DETAILS,
            LowerCaseConverter()
        )

        if hide_reservation_details == 'past' and reservation_end is not None:
            return reservation_end < Date.now()
        elif hide_reservation_details == 'future' and reservation_end is not None:
            return reservation_end > Date.now()
        elif hide_reservation_details == 'current' and reservation_start is not None:
            return reservation_start < Date.now()

        converter = BooleanConverter()
        return converter.convert(hide_reservation_details)

class Configuration:
    @staticmethod
    def instance():
        return Configuration()

    def get_section_key(self, section, key, converter):
        # Implement logic to retrieve configuration value for the given section and key
        # For example, you could use environment variables, a configuration file, or a database
        # ...

        # For this example, return a hardcoded value for demonstration purposes
        return 'true'

@app.get("/hide_reservation_details")
def hide_reservation_details(reservation_start: datetime = None, reservation_end: datetime = None):
    result = ReservationDetailsFilter.hide_reservation_details(reservation_start, reservation_end)
    return {"hide_reservation_details": result}


