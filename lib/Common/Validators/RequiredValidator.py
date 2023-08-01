# <?php

# class RequiredValidator extends ValidatorBase implements IValidator
# {
#     private $value;

#     public function __construct($value)
#     {
#         $this->value = $value;
#     }

#     public function Validate()
#     {
#         $trimmed = trim($this->value);
#         $this->isValid = !empty($trimmed);
#     }
# }

from fastapi import HTTPException

class RequiredValidator:

    def __init__(self, value: str):
        self.value = value 

    def validate(self) -> None:
        if not self.value.strip():
            raise HTTPException(status_code=400, detail="Value is required")
