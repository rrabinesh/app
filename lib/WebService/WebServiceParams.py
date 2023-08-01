# <?php

# class WebServiceParams
# {
#     public const AccessoryId = 'accessoryId';
#     public const AttributeId = 'attributeId';
#     public const AttributeCategoryId = 'categoryId';
#     public const GroupId = 'groupId';
#     public const ReferenceNumber = 'referenceNumber';
#     public const ResourceId = 'resourceId';
#     public const ScheduleId = 'scheduleId';
#     public const UserId = 'userId';
# }

from pydantic import BaseModel

class WebServiceParams(BaseModel):
    AccessoryId: str = 'accessoryId'
    AttributeId: str = 'attributeId'
    AttributeCategoryId: str = 'categoryId'
    GroupId: str = 'groupId'
    ReferenceNumber: str = 'referenceNumber'
    ResourceId: str = 'resourceId'
    ScheduleId: str = 'scheduleId'
    UserId: str = 'userId'

