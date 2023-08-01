# <?php

# interface IDomainEvent
# {
#     /**
#      * @return string
#      */
#     public function EventType();

#     /**
#      * @return EventCategory|string
#      */
#     public function EventCategory();
# }

from abc import ABC, abstractmethod
from enum import Enum

class EventCategory(Enum):
    # Define your event categories here
    CATEGORY_1 = 1
    CATEGORY_2 = 2
    CATEGORY_3 = 3

class IDomainEvent(ABC):
    @abstractmethod
    def EventType(self) -> str:
        pass

    @abstractmethod
    def EventCategory(self) -> EventCategory:
        pass

