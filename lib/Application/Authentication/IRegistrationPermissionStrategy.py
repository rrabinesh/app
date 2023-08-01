# <?php

# interface IRegistrationPermissionStrategy
# {
#     public function AddAccount(User $user);
# }


class User:
    pass


# IRegistrationPermissionStrategy interface (Using abstract class)

from abc import ABC, abstractmethod

class IRegistrationPermissionStrategy(ABC):
    @abstractmethod
    def add_account(self, user: User) -> None:
        pass


# RegistrationPermissionStrategy implementation of IRegistrationPermissionStrategy interface

class RegistrationPermissionStrategy(IRegistrationPermissionStrategy):
    def add_account(self, user: User) -> None:
        # Implement the logic to add account permissions for the user
        # For demonstration purposes, we do nothing here.
        pass

