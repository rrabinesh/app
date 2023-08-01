# <?php

# class ColumnNames
# {
#     private function __construct()
#     {
#     }

#     // USERS //
#     public const USER_ID = 'user_id';
#     public const USERNAME = 'username';
#     public const EMAIL = 'email';
#     public const FIRST_NAME = 'fname';
#     public const LAST_NAME = 'lname';
#     public const PASSWORD = 'password';
#     public const OLD_PASSWORD = 'legacypassword';
#     public const USER_CREATED = 'date_created';
#     public const USER_MODIFIED = 'last_modified';
#     public const USER_STATUS_ID = 'status_id';
#     public const HOMEPAGE_ID = 'homepageid';
#     public const LAST_LOGIN = 'lastlogin';
#     public const TIMEZONE_NAME = 'timezone';
#     public const LANGUAGE_CODE = 'language';
#     public const SALT = 'salt';
#     public const PHONE_NUMBER = 'phone';
#     public const ORGANIZATION = 'organization';
#     public const POSITION = 'position';
#     DEFAULT_SCHEDULE_ID = 'default_schedule_id';
#     USER_PREFERENCES = 'preferences';
#     USER_STATUS = 'status_id';

#     // USER_ADDRESSES //
#     ADDRESS_ID = 'address_id';

#     // USER_PREFERENCES //
#     PREFERENCE_NAME = 'name';
#     PREFERENCE_VALUE = 'value';

#     // ROLES //
#     ROLE_LEVEL = 'role_level';
#     ROLE_ID = 'role_id';
#     ROLE_NAME = 'name';

#     // ANNOUNCEMENTS //
#     ANNOUNCEMENT_ID = 'announcementid';
#     ANNOUNCEMENT_PRIORITY = 'priority';
#     ANNOUNCEMENT_START = 'start_date';
#     ANNOUNCEMENT_END = 'end_date';
#     ANNOUNCEMENT_TEXT = 'announcement_text';
#     ANNOUNCEMENT_DISPLAY_PAGE = 'display_page';

#     // GROUPS //
#     GROUP_ID = 'group_id';
#     GROUP_NAME = 'name';
#     GROUP_ADMIN_GROUP_ID = 'admin_group_id';
#     GROUP_ADMIN_GROUP_NAME = 'admin_group_name';
#     GROUP_ISDEFAULT = 'isdefault';

#     // RESOURCE_GROUPS //
#     RESOURCE_GROUP_ID = 'resource_group_id';
#     RESOURCE_GROUP_NAME = 'resource_group_name';
#     RESOURCE_GROUP_PARENT_ID = 'parent_id';

#     // TIME BLOCKS //
#     BLOCK_DAY_OF_WEEK = 'day_of_week';
#     BLOCK_LABEL = 'label';
#     BLOCK_LABEL_END = 'end_label';
#     BLOCK_CODE = 'availability_code';
#     BLOCK_TIMEZONE = 'timezone';
#     LAYOUT_TYPE = 'layout_type';

#     // TIME BLOCK USES //
#     BLOCK_START = 'start_time';
#     BLOCK_END = 'end_time';

#     CUSTOM_ATTRIBUTE_ID = 'custom_attribute_id';
#     CUSTOM_ATTRIBUTE_VALUE = 'attribute_value';

#     // RESERVATION SERIES //
#     RESERVATION_USER = 'user_id';
#     RESERVATION_GROUP = 'group_id';
#     RESERVATION_CREATED = 'date_created';
#     RESERVATION_MODIFIED = 'last_modified';
#     RESERVATION_TYPE = 'type_id';
#     RESERVATION_TITLE = 'title';
#     RESERVATION_DESCRIPTION = 'description';
#     RESERVATION_COST = 'total_cost';
#     RESERVATION_PARENT_ID = 'parent_id';
#     REPEAT_TYPE = 'repeat_type';
#     REPEAT_OPTIONS = 'repeat_options';
#     RESERVATION_STATUS = 'status_id';
#     SERIES_ID = 'series_id';
#     RESERVATION_OWNER = 'owner_id';
#     RESERVATION_ALLOW_PARTICIPATION = 'allow_participation';
#     RESERVATION_TERMS_ACCEPTANCE_DATE = 'terms_date_accepted';
#     RESERVATION_SERIES_ID = 'series_id';

#     // RESERVATION_INSTANCE //
#     RESERVATION_INSTANCE_ID = 'reservation_instance_id';
#     RESERVATION_START = 'start_date';
#     RESERVATION_END = 'end_date';
#     REFERENCE_NUMBER = 'reference_number';
#     CHECKIN_DATE = 'checkin_date';
#     CHECKOUT_DATE = 'checkout_date';
#     PREVIOUS_END_DATE = 'previous_end_date';

#     // RESERVATION_USER //
#     RESERVATION_USER_LEVEL = 'reservation_user_level';

#     // RESOURCE //
#     RESOURCE_ID = 'resource_id';
#     RESOURCE_NAME = 'name';
#     RESOURCE_LOCATION = 'location';
#     RESOURCE_CONTACT = 'contact_info';
#     RESOURCE_DESCRIPTION = 'description';
#     RESOURCE_NOTES = 'notes';
#     RESOURCE_MINDURATION = 'min_duration';
#     RESOURCE_MININCREMENT = 'min_increment';
#     RESOURCE_MAXDURATION = 'max_duration';
#     RESOURCE_COST = 'unit_cost';
#     RESOURCE_AUTOASSIGN = 'autoassign';
#     RESOURCE_REQUIRES_APPROVAL = 'requires_approval';
#     RESOURCE_ALLOW_MULTIDAY = 'allow_multiday_reservations';
#     RESOURCE_MAX_PARTICIPANTS = 'max_participants';
#     RESOURCE_MINNOTICE_ADD = 'min_notice_time_add';
#     RESOURCE_MINNOTICE_UPDATE = 'min_notice_time_update';
#     RESOURCE_MINNOTICE_DELETE = 'min_notice_time_delete';
#     RESOURCE_MAXNOTICE = 'max_notice_time';
#     RESOURCE_IMAGE_NAME = 'image_name';
#     RESOURCE_STATUS_ID = 'status_id';
#     RESOURCE_STATUS_ID_ALIAS = 'resource_status_id';
#     RESOURCE_STATUS_REASON_ID = 'resource_status_reason_id';
#     RESOURCE_STATUS_DESCRIPTION = 'description';
#     RESOURCE_ADMIN_GROUP_ID = 'admin_group_id';
#     RESOURCE_SORT_ORDER = 'sort_order';
#     RESOURCE_BUFFER_TIME = 'buffer_time';
#     ENABLE_CHECK_IN = 'enable_check_in';
#     AUTO_RELEASE_MINUTES = 'auto_release_minutes';
#     RESOURCE_ALLOW_DISPLAY = 'allow_display';
#     RESOURCE_IMAGE_LIST = 'image_list';
#     PERMISSION_TYPE = 'permission_type';
#     RESOURCE_ADDITIONAL_PROPERTIES = 'additional_properties';

#     // RESERVATION RESOURCES
#     RESOURCE_LEVEL_ID = 'resource_level_id';

#     // SCHEDULE //
#     SCHEDULE_ID = 'schedule_id';
#     SCHEDULE_NAME = 'name';
#     SCHEDULE_DEFAULT = 'isdefault';
#     SCHEDULE_WEEKDAY_START = 'weekdaystart';
#     SCHEDULE_DAYS_VISIBLE = 'daysvisible';
#     LAYOUT_ID = 'layout_id';
#     SCHEDULE_ADMIN_GROUP_ID = 'admin_group_id';
#     SCHEDULE_ADMIN_GROUP_ID_ALIAS = 's_admin_group_id';
#     SCHEDULE_AVAILABLE_START_DATE = 'start_date';
#     SCHEDULE_AVAILABLE_END_DATE = 'end_date';
#     SCHEDULE_ALLOW_CONCURRENT_RESERVATIONS = 'allow_concurrent_bookings';
#     SCHEDULE_DEFAULT_STYLE = 'default_layout';
#     TOTAL_CONCURRENT_RESERVATIONS = 'total_concurrent_reservations';
#     MAX_RESOURCES_PER_RESERVATION = 'max_resources_per_reservation';

#     // EMAIL PREFERENCES //
#     EVENT_CATEGORY = 'event_category';
#     EVENT_TYPE = 'event_type';

#     REPEAT_START = 'repeat_start';
#     REPEAT_END = 'repeat_end';

#     // QUOTAS //
#     QUOTA_ID = 'quota_id';
#     QUOTA_LIMIT = 'quota_limit';
#     QUOTA_UNIT = 'unit';
#     QUOTA_DURATION = 'duration';
#     ENFORCED_START_TIME = 'enforced_time_start';
#     ENFORCED_END_TIME = 'enforced_time_end';
#     ENFORCED_DAYS = 'enforced_days';
#     QUOTA_SCOPE = 'scope';

#     // ACCESSORIES //
#     ACCESSORY_ID = 'accessory_id';
#     ACCESSORY_NAME = 'accessory_name';
#     ACCESSORY_QUANTITY = 'accessory_quantity';
#     ACCESSORY_RESOURCE_COUNT = 'num_resources';
#     ACCESSORY_MINIMUM_QUANTITY = 'minimum_quantity';
#     ACCESSORY_MAXIMUM_QUANTITY = 'maximum_quantity';

#     // RESERVATION ACCESSORY //
    # QUANTITY = 'quantity';

#     // BLACKOUTS //
#     BLACKOUT_INSTANCE_ID = 'blackout_instance_id';
#     BLACKOUT_START = 'start_date';
#     BLACKOUT_END = 'end_date';
#     BLACKOUT_TITLE = 'title';
#     BLACKOUT_DESCRIPTION = 'description';
#     BLACKOUT_SERIES_ID = 'blackout_series_id';

#     // ATTRIBUTES //
#     ATTRIBUTE_ID = 'custom_attribute_id';
#     ATTRIBUTE_ADMIN_ONLY = 'admin_only';
#     ATTRIBUTE_LABEL = 'display_label';
#     ATTRIBUTE_TYPE = 'display_type';
#     ATTRIBUTE_CATEGORY = 'attribute_category';
#     ATTRIBUTE_CONSTRAINT = 'validation_regex';
#     ATTRIBUTE_REQUIRED = 'is_required';
#     ATTRIBUTE_POSSIBLE_VALUES = 'possible_values';
#     ATTRIBUTE_VALUE = 'attribute_value';
#     ATTRIBUTE_ENTITY_ID = 'entity_id';
#     ATTRIBUTE_ENTITY_IDS = 'entity_ids';
#     ATTRIBUTE_ENTITY_DESCRIPTIONS = 'entity_descriptions';
#     ATTRIBUTE_SORT_ORDER = 'sort_order';
#     ATTRIBUTE_SECONDARY_CATEGORY = 'secondary_category';
#     ATTRIBUTE_SECONDARY_ENTITY_IDS = 'secondary_entity_ids';
#     ATTRIBUTE_SECONDARY_ENTITY_DESCRIPTIONS = 'secondary_entity_descriptions';
#     ATTRIBUTE_IS_PRIVATE = 'is_private';

#     // RESERVATION FILES //
#     FILE_ID = 'file_id';
#     FILE_NAME = 'file_name';
#     FILE_TYPE = 'file_type';
#     FILE_SIZE = 'file_size';
#     FILE_EXTENSION = 'file_extension';

#     // SAVED REPORTS //
#     REPORT_ID = 'saved_report_id';
#     REPORT_NAME = 'report_name';
#     DATE_CREATED = 'date_created';
#     REPORT_DETAILS = 'report_details';

#     // USER SESSION //
#     SESSION_TOKEN = 'session_token';
#     USER_SESSION = 'user_session_value';
#     SESSION_LAST_MODIFIED = 'last_modified';

#     // REMINDERS //
#     REMINDER_ID = 'reminder_id';
#     REMINDER_SENDTIME = 'sendtime';
#     REMINDER_MESSAGE = 'message';
#     REMINDER_USER_ID = 'user_id';
#     REMINDER_ADDRESS = 'address';
#     REMINDER_REFNUMBER = 'refnumber';
#     REMINDER_MINUTES_PRIOR = 'minutes_prior';
#     REMINDER_TYPE = 'reminder_type';

#     // RESOURCE TYPE //
#     RESOURCE_TYPE_ID = 'resource_type_id';
#     RESOURCE_TYPE_NAME = 'resource_type_name';
#     RESOURCE_TYPE_DESCRIPTION = 'resource_type_description';

#     // DBVERSION //
#     VERSION_NUMBER = 'version_number';
#     VERSION_DATE = 'version_date';

#     // RESERVATION COLOR RULES //
#     REQUIRED_VALUE = 'required_value';
#     RESERVATION_COLOR = 'color';
#     RESERVATION_COLOR_RULE_ID = 'reservation_color_rule_id';
#     COLOR_ATTRIBUTE_TYPE = 'attribute_type';
#     COMPARISON_TYPE = 'comparison_type';

#     // CURRENT_CREDITS //
#     CREDIT_COUNT = 'credit_count';
#     PEAK_CREDIT_COUNT = 'peak_credit_count';
#     CREDIT_NOTE = 'credit_note';
#     ORIGINAL_CREDIT_COUNT = 'original_credit_count';

#     // PEAK TIMES //
#     PEAK_TIMES_ID = 'peak_times_id';
#     PEAK_ALL_DAY = 'all_day';
#     PEAK_START_TIME = 'start_time';
#     PEAK_END_TIME = 'end_time';
#     PEAK_EVERY_DAY = 'every_day';
#     PEAK_DAYS = 'peak_days';
#     PEAK_ALL_YEAR = 'all_year';
#     PEAK_BEGIN_MONTH = 'begin_month';
#     PEAK_BEGIN_DAY = 'begin_day';
#     PEAK_END_MONTH = 'end_month';
#     PEAK_END_DAY = 'end_day';

#     // RESERVATION_WAITLIST_REQUEST_ID //
#     RESERVATION_WAITLIST_REQUEST_ID = 'reservation_waitlist_request_id';

#     // PAYMENT CONFIGURATION //
#     CREDIT_COST = 'credit_cost';
#     CREDIT_CURRENCY = 'credit_currency';

#     // PAYMENT GATEWAYS //
#     GATEWAY_TYPE = 'gateway_type';
#     GATEWAY_SETTING_NAME = 'setting_name';
#     GATEWAY_SETTING_VALUE = 'setting_value';

#     // PAYMENT TRANSACTION LOG //
#     TRANSACTION_LOG_ID = 'payment_transaction_log_id';
#     TRANSACTION_LOG_STATUS = 'status';
#     TRANSACTION_LOG_INVOICE = 'invoice_number';
#     TRANSACTION_LOG_TRANSACTION_ID = 'transaction_id';
#     TRANSACTION_LOG_TOTAL = 'total_amount';
#     TRANSACTION_LOG_FEE = 'transaction_fee';
#     TRANSACTION_LOG_CURRENCY = 'currency';
#     TRANSACTION_LOG_TRANSACTION_HREF = 'transaction_href';
#     TRANSACTION_LOG_REFUND_HREF = 'refund_href';
#     TRANSACTION_LOG_GATEWAY_NAME = 'gateway_name';
#     TRANSACTION_LOG_GATEWAY_DATE = 'gateway_date_created';
#     TRANSACTION_LOG_REFUND_AMOUNT = 'refund_amount';

#     // TERMS OF SERVICE //
#     TERMS_ID = 'terms_of_service_id';
#     TERMS_TEXT = 'terms_text';
#     TERMS_URL = 'terms_url';
#     TERMS_FILE = 'terms_file';
#     TERMS_APPLICABILITY = 'applicability';

#     // dynamic
#     TOTAL = 'total';
#     TOTAL_TIME = 'totalTime';
#     OWNER_FIRST_NAME = 'owner_fname';
#     OWNER_LAST_NAME = 'owner_lname';
#     OWNER_FULL_NAME_ALIAS = 'owner_name';
#     OWNER_USER_ID = 'owner_id';
#     OWNER_PHONE = 'owner_phone';
#     OWNER_ORGANIZATION = 'owner_organization';
#     OWNER_POSITION = 'owner_position';
#     GROUP_NAME_ALIAS = 'group_name';
#     RESOURCE_NAME_ALIAS = 'resource_name';
#     RESOURCE_NAMES = 'resource_names';
#     SCHEDULE_NAME_ALIAS = 'schedule_name';
#     PARTICIPANT_LIST = 'participant_list';
#     INVITEE_LIST = 'invitee_list';
#     ATTRIBUTE_LIST = 'attribute_list';
#     RESOURCE_ATTRIBUTE_LIST = 'resource_attribute_list';
#     RESOURCE_TYPE_ATTRIBUTE_LIST = 'resource_type_attribute_list';
#     USER_ATTRIBUTE_LIST = 'user_attribute_list';
#     RESOURCE_ACCESSORY_LIST = 'resource_accessory_list';
#     RESOURCE_GROUP_LIST = 'group_list';
#     GROUP_LIST = 'owner_group_list';
#     START_REMINDER_MINUTES_PRIOR = 'start_reminder_minutes';
#     END_REMINDER_MINUTES_PRIOR = 'end_reminder_minutes';
#     DURATION_ALIAS = 'duration';
#     DURATION_HOURS = 'duration_in_hours';
#     GROUP_IDS = 'group_ids';
#     RESOURCE_IDS = 'resource_ids';
#     GUEST_LIST = 'guest_list';
#     USER_GROUP_LIST = 'user_group_list';
#     GROUP_ROLE_LIST = 'group_role_list';
#     UTILIZATION_TYPE = 'utilization_type';
#     DATE = 'date';
#     UTILIZATION = 'utilization';

#     // shared
#     ALLOW_CALENDAR_SUBSCRIPTION = 'allow_calendar_subscription';
#     PUBLIC_ID = 'public_id';
#     RESOURCE_ADMIN_GROUP_ID_RESERVATIONS = 'resource_admin_group_id';
#     SCHEDULE_ADMIN_GROUP_ID_RESERVATIONS = 'schedule_admin_group_id';
# }




from enum import Enum

class ColumnNames(str, Enum):
    USER_ID = 'user_id'
    USERNAME = 'username'
    EMAIL = 'email'
    FIRST_NAME = 'fname'
    LAST_NAME = 'lname'
    PASSWORD = 'password'
    OLD_PASSWORD = 'legacypassword'
    USER_CREATED = 'date_created'
    USER_MODIFIED = 'last_modified'
    USER_STATUS_ID = 'status_id'
    HOMEPAGE_ID = 'homepageid'
    LAST_LOGIN = 'lastlogin'
    TIMEZONE_NAME = 'timezone'
    LANGUAGE_CODE = 'language' 
    SALT = 'salt'
    PHONE_NUMBER = 'phone'
    ORGANIZATION = 'organization'
    POSITION = 'position'
    DEFAULT_SCHEDULE_ID = 'default_schedule_id'
    USER_PREFERENCES = 'preferences'
    USER_STATUS = 'status_id'

    
    ADDRESS_ID = 'address_id'

     
    PREFERENCE_NAME = 'name'
    PREFERENCE_VALUE = 'value'

    
    ROLE_LEVEL = 'role_level'
    ROLE_ID = 'role_id'
    ROLE_NAME = 'name'

     
    ANNOUNCEMENT_ID = 'announcementid'
    ANNOUNCEMENT_PRIORITY = 'priority'
    ANNOUNCEMENT_START = 'start_date'
    ANNOUNCEMENT_END = 'end_date'
    ANNOUNCEMENT_TEXT = 'announcement_text'
    ANNOUNCEMENT_DISPLAY_PAGE = 'display_page'

    
    GROUP_ID = 'group_id'
    GROUP_NAME = 'name'
    GROUP_ADMIN_GROUP_ID = 'admin_group_id'
    GROUP_ADMIN_GROUP_NAME = 'admin_group_name'
    GROUP_ISDEFAULT = 'isdefault'

    
    RESOURCE_GROUP_ID = 'resource_group_id'
    RESOURCE_GROUP_NAME = 'resource_group_name'
    RESOURCE_GROUP_PARENT_ID = 'parent_id'


    BLOCK_DAY_OF_WEEK = 'day_of_week'
    BLOCK_LABEL = 'label'
    BLOCK_LABEL_END = 'end_label'
    BLOCK_CODE = 'availability_code'
    BLOCK_TIMEZONE = 'timezone'
    LAYOUT_TYPE = 'layout_type'

    
    BLOCK_START = 'start_time'
    BLOCK_END = 'end_time'

    CUSTOM_ATTRIBUTE_ID = 'custom_attribute_id'
    CUSTOM_ATTRIBUTE_VALUE = 'attribute_value'


    RESERVATION_USER = 'user_id'
    RESERVATION_GROUP = 'group_id'
    RESERVATION_CREATED = 'date_created'
    RESERVATION_MODIFIED = 'last_modified'
    RESERVATION_TYPE = 'type_id'
    RESERVATION_TITLE = 'title'
    RESERVATION_DESCRIPTION = 'description'
    RESERVATION_COST = 'total_cost'
    RESERVATION_PARENT_ID = 'parent_id'
    REPEAT_TYPE = 'repeat_type'
    REPEAT_OPTIONS = 'repeat_options'
    RESERVATION_STATUS = 'status_id'
    SERIES_ID = 'series_id'
    RESERVATION_OWNER = 'owner_id'
    RESERVATION_ALLOW_PARTICIPATION = 'allow_participation'
    RESERVATION_TERMS_ACCEPTANCE_DATE = 'terms_date_accepted'
    RESERVATION_SERIES_ID = 'series_id'

      
    RESERVATION_INSTANCE_ID = 'reservation_instance_id'
    RESERVATION_START = 'start_date'
    RESERVATION_END = 'end_date'
    REFERENCE_NUMBER = 'reference_number'
    CHECKIN_DATE = 'checkin_date'
    CHECKOUT_DATE = 'checkout_date'
    PREVIOUS_END_DATE = 'previous_end_date'

     
    RESERVATION_USER_LEVEL = 'reservation_user_level'

    
    RESOURCE_ID = 'resource_id'
    RESOURCE_NAME = 'name'
    RESOURCE_LOCATION = 'location'
    RESOURCE_CONTACT = 'contact_info'
    RESOURCE_DESCRIPTION = 'description'
    RESOURCE_NOTES = 'notes'
    RESOURCE_MINDURATION = 'min_duration'
    RESOURCE_MININCREMENT = 'min_increment'
    RESOURCE_MAXDURATION = 'max_duration'
    RESOURCE_COST = 'unit_cost'
    RESOURCE_AUTOASSIGN = 'autoassign'
    RESOURCE_REQUIRES_APPROVAL = 'requires_approval'
    RESOURCE_ALLOW_MULTIDAY = 'allow_multiday_reservations'
    RESOURCE_MAX_PARTICIPANTS = 'max_participants'
    RESOURCE_MINNOTICE_ADD = 'min_notice_time_add'
    RESOURCE_MINNOTICE_UPDATE = 'min_notice_time_update'
    RESOURCE_MINNOTICE_DELETE = 'min_notice_time_delete'
    RESOURCE_MAXNOTICE = 'max_notice_time'
    RESOURCE_IMAGE_NAME = 'image_name'
    RESOURCE_STATUS_ID = 'status_id'
    RESOURCE_STATUS_ID_ALIAS = 'resource_status_id'
    RESOURCE_STATUS_REASON_ID = 'resource_status_reason_id'
    RESOURCE_STATUS_DESCRIPTION = 'description'
    RESOURCE_ADMIN_GROUP_ID = 'admin_group_id'
    RESOURCE_SORT_ORDER = 'sort_order'
    RESOURCE_BUFFER_TIME = 'buffer_time'
    ENABLE_CHECK_IN = 'enable_check_in'
    AUTO_RELEASE_MINUTES = 'auto_release_minutes'
    RESOURCE_ALLOW_DISPLAY = 'allow_display'
    RESOURCE_IMAGE_LIST = 'image_list'
    PERMISSION_TYPE = 'permission_type'
    RESOURCE_ADDITIONAL_PROPERTIES = 'additional_properties'

     
    RESOURCE_LEVEL_ID = 'resource_level_id'

     
    SCHEDULE_ID = 'schedule_id'
    SCHEDULE_NAME = 'name'
    SCHEDULE_DEFAULT = 'isdefault'
    SCHEDULE_WEEKDAY_START = 'weekdaystart'
    SCHEDULE_DAYS_VISIBLE = 'daysvisible'
    LAYOUT_ID = 'layout_id'
    SCHEDULE_ADMIN_GROUP_ID = 'admin_group_id'
    SCHEDULE_ADMIN_GROUP_ID_ALIAS = 's_admin_group_id'
    SCHEDULE_AVAILABLE_START_DATE = 'start_date'
    SCHEDULE_AVAILABLE_END_DATE = 'end_date'
    SCHEDULE_ALLOW_CONCURRENT_RESERVATIONS = 'allow_concurrent_bookings'
    SCHEDULE_DEFAULT_STYLE = 'default_layout'
    TOTAL_CONCURRENT_RESERVATIONS = 'total_concurrent_reservations'
    MAX_RESOURCES_PER_RESERVATION = 'max_resources_per_reservation'

    
    EVENT_CATEGORY = 'event_category'
    EVENT_TYPE = 'event_type'

    REPEAT_START = 'repeat_start'
    REPEAT_END = 'repeat_end'

     
    QUOTA_ID = 'quota_id'
    QUOTA_LIMIT = 'quota_limit'
    QUOTA_UNIT = 'unit'
    QUOTA_DURATION = 'duration'
    ENFORCED_START_TIME = 'enforced_time_start'
    ENFORCED_END_TIME = 'enforced_time_end'
    ENFORCED_DAYS = 'enforced_days'
    QUOTA_SCOPE = 'scope'

    
    ACCESSORY_ID = 'accessory_id'
    ACCESSORY_NAME = 'accessory_name'
    ACCESSORY_QUANTITY = 'accessory_quantity'
    ACCESSORY_RESOURCE_COUNT = 'num_resources'
    ACCESSORY_MINIMUM_QUANTITY = 'minimum_quantity'
    ACCESSORY_MAXIMUM_QUANTITY = 'maximum_quantity'

     
    QUANTITY = 'quantity'

    
    BLACKOUT_INSTANCE_ID = 'blackout_instance_id'
    BLACKOUT_START = 'start_date'
    BLACKOUT_END = 'end_date'
    BLACKOUT_TITLE = 'title'
    BLACKOUT_DESCRIPTION = 'description'
    BLACKOUT_SERIES_ID = 'blackout_series_id'
    ATTRIBUTE_ID = 'custom_attribute_id'
    ATTRIBUTE_ADMIN_ONLY = 'admin_only'
    ATTRIBUTE_LABEL = 'display_label'
    ATTRIBUTE_TYPE = 'display_type'
    ATTRIBUTE_CATEGORY = 'attribute_category'
    ATTRIBUTE_CONSTRAINT = 'validation_regex'
    ATTRIBUTE_REQUIRED = 'is_required'
    ATTRIBUTE_POSSIBLE_VALUES = 'possible_values'
    ATTRIBUTE_VALUE = 'attribute_value'
    ATTRIBUTE_ENTITY_ID = 'entity_id'
    ATTRIBUTE_ENTITY_IDS = 'entity_ids'
    ATTRIBUTE_ENTITY_DESCRIPTIONS = 'entity_descriptions'
    ATTRIBUTE_SORT_ORDER = 'sort_order'
    ATTRIBUTE_SECONDARY_CATEGORY = 'secondary_category'
    ATTRIBUTE_SECONDARY_ENTITY_IDS = 'secondary_entity_ids'
    ATTRIBUTE_SECONDARY_ENTITY_DESCRIPTIONS = 'secondary_entity_descriptions'
    ATTRIBUTE_IS_PRIVATE = 'is_private'

    
    FILE_ID = 'file_id'
    FILE_NAME = 'file_name'
    FILE_TYPE = 'file_type'
    FILE_SIZE = 'file_size'
    FILE_EXTENSION = 'file_extension'


    REPORT_ID = 'saved_report_id'
    REPORT_NAME = 'report_name'
    DATE_CREATED = 'date_created'
    REPORT_DETAILS = 'report_details'

    
    SESSION_TOKEN = 'session_token'
    USER_SESSION = 'user_session_value'
    SESSION_LAST_MODIFIED = 'last_modified'

    
    REMINDER_ID = 'reminder_id'
    REMINDER_SENDTIME = 'sendtime'
    REMINDER_MESSAGE = 'message'
    REMINDER_USER_ID = 'user_id'
    REMINDER_ADDRESS = 'address'
    REMINDER_REFNUMBER = 'refnumber'
    REMINDER_MINUTES_PRIOR = 'minutes_prior'
    REMINDER_TYPE = 'reminder_type'

     
    RESOURCE_TYPE_ID = 'resource_type_id'
    RESOURCE_TYPE_NAME = 'resource_type_name'
    RESOURCE_TYPE_DESCRIPTION = 'resource_type_description'

     
    VERSION_NUMBER = 'version_number'
    VERSION_DATE = 'version_date'

     
    REQUIRED_VALUE = 'required_value'
    RESERVATION_COLOR = 'color'
    RESERVATION_COLOR_RULE_ID = 'reservation_color_rule_id'
    COLOR_ATTRIBUTE_TYPE = 'attribute_type'
    COMPARISON_TYPE = 'comparison_type'

    
    CREDIT_COUNT = 'credit_count'
    PEAK_CREDIT_COUNT = 'peak_credit_count'
    CREDIT_NOTE = 'credit_note'
    ORIGINAL_CREDIT_COUNT = 'original_credit_count'

    PEAK_TIMES_ID = 'peak_times_id'
    PEAK_ALL_DAY = 'all_day'
    PEAK_START_TIME = 'start_time'
    PEAK_END_TIME = 'end_time'
    PEAK_EVERY_DAY = 'every_day'
    PEAK_DAYS = 'peak_days'
    PEAK_ALL_YEAR = 'all_year'
    PEAK_BEGIN_MONTH = 'begin_month'
    PEAK_BEGIN_DAY = 'begin_day'
    PEAK_END_MONTH = 'end_month'
    PEAK_END_DAY = 'end_day'

     
    RESERVATION_WAITLIST_REQUEST_ID = 'reservation_waitlist_request_id'

    
    CREDIT_COST = 'credit_cost'
    CREDIT_CURRENCY = 'credit_currency'


    GATEWAY_TYPE = 'gateway_type'
    GATEWAY_SETTING_NAME = 'setting_name'
    GATEWAY_SETTING_VALUE = 'setting_value'

    
    TRANSACTION_LOG_ID = 'payment_transaction_log_id'
    TRANSACTION_LOG_STATUS = 'status'
    TRANSACTION_LOG_INVOICE = 'invoice_number'
    TRANSACTION_LOG_TRANSACTION_ID = 'transaction_id'
    TRANSACTION_LOG_TOTAL = 'total_amount'
    TRANSACTION_LOG_FEE = 'transaction_fee'
    TRANSACTION_LOG_CURRENCY = 'currency'
    TRANSACTION_LOG_TRANSACTION_HREF = 'transaction_href'
    TRANSACTION_LOG_REFUND_HREF = 'refund_href'
    TRANSACTION_LOG_GATEWAY_NAME = 'gateway_name'
    TRANSACTION_LOG_GATEWAY_DATE = 'gateway_date_created'
    TRANSACTION_LOG_REFUND_AMOUNT = 'refund_amount'

     
    TERMS_ID = 'terms_of_service_id'
    TERMS_TEXT = 'terms_text'
    TERMS_URL = 'terms_url'
    TERMS_FILE = 'terms_file'
    TERMS_APPLICABILITY = 'applicability'

     
    TOTAL = 'total'
    TOTAL_TIME = 'totalTime'
    OWNER_FIRST_NAME = 'owner_fname'
    OWNER_LAST_NAME = 'owner_lname'
    OWNER_FULL_NAME_ALIAS = 'owner_name'
    OWNER_USER_ID = 'owner_id'
    OWNER_PHONE = 'owner_phone'
    OWNER_ORGANIZATION = 'owner_organization'
    OWNER_POSITION = 'owner_position'
    GROUP_NAME_ALIAS = 'group_name'
    RESOURCE_NAME_ALIAS = 'resource_name'
    RESOURCE_NAMES = 'resource_names'
    SCHEDULE_NAME_ALIAS = 'schedule_name'
    PARTICIPANT_LIST = 'participant_list'
    INVITEE_LIST = 'invitee_list'
    ATTRIBUTE_LIST = 'attribute_list'
    RESOURCE_ATTRIBUTE_LIST = 'resource_attribute_list'
    RESOURCE_TYPE_ATTRIBUTE_LIST = 'resource_type_attribute_list'
    USER_ATTRIBUTE_LIST = 'user_attribute_list'
    RESOURCE_ACCESSORY_LIST = 'resource_accessory_list'
    RESOURCE_GROUP_LIST = 'group_list'
    GROUP_LIST = 'owner_group_list'
    START_REMINDER_MINUTES_PRIOR = 'start_reminder_minutes'
    END_REMINDER_MINUTES_PRIOR = 'end_reminder_minutes'
    DURATION_ALIAS = 'duration'
    DURATION_HOURS = 'duration_in_hours'
    GROUP_IDS = 'group_ids'
    RESOURCE_IDS = 'resource_ids'
    GUEST_LIST = 'guest_list'
    USER_GROUP_LIST = 'user_group_list'
    GROUP_ROLE_LIST = 'group_role_list'
    UTILIZATION_TYPE = 'utilization_type'
    DATE = 'date'
    UTILIZATION = 'utilization'

     
    ALLOW_CALENDAR_SUBSCRIPTION = 'allow_calendar_subscription'
    PUBLIC_ID = 'public_id'
    RESOURCE_ADMIN_GROUP_ID_RESERVATIONS = 'resource_admin_group_id'
    SCHEDULE_ADMIN_GROUP_ID_RESERVATIONS = 'schedule_admin_group_id'
    # other constants
    
    @staticmethod
    def get_column(name: str) -> str:
        return ColumnNames(name).value