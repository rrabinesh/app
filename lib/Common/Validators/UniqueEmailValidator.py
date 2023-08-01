# <?php

# class UniqueEmailValidator extends ValidatorBase implements IValidator
# {
#     private $_email;
#     private $_userid;
#     private $userRepository;

#     public function __construct(IUserViewRepository $userRepository, $email, $userid = null)
#     {
#         $this->_email = $email;
#         $this->_userid = $userid;
#         $this->userRepository = $userRepository;
#     }

#     public function Validate()
#     {
#         $this->isValid = true;

#         $userId = $this->userRepository->UserExists($this->_email, null);

#         if (!empty($userId)) {
#             $this->isValid = $userId == $this->_userid;
#         }

#         if (!$this->isValid) {
#             $this->AddMessageKey('UniqueEmailRequired');
#         }
#     }
# }


from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()

# Assuming you have already defined IUserViewRepository implementation and it is available as user_repo.

class IUserViewRepository:
    async def user_exists(self, email: str, user_id: Optional[int] = None) -> Optional[int]:
        # Your implementation to check if the email exists and return the user_id if found
        pass

class UniqueEmailValidator:
    def __init__(self, user_repo: IUserViewRepository, email: str, user_id: int = None):
        self._email = email
        self._user_id = user_id
        self.user_repo = user_repo
        self.is_valid = False

    async def validate(self):
        self.is_valid = True

        user_id = await self.user_repo.user_exists(self._email)

        if user_id is not None:
            self.is_valid = user_id == self._user_id

        if not self.is_valid:
            raise HTTPException(status_code=400, detail="Email is not unique.")

