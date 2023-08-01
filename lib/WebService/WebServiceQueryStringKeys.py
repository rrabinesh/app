# <?php

# class WebServiceQueryStringKeys
# {
#     public const USER_ID = 'userId';
#     public const DATE_TIME = 'dateTime';
#     public const START_DATE_TIME = 'startDateTime';
#     public const END_DATE_TIME = 'endDateTime';
#     public const RESOURCE_ID = 'resourceId';
#     public const SCHEDULE_ID = 'scheduleId';
#     public const UPDATE_SCOPE = 'updateScope';
#     public const USERNAME = 'username';
#     public const EMAIL = 'email';
#     public const FIRST_NAME = 'firstName';
#     public const LAST_NAME = 'lastName';
#     public const PHONE = 'phone';
#     public const ORGANIZATION = 'organization';
#     public const POSITION = 'position';
#     public const ATTRIBUTE_PREFIX = 'att';
# }

from pydantic import BaseModel

class WebServiceQueryStringKeys(BaseModel):
    USER_ID: str = 'userId'
    DATE_TIME: str = 'dateTime'
    START_DATE_TIME: str = 'startDateTime'
    END_DATE_TIME: str = 'endDateTime'
    RESOURCE_ID: str = 'resourceId'
    SCHEDULE_ID: str = 'scheduleId'
    UPDATE_SCOPE: str = 'updateScope'
    USERNAME: str = 'username'
    EMAIL: str = 'email'
    FIRST_NAME: str = 'firstName'
    LAST_NAME: str = 'lastName'
    PHONE: str = 'phone'
    ORGANIZATION: str = 'organization'
    POSITION: str = 'position'
    ATTRIBUTE_PREFIX: str = 'att'

