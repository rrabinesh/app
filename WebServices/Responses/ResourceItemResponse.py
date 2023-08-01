# <?php

# require_once(ROOT_DIR . 'lib/WebService/namespace.php');

# class ResourceItemResponse extends RestResponse
# {
#     public $id;
#     public $name;
#     public $type;
#     public $groups;

#     public function __construct(IRestServer $server, $id, $name)
#     {
#         $this->id = $id;
#         $this->name = $name;

#         /*
#          * Unfortunately we have to get the full resource here to be able to get the
#          * resource_type_id
#          */
#         $resourceRepository = new ResourceRepository();
#         $resource = $resourceRepository->LoadById($id);

#         if ($resource->HasResourceType()) {
#             $this->type = $resourceRepository->LoadResourceType($resource->GetResourceTypeId())->Name();
#         }

#         /*
#          * For every resource we want to see the full hierarchical path of groups it belongs to.
#          * This will add an array containing first parent and consecutive ancestors.
#          * This is added here so it is not necessary to retrieve this in separate queries for
#          * every resource and group it's assigned to.
#          */
#         $this->groups = [];

#         foreach ($resource->GetResourceGroupIds() as $resourceGroupId) {
#             $this->groups[$resourceGroupId] = $this->BuildParentList($resourceGroupId);
#         }

#         $this->AddService($server, WebServices::GetResource, [WebServiceParams::ResourceId => $id]);
#     }

#     private function BuildParentList($resourceGroupId, &$parents=[])
#     {
#         $groupsReader = ServiceLocator::GetDatabase()->Query(new GetResourceGroupCommand($resourceGroupId));
#         if ($group = $groupsReader->GetRow()) {
#             $parents[$group[ColumnNames::RESOURCE_GROUP_ID]] = new ResourceGroup(
#                 $group[ColumnNames::RESOURCE_GROUP_ID],
#                 $group[ColumnNames::RESOURCE_GROUP_NAME],
#                 $group[ColumnNames::RESOURCE_GROUP_PARENT_ID]
#             );

#             $this->BuildParentList($group[ColumnNames::RESOURCE_GROUP_PARENT_ID], $parents);
#         }
#         $groupsReader->Free();

#         return $parents;
#     }

#     public static function Example()
#     {
#         return new ExampleResourceItemResponse();
#     }
# }

# class ExampleResourceItemResponse extends ResourceItemResponse
# {
#     public function __construct()
#     {
#         $this->id = 123;
#         $this->name = 'resource name';
#     }
# }




from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Define the Pydantic model for ResourceItemResponse
class ResourceItemResponse(BaseModel):
    id: int
    name: str
    type: str = None
    groups: Dict[int, Dict[str, str]] = {}

# Define the ExampleResourceItemResponse Pydantic model
class ExampleResourceItemResponse(ResourceItemResponse):
    id: int = 123
    name: str = 'resource name'

# Define the endpoint to get the example resource item response
@app.get("/resource_item/")
def resource_item():
    return ExampleResourceItemResponse()



