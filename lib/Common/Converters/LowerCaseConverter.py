# <?php

# class LowerCaseConverter implements IConvert
# {
#     public function Convert($value)
#     {
#         return strtolower($value);
#     }
# }
class LowerCaseConverter:
    
    @staticmethod
    def convert(value: str) -> str:
        return value.lower()

