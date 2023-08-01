# <?php

# interface IAccountActivation
# {
#     /**
#      * @abstract
#      * @param User $user
#      * @return void
#      */
#     public function Notify(User $user);

#     /**
#      * @abstract
#      * @param string $activationCode
#      * @return ActivationResult
#      */
#     public function Activate($activationCode);
# }

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Union

# Define a User model
class User(BaseModel):
    username: str
    email: str

# Define an ActivationResult model
class ActivationResult(BaseModel):
    activated: bool
    user: Optional[User] = None

# Create a FastAPI app instance
app = FastAPI()

# Create a Python protocol (interface) for IAccountActivation
from typing_extensions import Protocol

class IAccountActivation(Protocol):
    def Notify(self, user: User) -> None:
        ...

    def Activate(self, activation_code: str) -> ActivationResult:
        ...

# Create an implementation of the IAccountActivation interface
class AccountActivation:
    def Notify(self, user: User) -> None:
        # Your implementation of the Notify method here
        # For example, send an activation email to the user
        pass

    def Activate(self, activation_code: str) -> ActivationResult:
        # Your implementation of the Activate method here
        # For example, activate the user account and return the result
        return ActivationResult(activated=True)

# Create an instance of the AccountActivation class
account_activation = AccountActivation()

# Define a route to handle account activation
@app.post("/activate/")
async def activate_account(activation_code: str):
    result: ActivationResult = account_activation.Activate(activation_code)
    return {"activated": result.activated, "user": result.user}

# Define a route to handle account notification
@app.post("/notify/")
async def notify_account(user: User):
    account_activation.Notify(user)
    return {"message": "Account activation notification sent."}


