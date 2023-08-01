# <?php

# interface IValidator
# {
#     /**
#      * @return bool
#      */
#     public function IsValid();

#     /**
#      * @return void
#      */
#     public function Validate();

#     /**
#      * @return string[]|null
#      */
#     public function Messages();

#     /**
#      * @return bool
#      */
#     public function ReturnsErrorResponse();
# }

from abc import ABC, abstractmethod

class IValidator(ABC):

    @property
    @abstractmethod
    def is_valid(self) -> bool:
        pass

    @abstractmethod
    def validate(self) -> None:
        pass

    @property
    @abstractmethod
    def messages(self) -> list[str]:
        pass

    @property  
    @abstractmethod
    def returns_error_response(self) -> bool:
        pass
