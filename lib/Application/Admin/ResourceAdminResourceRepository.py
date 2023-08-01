# <!-- <?php

# require_once(ROOT_DIR . 'Domain/Access/ResourceRepository.php');

# class ResourceAdminResourceRepository extends ResourceRepository
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

#     /**
#      * @return array|BookableResource[] array of all resources
#      */
#     public function GetResourceList()
#     {
#         $resources = parent::GetResourceList();

#         return $this->GetFilteredResources($resources);
#     }

#     public function GetList($pageNumber, $pageSize, $sortField = null, $sortDirection = null, $filter = null)
#     {
#         if (!$this->user->IsAdmin) {
#             $scheduleAdminGroupIds = [];
#             $resourceAdminGroupIds = [];

#             $groups = $this->repo->LoadGroups($this->user->UserId, [RoleLevel::SCHEDULE_ADMIN, RoleLevel::RESOURCE_ADMIN]);
#             foreach ($groups as $group) {
#                 if ($group->IsResourceAdmin) {
#                     $resourceAdminGroupIds[] = $group->GroupId;
#                 }

#                 if ($group->IsScheduleAdmin) {
#                     $scheduleAdminGroupIds[] = $group->GroupId;
#                 }
#             }

#             if ($filter == null) {
#                 $filter = new SqlFilterNull();
#             }

#             $additionalFilter = new SqlFilterIn(new SqlFilterColumn(TableNames::SCHEDULES_ALIAS, ColumnNames::SCHEDULE_ADMIN_GROUP_ID), $scheduleAdminGroupIds);
#             $filter->_And($additionalFilter->_Or(new SqlFilterIn(new SqlFilterColumn(TableNames::RESOURCES_ALIAS, ColumnNames::RESOURCE_ADMIN_GROUP_ID), $resourceAdminGroupIds)));
#         }

#         return parent::GetList($pageNumber, $pageSize, $sortField, $sortDirection, $filter);
#     }

#     public function Update(BookableResource $resource)
#     {
#         if (!$this->user->IsAdmin) {
#             $user = $this->repo->LoadById($this->user->UserId);
#             if (!$user->IsResourceAdminFor($resource)) {
#                 // if we got to this point, the user does not have the ability to update the resource
#                 throw new Exception(sprintf('Resource Update Failed. User %s does not have admin access to resource %s.', $this->user->UserId, $resource->GetId()));
#             }
#         }

#         parent::Update($resource);
#     }

#     public function GetScheduleResources($scheduleId)
#     {
#         $resources =  parent::GetScheduleResources($scheduleId);
#         return $this->GetFilteredResources($resources);
#     }

#     /**
#      * @param $resources
#      * @return array|BookableResource[]
#      */
#     private function GetFilteredResources($resources)
#     {
#         if ($this->user->IsAdmin) {
#             return $resources;
#         }

#         $user = $this->repo->LoadById($this->user->UserId);

#         $filteredResources = [];
#         /** @var $resource BookableResource */
#         foreach ($resources as $resource) {
#             if ($user->IsResourceAdminFor($resource)) {
#                 $filteredResources[] = $resource;
#             }
#         }

#         return $filteredResources;
#     }
# } -->

from fastapi import FastAPI, Depends, HTTPException

# Assume you have defined the necessary Pydantic models and FastAPI dependencies.
# You can add them here or import them from other modules.

# Create a FastAPI app
app = FastAPI()

# Sample UserRepository and ResourceRepository classes
class UserRepository:
    def LoadGroups(self, user_id, role_levels):
        # Implementation for loading user groups based on user_id and role_levels
        pass

class ResourceRepository:
    def GetResourceList(self):
        # Implementation for getting a list of all resources
        pass

    def GetList(self, page_number, page_size, sort_field=None, sort_direction=None, filter=None):
        # Implementation for getting a list of resources based on the provided parameters
        pass

    def Update(self, resource):
        # Implementation for updating a resource
        pass

    def GetScheduleResources(self, schedule_id):
        # Implementation for getting a list of resources for a schedule
        pass

# ResourceAdminResourceRepository
class ResourceAdminResourceRepository(ResourceRepository):
    def __init__(self, repo, user_session):
        self.repo = repo
        self.user = user_session
        super().__init__()

    def GetResourceList(self):
        resources = super().GetResourceList()
        return self.GetFilteredResources(resources)

    def GetList(self, page_number, page_size, sort_field=None, sort_direction=None, filter=None):
        if not self.user.IsAdmin:
            schedule_admin_group_ids = []
            resource_admin_group_ids = []

            groups = self.repo.LoadGroups(self.user.UserId, [RoleLevel.SCHEDULE_ADMIN, RoleLevel.RESOURCE_ADMIN])
            for group in groups:
                if group.IsResourceAdmin:
                    resource_admin_group_ids.append(group.GroupId)

                if group.IsScheduleAdmin:
                    schedule_admin_group_ids.append(group.GroupId)

            if not filter:
                filter = SqlFilterNull()

            additional_filter = SqlFilterIn(SqlFilterColumn(TableNames.SCHEDULES_ALIAS, ColumnNames.SCHEDULE_ADMIN_GROUP_ID), schedule_admin_group_ids)
            filter._And(additional_filter._Or(SqlFilterIn(SqlFilterColumn(TableNames.RESOURCES_ALIAS, ColumnNames.RESOURCE_ADMIN_GROUP_ID), resource_admin_group_ids)))

        return super().GetList(page_number, page_size, sort_field, sort_direction, filter)

    def Update(self, resource):
        if not self.user.IsAdmin:
            user = self.repo.LoadById(self.user.UserId)
            if not user.IsResourceAdminFor(resource):
                # if we got to this point, the user does not have the ability to update the resource
                raise HTTPException(status_code=403, detail=f"Resource Update Failed. User {self.user.UserId} does not have admin access to resource {resource.GetId()}.")

        super().Update(resource)

    def GetScheduleResources(self, schedule_id):
        resources = super().GetScheduleResources(schedule_id)
        return self.GetFilteredResources(resources)

    def GetFilteredResources(self, resources):
        if self.user.IsAdmin:
            return resources

        user = self.repo.LoadById(self.user.UserId)
        filtered_resources = [resource for resource in resources if user.IsResourceAdminFor(resource)]
        return filtered_resources

# FastAPI endpoint for getting a list of resources
@app.get("/resources/")
async def get_resources(
    page_number: int = 1,
    page_size: int = 10,
    sort_field: str = None,
    sort_direction: str = None,
    filter: ReservationFilter = None,
    user: UserSession = Depends(get_current_user),
    resource_repo: ResourceAdminResourceRepository = Depends(get_resource_admin_resource_repository)
):
    # Here, you can use the `resource_repo` instance to call the GetList method
    resources = resource_repo.GetList(page_number, page_size, sort_field, sort_direction, filter)

    # Process the resources and return the response
    return {"data": resources, "total": len(resources)}

# Define the dependency to get the ResourceAdminResourceRepository instance
def get_resource_admin_resource_repository(
    repo: UserRepository = Depends(),
    user_session: UserSession = Depends(get_current_user)
):
    return ResourceAdminResourceRepository(repo, user_session)

# Define other dependencies as needed (e.g., get_current_user function to get the UserSession)
def get_current_user():
    # Implementation to get the UserSession based on authentication or request context
    pass

