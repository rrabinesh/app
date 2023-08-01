# <?php

# class ReservationResource implements IPermissibleResource
# {
#     private $_id;
#     private $_resourceName;

#     public function __construct($resourceId, $resourceName = '')
#     {
#         $this->_id = $resourceId;
#         $this->_resourceName = $resourceName;
#     }

#     public function GetResourceId()
#     {
#         return $this->_id;
#     }

#     public function GetName()
#     {
#         return $this->_resourceName;
#     }

#     public function GetId()
#     {
#         return $this->_id;
#     }
# }


class ReservationResource:
    def __init__(self, resource_id: int, resource_name: str = ''):
        self._id = resource_id
        self._resource_name = resource_name

    def get_resource_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._resource_name

    def get_id(self) -> int:
        return self._id


