# <?php

# require_once(ROOT_DIR . 'lib/external/is_email/is_email.php');

# class EmailValidator extends ValidatorBase implements IValidator
# {
#     private $email;

#     public function __construct($email)
#     {
#         $this->email = $email;
#     }

#     public function Validate()
#     {
#         $this->isValid = psi_is_email($this->email);

#         if (!$this->isValid) {
#             $this->AddMessageKey('ValidEmailRequired');
#         }
#     }
# }

from fastapi import HTTPException
from pydantic import EmailStr

from .is_email import is_email

class EmailValidator:
    
    def __init__(self, email: str):
        self.email = email
        
    def validate(self) -> None:
        if not is_email(self.email):
            raise HTTPException(
                status_code=400, 
                detail="Valid email required"
            )
