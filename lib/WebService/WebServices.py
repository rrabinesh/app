# <?php

# class WebServices
# {
#     public const AllAccessories = 'all_accessories';
#     public const AllAvailability = 'all_availability';
#     public const AllCustomAttributes = 'all_custom_attributes';
#     public const AllGroups = 'all_groups';
#     public const AllResources = 'all_resources';
#     public const AllReservations = 'all_reservations';
#     public const AllSchedules = 'all_schedules';
#     public const AllUsers = 'all_users';
#     public const ApproveReservation = 'approve_reservation';
#     public const CheckinReservation = 'checkin_reservation';
#     public const CheckoutReservation = 'checkout_reservation';
#     public const CreateCustomAttribute = 'create_custom_attribute';
#     public const CreateReservation = 'create_reservation';
#     public const CreateResource = 'create_resource';
#     public const CreateUser = 'create_user';
#     public const CreateGroup = 'create_group';
#     public const DeleteCustomAttribute = 'delete_custom_attribute';
#     public const DeleteReservation = 'delete_reservation';
#     public const DeleteResource = 'delete_resource';
#     public const DeleteUser = 'delete_user';
#     public const DeleteGroup = 'delete_group';
#     public const Login = 'login';
#     public const Logout = 'logout';
#     public const GetAccessory = 'get_accessory';
#     public const GetCustomAttribute = 'get_custom_attribute';
#     public const GetGroup = 'get_group';
#     public const GetReservation = 'get_reservation';
#     public const GetResource = 'get_resource';
#     public const GetResourceAvailability = 'get_resource_availability';
#     public const GetResourceGroups = 'get_resource_groups';
#     public const GetSchedule = 'get_schedule';
#     public const GetScheduleSlots = 'get_schedule_reservations';
#     public const GetUser = 'get_user';
#     public const GetUserByEmail = 'get_user_by_email';
#     public const UpdateCustomAttribute = 'update_custom_attribute';
#     public const UpdateReservation = 'update_reservation';
#     public const UpdateResource = 'update_resource';
#     public const UpdatePassword = 'update_password';
#     public const UpdateUser = 'update_user';
#     public const UpdateGroup = 'update_group';
#     public const UpdateGroupRoles = 'update_group_roles';
#     public const UpdateGroupPermissions = 'update_group_permissions';
#     public const UpdateGroupUsers = 'update_group_users';
#     public const GetStatuses = 'get_resource_statuses';
#     public const GetStatusReasons = 'get_resource_status_reasons';
#     public const GetAccount = 'get_user_account';
#     public const CreateAccount = 'create_user_account';
#     public const UpdateAccount = 'update_user_account';
#     public const UpdateAccountPassword = 'update_user_account_password';
# }

from enum import Enum

class WebServices(str, Enum):
    AllAccessories = 'all_accessories'
    AllAvailability = 'all_availability'
    AllCustomAttributes = 'all_custom_attributes'
    AllGroups = 'all_groups'
    AllResources = 'all_resources'
    AllReservations = 'all_reservations'
    AllSchedules = 'all_schedules'
    AllUsers = 'all_users'
    ApproveReservation = 'approve_reservation'
    CheckinReservation = 'checkin_reservation'
    CheckoutReservation = 'checkout_reservation'
    CreateCustomAttribute = 'create_custom_attribute'
    CreateReservation = 'create_reservation'
    CreateResource = 'create_resource'
    CreateUser = 'create_user'
    CreateGroup = 'create_group'
    DeleteCustomAttribute = 'delete_custom_attribute'
    DeleteReservation = 'delete_reservation'
    DeleteResource = 'delete_resource'
    DeleteUser = 'delete_user'
    DeleteGroup = 'delete_group'
    Login = 'login'
    Logout = 'logout'
    GetAccessory = 'get_accessory'
    GetCustomAttribute = 'get_custom_attribute'
    GetGroup = 'get_group'
    GetReservation = 'get_reservation'
    GetResource = 'get_resource'
    GetResourceAvailability = 'get_resource_availability'
    GetResourceGroups = 'get_resource_groups'
    GetSchedule = 'get_schedule'
    GetScheduleSlots = 'get_schedule_reservations'
    GetUser = 'get_user'
    GetUserByEmail = 'get_user_by_email'
    UpdateCustomAttribute = 'update_custom_attribute'
    UpdateReservation = 'update_reservation'
    UpdateResource = 'update_resource'
    UpdatePassword = 'update_password'
    UpdateUser = 'update_user'
    UpdateGroup = 'update_group'
    UpdateGroupRoles = 'update_group_roles'
    UpdateGroupPermissions = 'update_group_permissions'
    UpdateGroupUsers = 'update_group_users'
    GetStatuses = 'get_resource_statuses'
    GetStatusReasons = 'get_resource_status_reasons'
    GetAccount = 'get_user_account'
    CreateAccount = 'create_user_account'
    UpdateAccount = 'update_user_account'
    UpdateAccountPassword = 'update_user_account_password'


