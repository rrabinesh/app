# <?php

# class EqualValidator extends ValidatorBase implements IValidator
# {
#     private $_value1;
#     private $_value2;

#     public function __construct($value1, $value2)
#     {
#         $this->_value1 = $value1;
#         $this->_value2 = $value2;
#     }

#     public function Validate()
#     {
#         $this->isValid = ($this->_value1 == $this->_value2);
#     }

#     public function __toString()
#     {
#         return sprintf('value1: %s, value2: %s', $this->_value1, $this->_value2);
#     }
# }

from fastapi import HTTPException

class EqualValidator:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def validate(self) -> None:
        if self.value1 != self.value2:
            raise HTTPException(status_code=400, detail="Values are not equal")

    def __str__(self):
        return f"value1: {self.value1}, value2: {self.value2}"
