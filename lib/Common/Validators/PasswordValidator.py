# <?php

# class PasswordValidator extends ValidatorBase implements IValidator
# {
#     /**
#      * @var User
#      */
#     private $user;
#     private $currentPasswordPlainText;

#     /**
#      * @param string $currentPasswordPlainText
#      * @param User $user
#      */
#     public function __construct($currentPasswordPlainText, User $user)
#     {
#         $this->currentPasswordPlainText = $currentPasswordPlainText;
#         $this->user = $user;
#     }

#     public function Validate()
#     {
#         $pw = new Password($this->currentPasswordPlainText, $this->user->encryptedPassword);
#         $this->isValid = $pw->Validate($this->user->passwordSalt);

#         if (!$this->isValid) {
#             $this->AddMessage(Resources::GetInstance()->GetString('PwMustMatch'));
#         }
#     }
# }

from fastapi import HTTPException
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User:
    def __init__(self, password_hash):
        self.password_hash = password_hash

class PasswordValidator:

    def __init__(self, plain_password: str, user: User):
        self.plain_password = plain_password
        self.user = user

    def validate(self) -> None:
        is_valid = pwd_context.verify(self.plain_password, self.user.password_hash)
        if not is_valid:
            raise HTTPException(status_code=400, detail="Invalid password")
