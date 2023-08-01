# <?php

# interface IReservationInitializerFactory
# {
#     /**
#      * @param INewReservationPage $page
#      * @return IReservationInitializer
#      */
#     public function GetNewInitializer(INewReservationPage $page);

#     /**
#      * @param IExistingReservationPage $page
#      * @param ReservationView $reservationView
#      * @return IReservationInitializer
#      */
#     public function GetExistingInitializer(IExistingReservationPage $page, ReservationView $reservationView);
# }


from abc import ABC, abstractmethod
from pydantic import BaseModel  # Import pydantic's BaseModel for type hints

class INewReservationPage(ABC):
    pass

class IExistingReservationPage(ABC):
    pass

class ReservationView(BaseModel):  # Using pydantic's BaseModel for type hints
    # Define fields for ReservationView if needed
    pass

class IReservationInitializer(ABC):
    @abstractmethod
    def initialize(self):
        pass

class IReservationInitializerFactory(ABC):
    @abstractmethod
    def get_new_initializer(self, page: INewReservationPage) -> IReservationInitializer:
        pass

    @abstractmethod
    def get_existing_initializer(self, page: IExistingReservationPage, reservation_view: ReservationView) -> IReservationInitializer:
        pass

