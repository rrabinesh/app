# <?php

# class AccessoriesResponse extends RestResponse
# {
#     /**
#      * @var AccessoryItemResponse
#      */
#     public $accessories;

#     /**
#      * @param IRestServer $server
#      * @param AccessoryDto[] $accessories
#      */
#     public function __construct(IRestServer $server, $accessories)
#     {
#         /** @var $accessory AccessoryDto */
#         foreach ($accessories as $accessory) {
#             $this->accessories[] = new AccessoryItemResponse($server, $accessory);
#         }
#     }

#     public static function Example()
#     {
#         return new ExampleAccessoriesResponse();
#     }
# }

# class ExampleAccessoriesResponse extends AccessoriesResponse
# {
#     public function __construct()
#     {
#         $this->accessories = [AccessoryItemResponse::Example()];
#     }
# }

# class AccessoryItemResponse extends RestResponse
# {
#     public $id;
#     public $name;
#     public $quantityAvailable;
#     public $associatedResourceCount;

#     public function __construct(IRestServer $server, AccessoryDto $accessory)
#     {
#         $this->id = $accessory->Id;
#         $this->name = $accessory->Name;
#         $this->quantityAvailable = $accessory->QuantityAvailable;
#         $this->associatedResourceCount = $accessory->AssociatedResources;
#         $this->AddService($server, WebServices::GetAccessory, [WebServiceParams::AccessoryId => $this->id]);
#     }

#     public static function Example()
#     {
#         return new ExampleAccessoryItemResponse();
#     }
# }

# class ExampleAccessoryItemResponse extends AccessoryItemResponse
# {
#     public function __construct()
#     {
#         $this->id = 1;
#         $this->name = 'accessoryName';
#         $this->quantityAvailable = 3;
#         $this->associatedResourceCount = 10;
#     }
# }

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define the AccessoryDto equivalent Pydantic model
class AccessoryDto(BaseModel):
    Id: int
    Name: str
    QuantityAvailable: int
    AssociatedResources: int

# Define the AccessoryItemResponse equivalent Pydantic model
class AccessoryItemResponse(BaseModel):
    id: int
    name: str
    quantityAvailable: int
    associatedResourceCount: int

# Define the AccessoriesResponse equivalent Pydantic model
class AccessoriesResponse(BaseModel):
    accessories: List[AccessoryItemResponse]

# Sample data (replace with actual data from the database)
accessories_data = [
    {
        "Id": 1,
        "Name": "Accessory 1",
        "QuantityAvailable": 5,
        "AssociatedResources": 10,
    },
    {
        "Id": 2,
        "Name": "Accessory 2",
        "QuantityAvailable": 3,
        "AssociatedResources": 8,
    },
    # Add more sample data as needed
]

# Endpoint to get accessories
@app.get("/accessories/", response_model=AccessoriesResponse)
def get_accessories():
    accessories = [
        AccessoryItemResponse(
            id=accessory["Id"],
            name=accessory["Name"],
            quantityAvailable=accessory["QuantityAvailable"],
            associatedResourceCount=accessory["AssociatedResources"],
        )
        for accessory in accessories_data
    ]
    return {"accessories": accessories}


