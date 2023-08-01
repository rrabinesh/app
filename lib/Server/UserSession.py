# <?php

# class UserSession
# {
#     public $UserId = '';
#     public $FirstName = '';
#     public $LastName = '';
#     public $Email = '';
#     public $Timezone = '';
#     public $HomepageId = 1;
#     public $IsAdmin = false;
#     public $IsGroupAdmin = false;
#     public $IsResourceAdmin = false;
#     public $IsScheduleAdmin = false;
#     public $LanguageCode = '';
#     public $PublicId = '';
#     public $LoginTime = '';
#     public $ScheduleId = '';
#     public $Groups = [];
#     public $AdminGroups = [];
#     public $CSRFToken = '';

#     public function __construct($id)
#     {
#         $this->UserId = $id;
#     }

#     public function IsLoggedIn()
#     {
#         return true;
#     }

#     public function IsGuest()
#     {
#         return false;
#     }

#     public function IsAdminForGroup($groupIds = [])
#     {
#         if (!is_array($groupIds)) {
#             $groupIds = [$groupIds];
#         }

#         if ($this->IsAdmin) {
#             return true;
#         }

#         if (!$this->IsGroupAdmin) {
#             return false;
#         }

#         foreach ($groupIds as $groupId) {
#             if (in_array($groupId, $this->AdminGroups)) {
#                 return true;
#             }
#         }

#         return false;
#     }

#     public function __toString()
#     {
#         return "{$this->FirstName} {$this->LastName} ({$this->Email})";
#     }

#     public function FullName()
#     {
#         return new FullName($this->FirstName, $this->LastName);
#     }
# }

# class NullUserSession extends UserSession
# {
#     public function __construct()
#     {
#         parent::__construct(0);
#         $this->Timezone = Configuration::Instance()->GetDefaultTimezone();
#     }

#     public function IsLoggedIn()
#     {
#         return false;
#     }

#     public function IsGuest()
#     {
#         return true;
#     }
# }


from typing import List
from fastapi import FastAPI, Depends

app = FastAPI()

class UserSession:
    def __init__(self, user_id: str):
        self.UserId = user_id
        self.FirstName = ''
        self.LastName = ''
        self.Email = ''
        self.Timezone = ''
        self.HomepageId = 1
        self.IsAdmin = False
        self.IsGroupAdmin = False
        self.IsResourceAdmin = False
        self.IsScheduleAdmin = False
        self.LanguageCode = ''
        self.PublicId = ''
        self.LoginTime = ''
        self.ScheduleId = ''
        self.Groups: List[str] = []
        self.AdminGroups: List[str] = []
        self.CSRFToken = ''

    def is_logged_in(self):
        return True

    def is_guest(self):
        return False

    def is_admin_for_group(self, group_ids: List[str] = []):
        if not isinstance(group_ids, list):
            group_ids = [group_ids]

        if self.IsAdmin:
            return True

        if not self.IsGroupAdmin:
            return False

        return any(group_id in self.AdminGroups for group_id in group_ids)

    def __str__(self):
        return f"{self.FirstName} {self.LastName} ({self.Email})"

    def full_name(self):
        return f"{self.FirstName} {self.LastName}"


class NullUserSession(UserSession):
    def __init__(self):
        super().__init__("0")
        self.Timezone = Configuration.Instance().GetDefaultTimezone()

    def is_logged_in(self):
        return False

    def is_guest(self):
        return True
