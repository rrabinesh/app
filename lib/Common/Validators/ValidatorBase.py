# <?php

# abstract class ValidatorBase implements IValidator
# {
#     /**
#      * @var bool
#      */
#     protected $isValid = true;

#     /**
#      * @var array|string[]
#      */
#     private $messages = [];

#     /**
#      * @return bool
#      */
#     public function IsValid()
#     {
#         return $this->isValid;
#     }

#     /**
#      * @return array|null|string[]
#      */
#     public function Messages()
#     {
#         return $this->messages;
#     }

#     /**
#      * @return bool
#      */
#     public function ReturnsErrorResponse()
#     {
#         return false;
#     }

#     /**
#      * @param string $message
#      */
#     protected function AddMessage($message)
#     {
#         $this->messages[] = $message;
#     }

#     /**
#      * @param string $resourceKey
#      * @param array $params
#      */
#     protected function AddMessageKey($resourceKey, $params = [])
#     {
#         $this->AddMessage(Resources::GetInstance()->GetString($resourceKey, $params));
#     }
# }

# validator_base.py

from typing import List

class ValidatorBase:
    def __init__(self):
        self.is_valid = True
        self.messages: List[str] = []

    def is_valid(self) -> bool:
        return self.is_valid

    def messages(self) -> List[str]:
        return self.messages

    def returns_error_response(self) -> bool:
        return False

    def add_message(self, message: str):
        self.messages.append(message)

    def add_message_key(self, resource_key: str, params: dict = {}):
        # Assuming you have a Resources class or localization mechanism to fetch resource strings
        # Replace Resources::GetInstance()->GetString with the appropriate logic in your application
        message = Resources.GetInstance().GetString(resource_key, params)
        self.add_message(message)




# unique_email_validator.py

from validator_base import ValidatorBase
from user_repository import IUserViewRepository

class UniqueEmailValidator(ValidatorBase):
    def __init__(self, user_repo: IUserViewRepository, email: str, user_id: int = None):
        super().__init__()
        self._email = email
        self._user_id = user_id
        self.user_repo = user_repo

    async def validate(self):
        self.is_valid = True

        user_id = await self.user_repo.user_exists_by_email(self._email, self._user_id)

        if user_id is not None:
            self.is_valid = user_id == self._user_id

        if not self.is_valid:
            self.add_message_key('UniqueEmailRequired')


