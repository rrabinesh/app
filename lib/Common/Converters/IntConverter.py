# <!-- <?php

# class IntConverter implements IConvert
# {
#     public function Convert($value)
#     {
#         return intval($value);
#     }
# } -->

from typing import Any

class IntConverter:

    @staticmethod
    def convert(value: Any) -> int:
        return int(value)

