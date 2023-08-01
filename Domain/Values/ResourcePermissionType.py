# <?php

# class ResourcePermissionType
# {
#     public const None = -1;
#     public const Full = 0;
#     public const View = 1;
# }

from enum import Enum

class ResourcePermissionType(Enum):
    none = -1
    Full = 0
    View = 1


