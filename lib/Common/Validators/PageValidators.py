# <?php

# class PageValidators
# {
#     /**
#      * @var array|IValidator[]
#      */
#     private $validators = [];

#     /**
#      * @var bool
#      */
#     private $isValidated = false;

#     /**
#      * @var SmartyPage
#      */
#     private $page;

#     public function __construct(SmartyPage $page)
#     {
#         $this->page = $page;
#     }

#     public function Register($id, $validator)
#     {
#         $this->validators[$id] = $validator;
#     }

#     public function Validate()
#     {
#         foreach ($this->validators as $id => $validator) {
#             $validator->Validate();

#             if (!$validator->IsValid()) {
#                 $this->page->AddFailedValidation($id, $validator);
#             }
#         }

#         $this->isValidated = true;
#     }

#     public function AreAllValid()
#     {
#         if (!$this->isValidated) {
#             $this->Validate();
#         }

#         foreach ($this->validators as $validator) {
#             if (!$validator->IsValid()) {
#                 return false;
#             }
#         }

#         return true;
#     }

#     public function Get($id)
#     {
#         if (!array_key_exists($id, $this->validators)) {
#             return new NullValidator();
#         }
#         return $this->validators[$id];
#     }
# }

# class NullValidator extends ValidatorBase implements IValidator
# {
#     public function Validate()
#     {
#         $this->isValid = true;
#     }
# }

from fastapi import HTTPException
from pydantic import BaseModel

from .interfaces import IValidator

class PageValidators:
    
    def __init__(self, validators: dict[str, IValidator]):
        self.validators = validators
        self.is_validated = False
        
    def validate(self) -> None:
        for name, validator in self.validators.items():
            try:
                validator.validate()
            except HTTPException:
                raise HTTPException(status_code=400, detail=f"{name} validation failed")
                
        self.is_validated = True
            
    def is_valid(self) -> bool:
        if not self.is_validated:
            self.validate()
            
        return all(v.is_valid for v in self.validators.values())
