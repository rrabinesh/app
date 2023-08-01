# <?php

# class JsonRequest
# {
#     public function __construct($jsonObject = null)
#     {
#         $this->Hydrate($jsonObject);
#     }

#     private function Hydrate($jsonObject)
#     {
#         if (empty($jsonObject)) {
#             return;
#         }

#         foreach ($jsonObject as $key => $value) {
#             $this->$key = $value;
#         }
#     }
# }

from typing import Optional
from pydantic import BaseModel

class JsonRequest(BaseModel):
    def __init__(self, **data):
        super().__init__(**data)

    def __init_subclass__(cls):
        cls.__signature__ = None  # Remove the signature validation for sub-classes
        super().__init_subclass__()

    def hydrate(self, json_object: dict):
        # Set the attributes of the class based on the keys in the JSON object
        for key, value in json_object.items():
            setattr(self, key, value)


