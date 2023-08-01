# <?php

# require_once(ROOT_DIR . 'lib/Email/Messages/GuestAccountCreationEmail.php');

# class GuestRegistrationNotificationStrategy implements IRegistrationNotificationStrategy
# {
#     public function NotifyAccountCreated(User $user, $password)
#     {
#         ServiceLocator::GetEmailService()->Send(new GuestAccountCreationEmail($user, $password));
#     }
# }

from fastapi import FastAPI
from pydantic import BaseModel

# Your email service implementation here (use a third-party library for sending emails)

class User(BaseModel):
    username: str
    email: str

class GuestRegistrationNotificationStrategy:
    def NotifyAccountCreated(self, user: User, password: str):
        # Your email service code to send the notification email here
        # For example, using a third-party library:
        # email_service.send_email(user.email, "Guest Account Created", f"Username: {user.username}\nPassword: {password}")
        pass
# Create a FastAPI app instance
app = FastAPI()

# Create an instance of the notification strategy
notification_strategy = GuestRegistrationNotificationStrategy()

# Define a route to handle guest registration and notify using the strategy
@app.post("/guest/register/")
async def guest_registration(user: User):
    password = "some_random_password"  # Generate a random password here

    # Register the guest user

    # Notify using the strategy
    notification_strategy.NotifyAccountCreated(user, password)

    return {"message": "Guest account registered and notification sent."}


