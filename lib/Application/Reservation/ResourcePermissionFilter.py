# <?php

# class ResourcePermissionFilter implements IResourceFilter
# {
#     /**
#      * @var IPermissionService $permissionService
#      */
#     private $permissionService;

#     /**
#      * @var UserSession $user
#      */
#     private $user;

#     public function __construct(IPermissionService $permissionService, UserSession $user)
#     {
#         $this->permissionService = $permissionService;
#         $this->user = $user;
#     }

#     public function ShouldInclude($resource)
#     {
#         return $this->permissionService->CanAccessResource($resource, $this->user);
#     }

#     public function CanBook($resource)
#     {
#         return $this->permissionService->CanBookResource($resource, $this->user);
#     }
# }


from fastapi import HTTPException
from fastapi import status

class IPermissionService:
    # Define the methods of IPermissionService here as required
    pass

class UserSession:
    # Define the properties and methods of UserSession here as required
    pass

class ResourcePermissionFilter:
    def __init__(self, permission_service: IPermissionService, user: UserSession):
        self.permission_service = permission_service
        self.user = user

    def should_include(self, resource):
        return self.permission_service.can_access_resource(resource, self.user)

    def can_book(self, resource):
        return self.permission_service.can_book_resource(resource, self.user)

    def filter_resources(self, resources):
        included_resources = [resource for resource in resources if self.should_include(resource)]
        return included_resources

    def filter_bookable_resources(self, resources):
        bookable_resources = [resource for resource in resources if self.can_book(resource)]
        return bookable_resources

# Sample usage in a FastAPI application:

from fastapi import FastAPI

app = FastAPI()

# Replace IPermissionService and UserSession with actual implementations
permission_service = IPermissionService()
user_session = UserSession()

resource_filter = ResourcePermissionFilter(permission_service, user_session)

@app.get("/resources/")
def get_resources():
    all_resources = [resource1, resource2, resource3]  # Replace with actual resource data
    return resource_filter.filter_resources(all_resources)

@app.get("/bookable-resources/")
def get_bookable_resources():
    all_resources = [resource1, resource2, resource3]  # Replace with actual resource data
    return resource_filter.filter_bookable_resources(all_resources)




