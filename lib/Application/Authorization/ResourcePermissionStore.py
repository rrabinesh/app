# <?php

# require_once(ROOT_DIR . 'Domain/Access/namespace.php');

# interface IResourcePermissionStore
# {
#     /**
#      * @param $userId int
#      * @return array[]int
#      */
#     public function GetAllResources($userId);

#     /**
#      * @param $userId int
#      * @return array[]int
#      */
#     public function GetBookableResources($userId);

#     /**
#      * @param $userId int
#      * @return array[]int
#      */
#     public function GetViewOnlyResources($userId);
# }

# class ResourcePermissionStore implements IResourcePermissionStore
# {
#     /**
#      * @var IScheduleUserRepository
#      */
#     private $_scheduleUserRepository;

#     /**
#      * @param IScheduleUserRepository $scheduleUserRepository
#      */
#     public function __construct(IScheduleUserRepository $scheduleUserRepository)
#     {
#         $this->_scheduleUserRepository = $scheduleUserRepository;
#     }

#     public function GetAllResources($userId)
#     {
#         $permittedResourceIds = [];

#         $user = $this->_scheduleUserRepository->GetUser($userId);

#         $resources = $user->GetAllResources();
#         foreach ($resources as $resource) {
#             $permittedResourceIds[] = $resource->Id();
#         }

#         return $permittedResourceIds;
#     }

#     public function GetBookableResources($userId)
#     {
#         $resourceIds = [];

#         $user = $this->_scheduleUserRepository->GetUser($userId);

#         $resources = $user->GetBookableResources();

#         foreach ($resources as $resource) {
#             $resourceIds[] = $resource->Id();
#         }

#         return $resourceIds;
#     }

#     public function GetViewOnlyResources($userId)
#     {
#         $resourceIds = [];

#         $user = $this->_scheduleUserRepository->GetUser($userId);

#         $resources = $user->GetViewOnlyResources();

#         foreach ($resources as $resource) {
#             $resourceIds[] = $resource->Id();
#         }

#         return $resourceIds;
#     }
# }


from typing import List

from fastapi import FastAPI, Depends

# Define your IScheduleUserRepository and other required classes or data models here

app = FastAPI()

class IResourcePermissionStore:
    def GetAllResources(self, userId: int) -> List[int]:
        pass

    def GetBookableResources(self, userId: int) -> List[int]:
        pass

    def GetViewOnlyResources(self, userId: int) -> List[int]:
        pass

class ResourcePermissionStore(IResourcePermissionStore):
    def __init__(self, scheduleUserRepository: IScheduleUserRepository):
        self._scheduleUserRepository = scheduleUserRepository

    def GetAllResources(self, userId: int) -> List[int]:
        permittedResourceIds = []
        user = self._scheduleUserRepository.GetUser(userId)
        resources = user.GetAllResources()
        for resource in resources:
            permittedResourceIds.append(resource.Id())
        return permittedResourceIds

    def GetBookableResources(self, userId: int) -> List[int]:
        resourceIds = []
        user = self._scheduleUserRepository.GetUser(userId)
        resources = user.GetBookableResources()
        for resource in resources:
            resourceIds.append(resource.Id())
        return resourceIds

    def GetViewOnlyResources(self, userId: int) -> List[int]:
        resourceIds = []
        user = self._scheduleUserRepository.GetUser(userId)
        resources = user.GetViewOnlyResources()
        for resource in resources:
            resourceIds.append(resource.Id())
        return resourceIds

# Dependency to get the resource permission store
def get_resource_permission_store() -> IResourcePermissionStore:
    schedule_user_repository = ...  # Replace this with the actual implementation of IScheduleUserRepository
    return ResourcePermissionStore(schedule_user_repository)

# Dependency to get the resource permission store
def get_resource_permission_store(resource_permission_store: IResourcePermissionStore = Depends(get_resource_permission_store)) -> IResourcePermissionStore:
    return resource_permission_store

