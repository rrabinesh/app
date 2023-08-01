# <?php

# class BooleanConverter implements IConvert
# {
#     public function Convert($value)
#     {
#         return self::ConvertValue($value);
#     }

#     /**
#      * @param mixed $value
#      * @return bool
#      */
#     public static function ConvertValue($value)
#     {
#         return $value === true || strtolower($value) == 'true' || $value === 1 || $value === '1';
#     }
# }


from typing import Any

class BooleanConverter:

    @staticmethod
    def convert(value: Any) -> bool:
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.lower() == 'true'
        if isinstance(value, int):
            return value == 1
        return False
