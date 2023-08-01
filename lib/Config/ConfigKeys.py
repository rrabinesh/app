# <?php

# class ConfigKeys
# {
#     public const ADMIN_EMAIL = 'admin.email';
#     public const ADMIN_EMAIL_NAME = 'admin.email.name';
#     public const COMPANY_NAME = 'company.name';
#     public const COMPANY_URL = 'company.url';
#     public const ALLOW_REGISTRATION = 'allow.self.registration';
#     public const CREDITS_ENABLED = 'enabled';
#     public const CREDITS_ALLOW_PURCHASE = 'allow.purchase';
#     public const CSS_EXTENSION_FILE = 'css.extension.file';
#     public const DEFAULT_HOMEPAGE = 'default.homepage';
#     public const DEFAULT_PAGE_SIZE = 'default.page.size';
#     public const DISABLE_PASSWORD_RESET = 'disable.password.reset';
#     public const ENABLE_EMAIL = 'enable.email';
#     public const HOME_URL = 'home.url';
#     public const INACTIVITY_TIMEOUT = 'inactivity.timeout';
#     public const LANGUAGE = 'default.language';
#     public const LOGOUT_URL = 'logout.url';
#     public const NAME_FORMAT = 'name.format';
#     public const SCRIPT_URL = 'script.url';
#     public const DEFAULT_TIMEZONE = 'default.timezone';
#     public const REGISTRATION_ENABLE_CAPTCHA = 'registration.captcha.enabled';
#     public const REGISTRATION_REQUIRE_ACTIVATION = 'registration.require.email.activation';
#     public const REGISTRATION_AUTO_SUBSCRIBE_EMAIL = 'registration.auto.subscribe.email';
#     public const REGISTRATION_NOTIFY = 'registration.notify.admin';

#     public const VERSION = 'version';

#     public const SCHEDULE_SHOW_INACCESSIBLE_RESOURCES = 'show.inaccessible.resources';
#     public const SCHEDULE_RESERVATION_LABEL = 'reservation.label';
#     public const SCHEDULE_HIDE_BLOCKED_PERIODS = 'hide.blocked.periods';
#     public const SCHEDULE_UPDATE_HIGHLIGHT_MINUTES = 'update.highlight.minutes';
#     public const SCHEDULE_SHOW_WEEK_NUMBERS = 'show.week.numbers';

#     public const DATABASE_TYPE = 'type';
#     public const DATABASE_USER = 'user';
#     public const DATABASE_PASSWORD = 'password';
#     public const DATABASE_HOSTSPEC = 'hostspec';
#     public const DATABASE_NAME = 'name';

#     public const PLUGIN_AUTHENTICATION = 'Authentication';
#     public const PLUGIN_AUTHORIZATION = 'Authorization';
#     public const PLUGIN_PERMISSION = 'Permission';
#     public const PLUGIN_POSTREGISTRATION = 'PostRegistration';
#     public const PLUGIN_PRERESERVATION = 'PreReservation';
#     public const PLUGIN_POSTRESERVATION = 'PostReservation';

#     public const RESERVATION_START_TIME_CONSTRAINT = 'start.time.constraint';
#     public const RESERVATION_UPDATES_REQUIRE_APPROVAL = 'updates.require.approval';
#     public const RESERVATION_PREVENT_PARTICIPATION = 'prevent.participation';
#     public const RESERVATION_PREVENT_RECURRENCE = 'prevent.recurrence';
#     public const RESERVATION_REMINDERS_ENABLED = 'enable.reminders';
#     public const RESERVATION_ALLOW_GUESTS = 'allow.guest.participation';
#     public const RESERVATION_ALLOW_WAITLIST = 'allow.wait.list';
#     public const RESERVATION_CHECKIN_MINUTES = 'checkin.minutes.prior';
#     public const RESERVATION_START_REMINDER = 'default.start.reminder';
#     public const RESERVATION_END_REMINDER = 'default.end.reminder';
#     public const RESERVATION_TITLE_REQUIRED = 'title.required';
#     public const RESERVATION_DESCRIPTION_REQUIRED = 'description.required';
#     public const RESERVATION_CHECKIN_ADMIN_ONLY = 'checkin.admin.only';
#     public const RESERVATION_CHECKOUT_ADMIN_ONLY = 'checkout.admin.only';

#     public const IMAGE_UPLOAD_DIRECTORY = 'image.upload.directory';
#     public const IMAGE_UPLOAD_URL = 'image.upload.url';

#     public const CACHE_TEMPLATES = 'cache.templates';

#     public const USE_LOCAL_JS = 'use.local.js.libs';

#     public const INSTALLATION_PASSWORD = 'install.password';

#     public const ICS_SUBSCRIPTION_KEY = 'subscription.key';
#     public const ICS_FUTURE_DAYS = 'future.days';
#     public const ICS_PAST_DAYS = 'past.days';

#     public const PRIVACY_HIDE_USER_DETAILS = 'hide.user.details';
#     public const PRIVACY_HIDE_RESERVATION_DETAILS = 'hide.reservation.details';
#     public const PRIVACY_VIEW_RESERVATIONS = 'view.reservations';
#     public const PRIVACY_VIEW_SCHEDULES = 'view.schedules';
#     public const PRIVACY_ALLOW_GUEST_BOOKING = 'allow.guest.reservations';

#     public const NOTIFY_CREATE_RESOURCE_ADMINS = 'resource.admin.add';
#     public const NOTIFY_CREATE_APPLICATION_ADMINS = 'application.admin.add';
#     public const NOTIFY_CREATE_GROUP_ADMINS = 'group.admin.add';

#     public const NOTIFY_UPDATE_RESOURCE_ADMINS = 'resource.admin.update';
#     public const NOTIFY_UPDATE_APPLICATION_ADMINS = 'application.admin.update';
#     public const NOTIFY_UPDATE_GROUP_ADMINS = 'group.admin.update';

#     public const NOTIFY_DELETE_RESOURCE_ADMINS = 'resource.admin.delete';
#     public const NOTIFY_DELETE_APPLICATION_ADMINS = 'application.admin.delete';
#     public const NOTIFY_DELETE_GROUP_ADMINS = 'group.admin.delete';

#     public const NOTIFY_APPROVAL_RESOURCE_ADMINS = 'resource.admin.approval';
#     public const NOTIFY_APPROVAL_APPLICATION_ADMINS = 'application.admin.approval';
#     public const NOTIFY_APPROVAL_GROUP_ADMINS = 'group.admin.approval';

#     public const UPLOAD_ENABLE_RESERVATION_ATTACHMENTS = 'enable.reservation.attachments';
#     public const UPLOAD_RESERVATION_ATTACHMENTS = 'reservation.attachment.path';
#     public const UPLOAD_RESERVATION_EXTENSIONS = 'reservation.attachment.extensions';

#     public const PAGES_ENABLE_CONFIGURATION = 'enable.configuration';

#     public const API_ENABLED = 'enabled';
#     public const RECAPTCHA_ENABLED = 'enabled';
#     public const RECAPTCHA_PUBLIC_KEY = 'public.key';
#     public const RECAPTCHA_PRIVATE_KEY = 'private.key';

#     public const DEFAULT_FROM_ADDRESS = 'default.from.address';
#     public const DEFAULT_FROM_NAME = 'default.from.name';

#     public const REPORTS_ALLOW_ALL = 'allow.all.users';

#     public const APP_TITLE = 'app.title';

#     public const SCHEDULE_PER_USER_COLORS = 'use.per.user.colors';

#     public const PASSWORD_UPPER_AND_LOWER = 'upper.and.lower';
#     public const PASSWORD_LETTERS = 'minimum.letters';
#     public const PASSWORD_NUMBERS = 'minimum.numbers';

#     public const RESERVATION_LABELS_ICS_SUMMARY = 'ics.summary';
#     public const RESERVATION_LABELS_MY_ICS_SUMMARY = 'ics.my.summary';
#     public const RESERVATION_LABELS_RSS_DESCRIPTION = 'rss.description';
#     public const RESERVATION_LABELS_MY_CALENDAR = 'my.calendar';
#     public const RESERVATION_LABELS_RESOURCE_CALENDAR = 'resource.calendar';
#     public const RESERVATION_LABELS_RESERVATION_POPUP = 'reservation.popup';

#     public const SECURITY_HEADERS = 'security.headers';
#     public const SECURITY_STRICT_TRANSPORT = 'security.strict-transport';
#     public const SECURITY_X_FRAME = 'security.x-frame';
#     public const SECURITY_X_XSS = 'security.x-xss';
#     public const SECURITY_X_CONTENT_TYPE = 'security.x-content-type';
#     public const SECURITY_CONTENT_SECURITY_POLICY = 'security.content-security-policy';

#     public const GOOGLE_ANALYTICS_TRACKING_ID = 'tracking.id';

#     public const AUTHENTICATION_ALLOW_FACEBOOK = 'allow.facebook.login';
#     public const AUTHENTICATION_ALLOW_GOOGLE = 'allow.google.login';
#     public const AUTHENTICATION_REQUIRED_EMAIL_DOMAINS = 'required.email.domains';
#     public const AUTHENTICATION_HIDE_BOOKED_LOGIN_PROMPT = 'hide.booked.login.prompt';
#     public const AUTHENTICATION_CAPTCHA_ON_LOGIN = 'captcha.on.login';

#     public const SLACK_TOKEN = 'token';

#     public const TABLET_VIEW_ALLOW_GUESTS = 'allow.guest.reservations';
#     public const TABLET_VIEW_AUTOCOMPLETE = 'auto.suggest.emails';

#     public const USE_DATABASE_SESSION = 'use.database.session';

#     public const REGISTRATION_REQUIRE_PHONE = 'require.phone';
#     public const REGISTRATION_REQUIRE_ORGANIZATION = 'require.organization';
#     public const REGISTRATION_REQUIRE_POSITION = 'require.position';
    
#     public const LOGGING_FOLDER = 'folder';
#     public const LOGGING_LEVEL = 'level';
#     public const LOGGING_SQL = 'sql';

# }

# class ConfigSection
# {
#     public const API = 'api';
#     public const AUTHENTICATION = 'authentication';
#     public const CREDITS = 'credits';
#     public const DATABASE = 'database';
#     public const EMAIL = 'email';
#     public const ICS = 'ics';
#     public const PAGES = 'pages';
#     public const PASSWORD = 'password';
#     public const PLUGINS = 'plugins';
#     public const PRIVACY = 'privacy';
#     public const REPORTS = 'reports';
#     public const RESERVATION = 'reservation';
#     public const RESERVATION_LABELS = 'reservation.labels';
#     public const RESERVATION_NOTIFY = 'reservation.notify';
#     public const SCHEDULE = 'schedule';
#     public const SECURITY = 'security';
#     public const UPLOADS = 'uploads';
#     public const RECAPTCHA = 'recaptcha';
#     public const USERS = 'users';
#     public const GOOGLE_ANALYTICS = 'google.analytics';
#     public const PAYMENTS = 'payments';
#     public const SLACK = 'slack';
#     public const TABLET_VIEW = 'tablet.view';
#     public const REGISTRATION = 'registration';
#     public const LOGGING = 'logging';
# }

from fastapi import FastAPI
from typing import List

class ConfigKeys:
    # Define all the configuration keys as class variables
    ADMIN_EMAIL = 'admin.email'
    ADMIN_EMAIL_NAME = 'admin.email.name'
    COMPANY_NAME = 'company.name'
    COMPANY_URL = 'company.url'
    ALLOW_REGISTRATION = 'allow.self.registration'
    CREDITS_ENABLED = 'enabled'
    CREDITS_ALLOW_PURCHASE = 'allow.purchase'
    CSS_EXTENSION_FILE = 'css.extension.file'
    DEFAULT_HOMEPAGE = 'default.homepage'
    DEFAULT_PAGE_SIZE = 'default.page.size'
    DISABLE_PASSWORD_RESET = 'disable.password.reset'
    ENABLE_EMAIL = 'enable.email'
    HOME_URL = 'home.url'
    INACTIVITY_TIMEOUT = 'inactivity.timeout'
    LANGUAGE = 'default.language'
    LOGOUT_URL = 'logout.url'
    NAME_FORMAT = 'name.format'
    SCRIPT_URL = 'script.url'
    DEFAULT_TIMEZONE = 'default.timezone'
    REGISTRATION_ENABLE_CAPTCHA = 'registration.captcha.enabled'
    REGISTRATION_REQUIRE_ACTIVATION = 'registration.require.email.activation'
    REGISTRATION_AUTO_SUBSCRIBE_EMAIL = 'registration.auto.subscribe.email'
    REGISTRATION_NOTIFY = 'registration.notify.admin'

    VERSION = 'version'

    SCHEDULE_SHOW_INACCESSIBLE_RESOURCES = 'show.inaccessible.resources'
    SCHEDULE_RESERVATION_LABEL = 'reservation.label'
    SCHEDULE_HIDE_BLOCKED_PERIODS = 'hide.blocked.periods'
    SCHEDULE_UPDATE_HIGHLIGHT_MINUTES = 'update.highlight.minutes'
    SCHEDULE_SHOW_WEEK_NUMBERS = 'show.week.numbers'

    DATABASE_TYPE = 'type'
    DATABASE_USER = 'user'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOSTSPEC = 'hostspec'
    DATABASE_NAME = 'name'

    PLUGIN_AUTHENTICATION = 'Authentication'
    PLUGIN_AUTHORIZATION = 'Authorization'
    PLUGIN_PERMISSION = 'Permission'
    PLUGIN_POSTREGISTRATION = 'PostRegistration'
    PLUGIN_PRERESERVATION = 'PreReservation'
    PLUGIN_POSTRESERVATION = 'PostReservation'

    RESERVATION_START_TIME_CONSTRAINT = 'start.time.constraint'
    RESERVATION_UPDATES_REQUIRE_APPROVAL = 'updates.require.approval'
    RESERVATION_PREVENT_PARTICIPATION = 'prevent.participation'
    RESERVATION_PREVENT_RECURRENCE = 'prevent.recurrence'
    RESERVATION_REMINDERS_ENABLED = 'enable.reminders'
    RESERVATION_ALLOW_GUESTS = 'allow.guest.participation'
    RESERVATION_ALLOW_WAITLIST = 'allow.wait.list'
    RESERVATION_CHECKIN_MINUTES = 'checkin.minutes.prior'
    RESERVATION_START_REMINDER = 'default.start.reminder'
    RESERVATION_END_REMINDER = 'default.end.reminder'
    RESERVATION_TITLE_REQUIRED = 'title.required'
    RESERVATION_DESCRIPTION_REQUIRED = 'description.required'
    RESERVATION_CHECKIN_ADMIN_ONLY = 'checkin.admin.only'
    RESERVATION_CHECKOUT_ADMIN_ONLY = 'checkout.admin.only'

    IMAGE_UPLOAD_DIRECTORY = 'image.upload.directory'
    IMAGE_UPLOAD_URL = 'image.upload.url'

    CACHE_TEMPLATES = 'cache.templates'

    USE_LOCAL_JS = 'use.local.js.libs'

    INSTALLATION_PASSWORD = 'install.password'

    ICS_SUBSCRIPTION_KEY = 'subscription.key'
    ICS_FUTURE_DAYS = 'future.days'
    ICS_PAST_DAYS = 'past.days'

    PRIVACY_HIDE_USER_DETAILS = 'hide.user.details'
    PRIVACY_HIDE_RESERVATION_DETAILS = 'hide.reservation.details'
    PRIVACY_VIEW_RESERVATIONS = 'view.reservations'
    PRIVACY_VIEW_SCHEDULES = 'view.schedules'
    PRIVACY_ALLOW_GUEST_BOOKING = 'allow.guest.reservations'

    NOTIFY_CREATE_RESOURCE_ADMINS = 'resource.admin.add'
    NOTIFY_CREATE_APPLICATION_ADMINS = 'application.admin.add'
    NOTIFY_CREATE_GROUP_ADMINS = 'group.admin.add'

    NOTIFY_UPDATE_RESOURCE_ADMINS = 'resource.admin.update'
    NOTIFY_UPDATE_APPLICATION_ADMINS = 'application.admin.update'
    NOTIFY_UPDATE_GROUP_ADMINS = 'group.admin.update'

    NOTIFY_DELETE_RESOURCE_ADMINS = 'resource.admin.delete'
    NOTIFY_DELETE_APPLICATION_ADMINS = 'application.admin.delete'
    NOTIFY_DELETE_GROUP_ADMINS = 'group.admin.delete'

    NOTIFY_APPROVAL_RESOURCE_ADMINS = 'resource.admin.approval'
    NOTIFY_APPROVAL_APPLICATION_ADMINS = 'application.admin.approval'
    NOTIFY_APPROVAL_GROUP_ADMINS = 'group.admin.approval'

    UPLOAD_ENABLE_RESERVATION_ATTACHMENTS = 'enable.reservation.attachments'
    UPLOAD_RESERVATION_ATTACHMENTS = 'reservation.attachment.path'
    UPLOAD_RESERVATION_EXTENSIONS = 'reservation.attachment.extensions'

    PAGES_ENABLE_CONFIGURATION = 'enable.configuration'

    API_ENABLED = 'enabled'
    RECAPTCHA_ENABLED = 'enabled'
    RECAPTCHA_PUBLIC_KEY = 'public.key'
    RECAPTCHA_PRIVATE_KEY = 'private.key'

    DEFAULT_FROM_ADDRESS = 'default.from.address'
    DEFAULT_FROM_NAME = 'default.from.name'

    REPORTS_ALLOW_ALL = 'allow.all.users'

    APP_TITLE = 'app.title'

    SCHEDULE_PER_USER_COLORS = 'use.per.user.colors'

    PASSWORD_UPPER_AND_LOWER = 'upper.and.lower'
    PASSWORD_LETTERS = 'minimum.letters'
    PASSWORD_NUMBERS = 'minimum.numbers'

    RESERVATION_LABELS_ICS_SUMMARY = 'ics.summary'
    RESERVATION_LABELS_MY_ICS_SUMMARY = 'ics.my.summary'
    RESERVATION_LABELS_RSS_DESCRIPTION = 'rss.description'
    RESERVATION_LABELS_MY_CALENDAR = 'my.calendar'
    RESERVATION_LABELS_RESOURCE_CALENDAR = 'resource.calendar'
    RESERVATION_LABELS_RESERVATION_POPUP = 'reservation.popup'

    SECURITY_HEADERS = 'security.headers'
    SECURITY_STRICT_TRANSPORT = 'security.strict-transport'
    SECURITY_X_FRAME = 'security.x-frame'
    SECURITY_X_XSS = 'security.x-xss'
    SECURITY_X_CONTENT_TYPE = 'security.x-content-type'
    SECURITY_CONTENT_SECURITY_POLICY = 'security.content-security-policy'

    GOOGLE_ANALYTICS_TRACKING_ID = 'tracking.id'

    AUTHENTICATION_ALLOW_FACEBOOK = 'allow.facebook.login'
    AUTHENTICATION_ALLOW_GOOGLE = 'allow.google.login'
    AUTHENTICATION_REQUIRED_EMAIL_DOMAINS = 'required.email.domains'
    AUTHENTICATION_HIDE_BOOKED_LOGIN_PROMPT = 'hide.booked.login.prompt'
    AUTHENTICATION_CAPTCHA_ON_LOGIN = 'captcha.on.login'

    SLACK_TOKEN = 'token'

    TABLET_VIEW_ALLOW_GUESTS = 'allow.guest.reservations'
    TABLET_VIEW_AUTOCOMPLETE = 'auto.suggest.emails'

    USE_DATABASE_SESSION = 'use.database.session'

    REGISTRATION_REQUIRE_PHONE = 'require.phone'
    REGISTRATION_REQUIRE_ORGANIZATION = 'require.organization'
    REGISTRATION_REQUIRE_POSITION = 'require.position'
    
    LOGGING_FOLDER = 'folder'
    LOGGING_LEVEL = 'level'
    LOGGING_SQL = 'sql'
    # ... Add other keys ...

class ConfigSection:
    # Define all the configuration sections as class variables
    API = 'api'
    AUTHENTICATION = 'authentication'
    CREDITS = 'credits'
    DATABASE = 'database'
    EMAIL = 'email'
    ICS = 'ics'
    PAGES = 'pages'
    PASSWORD = 'password'
    PLUGINS = 'plugins'
    PRIVACY = 'privacy'
    REPORTS = 'reports'
    RESERVATION = 'reservation'
    RESERVATION_LABELS = 'reservation.labels'
    RESERVATION_NOTIFY = 'reservation.notify'
    SCHEDULE = 'schedule'
    SECURITY = 'security'
    UPLOADS = 'uploads'
    RECAPTCHA = 'recaptcha'
    USERS = 'users'
    GOOGLE_ANALYTICS = 'google.analytics'
    PAYMENTS = 'payments'
    SLACK = 'slack'
    TABLET_VIEW = 'tablet.view'
    REGISTRATION = 'registration'
    LOGGING = 'logging'
