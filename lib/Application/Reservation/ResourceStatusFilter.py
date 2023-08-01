# <?php

# class ResourceStatusFilter implements IResourceFilter
# {
#     /**
#      * @var IUserRepository
#      */
#     private $userRepository;

#     /**
#      * @var UserSession
#      */
#     private $user;

#     public function __construct(IUserRepository $userRepository, UserSession $user)
#     {
#         $this->user = $user;
#         $this->userRepository = $userRepository;
#     }

#     /**
#      * @param IResource $resource
#      * @return bool
#      */
#     public function ShouldInclude($resource)
#     {
#         if ($resource->GetStatusId() != ResourceStatus::AVAILABLE) {
#             $user = $this->userRepository->LoadById($this->user->UserId);
#             return $user->IsResourceAdminFor($resource);
#         }

#         return true;
#     }
# }



from fastapi import HTTPException
from fastapi import status

class IUserRepository:
    # Define the methods of IUserRepository here as required
    pass

class UserSession:
    # Define the properties and methods of UserSession here as required
    pass

class ResourceStatusFilter:
    def __init__(self, user_repository: IUserRepository, user: UserSession):
        self.user_repository = user_repository
        self.user = user

    def should_include(self, resource):
        if resource.status_id != ResourceStatus.AVAILABLE:
            user = self.user_repository.load_by_id(self.user.user_id)
            return user.is_resource_admin_for(resource)

        return True

# Sample usage in a FastAPI application:

from fastapi import FastAPI

app = FastAPI()

# Replace IUserRepository and UserSession with actual implementations
user_repository = IUserRepository()
user_session = UserSession()

resource_filter = ResourceStatusFilter(user_repository, user_session)

@app.get("/resources/")
def get_resources():
    all_resources = [resource1, resource2, resource3]  # Replace with actual resource data
    filtered_resources = [resource for resource in all_resources if resource_filter.should_include(resource)]
    return filtered_resources




