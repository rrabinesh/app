# <?php

# class ResourceStatus
# {
#     public const HIDDEN = 0;
#     public const AVAILABLE = 1;
#     public const UNAVAILABLE = 2;
# }

# class ResourceStatusReason
# {
#     /**
#      * @var string
#      */
#     private $description;

#     /**
#      * @var int|null
#      */
#     private $id;

#     /**
#      * @var int|ResourceStatus
#      */
#     private $statusId;

#     /**
#      * @param int|null $id
#      * @param int|ResourceStatus $statusId
#      * @param string|null $description
#      */
#     public function __construct($id, $statusId, $description = null)
#     {
#         $this->description = $description;
#         $this->id = $id;
#         $this->statusId = $statusId;
#     }

#     /**
#      * @return int|null
#      */
#     public function Id()
#     {
#         return $this->id;
#     }

#     /**
#      * @return int|ResourceStatus
#      */
#     public function StatusId()
#     {
#         return $this->statusId;
#     }

#     /**
#      * @return string
#      */
#     public function Description()
#     {
#         return $this->description;
#     }
# }


from enum import IntEnum
from typing import Optional

class ResourceStatus(IntEnum):
    HIDDEN = 0
    AVAILABLE = 1
    UNAVAILABLE = 2

class ResourceStatusReason:
    def __init__(self, id: Optional[int], status_id: ResourceStatus, description: Optional[str] = None):
        self.description = description
        self.id = id
        self.statusId = status_id

    def get_id(self) -> Optional[int]:
        return self.id

    def get_status_id(self) -> ResourceStatus:
        return self.statusId

    def get_description(self) -> Optional[str]:
        return self.description


