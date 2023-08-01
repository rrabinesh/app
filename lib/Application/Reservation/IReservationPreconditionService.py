# <?php

# interface INewReservationPreconditionService
# {
#     /**
#      * @param INewReservationPage $page
#      */
#     public function CheckAll(INewReservationPage $page, UserSession $user);
# }

# interface IReservationPreconditionService
# {
#     /**
#      * @param IReservationPage $page
#      */
#     public function CheckAll(IReservationPage $page, UserSession $user);
# }

from abc import ABC, abstractmethod
from pydantic import BaseModel  # Import pydantic's BaseModel for type hints

class INewReservationPage(ABC):
    pass

class IReservationPage(ABC):
    pass

class UserSession(BaseModel):  # Using pydantic's BaseModel for type hints
    # Define fields for UserSession if needed
    pass

class INewReservationPreconditionService(ABC):
    @abstractmethod
    def check_all(self, page: INewReservationPage, user: UserSession):
        pass

class IReservationPreconditionService(ABC):
    @abstractmethod
    def check_all(self, page: IReservationPage, user: UserSession):
        pass

