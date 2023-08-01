# <?php

# class Announcement
# {
#     private $Id;
#     private $Text;
#     private $Start;
#     private $End;
#     private $Priority;
#     private $GroupIds = [];
#     private $ResourceIds = [];
#     private $DisplayPage;

#     /**
#      * @return int
#      */
#     public function Id()
#     {
#         return $this->Id;
#     }

#     /**
#      * @return string
#      */
#     public function Text()
#     {
#         return $this->Text;
#     }

#     /**
#      * @return Date
#      */
#     public function Start()
#     {
#         return $this->Start;
#     }

#     /**
#      * @return Date
#      */
#     public function End()
#     {
#         return $this->End;
#     }

#     /**
#      * @return int
#      */
#     public function Priority()
#     {
#         return empty($this->Priority) ? null : (int)$this->Priority;
#     }

#     /**
#      * @return int[]
#      */
#     public function GroupIds()
#     {
#         return empty($this->GroupIds) ? [] : $this->GroupIds;
#     }

#     /**
#      * @return int[]
#      */
#     public function ResourceIds()
#     {
#         return empty($this->ResourceIds) ? [] : $this->ResourceIds;
#     }

#     /**
#      * @return int
#      */
#     public function DisplayPage()
#     {
#         return $this->DisplayPage;
#     }

#     public function __construct($id, $text, Date $start, Date $end, $priority, $groupIds, $resourceIds, $displayPage)
#     {
#         $this->Id = $id;
#         $text = str_replace('&lt;script&gt;', '', $text);
#         $text = str_replace('&lt;/script&gt;', '', $text);
#         $this->Text = $text;
#         $this->Start = $start;
#         $this->End = $end;
#         $this->Priority = $priority;
#         $this->GroupIds = $groupIds;
#         $this->ResourceIds = $resourceIds;
#         $this->DisplayPage = $displayPage;
#     }

#     public static function FromRow($row)
#     {
#         $groupIds = $row[ColumnNames::GROUP_IDS];
#         $resourceIds = $row[ColumnNames::RESOURCE_IDS];

#         return new Announcement(
#             $row[ColumnNames::ANNOUNCEMENT_ID],
#             $row[ColumnNames::ANNOUNCEMENT_TEXT],
#             Date::FromDatabase($row[ColumnNames::ANNOUNCEMENT_START]),
#             Date::FromDatabase($row[ColumnNames::ANNOUNCEMENT_END]),
#             $row[ColumnNames::ANNOUNCEMENT_PRIORITY],
#             empty($groupIds) ? [] : explode(',', $groupIds),
#             empty($resourceIds) ? [] : explode(',', $resourceIds),
#             $row[ColumnNames::ANNOUNCEMENT_DISPLAY_PAGE]
#         );
#     }

#     /**
#      * @static
#      * @param string $text
#      * @param Date $start
#      * @param Date $end
#      * @param int $priority
#      * @param int[] $groupIds
#      * @param int[] $resourceIds
#      * @param int $displayPage
#      * @return Announcement
#      */
#     public static function Create($text, Date $start, Date $end, $priority, $groupIds, $resourceIds, $displayPage)
#     {
#         if (empty($priority)) {
#             $priority = null;
#         }
#         return new Announcement(null, $text, $start, $end, $priority, $groupIds, $resourceIds, $displayPage);
#     }

#     /**
#      * @param string $text
#      */
#     public function SetText($text)
#     {
#         $this->Text = $text;
#     }

#     /**
#      * @param Date $start
#      * @param Date $end
#      */
#     public function SetDates(Date $start, Date $end)
#     {
#         $this->Start = $start;
#         $this->End = $end;
#     }

#     /**
#      * @param int $priority
#      */
#     public function SetPriority($priority)
#     {
#         $this->Priority = $priority;
#     }

#     /**
#      * @param int[] $groupIds
#      */
#     public function SetGroups($groupIds)
#     {
#         $this->GroupIds = $groupIds;
#     }

#     /**
#      * @param int[] $resourceIds
#      */
#     public function SetResources($resourceIds)
#     {
#         $this->ResourceIds = $resourceIds;
#     }

#     /**
#      * @param UserSession $user
#      * @param IPermissionService $permissionService
#      * @return bool
#      */
#     public function AppliesToUser(UserSession $user, IPermissionService $permissionService)
#     {
#         $groupIds = $this->GroupIds();
#         $resourceIds = $this->ResourceIds();

#         $allowedForGroup = empty($groupIds);
#         $allowedForResource = empty($resourceIds);

#         foreach ($this->ResourceIds() as $resourceId) {
#             if ($permissionService->CanAccessResource(new AnnouncementResource($resourceId), $user)) {
#                 $allowedForResource = true;
#                 break;
#             }
#         }

#         foreach ($this->GroupIds() as $groupId) {
#             if (in_array($groupId, $user->Groups)) {
#                 $allowedForGroup = true;
#                 break;
#             }
#         }

#         return $allowedForGroup && $allowedForResource;
#     }

#     /**
#      * @return bool
#      */
#     public function CanEmail()
#     {
#         return $this->DisplayPage() == 1;
#     }
# }

# class AnnouncementResource implements IPermissibleResource
# {
#     private $resourceId;

#     public function __construct($resourceId)
#     {
#         $this->resourceId = $resourceId;
#     }

#     public function GetResourceId()
#     {
#         return $this->resourceId;
#     }
# }


from datetime import date
from typing import List, Optional
from pydantic import BaseModel

class AnnouncementResource(BaseModel):
    resource_id: int

class Announcement(BaseModel):
    id: Optional[int]
    text: str
    start: date
    end: date
    priority: Optional[int]
    group_ids: List[int]
    resource_ids: List[int]
    display_page: int

    def set_text(self, text):
        self.text = text

    def set_dates(self, start: date, end: date):
        self.start = start
        self.end = end

    def set_priority(self, priority: Optional[int]):
        self.priority = priority

    def set_groups(self, group_ids: List[int]):
        self.group_ids = group_ids

    def set_resources(self, resource_ids: List[int]):
        self.resource_ids = resource_ids

    def applies_to_user(self, user, permission_service):
        allowed_for_group = not self.group_ids
        allowed_for_resource = not self.resource_ids

        for resource_id in self.resource_ids:
            if permission_service.can_access_resource(AnnouncementResource(resource_id), user):
                allowed_for_resource = True
                break

        for group_id in self.group_ids:
            if group_id in user.groups:
                allowed_for_group = True
                break

        return allowed_for_group and allowed_for_resource

    def can_email(self):
        return self.display_page == 1

