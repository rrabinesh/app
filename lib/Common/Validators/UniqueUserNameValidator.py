# <?php

# class UniqueUserNameValidator extends ValidatorBase implements IValidator
# {
#     private $_username;
#     private $_userid;
#     private $userRepository;

#     public function __construct(IUserViewRepository $userRepository, $username, $userid = null)
#     {
#         $this->_username = $username;
#         $this->_userid = $userid;
#         $this->userRepository = $userRepository;
#     }

#     public function Validate()
#     {
#         $this->isValid = true;
#         $userId = $this->userRepository->UserExists(null, $this->_username);

#         if (!empty($userId)) {
#             $this->isValid = $userId == $this->_userid;
#         }

#         if (!$this->isValid) {
#             $this->AddMessageKey('UniqueUsernameRequired');
#         }
#     }
# }


from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()

# Assuming you have already defined IUserViewRepository implementation and it is available as user_repo.

class IUserViewRepository:
    async def user_exists_by_username(self, username: str, user_id: Optional[int] = None) -> Optional[int]:
        # Your implementation to check if the username exists and return the user_id if found
        pass

class UniqueUserNameValidator:
    def __init__(self, user_repo: IUserViewRepository, username: str, user_id: int = None):
        self._username = username
        self._user_id = user_id
        self.user_repo = user_repo
        self.is_valid = False

    async def validate(self):
        self.is_valid = True

        user_id = await self.user_repo.user_exists_by_username(self._username)

        if user_id is not None:
            self.is_valid = user_id == self._user_id

        if not self.is_valid:
            raise HTTPException(status_code=400, detail="Username is not unique.")
