# <?php

# interface IResourceRepository
# {
#     /**
#      * Gets all Resources for the given scheduleId
#      *
#      * @param int $scheduleId
#      * @return array|BookableResource[]
#      */
#     public function GetScheduleResources($scheduleId);

#     /**
#      * @param int $resourceId
#      * @return BookableResource
#      */
#     public function LoadById($resourceId);

#     /**
#      * @param string $publicId
#      * @return BookableResource
#      */
#     public function LoadByPublicId($publicId);

#     /**
#      * @param string $resourceName
#      * @return BookableResource
#      */
#     public function LoadByName($resourceName);

#     /**
#      * @param BookableResource $resource
#      * @return int ID of created resource
#      */
#     public function Add(BookableResource $resource);

#     /**
#      * @param BookableResource $resource
#      */
#     public function Update(BookableResource $resource);

#     /**
#      * @param BookableResource $resource
#      */
#     public function Delete(BookableResource $resource);

#     /**
#      * @return array|BookableResource[] array of all resources
#      */
#     public function GetResourceList();

#     /**
#      * @param int $pageNumber
#      * @param int $pageSize
#      * @param string|null $sortField
#      * @param string|null $sortDirection
#      * @param ISqlFilter $filter
#      * @return PageableData|BookableResource[]
#      */
#     public function GetList($pageNumber, $pageSize, $sortField = null, $sortDirection = null, $filter = null);

#     /**
#      * @param null|string $sortField
#      * @param null|string $sortDirection
#      * @return AccessoryDto[]|array all accessories
#      */
#     public function GetAccessoryList($sortField = null, $sortDirection = null);

#     /**
#      * @param int|null $scheduleId
#      * @param IResourceFilter|null $resourceFilter
#      * @return ResourceGroupTree
#      */
#     public function GetResourceGroups($scheduleId = null, $resourceFilter = null);

#     /**
#      * @param int $resourceId
#      * @param int $groupId
#      */
#     public function AddResourceToGroup($resourceId, $groupId);

#     /**
#      * @param int $resourceId
#      * @param int $groupId
#      */
#     public function RemoveResourceFromGroup($resourceId, $groupId);

#     /**
#      * @param ResourceGroup $group
#      * @return ResourceGroup
#      */
#     public function AddResourceGroup(ResourceGroup $group);

#     /**
#      * @param int $groupId
#      * @return ResourceGroup
#      */
#     public function LoadResourceGroup($groupId);

#     /**
#      * @param string $publicResourceGroupId
#      * @return ResourceGroup
#      */
#     public function LoadResourceGroupByPublicId($publicResourceGroupId);

#     /**
#      * @param ResourceGroup $group
#      */
#     public function UpdateResourceGroup(ResourceGroup $group);

#     /**
#      * @param $groupId
#      */
#     public function DeleteResourceGroup($groupId);

#     /**
#      * @return ResourceType[]|array
#      */
#     public function GetResourceTypes();

#     /**
#      * @param int $resourceTypeId
#      * @return ResourceType
#      */
#     public function LoadResourceType($resourceTypeId);

#     /**
#      * @param ResourceType $type
#      * @return int
#      */
#     public function AddResourceType(ResourceType $type);

#     /**
#      * @param ResourceType $type
#      */
#     public function UpdateResourceType(ResourceType $type);

#     /**
#      * @param int $id
#      */
#     public function RemoveResourceType($id);

#     /**
#      * @return ResourceStatusReason[]
#      */
#     public function GetStatusReasons();

#     /**
#      * @param int $statusId
#      * @param string $reasonDescription
#      * @return int
#      */
#     public function AddStatusReason($statusId, $reasonDescription);

#     /**
#      * @param int $reasonId
#      * @param string $reasonDescription
#      */
#     public function UpdateStatusReason($reasonId, $reasonDescription);

#     /**
#      * @param int $reasonId
#      */
#     public function RemoveStatusReason($reasonId);

#     /**
#      * @param int $resourceId
#      * @param int|null $pageNumber
#      * @param int|null $pageSize
#      * @param ISqlFilter|null $filter
#      * @param int $accountStatus
#      * @return PageableData|UserPermissionItemView[]
#      */
#     public function GetUsersWithPermission($resourceId, $pageNumber = null, $pageSize = null, $filter = null, $accountStatus = AccountStatus::ACTIVE);

#     /**
#      * @param int $resourceId
#      * @param int|null $pageNumber
#      * @param int|null $pageSize
#      * @param ISqlFilter|null $filter
#      * @param int $accountStatus
#      * @return PageableData|UserPermissionItemView[]
#      */
#     public function GetUsersWithPermissionsIncludingGroups($resourceId, $pageNumber = null, $pageSize = null, $filter = null, $accountStatus = AccountStatus::ACTIVE);

#     /**
#      * @param int $resourceId
#      * @param int|null $pageNumber
#      * @param int|null $pageSize
#      * @param ISqlFilter|null $filter
#      * @return PageableData|GroupPermissionItemView[]
#      */
#     public function GetGroupsWithPermission($resourceId, $pageNumber = null, $pageSize = null, $filter = null);

#     /**
#      * @param int $resourceId
#      * @param int $userId
#      * @param int $type
#      */
#     public function ChangeResourceUserPermission($resourceId, $userId, $type);

#     /**
#      * @param int $resourceId
#      * @param int $groupId
#      * @param int $type
#      */
#     public function ChangeResourceGroupPermission($resourceId, $groupId, $type);

#     /**
#      * @return array all public resource ids in key value id=>publicid
#      */
#     public function GetPublicResourceIds();
# }

from typing import List, Optional
from fastapi import FastAPI

app = FastAPI()

# Define your data models as Pydantic models if needed.


class BookableResource:
    # Define the fields and methods of the BookableResource class here.
    pass


class AccessoryDto:
    # Define the fields and methods of the AccessoryDto class here.
    pass


class ResourceGroupTree:
    # Define the fields and methods of the ResourceGroupTree class here.
    pass


class ResourceGroup:
    # Define the fields and methods of the ResourceGroup class here.
    pass


class ResourceType:
    # Define the fields and methods of the ResourceType class here.
    pass


class ResourceStatusReason:
    # Define the fields and methods of the ResourceStatusReason class here.
    pass


class UserPermissionItemView:
    # Define the fields and methods of the UserPermissionItemView class here.
    pass


class GroupPermissionItemView:
    # Define the fields and methods of the GroupPermissionItemView class here.
    pass


class IResourceRepository:
    # Define the repository methods here.

    def GetScheduleResources(self, scheduleId: int) -> List[BookableResource]:
        pass

    def LoadById(self, resourceId: int) -> BookableResource:
        pass

    def LoadByPublicId(self, publicId: str) -> BookableResource:
        pass

    def LoadByName(self, resourceName: str) -> BookableResource:
        pass

    def Add(self, resource: BookableResource) -> int:
        pass

    def Update(self, resource: BookableResource) -> None:
        pass

    def Delete(self, resource: BookableResource) -> None:
        pass

    def GetResourceList(self) -> List[BookableResource]:
        pass

    def GetList(
        self,
        pageNumber: int,
        pageSize: int,
        sortField: Optional[str] = None,
        sortDirection: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> List[BookableResource]:
        pass

    def GetAccessoryList(
        self,
        sortField: Optional[str] = None,
        sortDirection: Optional[str] = None,
    ) -> List[AccessoryDto]:
        pass

    def GetResourceGroups(
        self,
        scheduleId: Optional[int] = None,
        resourceFilter: Optional[IResourceFilter] = None,
    ) -> ResourceGroupTree:
        pass

    def AddResourceToGroup(self, resourceId: int, groupId: int) -> None:
        pass

    def RemoveResourceFromGroup(self, resourceId: int, groupId: int) -> None:
        pass

    def AddResourceGroup(self, group: ResourceGroup) -> ResourceGroup:
        pass

    def LoadResourceGroup(self, groupId: int) -> ResourceGroup:
        pass

    def LoadResourceGroupByPublicId(self, publicResourceGroupId: str) -> ResourceGroup:
        pass

    def UpdateResourceGroup(self, group: ResourceGroup) -> ResourceGroup:
        pass

    def DeleteResourceGroup(self, groupId: int) -> None:
        pass

    def GetResourceTypes(self) -> List[ResourceType]:
        pass

    def LoadResourceType(self, resourceTypeId: int) -> ResourceType:
        pass

    def AddResourceType(self, type: ResourceType) -> int:
        pass

    def UpdateResourceType(self, type: ResourceType) -> None:
        pass

    def RemoveResourceType(self, id: int) -> None:
        pass

    def GetStatusReasons(self) -> List[ResourceStatusReason]:
        pass

    def AddStatusReason(self, statusId: int, reasonDescription: str) -> int:
        pass

    def UpdateStatusReason(self, reasonId: int, reasonDescription: str) -> None:
        pass

    def RemoveStatusReason(self, reasonId: int) -> None:
        pass

    def GetUsersWithPermission(
        self,
        resourceId: int,
        pageNumber: Optional[int] = None,
        pageSize: Optional[int] = None,
        filter: Optional[str] = None,
        accountStatus: int = AccountStatus.ACTIVE,
    ) -> List[UserPermissionItemView]:
        pass

    def GetUsersWithPermissionsIncludingGroups(
        self,
        resourceId: int,
        pageNumber: Optional[int] = None,
        pageSize: Optional[int] = None,
        filter: Optional[str] = None,
        accountStatus: int = AccountStatus.ACTIVE,
    ) -> List[UserPermissionItemView]:
        pass

    def GetGroupsWithPermission(
        self,
        resourceId: int,
        pageNumber: Optional[int] = None,
        pageSize: Optional[int] = None,
        filter: Optional[str] = None,
    ) -> List[GroupPermissionItemView]:
        pass

    def ChangeResourceUserPermission(self, resourceId: int, userId: int, type: int) -> None:
        pass

    def ChangeResourceGroupPermission(self, resourceId: int, groupId: int, type: int) -> None:
        pass

    def GetPublicResourceIds(self) -> dict:
        pass

# Implement your FastAPI routes


