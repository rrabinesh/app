# <?php

# class AccessoryResponse extends RestResponse
# {
#     public $id;
#     public $name;
#     public $quantityAvailable;
#     public $associatedResources = [];

#     public function __construct(IRestServer $server, Accessory $accessory)
#     {
#         $this->id = $accessory->GetId();
#         $this->name = $accessory->GetName();
#         $this->quantityAvailable = $accessory->GetQuantityAvailable();
#         $this->associatedResources = $this->GetResources($server, $accessory->Resources());
#     }

#     public static function Example()
#     {
#         return new ExampleAccessoryResponse(null, new Accessory(1, 'accessoryName', 10));
#     }

#     /**
#      * @param IRestServer $server
#      * @param ResourceAccessory[] $resources
#      * @return AssociatedResourceResponse[]
#      */
#     private function GetResources(IRestServer $server, $resources)
#     {
#         $items = [];
#         foreach ($resources as $r) {
#             $items[] = new AssociatedResourceResponse($server, $r);
#         }

#         return $items;
#     }
# }

# class AssociatedResourceResponse extends RestResponse
# {
#     public $resourceId;
#     public $minQuantity;
#     public $maxQuantity;

#     public function __construct(IRestServer $server, ResourceAccessory $resourceAccessory)
#     {
#         $this->resourceId = $resourceAccessory->ResourceId;
#         $this->minQuantity = $resourceAccessory->MinQuantity;
#         $this->maxQuantity = $resourceAccessory->MaxQuantity;
#         $this->AddService($server, WebServices::GetResource, [WebServiceParams::ResourceId => $resourceAccessory->ResourceId]);
#     }

#     public static function Example()
#     {
#         return new ExampleAssociatedResourceResponse();
#     }
# }

# class ExampleAccessoryResponse extends AccessoryResponse
# {
#     public function __construct()
#     {
#         $this->id = 1;
#         $this->name = 'accessoryName';
#         $this->quantityAvailable = 10;
#         $this->associatedResources = [AssociatedResourceResponse::Example()];
#     }
# }

# class ExampleAssociatedResourceResponse extends AssociatedResourceResponse
# {
#     public function __construct()
#     {
#         $this->resourceId = 1;
#         $this->maxQuantity = 10;
#         $this->minQuantity = 4;
#     }
# }

from fastapi import FastAPI
from typing import List

app = FastAPI()

# Define the ResourceAccessory equivalent Pydantic model
class ResourceAccessory(BaseModel):
    ResourceId: int
    MinQuantity: int
    MaxQuantity: int

# Define the Accessory equivalent Pydantic model
class Accessory(BaseModel):
    Id: int
    Name: str
    QuantityAvailable: int
    Resources: List[ResourceAccessory]

# Define the AssociatedResourceResponse equivalent Pydantic model
class AssociatedResourceResponse(BaseModel):
    resourceId: int
    minQuantity: int
    maxQuantity: int

# Define the AccessoryResponse equivalent Pydantic model
class AccessoryResponse(BaseModel):
    id: int
    name: str
    quantityAvailable: int
    associatedResources: List[AssociatedResourceResponse]

# Sample data (replace with actual data from the database)
associated_resources_data = [
    {
        "ResourceId": 1,
        "MinQuantity": 4,
        "MaxQuantity": 10,
    },
    # Add more sample data as needed
]

accessory_data = {
    "Id": 1,
    "Name": "Accessory 1",
    "QuantityAvailable": 10,
    "Resources": associated_resources_data,
}

# Convert sample data into Pydantic models
associated_resources = [
    AssociatedResourceResponse(**resource) for resource in associated_resources_data
]
accessory = Accessory(**accessory_data)
accessory_response = AccessoryResponse(
    id=accessory.Id,
    name=accessory.Name,
    quantityAvailable=accessory.QuantityAvailable,
    associatedResources=associated_resources,
)

# Endpoint to get accessory by ID
@app.get("/accessories/{accessory_id}", response_model=AccessoryResponse)
def get_accessory(accessory_id: int):
    # Replace this part with your actual logic to fetch accessory data from the database or data source
    # For demonstration purposes, we are returning the pre-built accessory_response based on the sample data
    return accessory_response



