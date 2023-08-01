# <?php

# interface ILoginContext
# {
#     /**
#      * @abstract
#      * @return LoginData
#      */
#     public function GetData();
# }

# class LoginData
# {
#     /**
#      * @var bool
#      */
#     public $Persist;

#     /**
#      * @var string
#      */
#     public $Language;

#     public function __construct($persist = false, $language = '')
#     {
#         $this->Persist = $persist;
#         $this->Language = $language;
#     }
# }



# LoginData class

class LoginData:
    def __init__(self, persist=False, language=''):
        self.Persist = persist
        self.Language = language


# ILoginContext interface (using an abstract class)

from abc import ABC, abstractmethod

class ILoginContext(ABC):
    @abstractmethod
    def get_data(self) -> LoginData:
        pass


# LoginContext implementation of ILoginContext interface

class LoginContext(ILoginContext):
    def get_data(self) -> LoginData:
        # Implement the logic to retrieve login data
        # For demonstration purposes, we return a default LoginData object.
        return LoginData()

