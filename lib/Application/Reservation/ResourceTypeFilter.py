# <?php

# class ResourceTypeFilter implements IResourceFilter
# {
#     /**
#      * @var $resourcetypename
#      */
#     private $resourcetypeids = [];

#     public function __construct($resourcetypename)
#     {
#         $reader = ServiceLocator::GetDatabase()
#                   ->Query(new GetResourceTypeByNameCommand($resourcetypename));

#         while ($row = $reader->GetRow()) {
#             $this->resourcetypeids[] = $row[ColumnNames::RESOURCE_TYPE_ID];
#         }

#         $reader->Free();
#     }

#     /**
#      * @param IResource $resource
#      * @return bool
#      */
#     public function ShouldInclude($assignment)
#     {
#         return in_array($assignment->GetResourceTypeId(), $this->resourcetypeids);
#     }
# }



from fastapi import FastAPI, HTTPException, status

# Define the ResourceStatus class with the necessary constants (if not already defined)
class ResourceStatus:
    AVAILABLE = "available"

# Define the IUserRepository and UserSession classes (if not already defined)
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

app = FastAPI()

# Replace IUserRepository and UserSession with actual implementations
user_repository = IUserRepository()
user_session = UserSession()

resource_filter = ResourceStatusFilter(user_repository, user_session)

# Define a Resource model (if not already defined)
class Resource:
    def __init__(self, resource_id, status_id):
        self.resource_id = resource_id
        self.status_id = status_id

# Sample usage in the FastAPI application:

resource1 = Resource(resource_id=1, status_id=ResourceStatus.AVAILABLE)
resource2 = Resource(resource_id=2, status_id=ResourceStatus.AVAILABLE)
resource3 = Resource(resource_id=3, status_id=ResourceStatus.AVAILABLE)

all_resources = [resource1, resource2, resource3]

@app.get("/resources/")
def get_resources():
    filtered_resources = [resource for resource in all_resources if resource_filter.should_include(resource)]
    return filtered_resources




