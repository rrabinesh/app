# <?php

# require_once(ROOT_DIR . 'Domain/Values/ResourcePermissionType.php');

# interface IGroupRepository
# {
#     /**
#      * @param int $groupId
#      * @return Group
#      */
#     public function LoadById($groupId);

#     /**
#      * @param Group $group
#      * @return int newly inserted group id
#      */
#     public function Add(Group $group);

#     /**
#      * @param Group $group
#      * @return void
#      */
#     public function Update(Group $group);

#     /**
#      * @param Group $group
#      * @return void
#      */
#     public function Remove(Group $group);
# }

# interface IGroupViewRepository
# {
#     /**
#      * @param int $pageNumber
#      * @param int $pageSize
#      * @param string $sortField
#      * @param string $sortDirection
#      * @param ISqlFilter $filter
#      * @return PageableData|GroupItemView[]
#      */
#     public function GetList(
#         $pageNumber = null,
#         $pageSize = null,
#         $sortField = null,
#         $sortDirection = null,
#         $filter = null
#     );

#     /**
#      * @param int|array|int[] $groupIds
#      * @param int $pageNumber
#      * @param int $pageSize
#      * @param ISqlFilter $filter
#      * @param AccountStatus|int $accountStatus
#      * @return PageableData|UserItemView[]
#      */
#     public function GetUsersInGroup(
#         $groupIds,
#         $pageNumber = null,
#         $pageSize = null,
#         $filter = null,
#         $accountStatus = AccountStatus::ALL
#     );

#     /**
#      * @param $roleLevel int|RoleLevel
#      * @return GroupItemView[]|array
#      */
#     public function GetGroupsByRole($roleLevel);

#     /**
#      * @return GroupResourcePermission[]
#      */
#     public function GetPermissionList();
# }

# class GroupRepository implements IGroupRepository, IGroupViewRepository
# {
#     /**
#      * @var DomainCache
#      */
#     private $_cache;

#     public function __construct()
#     {
#         $this->_cache = new DomainCache();
#     }

#     /**
#      * @param int $pageNumber
#      * @param int $pageSize
#      * @param string $sortField
#      * @param string $sortDirection
#      * @param ISqlFilter $filter
#      * @return PageableData|GroupItemView[]
#      */
#     public function GetList(
#         $pageNumber = null,
#         $pageSize = null,
#         $sortField = null,
#         $sortDirection = null,
#         $filter = null
#     ) {
#         $command = new GetAllGroupsCommand();

#         if ($filter != null) {
#             $command = new FilterCommand($command, $filter);
#         }

#         $builder = ['GroupItemView', 'Create'];
#         return PageableDataStore::GetList($command, $builder, $pageNumber, $pageSize, $sortField, $sortDirection);
#     }

#     /**
#      * @param array|int|int[] $groupIds
#      * @param null $pageNumber
#      * @param null $pageSize
#      * @param null $filter
#      * @param AccountStatus|int $accountStatus
#      * @return PageableData|UserItemView[]
#      */
#     public function GetUsersInGroup(
#         $groupIds,
#         $pageNumber = null,
#         $pageSize = null,
#         $filter = null,
#         $accountStatus = AccountStatus::ACTIVE
#     ) {
#         $command = new GetAllGroupUsersCommand($groupIds, $accountStatus);

#         if ($filter != null) {
#             $command = new FilterCommand($command, $filter);
#         }

#         $builder = ['UserItemView', 'Create'];
#         return PageableDataStore::GetList($command, $builder, $pageNumber, $pageSize);
#     }

#     public function LoadById($groupId)
#     {
#         if ($this->_cache->Exists($groupId)) {
#             return $this->_cache->Get($groupId);
#         }

#         $group = null;
#         $db = ServiceLocator::GetDatabase();

#         $reader = $db->Query(new GetGroupByIdCommand($groupId));
#         if ($row = $reader->GetRow()) {
#             $group = new Group($row[ColumnNames::GROUP_ID], $row[ColumnNames::GROUP_NAME], $row[ColumnNames::GROUP_ISDEFAULT]);
#             $group->WithGroupAdmin($row[ColumnNames::GROUP_ADMIN_GROUP_ID]);
#         }
#         $reader->Free();

#         $reader = $db->Query(new GetAllGroupUsersCommand($groupId, AccountStatus::ACTIVE));
#         while ($row = $reader->GetRow()) {
#             $group->WithUser($row[ColumnNames::USER_ID]);
#         }
#         $reader->Free();

#         $reader = $db->Query(new GetAllGroupPermissionsCommand($groupId));
#         while ($row = $reader->GetRow()) {
#             if ($row[ColumnNames::PERMISSION_TYPE] == ResourcePermissionType::Full) {
#                 $group->WithFullPermission($row[ColumnNames::RESOURCE_ID]);
#             } else {
#                 $group->WithViewablePermission($row[ColumnNames::RESOURCE_ID]);
#             }
#         }
#         $reader->Free();

#         $reader = $db->Query(new GetAllGroupRolesCommand($groupId));
#         while ($row = $reader->GetRow()) {
#             $group->WithRole($row[ColumnNames::ROLE_ID]);
#         }
#         $reader->Free();

#         $this->_cache->Add($groupId, $group);
#         return $group;
#     }

#     /**
#      * @param Group $group
#      * @return void
#      */
#     public function Update(Group $group)
#     {
#         $db = ServiceLocator::GetDatabase();

#         $groupId = $group->Id();
#         foreach ($group->RemovedUsers() as $userId) {
#             $db->Execute(new DeleteUserGroupCommand($userId, $groupId));
#         }

#         foreach ($group->AddedUsers() as $userId) {
#             $db->Execute(new AddUserGroupCommand($userId, $groupId));
#         }

#         foreach ($group->RemovedPermissions() as $resourceId) {
#             $db->Execute(new DeleteGroupResourcePermission($groupId, $resourceId));
#         }

#         foreach ($group->AddedPermissions() as $resourceId) {
#             $db->Execute(new AddGroupResourcePermission($group->Id(), $resourceId, ResourcePermissionType::Full));
#         }

#         foreach ($group->AddedViewPermissions() as $resourceId) {
#             $db->Execute(new AddGroupResourcePermission($group->Id(), $resourceId, ResourcePermissionType::View));
#         }

#         foreach ($group->RemovedRoles() as $roleId) {
#             $db->Execute(new DeleteGroupRoleCommand($groupId, $roleId));
#         }

#         foreach ($group->AddedRoles() as $roleId) {
#             $db->Execute(new AddGroupRoleCommand($groupId, $roleId));
#         }

#         $db->Execute(new UpdateGroupCommand($groupId, $group->Name(), $group->AdminGroupId(), $group->IsDefault()));

#         $this->_cache->Add($groupId, $group);
#     }

#     public function Remove(Group $group)
#     {
#         ServiceLocator::GetDatabase()->Execute(new DeleteGroupCommand($group->Id()));

#         $this->_cache->Remove($group->Id());
#     }

#     public function Add(Group $group)
#     {
#         $groupId = ServiceLocator::GetDatabase()->ExecuteInsert(new AddGroupCommand($group->Name(), $group->IsDefault()));
#         $group->WithId($groupId);

#         return $groupId;
#     }

#     /**
#      * @param $roleLevel int|RoleLevel
#      * @return GroupItemView[]|array
#      */
#     public function GetGroupsByRole($roleLevel)
#     {
#         $reader = ServiceLocator::GetDatabase()->Query(new GetAllGroupsByRoleCommand($roleLevel));
#         $groups = [];
#         while ($row = $reader->GetRow()) {
#             $groups[] = GroupItemView::Create($row);
#         }
#         $reader->Free();

#         return $groups;
#     }

#     public function GetPermissionList()
#     {
#         $reader = ServiceLocator::GetDatabase()->Query(new GetAllGroupResourcePermissions());

#         $groups = [];
#         while ($row = $reader->GetRow()) {
#             $groups[] = GroupResourcePermission::Create($row);
#         }
#         $reader->Free();

#         return $groups;
#     }
# }

# class GroupUserView
# {
#     public static function Create($row)
#     {
#         return new GroupUserView(
#             $row[ColumnNames::USER_ID],
#             $row[ColumnNames::FIRST_NAME],
#             $row[ColumnNames::LAST_NAME]
#         );
#     }

#     public $UserId;
#     public $FirstName;
#     public $LastName;
#     public $GroupId;

#     public function __construct($userId, $firstName, $lastName)
#     {
#         $this->UserId = $userId;
#         $this->FirstName = $firstName;
#         $this->LastName = $lastName;
#     }
# }

# class GroupItemView
# {
#     public static function Create($row)
#     {
#         $adminName = isset($row[ColumnNames::GROUP_ADMIN_GROUP_NAME]) ? $row[ColumnNames::GROUP_ADMIN_GROUP_NAME] : null;
#         $isDefault = intval($row[ColumnNames::GROUP_ISDEFAULT]);
#         $roles = explode(',', $row[ColumnNames::GROUP_ROLE_LIST] ?? '');
#         return new GroupItemView($row[ColumnNames::GROUP_ID], $row[ColumnNames::GROUP_NAME], $adminName, $isDefault, $roles);
#     }

#     /**
#      * @var int
#      */
#     public $Id;

#     /**
#      * @return int
#      */
#     public function Id()
#     {
#         return $this->Id;
#     }

#     /**
#      * @var string
#      */
#     public $Name;

#     /**
#      * @return string
#      */
#     public function Name()
#     {
#         return $this->Name;
#     }

#     /**
#      * @var string
#      */
#     public $AdminGroupName;

#     /**
#      * @return string|null
#      */
#     public function AdminGroupName()
#     {
#         return $this->AdminGroupName;
#     }

#     /**
#      * @var int
#      */
#     public $IsDefault;

#     public function IsDefault()
#     {
#         return $this->IsDefault;
#     }

#     /**
#      * @var int[]
#      */
#     public $Roles;

#     /**
#      * @return bool
#      */
#     public function IsAdmin()
#     {
#         return in_array(RoleLevel::APPLICATION_ADMIN, $this->Roles);
#     }

#     /**
#      * @return bool
#      */
#     public function IsGroupAdmin()
#     {
#         return in_array(RoleLevel::GROUP_ADMIN, $this->Roles);
#     }

#     /**
#      * @return bool
#      */
#     public function IsResourceAdmin()
#     {
#         return in_array(RoleLevel::RESOURCE_ADMIN, $this->Roles);
#     }

#     /**
#      * @return bool
#      */
#     public function IsScheduleAdmin()
#     {
#         return in_array(RoleLevel::SCHEDULE_ADMIN, $this->Roles);
#     }

#     /**
#      * @return bool
#      */
#     public function IsExtendedAdmin()
#     {
#         return $this->IsGroupAdmin() || $this->IsScheduleAdmin() || $this->IsResourceAdmin();
#     }

#     public function __construct($groupId, $groupName, $adminGroupName = null, $isDefault = 0, $roles = [])
#     {
#         $this->Id = $groupId;
#         $this->Name = $groupName;
#         $this->AdminGroupName = $adminGroupName;
#         $this->IsDefault = $isDefault;
#         $this->Roles = $roles;
#     }
# }

# class GroupPermissionItemView extends GroupItemView
# {
#     public $PermissionType;

#     public function __construct($groupId, $groupName, $adminGroupName = null, $isDefault = 0)
#     {
#         parent::__construct($groupId, $groupName, $adminGroupName, $isDefault);
#         $this->PermissionType = ResourcePermissionType::None;
#     }

#     public function PermissionType()
#     {
#         return $this->PermissionType;
#     }

#     public static function Create($row)
#     {
#         $item = GroupItemView::Create($row);
#         $me = new GroupPermissionItemView($item->Id, $item->Name, $item->AdminGroupName, $item->IsDefault);
#         $me->PermissionType = $row[ColumnNames::PERMISSION_TYPE];
#         return $me;
#     }
# }

# class RoleDto
# {
#     /**
#      * @var int
#      */
#     public $Id;

#     /**
#      * @var string
#      */
#     public $Name;

#     /**
#      * @var int|RoleLevel
#      */
#     public $Level;

#     /**
#      * @param $id int
#      * @param $name string
#      * @param $level RoleLevel|int
#      */
#     public function __construct($id, $name, $level)
#     {
#         $this->Id = $id;
#         $this->Name = $name;
#         $this->Level = $level;
#     }
# }

# class GroupResourcePermission
# {
#     private $groupId;
#     private $resourceId;
#     private $resourceName;
#     private $permissionType;

#     /**
#      * @return int
#      */
#     public function GroupId()
#     {
#         return $this->groupId;
#     }

#     /**
#      * @return int
#      */
#     public function ResourceId()
#     {
#         return $this->resourceId;
#     }

#     /**
#      * @return string
#      */
#     public function ResourceName()
#     {
#         return $this->resourceName;
#     }

#     /**
#      * @return int|ResourcePermissionType
#      */
#     public function PermissionType()
#     {
#         return $this->permissionType;
#     }

#     /**
#      * @param array $row
#      * @return GroupResourcePermission
#      */
#     public static function Create($row)
#     {
#         $grp = new GroupResourcePermission();
#         $grp->groupId = $row[ColumnNames::GROUP_ID];
#         $grp->resourceId = $row[ColumnNames::RESOURCE_ID];
#         $grp->resourceName = $row[ColumnNames::RESOURCE_NAME];
#         $grp->permissionType = $row[ColumnNames::PERMISSION_TYPE];
#         return $grp;
#     }
# }


from typing import List, Optional
from fastapi import FastAPI

app = FastAPI()

# FastAPI doesn't require explicit class definitions for data models, but you can use Pydantic models if needed.


class DomainCache:
    def __init__(self):
        self._cache = {}

    def exists(self, key):
        return key in self._cache

    def get(self, key):
        return self._cache[key]

    def add(self, key, obj):
        self._cache[key] = obj

    def remove(self, key):
        del self._cache[key]


class ResourcePermissionType:
    None_ = -1
    Full = 0
    View = 1


class Group:
    def __init__(self, group_id: int, group_name: str, is_default: bool):
        self.group_id = group_id
        self.group_name = group_name
        self.is_default = is_default

    # Define other methods as needed


class GroupItemView:
    def __init__(
        self,
        group_id: int,
        group_name: str,
        admin_group_name: Optional[str] = None,
        is_default: int = 0,
        roles: List[int] = [],
    ):
        self.group_id = group_id
        self.group_name = group_name
        self.admin_group_name = admin_group_name
        self.is_default = is_default
        self.roles = roles

    # Define other methods as needed


class GroupResourcePermission:
    def __init__(
        self,
        group_id: int,
        resource_id: int,
        resource_name: str,
        permission_type: int,
    ):
        self.group_id = group_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.permission_type = permission_type

    # Define other methods as needed


class GroupRepository:
    def __init__(self):
        self._cache = DomainCache()

    def load_by_id(self, group_id: int) -> Group:
        if self._cache.exists(group_id):
            return self._cache.get(group_id)

        # Simulate fetching data from a database or other data source
        # Replace this part with your actual database query
        group = Group(group_id, "Sample Group", False)
        self._cache.add(group_id, group)
        return group

    def add(self, group: Group) -> int:
        # Simulate inserting data into a database and getting the new group_id
        group_id = 123
        group.group_id = group_id
        self._cache.add(group_id, group)
        return group_id

    def update(self, group: Group) -> None:
        # Simulate updating the group in a database
        self._cache.add(group.group_id, group)

    def remove(self, group: Group) -> None:
        # Simulate deleting the group from a database
        self._cache.remove(group.group_id)

    # Implement other methods as needed

    # Define your FastAPI routes and endpoints here


@app.get("/group/{group_id}")
def get_group(group_id: int):
    group_repo = GroupRepository()
    group = group_repo.load_by_id(group_id)
    return {"group_id": group.group_id, "group_name": group.group_name, "is_default": group.is_default}

# Implement other FastAPI routes and endpoints as needed


