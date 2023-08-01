# <?php

# require_once(ROOT_DIR . 'Domain/Access/ScheduleRepository.php');

# class ScheduleAdminScheduleRepository extends ScheduleRepository
# {
#     /**
#      * @var IUserRepository
#      */
#     private $repo;

#     /**
#      * @var UserSession
#      */
#     private $user;

#     public function __construct(IUserRepository $repo, UserSession $userSession)
#     {
#         $this->repo = $repo;
#         $this->user = $userSession;
#         parent::__construct();
#     }

#     public function GetAll()
#     {
#         $schedules = parent::GetAll();

#         return $this->Filter($schedules);
#     }

#     public function Update(Schedule $schedule)
#     {
#         $user = $this->repo->LoadById($this->user->UserId);
#         if (!$user->IsScheduleAdminFor($schedule)) {
#             // if we got to this point, the user does not have the ability to update the schedule
#             throw new Exception(sprintf('Schedule Update Failed. User %s does not have admin access to schedule %s.', $this->user->UserId, $schedule->GetId()));
#         }

#         parent::Update($schedule);
#     }

#     public function Add(Schedule $schedule, $copyLayoutFromScheduleId)
#     {
#         $user = $this->repo->LoadById($this->user->UserId);
#         if (!$user->IsInRole(RoleLevel::SCHEDULE_ADMIN)) {
#             throw new Exception(sprintf('Schedule Add Failed. User %s does not have admin access.', $this->user->UserId));
#         }

#         foreach ($user->Groups() as $group) {
#             if ($group->IsScheduleAdmin) {
#                 $schedule->SetAdminGroupId($group->GroupId);
#                 break;
#             }
#         }

#         parent::Add($schedule, $copyLayoutFromScheduleId);
#     }

#     /**
#      * @param Schedule[] $schedules
#      * @return Schedule[]
#      */
#     private function Filter($schedules)
#     {
#         if ($this->user->IsAdmin) {
#             return $schedules;
#         }

#         $user = $this->repo->LoadById($this->user->UserId);

#         $filteredList = [];
#         /** @var $schedule Schedule */
#         foreach ($schedules as $schedule) {
#             if ($user->IsScheduleAdminFor($schedule)) {
#                 $filteredList[] = $schedule;
#             }
#         }

#         return $filteredList;
#     }

#     public function GetList($pageNumber, $pageSize, $sortField = null, $sortDirection = null, $filter = null)
#     {
#         $user = $this->repo->LoadById($this->user->UserId);

#         if (!$user->IsInRole(RoleLevel::SCHEDULE_ADMIN)) {
#             return new PageableData();
#         }
#         $ids = [];

#         $filter = new SqlFilterNull();

#         foreach ($user->Groups() as $group) {
#             if ($group->IsScheduleAdmin) {
#                 $ids[] = $group->GroupId;
#             }
#         }

#         $filter->_And(new SqlFilterIn(new SqlFilterColumn(TableNames::SCHEDULES_ALIAS, ColumnNames::RESOURCE_ADMIN_GROUP_ID), $ids));

#         return parent::GetList($pageNumber, $pageSize, $sortField, $sortDirection, $filter);
#     }
# }


from fastapi import FastAPI

# Assume you have defined the necessary Pydantic models and FastAPI dependencies.
# You can add them here or import them from other modules.

# Create a FastAPI app
app = FastAPI()

# Sample IUserRepository and UserSession
# You may need to define these classes properly.
class IUserRepository:
    pass

class UserSession:
    pass

# Sample Schedule and PageableData
# You may need to define these models properly.
class Schedule:
    pass

class PageableData:
    pass

# ScheduleAdminScheduleRepository
class ScheduleAdminScheduleRepository:
    def __init__(self, repo: IUserRepository, user_session: UserSession):
        self.repo = repo
        self.user = user_session

    def get_all(self):
        schedules = self.parent_get_all()
        return self.filter(schedules)

    def update(self, schedule):
        user = self.repo.LoadById(self.user.UserId)
        if not user.IsScheduleAdminFor(schedule):
            # if we got to this point, the user does not have the ability to update the schedule
            raise Exception(
                f'Schedule Update Failed. User {self.user.UserId} does not have admin access to schedule {schedule.GetId()}.'
            )

        self.parent_update(schedule)

    def add(self, schedule, copy_layout_from_schedule_id):
        user = self.repo.LoadById(self.user.UserId)
        if not user.IsInRole(RoleLevel.SCHEDULE_ADMIN):
            raise Exception(f'Schedule Add Failed. User {self.user.UserId} does not have admin access.')

        for group in user.Groups():
            if group.IsScheduleAdmin:
                schedule.SetAdminGroupId(group.GroupId)
                break

        self.parent_add(schedule, copy_layout_from_schedule_id)

    def filter(self, schedules):
        if self.user.IsAdmin:
            return schedules

        user = self.repo.LoadById(self.user.UserId)
        filtered_list = []
        for schedule in schedules:
            if user.IsScheduleAdminFor(schedule):
                filtered_list.append(schedule)

        return filtered_list

    def get_list(self, page_number, page_size, sort_field=None, sort_direction=None, filter=None):
        user = self.repo.LoadById(self.user.UserId)

        if not user.IsInRole(RoleLevel.SCHEDULE_ADMIN):
            return PageableData()

        ids = []
        filter = SqlFilterNull()

        for group in user.Groups():
            if group.IsScheduleAdmin:
                ids.append(group.GroupId)

        filter._And(SqlFilterIn(SqlFilterColumn(TableNames.SCHEDULES_ALIAS, ColumnNames.RESOURCE_ADMIN_GROUP_ID), ids))

        return self.parent_get_list(page_number, page_size, sort_field, sort_direction, filter)


# FastAPI endpoint for getting all schedules
@app.get("/get_all_schedules/")
async def get_all_schedules(
    user: UserSession = ...  # Define the Pydantic model for UserSession here
):
    schedule_admin_repo = ScheduleAdminScheduleRepository(repo=IUserRepository(), user_session=user)

    schedules = schedule_admin_repo.get_all()
    # Process the schedules or return them as needed.
    return {"schedules": schedules}


