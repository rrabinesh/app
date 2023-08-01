# <?php

# interface IReservationInitializer
# {
#     public function Initialize();
# }

from abc import ABC, abstractmethod

class IReservationInitializer(ABC):
    @abstractmethod
    def initialize(self):
        pass

