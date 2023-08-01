# <?php

# class Actions
# {
#     private function __construct()
#     {
#     }

#     public const CHANGE_PASSWORD = 'change_password';
#     public const GET_REPORT = 'get_report';
#     public const LOGIN = 'login';
#     public const REGISTER = 'register';
#     public const RESET = 'reset';
#     public const SAVE = 'save';
# }

from enum import Enum

class Actions(str, Enum):
    CHANGE_PASSWORD = 'change_password'
    GET_REPORT = 'get_report'
    LOGIN = 'login'
    REGISTER = 'register'
    RESET = 'reset'
    SAVE = 'save'


