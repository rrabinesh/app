# <?php

# class ErrorMessages
# {
#     public const UNKNOWN_ERROR = 0;
#     public const INSUFFICIENT_PERMISSIONS = 1;
#     public const MISSING_RESOURCE = 2;
#     public const MISSING_SCHEDULE = 3;
#     public const RESERVATION_NOT_FOUND = 4;
#     public const RESERVATION_NOT_AVAILABLE = 5;

#     private $_resourceKeys = [];
#     private static $_instance;

#     private function __construct()
#     {
#         $this->SetKey(ErrorMessages::INSUFFICIENT_PERMISSIONS, 'InsufficientPermissionsError');
#         $this->SetKey(ErrorMessages::MISSING_RESOURCE, 'MissingReservationResourceError');
#         $this->SetKey(ErrorMessages::MISSING_SCHEDULE, 'MissingReservationScheduleError');
#         $this->SetKey(ErrorMessages::RESERVATION_NOT_FOUND, 'ReservationNotFoundError');
#         $this->SetKey(ErrorMessages::RESERVATION_NOT_AVAILABLE, 'ReservationNotAvailable');
#     }

#     /**
#      * @static
#      * @return ErrorMessages
#      */
#     public static function Instance()
#     {
#         if (self::$_instance == null) {
#             self::$_instance = new ErrorMessages();
#         }

#         return self::$_instance;
#     }

#     private function SetKey($errorMessageId, $resourceKey)
#     {
#         $this->_resourceKeys[$errorMessageId] = $resourceKey;
#     }

#     public function GetResourceKey($errorMessageId)
#     {
#         if (!isset($this->_resourceKeys[$errorMessageId])) {
#             return 'UnknownError';
#         }

#         return $this->_resourceKeys[$errorMessageId];
#     }
# }

from enum import IntEnum
from typing import Dict
from fastapi import FastAPI

app = FastAPI()

class ErrorMessages(IntEnum):
    UNKNOWN_ERROR = 0
    INSUFFICIENT_PERMISSIONS = 1
    MISSING_RESOURCE = 2
    MISSING_SCHEDULE = 3
    RESERVATION_NOT_FOUND = 4
    RESERVATION_NOT_AVAILABLE = 5

class ErrorMessageManager:
    _resource_keys: Dict[ErrorMessages, str] = {
        ErrorMessages.INSUFFICIENT_PERMISSIONS: 'InsufficientPermissionsError',
        ErrorMessages.MISSING_RESOURCE: 'MissingReservationResourceError',
        ErrorMessages.MISSING_SCHEDULE: 'MissingReservationScheduleError',
        ErrorMessages.RESERVATION_NOT_FOUND: 'ReservationNotFoundError',
        ErrorMessages.RESERVATION_NOT_AVAILABLE: 'ReservationNotAvailable',
    }

    @classmethod
    def get_resource_key(cls, error_message_id: ErrorMessages) -> str:
        return cls._resource_keys.get(error_message_id, 'UnknownError')

@app.get("/errormessages/{error_message_id}")
def get_error_message(error_message_id: ErrorMessages):
    resource_key = ErrorMessageManager.get_resource_key(error_message_id)
    return {"error_message_id": error_message_id, "resource_key": resource_key}

