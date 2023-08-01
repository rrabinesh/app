# <?php

# interface IConvert
# {
#     public function Convert($value);
# }

from abc import ABC, abstractmethod

class IConvert(ABC):

    @abstractmethod
    def convert(self, value):
        pass

