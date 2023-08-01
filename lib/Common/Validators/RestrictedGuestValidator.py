# <?php

# require_once(ROOT_DIR . 'lib/Application/Authentication/GuestUserService.php');

# class RestrictedGuestValidator extends ValidatorBase implements IValidator
# {
#     private $email;
#     /**
#      * @var IGuestUserService
#      */
#     private $guestUserService;

#     public function __construct($email, IGuestUserService $guestUserService)
#     {
#         $this->email = $email;
#         $this->guestUserService = $guestUserService;
#     }

#     public function Validate()
#     {
#         $this->isValid = $this->guestUserService->EmailExists($this->email);

#         if (!$this->isValid) {
#             $this->AddMessageKey('RegisteredAccountRequired');
#         }
#     }
# }


from fastapi import HTTPException

from guest_user_service import GuestUserService

class RestrictedGuestValidator:

    def __init__(self, email: str, guest_service: GuestUserService):
        self.email = email
        self.guest_service = guest_service

    async def validate(self) -> None:
        exists = await self.guest_service.email_exists(self.email)
        if not exists:
            raise HTTPException(status_code=400, detail="Registered account required")
