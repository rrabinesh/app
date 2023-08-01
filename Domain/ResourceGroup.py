# <?php

# class ResourceGroupTree
# {
#     /**
#      * @var $references ResourceGroup[]
#      */
#     protected $references = [];

#     /**
#      * @var array|ResourceGroup[]
#      */
#     protected $groups = [];

#     /**
#      * @var array|ResourceDto[]
#      */
#     protected $resources = [];

#     /**
#      * @var ResourceGroup[]
#      */
#     private $orphaned = [];

#     public function AddGroup(ResourceGroup $group)
#     {
#         $groupId = $group->id;
#         $this->references[$groupId] = $group;

#         if (array_key_exists($groupId, $this->orphaned)) {
#             foreach ($this->orphaned as $orphanedGroup) {
#                 $this->references[$groupId]->AddChild($orphanedGroup);
#             }

#             unset($this->orphaned[$groupId]);
#         }

#         // It it's a root node, we add it directly to the tree
#         $parent_id = $group->parent_id;
#         if (empty($parent_id)) {
#             $this->groups[] = $group;
#         } else {
#             if (!array_key_exists($parent_id, $this->references)) {
#                 // parent hasn't been added yet, hold this off until the parent shows up
#                 $this->orphaned[$parent_id] = $group;
#             } else {
#                 // It was not a root node, add this node as a reference in the parent.
#                 $this->references[$parent_id]->AddChild($group);
#             }
#         }
#     }

#     public function AddAssignment(ResourceGroupAssignment $assignment)
#     {
#         if (array_key_exists($assignment->group_id, $this->references)) {
#             $this->resources[$assignment->resource_id] = new ResourceDto(
#                 $assignment->resource_id,
#                 $assignment->resource_name,
#                 true,
#                 true,
#                 $assignment->GetScheduleId(),
#                 $assignment->GetMinimumLength(),
#                 $assignment->GetResourceTypeId(),
#                 $assignment->GetAdminGroupId(),
#                 $assignment->GetScheduleAdminGroupId(),
#                 $assignment->GetStatusId(),
#                 $assignment->GetRequiresApproval(),
#                 $assignment->IsCheckInEnabled(),
#                 $assignment->IsAutoReleased(),
#                 $assignment->GetAutoReleaseMinutes(),
#                 $assignment->GetColor(),
#                 $assignment->GetMaxConcurrentReservations()
#             );
#             $this->references[$assignment->group_id]->AddResource($assignment);
#         }
#     }

#     /**
#      * @param bool $includeDefaultGroup
#      * @return array|ResourceGroup[]
#      */
#     public function GetGroups($includeDefaultGroup = true)
#     {
#         if ($includeDefaultGroup) {
#             return $this->groups;
#         } else {
#             return array_slice($this->groups, 1);
#         }
#     }

#     /**
#      * @param bool $includeDefaultGroup
#      * @return array|ResourceGroup[]
#      */
#     public function GetGroupList($includeDefaultGroup = true)
#     {
#         if ($includeDefaultGroup) {
#             return $this->references;
#         } else {
#             return array_slice($this->references, 1, null, true);
#         }
#     }

#     /**
#      * @param int $groupId
#      * @param int[] $resourceIds
#      * @return int[]
#      */
#     public function GetResourceIds($groupId, &$resourceIds = [])
#     {
#         $group = $this->references[$groupId];

#         if (empty($group->children)) {
#             return $resourceIds;
#         }

#         foreach ($group->children as $child) {
#             if ($child->type == ResourceGroup::RESOURCE_TYPE) {
#                 $resourceIds[] = $child->resource_id;
#             } else {
#                 $this->GetResourceIds($child->id, $resourceIds);
#             }
#         }

#         return $resourceIds;
#     }

#     /**
#      * @param int $groupId
#      * @return ResourceGroup
#      */
#     public function GetGroup($groupId)
#     {
#         return $this->references[$groupId];
#     }

#     /**
#      * @return IBookableResource[] array of resources keyed by their ids
#      */
#     public function GetAllResources()
#     {
#         return $this->resources;
#     }
# }

# class ResourceGroup
# {
#     public const RESOURCE_TYPE = 'resource';
#     public const GROUP_TYPE = 'group';

#     public $id;
#     public $name;
#     public $label;
#     public $parent;
#     public $parent_id;
#     /**
#      * @var ResourceGroup[]|ResourceGroupAssignment[]
#      */
#     public $children = [];
#     public $type = ResourceGroup::GROUP_TYPE;

#     public function __construct($id, $name, $parentId = null)
#     {
#         $this->WithId($id);
#         $this->SetName($name);
#         $this->parent_id = $parentId;
#     }

#     /**
#      * @param $resourceGroup ResourceGroup
#      */
#     public function AddChild(ResourceGroup $resourceGroup)
#     {
#         $resourceGroup->parent_id = $this->id;
#         $this->children[] = $resourceGroup;
#     }

#     /**
#      * @param $assignment ResourceGroupAssignment
#      */
#     public function AddResource(ResourceGroupAssignment $assignment)
#     {
#         $this->children[] = $assignment;
#     }

#     /**
#      * @param string $groupName
#      * @param int $parentId
#      * @return ResourceGroup
#      */
#     public static function Create($groupName, $parentId = null)
#     {
#         return new ResourceGroup(null, $groupName, $parentId);
#     }

#     /**
#      * @param int|long $id
#      */
#     public function WithId($id)
#     {
#         $this->id = $id;
#     }

#     public function SetName($name)
#     {
#         $this->name = $name;
#         $this->label = $name;
#     }

#     /**
#      * @param int $targetId
#      */
#     public function MoveTo($targetId)
#     {
#         $this->parent_id = $targetId;
#     }

#     public function Rename($newName)
#     {
#         $this->SetName($newName);
#     }

#     public function __toString()
#     {
#         return $this->name;
#     }
# }

# class ResourceGroupAssignment implements IBookableResource
# {
#     public $type = ResourceGroup::RESOURCE_TYPE;
#     public $group_id;
#     public $resource_name;
#     public $id;
#     public $label;
#     public $resource_id;
#     public $resourceAdminGroupId;
#     public $scheduleId;
#     public $statusId;
#     public $scheduleAdminGroupId;
#     public $requiresApproval;
#     public $isCheckInEnabled;
#     public $isAutoReleased;
#     public $autoReleaseMinutes;
#     public $minLength;
#     public $resourceTypeId;
#     public $color;
#     public $textColor;
#     public $maxConcurrentReservations;

#     public function __construct(
#         $group_id,
#         $resource_name,
#         $resource_id,
#         $resourceAdminGroupId,
#         $scheduleId,
#         $statusId,
#         $scheduleAdminGroupId,
#         $requiresApproval,
#         $isCheckInEnabled,
#         $isAutoReleased,
#         $autoReleaseMinutes,
#         $minLength,
#         $resourceTypeId,
#         $color,
#         $maxConcurrentReservations
#     ) {
#         $this->group_id = $group_id;
#         $this->resource_name = $resource_name;
#         $this->id = "{$this->type}-{$group_id}-{$resource_id}";
#         $this->label = $resource_name;
#         $this->resource_id = $resource_id;
#         $this->resourceAdminGroupId = $resourceAdminGroupId;
#         $this->scheduleId = $scheduleId;
#         $this->statusId = $statusId;
#         $this->scheduleAdminGroupId = $scheduleAdminGroupId;
#         $this->requiresApproval = $requiresApproval;
#         $this->isCheckInEnabled = $isCheckInEnabled;
#         $this->isAutoReleased = $isAutoReleased;
#         $this->autoReleaseMinutes = $autoReleaseMinutes;
#         $this->minLength = $minLength;
#         $this->resourceTypeId = $resourceTypeId;
#         $this->color = $color;
#         $this->textColor = '';
#         if (!empty($color)) {
#             $textColor = new ContrastingColor($color);
#             $this->textColor = $textColor->__toString();
#         }
#         $this->maxConcurrentReservations = $maxConcurrentReservations;
#     }

#     public function GetId()
#     {
#         return $this->resource_id;
#     }

#     public function GetName()
#     {
#         return $this->resource_name;
#     }

#     public function GetAdminGroupId()
#     {
#         return $this->resourceAdminGroupId;
#     }

#     public function GetScheduleId()
#     {
#         return $this->scheduleId;
#     }

#     public function GetScheduleAdminGroupId()
#     {
#         return $this->scheduleAdminGroupId;
#     }

#     public function GetStatusId()
#     {
#         return $this->statusId;
#     }

#     public function GetResourceId()
#     {
#         return $this->resource_id;
#     }

#     public function GetRequiresApproval()
#     {
#         return $this->requiresApproval;
#     }

#     public function IsCheckInEnabled()
#     {
#         return $this->isCheckInEnabled;
#     }

#     public function IsAutoReleased()
#     {
#         return $this->isAutoReleased;
#     }

#     public function GetAutoReleaseMinutes()
#     {
#         return $this->autoReleaseMinutes;
#     }

#     public function GetMinimumLength()
#     {
#         return $this->minLength;
#     }

#     public function GetResourceTypeId()
#     {
#         return $this->resourceTypeId;
#     }

#     public function GetColor()
#     {
#         return $this->color;
#     }

#     public function GetTextColor()
#     {
#         return $this->textColor;
#     }

#     public function GetMaxConcurrentReservations()
#     {
#         return $this->maxConcurrentReservations;
#     }
# }


from typing import List, Dict
from fastapi import FastAPI

class ResourceGroup:
    RESOURCE_TYPE = 'resource'
    GROUP_TYPE = 'group'

    def __init__(self, id: int, name: str, parentId: int = None):
        self.id = id
        self.name = name
        self.label = name
        self.parent = None
        self.parent_id = parentId
        self.children = []
        self.type = ResourceGroup.GROUP_TYPE

    def add_child(self, resource_group):
        resource_group.parent_id = self.id
        self.children.append(resource_group)

    def add_resource(self, assignment):
        self.children.append(assignment)

    @staticmethod
    def create(group_name: str, parent_id: int = None):
        return ResourceGroup(None, group_name, parent_id)

    def with_id(self, group_id: int):
        self.id = group_id

    def set_name(self, name: str):
        self.name = name
        self.label = name

    def move_to(self, target_id: int):
        self.parent_id = target_id

    def rename(self, new_name: str):
        self.set_name(new_name)

    def __str__(self):
        return self.name

class ResourceGroupAssignment:
    def __init__(
        self,
        group_id: int,
        resource_name: str,
        resource_id: int,
        resourceAdminGroupId: int,
        scheduleId: int,
        statusId: int,
        scheduleAdminGroupId: int,
        requiresApproval: bool,
        isCheckInEnabled: bool,
        isAutoReleased: bool,
        autoReleaseMinutes: int,
        minLength: int,
        resourceTypeId: int,
        color: str,
        maxConcurrentReservations: int
    ):
        self.type = ResourceGroup.RESOURCE_TYPE
        self.group_id = group_id
        self.resource_name = resource_name
        self.id = f"{self.type}-{group_id}-{resource_id}"
        self.label = resource_name
        self.resource_id = resource_id
        self.resourceAdminGroupId = resourceAdminGroupId
        self.scheduleId = scheduleId
        self.statusId = statusId
        self.scheduleAdminGroupId = scheduleAdminGroupId
        self.requiresApproval = requiresApproval
        self.isCheckInEnabled = isCheckInEnabled
        self.isAutoReleased = isAutoReleased
        self.autoReleaseMinutes = autoReleaseMinutes
        self.minLength = minLength
        self.resourceTypeId = resourceTypeId
        self.color = color
        self.textColor = ''
        if color:
            text_color = ContrastingColor(color)
            self.textColor = text_color.__str__()
        self.maxConcurrentReservations = maxConcurrentReservations

class ResourceDto:
    def __init__(
        self,
        resource_id: int,
        resource_name: str,
        resource_type: bool,
        group_type: bool,
        schedule_id: int,
        minimum_length: int,
        resource_type_id: int,
        admin_group_id: int,
        schedule_admin_group_id: int,
        status_id: int,
        requires_approval: bool,
        check_in_enabled: bool,
        auto_released: bool,
        auto_release_minutes: int,
        color: str,
        max_concurrent_reservations: int
    ):
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.group_type = group_type
        self.schedule_id = schedule_id
        self.minimum_length = minimum_length
        self.resource_type_id = resource_type_id
        self.admin_group_id = admin_group_id
        self.schedule_admin_group_id = schedule_admin_group_id
        self.status_id = status_id
        self.requires_approval = requires_approval
        self.check_in_enabled = check_in_enabled
        self.auto_released = auto_released
        self.auto_release_minutes = auto_release_minutes
        self.color = color
        self.max_concurrent_reservations = max_concurrent_reservations

app = FastAPI()

class ResourceGroupTree:
    def __init__(self):
        self.references = {}
        self.groups = []
        self.resources = []
        self.orphaned = []

    def add_group(self, group: ResourceGroup):
        group_id = group.id
        self.references[group_id] = group

        if group_id in self.orphaned:
            for orphaned_group in self.orphaned[group_id]:
                self.references[group_id].add_child(orphaned_group)

            self.orphaned.pop(group_id)

        parent_id = group.parent_id
        if parent_id is None:
            self.groups.append(group)
        else:
            if parent_id not in self.references:
                self.orphaned.setdefault(parent_id, []).append(group)
            else:
                self.references[parent_id].add_child(group)

    def add_assignment(self, assignment: ResourceGroupAssignment):
        if assignment.group_id in self.references:
            self.resources.append(ResourceDto(
                assignment.resource_id,
                assignment.resource_name,
                True,
                True,
                assignment.scheduleId,
                assignment.minLength,
                assignment.resourceTypeId,
                assignment.resourceAdminGroupId,
                assignment.scheduleAdminGroupId,
                assignment.statusId,
                assignment.requiresApproval,
                assignment.isCheckInEnabled,
                assignment.isAutoReleased,
                assignment.autoReleaseMinutes,
                assignment.color,
                assignment.maxConcurrentReservations
            ))
            self.references[assignment.group_id].add_resource(assignment)

    def get_groups(self, include_default_group: bool = True) -> List[ResourceGroup]:
        if include_default_group:
            return self.groups
        else:
            return self.groups[1:]

    def get_group_list(self, include_default_group: bool = True) -> Dict[int, ResourceGroup]:
        if include_default_group:
            return self.references
        else:
            return dict(list(self.references.items())[1:])

    def get_resource_ids(self, group_id: int, resource_ids: List[int] = []) -> List[int]:
        group = self.references[group_id]

        if not group.children:
            return resource_ids

        for child in group.children:
            if child.type == ResourceGroup.RESOURCE_TYPE:
                resource_ids.append(child.resource_id)
            else:
                self.get_resource_ids(child.id, resource_ids)

        return resource_ids

    def get_group(self, group_id: int) -> ResourceGroup:
        return self.references[group_id]

    def get_all_resources(self) -> List[ResourceDto]:
        return self.resources

# Sample usage:
# tree = ResourceGroupTree()
# group1 = ResourceGroup(1, "Group 1")
# group2 = ResourceGroup(2, "Group 2", 1)
# assignment = ResourceGroupAssignment(...)
# tree.add_group(group1)
# tree.add_group(group2)
# tree.add_assignment(assignment)

# FastAPI Endpoints can be defined to interact with the ResourceGroupTree instance.

