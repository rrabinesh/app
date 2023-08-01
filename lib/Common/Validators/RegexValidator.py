# <?php

# class RegexValidator extends ValidatorBase implements IValidator
# {
#     public function __construct($value, $regex)
#     {
#         $this->_value = $value;
#         $this->_regex = $regex;
#     }

#     public function Validate()
#     {
#         $this->isValid = false;
#         if (preg_match($this->_regex, $this->_value)) {
#             $this->isValid = true;
#         }
#     }
# }

import re
from fastapi import HTTPException

class RegexValidator:

    def __init__(self, value: str, regex: str):
        self.value = value
        self.regex = regex

    def validate(self) -> None:
        if not re.search(self.regex, self.value):
            raise HTTPException(status_code=400, detail="Invalid format")

