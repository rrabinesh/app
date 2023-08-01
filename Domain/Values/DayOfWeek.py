# <?php

# class DayOfWeek
# {
#     public const SUNDAY = 0;
#     public const MONDAY = 1;
#     public const TUESDAY = 2;
#     public const WEDNESDAY = 3;
#     public const THURSDAY = 4;
#     public const FRIDAY = 5;
#     public const SATURDAY = 6;

#     public const NumberOfDays = 7;

#     /**
#      * @return array|int[]|DayOfWeek
#      */
#     public static function Days()
#     {
#         return range(self::SUNDAY, self::SATURDAY);
#     }
# }


from enum import Enum

class DayOfWeek(Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6

    NumberOfDays = 7

    @classmethod
    def Days(cls):
        return list(cls)

