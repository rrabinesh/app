# <?php

# class RoleLevel
# {
#     private function __construct()
#     {
#     }

#     public const NONE = null;
#     public const GROUP_ADMIN = 1;
#     public const APPLICATION_ADMIN = 2;
#     public const RESOURCE_ADMIN = 3;
#     public const SCHEDULE_ADMIN = 4;

#     /**
#      * @return RoleLevel[]
#      */
#     public static function All()
#     {
#         return [
#             RoleLevel::GROUP_ADMIN,
#             RoleLevel::APPLICATION_ADMIN,
#             RoleLevel::RESOURCE_ADMIN,
#             RoleLevel::SCHEDULE_ADMIN
#         ];
#     }
# }

from enum import Enum


class RoleLevel(Enum):
    NONE = None
    GROUP_ADMIN = 1
    APPLICATION_ADMIN = 2
    RESOURCE_ADMIN = 3
    SCHEDULE_ADMIN = 4

    @classmethod
    def all(cls):
        return [role for role in RoleLevel]
