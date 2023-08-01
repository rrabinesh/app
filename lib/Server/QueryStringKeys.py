# <?php

# class QueryStringKeys
# {
#     private function __construct()
#     {
#     }

#     public const ACCESSORY_ID = 'aid';
#     public const ACCESSORY_NAME = 'an';
#     public const ACTION = 'action';
#     public const ACCOUNT_ACTIVATION_CODE = 'ac';
#     public const ACCOUNT_STATUS = 'as';
#     public const ANNOUNCEMENT_ID = 'aid';
#     public const ATTACHMENT_FILE_ID = 'afid';
#     public const ATTRIBUTE_CATEGORY = 'ac';
#     public const ATTRIBUTE_ID = 'aid';
#     public const AUTOCOMPLETE_TERM = 'term';
#     public const AUTOCOMPLETE_TYPE = 'type';
#     public const BLACKOUT_ID = 'bid';
#     public const CALENDAR_TYPE = 'ct';
#     public const CONFIG_FILE = 'cf';
#     public const DATA_REQUEST = 'dr';
#     public const DAY = 'd';
#     public const EMAIL = 'e';
#     public const END = 'end';
#     public const END_DATE = 'ed';
#     public const END_TIME = 'et';
#     public const FORMAT = 'format';
#     public const GROUP_ID = 'gid';
#     public const INVITATION_ACTION = 'ia';
#     public const INVITEE_ID = 'iid';
#     public const LANGUAGE = 'lang';
#     public const LAYOUT_DATE = 'ld';
#     public const MESSAGE_ID = 'mid';
#     public const MONTH = 'm';
#     public const MISSED_CHECKIN = 'in';
#     public const MISSED_CHECKOUT = 'out';
#     public const NODE_ID = 'nid';
#     public const PAGE = 'page';
#     public const PAGE_SIZE = 'pageSize';
#     public const PAYPAL_ACTION = 'paypalaction';
#     public const PARTICIPANT_ID = 'pid';
#     public const PERIOD_ID = 'pid';
#     public const PREVIOUS_ID = 'pid';
#     public const COUNT = 'count';
#     public const QUANTITY = 'quantity';
#     public const QUOTA_ID = 'qid';
#     public const READ_ONLY = 'ro';
#     public const REDIRECT = 'redirect';
#     public const REFERENCE_NUMBER = 'rn';
#     public const REMINDER_ID = 'aid';
#     public const REPORT_ID = 'rid';
#     public const RESERVATION_DATE = 'rd';
#     public const RESERVATION_STATUS_ID = 'rsid';
#     public const RESERVATION_STATUS_REASON_ID = 'rsrid';
#     public const RESERVATION_WAITLIST_REQUEST_ID = 'rwrid';
#     public const RESPONSE_TYPE = 'rs';
#     public const RESOURCE_ID = 'rid';
#     public const RESOURCE_GROUP_ID = 'rgid';
#     public const RESOURCE_TYPE_ID = 'rtid';
#     public const RESERVATION_RESOURCE_STATUS_ID = 'rrsid';
#     public const RESERVATION_RESOURCE_REASON_ID = 'rrsrid';
#     public const RESERVATION_TITLE = 'rtitle';
#     public const RESERVATION_DESCRIPTION = 'rdesc';
#     public const SCHEDULE_ID = 'sid';
#     public const SHOW_FULL_WEEK = 'sfw';
#     public const SOURCE_REFERENCE_NUMBER = 'srn';
#     public const SORT_DIRECTION = 'dir';
#     public const SORT_FIELD = 'sort';
#     public const START = 'start';
#     public const START_DATE = 'sd';
#     public const START_TIME = 'st';
#     public const START_DATES = 'sds';
#     public const SUBSCRIPTION_KEY = 'icskey';
#     public const SUBSCRIPTION_DAYS_PAST = 'pastDayCount';
#     public const SUBSCRIPTION_DAYS_FUTURE = 'futureDayCount';
#     public const EMAIL_TEMPLATE_NAME = 'tn';
#     public const TRANSACTION_LOG_ID = 'id';
#     public const TYPE = 'type';
#     public const USER_ID = 'uid';
#     public const USER_NAME = 'un';
#     public const WEB_SERVICE_ACTION = 'action';
#     public const YEAR = 'y';
# }


from enum import Enum

class QueryStringKeys(Enum):
    ACCESSORY_ID = 'aid'
    ACCESSORY_NAME = 'an'
    ACTION = 'action'
    ACCOUNT_ACTIVATION_CODE = 'ac' 
    ACCOUNT_STATUS = 'as'
    ANNOUNCEMENT_ID = 'aid'
    ATTACHMENT_FILE_ID = 'afid'
    ATTRIBUTE_CATEGORY = 'ac'
    ATTRIBUTE_ID = 'aid'
    AUTOCOMPLETE_TERM = 'term'  
    AUTOCOMPLETE_TYPE = 'type'
    BLACKOUT_ID = 'bid' 
    CALENDAR_TYPE = 'ct'
    CONFIG_FILE = 'cf'
    DATA_REQUEST = 'dr' 
    DAY = 'd'
    EMAIL = 'e'    
    END = 'end'
    END_DATE = 'ed'
    END_TIME = 'et'
    FORMAT = 'format' 
    GROUP_ID = 'gid'
    INVITATION_ACTION = 'ia'
    INVITEE_ID = 'iid'
    LANGUAGE = 'lang'
    LAYOUT_DATE = 'ld'
    MESSAGE_ID = 'mid'
    MONTH = 'm'
    MISSED_CHECKIN = 'in'
    MISSED_CHECKOUT = 'out'
    NODE_ID = 'nid'
    PAGE = 'page'
    PAGE_SIZE = 'pageSize'
    PAYPAL_ACTION = 'paypalaction'
    PARTICIPANT_ID = 'pid'
    PERIOD_ID = 'pid'
    PREVIOUS_ID = 'pid' 
    COUNT = 'count'
    QUANTITY = 'quantity'
    QUOTA_ID = 'qid' 
    READ_ONLY = 'ro'
    REDIRECT = 'redirect'
    REFERENCE_NUMBER = 'rn'
    REMINDER_ID = 'aid'
    REPORT_ID = 'rid'
    RESERVATION_DATE = 'rd'
    RESERVATION_STATUS_ID = 'rsid'
    RESERVATION_STATUS_REASON_ID = 'rsrid'
    RESERVATION_WAITLIST_REQUEST_ID = 'rwrid'
    RESPONSE_TYPE = 'rs'
    RESOURCE_ID = 'rid'
    RESOURCE_GROUP_ID = 'rgid' 
    RESOURCE_TYPE_ID = 'rtid'
    RESERVATION_RESOURCE_STATUS_ID = 'rrsid'
    RESERVATION_RESOURCE_REASON_ID = 'rrsrid'
    RESERVATION_TITLE = 'rtitle'
    RESERVATION_DESCRIPTION = 'rdesc'
    SCHEDULE_ID = 'sid'
    SHOW_FULL_WEEK = 'sfw'
    SOURCE_REFERENCE_NUMBER = 'srn' 
    SORT_DIRECTION = 'dir'
    SORT_FIELD = 'sort'
    START = 'start' 
    START_DATE = 'sd'
    START_TIME = 'st'
    START_DATES = 'sds'
    SUBSCRIPTION_KEY = 'icskey'
    SUBSCRIPTION_DAYS_PAST = 'pastDayCount'
    SUBSCRIPTION_DAYS_FUTURE = 'futureDayCount'
    EMAIL_TEMPLATE_NAME = 'tn'
    TRANSACTION_LOG_ID = 'id'
    TYPE = 'type'
    USER_ID = 'uid'
    USER_NAME = 'un'
    WEB_SERVICE_ACTION = 'action'
    YEAR = 'y'

    @staticmethod
    def get(key):
        return QueryStringKeys[key].value

