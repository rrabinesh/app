# <?php

# require_once(ROOT_DIR . 'lib/Email/Messages/AccountActivationEmail.php');

# class AccountActivation implements IAccountActivation
# {
#     /**
#      * @var IAccountActivationRepository
#      */
#     private $activationRepository;

#     /**
#      * @var IUserRepository
#      */
#     private $userRepository;

#     public function __construct(IAccountActivationRepository $activationRepository, IUserRepository $userRepository)
#     {
#         $this->activationRepository = $activationRepository;
#         $this->userRepository = $userRepository;
#     }

#     public function Notify(User $user)
#     {
#         $activationCode = BookedStringHelper::Random(30);

#         $this->activationRepository->AddActivation($user, $activationCode);

#         ServiceLocator::GetEmailService()->Send(new AccountActivationEmail($user, $activationCode));
#     }

#     public function Activate($activationCode)
#     {
#         $userId = $this->activationRepository->FindUserIdByCode($activationCode);
#         $this->activationRepository->DeleteActivation($activationCode);

#         if ($userId != null) {
#             $user = $this->userRepository->LoadById($userId);
#             $user->Activate();
#             $this->userRepository->Update($user);
#             return new ActivationResult(true, $user);
#         }

#         return new ActivationResult(false);
#     }
# }

# class ActivationResult
# {
#     /**
#      * @var bool
#      */
#     private $activated;

#     /**
#      * @var null|User
#      */
#     private $user;

#     /**
#      * @param bool $activated
#      * @param User|null $user
#      */
#     public function __construct($activated, $user = null)
#     {
#         $this->activated = $activated;
#         $this->user = $user;
#     }

#     /**
#      * @return boolean
#      */
#     public function Activated()
#     {
#         return $this->activated;
#     }

#     /**
#      * @return null|User
#      */
#     public function User()
#     {
#         return $this->user;
#     }
# }

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    email: str
    activated: bool = False

class ActivationResult(BaseModel):
    activated: bool
    user: User = None



class IAccountActivationRepository:
    pass  # Placeholder for IAccountActivationRepository interface

class IUserRepository:
    pass  # Placeholder for IUserRepository interface

class BookedStringHelper:
    @staticmethod
    def Random(length):
        pass  # Placeholder for BookedStringHelper.Random static method

class ServiceLocator:
    @staticmethod
    def GetEmailService():
        pass  # Placeholder for ServiceLocator.GetEmailService static method

class AccountActivationEmail:
    pass  # Placeholder for AccountActivationEmail class

@app.post("/account/activation/notify")
def notify_account_activation(user_id: int):
    # Assuming you have your UserRepository implementation to load the user data.
    user = UserRepository.load_by_id(user_id)
    
    activation_code = BookedStringHelper.Random(30)

    # Assuming you have your AccountActivationRepository implementation to store the activation data.
    activation_repository.add_activation(user, activation_code)

    # Assuming you have an EmailService implementation to send emails.
    ServiceLocator.GetEmailService().Send(AccountActivationEmail(user, activation_code))

    return {"message": "Account activation notification sent."}

@app.post("/account/activation/activate", response_model=ActivationResult)
def activate_account(activation_code: str):
    # Assuming you have your AccountActivationRepository implementation to check the activation code.
    user_id = activation_repository.find_user_id_by_code(activation_code)
    activation_repository.delete_activation(activation_code)

    if user_id is not None:
        # Assuming you have your UserRepository implementation to load the user data.
        user = UserRepository.load_by_id(user_id)
        user.activated = True
        # Assuming you have your UserRepository implementation to update the user data.
        UserRepository.update(user)
        return ActivationResult(activated=True, user=user)

    return ActivationResult(activated=False)



