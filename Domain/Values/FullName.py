# <?php

# class FullName
# {
#     /**
#      * @var string
#      */
#     private $fullName;

#     public function __construct($firstName, $lastName)
#     {
#         $formatter = Configuration::Instance()->GetKey(ConfigKeys::NAME_FORMAT);
#         if (empty($formatter)) {
#             $this->fullName = "$firstName $lastName";
#         } else {
#             $this->fullName = str_replace('{first}', $firstName, $formatter);
#             $this->fullName = str_replace('{last}', $lastName, $this->fullName);
#         }
#     }

#     public function __toString()
#     {
#         return $this->fullName;
#     }
# }


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the FullName model using Pydantic
class FullNameModel(BaseModel):
    first_name: str
    last_name: str

# Implement the FullName class functionality
class FullName:
    def __init__(self, first_name: str, last_name: str):
        formatter = " {first} {last}"  # Default formatter if no configuration is available
        # You can replace the above line with the actual configuration retrieval logic
        self.full_name = formatter.format(first=first_name, last=last_name)

    def __str__(self):
        return self.full_name

