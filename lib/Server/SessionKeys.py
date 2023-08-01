# <?php

# class SessionKeys
# {
#     private function __construct()
#     {
#     }

#     public const CREDIT_CART = 'CREDIT_CART';
#     public const USER_SESSION = 'USER_SESSION';
#     public const INSTALLATION = 'INSTALLATION';
# }

from enum import Enum

class SessionKeys(Enum):
    CREDIT_CART = 'CREDIT_CART'
    USER_SESSION = 'USER_SESSION'
    INSTALLATION = 'INSTALLATION'
