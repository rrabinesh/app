# <?php

# class Accessory
# {
#     /**
#      * @var int
#      */
#     private $id;


#     /**
#      * @var string
#      */
#     private $name;

#     /**
#      * @var int
#      */
#     private $quantityAvailable;

#     /**
#      * @var ResourceAccessory[]
#      */
#     private $resources = [];

#     /**
#      * @param int $id
#      * @param string $name
#      * @param int $quantityAvailable
#      */
#     public function __construct($id, $name, $quantityAvailable)
#     {
#         $this->id = $id;
#         $this->SetName($name);
#         $this->SetQuantityAvailable($quantityAvailable);
#     }

#     /**
#      * @return int
#      */
#     public function GetId()
#     {
#         return $this->id;
#     }

#     /**
#      * @return string
#      */
#     public function GetName()
#     {
#         return $this->name;
#     }

#     /**
#      * @param string $name
#      * @return void
#      */
#     public function SetName($name)
#     {
#         $this->name = $name;
#     }

#     /**
#      * @param int $quantity
#      */
#     public function SetQuantityAvailable($quantity)
#     {
#         $q = intval($quantity);
#         $this->quantityAvailable = empty($q) ? null : $q;
#     }

#     /**
#      * @return int
#      */
#     public function GetQuantityAvailable()
#     {
#         return $this->quantityAvailable;
#     }

#     /**
#      * @return ResourceAccessory[]
#      */
#     public function Resources()
#     {
#         return $this->resources;
#     }

#     /**
#      * @return int[]
#      */
#     public function ResourceIds()
#     {
#         $ids = [];
#         foreach ($this->resources as $resource) {
#             $ids[] = $resource->ResourceId;
#         }

#         return $ids;
#     }

#     /**
#      * @static
#      * @param string $name
#      * @param int $quantity
#      * @return Accessory
#      */
#     public static function Create($name, $quantity)
#     {
#         return new Accessory(null, $name, $quantity);
#     }

#     /**
#      * @return bool
#      */
#     public function HasUnlimitedQuantity()
#     {
#         return empty($this->quantityAvailable);
#     }

#     public function AddResource($resourceId, $minQuantity, $maxQuantity)
#     {
#         $this->resources[] = new ResourceAccessory($resourceId, $minQuantity, $maxQuantity);
#     }

#     /**
#      * @param ResourceAccessory[] $resources
#      */
#     public function ChangeResources($resources)
#     {
#         $this->resources = $resources;
#     }

#     /**
#      * @return bool
#      */
#     public function IsTiedToResource()
#     {
#         return count($this->resources) > 0;
#     }

#     /**
#      * @param int $resourceId
#      * @return ResourceAccessory
#      */
#     public function GetResource($resourceId)
#     {
#         foreach ($this->resources as $resource) {
#             if ($resource->ResourceId == $resourceId) {
#                 return $resource;
#             }
#         }

#         return null;
#     }
# }

# class ResourceAccessory
# {
#     public $ResourceId;
#     public $MinQuantity;
#     public $MaxQuantity;

#     public function __construct($resourceId, $minQuantity, $maxQuantity)
#     {
#         $this->ResourceId = $resourceId;
#         $this->MinQuantity = empty($minQuantity) ? null : (int)$minQuantity;
#         $this->MaxQuantity = empty($maxQuantity) ? null : (int)$maxQuantity;
#         ;
#     }
# }


from typing import List, Optional
from pydantic import BaseModel

class ResourceAccessory(BaseModel):
    resource_id: int
    min_quantity: Optional[int] = None
    max_quantity: Optional[int] = None

class Accessory(BaseModel):
    id: Optional[int] = None
    name: str
    quantity_available: Optional[int] = None
    resources: List[ResourceAccessory] = []

    @staticmethod
    def create(name: str, quantity: Optional[int]):
        return Accessory(name=name, quantity_available=quantity)

    def add_resource(self, resource_id: int, min_quantity: Optional[int], max_quantity: Optional[int]):
        self.resources.append(ResourceAccessory(resource_id=resource_id, min_quantity=min_quantity, max_quantity=max_quantity))

    def change_resources(self, resources: List[ResourceAccessory]):
        self.resources = resources

    def has_unlimited_quantity(self) -> bool:
        return self.quantity_available is None

    def is_tied_to_resource(self) -> bool:
        return len(self.resources) > 0

    def get_resource(self, resource_id: int) -> Optional[ResourceAccessory]:
        for resource in self.resources:
            if resource.resource_id == resource_id:
                return resource
        return None

