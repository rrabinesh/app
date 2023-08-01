# <?php

# interface IRegistrationNotificationStrategy
# {
#     public function NotifyAccountCreated(User $user, $password);
# }


class User:
    pass


# IRegistrationNotificationStrategy interface (Using abstract class)

from abc import ABC, abstractmethod

class IRegistrationNotificationStrategy(ABC):
    @abstractmethod
    def notify_account_created(self, user: User, password: str) -> None:
        pass


# RegistrationNotificationStrategy implementation of IRegistrationNotificationStrategy interface

class RegistrationNotificationStrategy(IRegistrationNotificationStrategy):
    def notify_account_created(self, user: User, password: str) -> None:
        # Implement the logic to notify the user about the account creation
        # For demonstration purposes, we print a message.
        print(f"Account created for user: {user}, Password: {password}")

