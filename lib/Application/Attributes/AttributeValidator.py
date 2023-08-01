# <?php

# require_once(ROOT_DIR . 'lib/Common/Validators/namespace.php');

# class AttributeValidator extends ValidatorBase
# {
#     /**
#      * @var IAttributeService
#      */
#     private $service;

#     /**
#      * @var CustomAttributeCategory|int
#      */
#     private $category;

#     /**
#      * @var array|AttributeValue[]
#      */
#     private $attributes;

#     /**
#      * @var array|string[]
#      */
#     private $messages;

#     /**
#      * @var int|null
#      */
#     private $entityId;

#     /**
#      * @var bool
#      */
#     private $ignoreEmpty;

#     /**
#      * @var bool
#      */
#     private $isAdmin;

#     /**
#      * @param IAttributeService $service
#      * @param $category int|CustomAttributeCategory
#      * @param $attributes AttributeValue|array|AttributeValue[]
#      * @param $entityId int
#      * @param bool $ignoreEmpty
#      * @param bool $isAdmin
#      */
#     public function __construct(IAttributeService $service, $category, $attributes, $entityId = null, $ignoreEmpty = false, $isAdmin = false)
#     {
#         $this->service = $service;
#         $this->category = $category;
#         $this->attributes = is_array($attributes) ? $attributes : [$attributes];
#         $this->entityId = $entityId;
#         $this->ignoreEmpty = $ignoreEmpty;
#         $this->isAdmin = $isAdmin;
#     }

#     /**
#      * @return void
#      */
#     public function Validate()
#     {
#         if (empty($this->attributes)) {
#             $this->isValid = true;
#             return;
#         }

#         $result = $this->service->Validate($this->category, $this->attributes, $this->entityId, $this->ignoreEmpty, $this->isAdmin);
#         $this->isValid = $result->IsValid();
#         $this->messages = $result->Errors();
#     }

#     public function Messages()
#     {
#         return $this->messages;
#     }
# }

# class AttributeValidatorInline extends AttributeValidator
# {
#     public function ReturnsErrorResponse()
#     {
#         return true;
#     }
# }


from fastapi import FastAPI

app = FastAPI()

# Define custom attribute categories if needed
class CustomAttributeCategory:
    # Your custom attribute category definitions go here
    pass

class IAttributeService:
    # Your IAttributeService interface definition goes here
    pass

class AttributeValue:
    # Your AttributeValue class definition goes here
    pass

class AttributeValidator:
    def __init__(self, service, category, attributes, entity_id=None, ignore_empty=False, is_admin=False):
        self.service = service
        self.category = category
        self.attributes = attributes if isinstance(attributes, list) else [attributes]
        self.entity_id = entity_id
        self.ignore_empty = ignore_empty
        self.is_admin = is_admin
        self.messages = []
        self.is_valid = None

    def validate(self):
        if not self.attributes:
            self.is_valid = True
            return

        result = self.service.Validate(self.category, self.attributes, self.entity_id, self.ignore_empty, self.is_admin)
        self.is_valid = result.IsValid()
        self.messages = result.Errors()

    def get_messages(self):
        return self.messages

class AttributeValidatorInline(AttributeValidator):
    def returns_error_response(self):
        return True

# Instantiate the AttributeService with the required dependencies
class AttributeService:
    # Your AttributeService class definition goes here
    pass

attribute_service = AttributeService()  # Replace with the actual service implementation

@app.post("/validate/attributes/")
def validate_attributes(category: int, attributes: List[AttributeValue], entity_id: int = None, ignore_empty: bool = False, is_admin: bool = False):
    validator = AttributeValidator(attribute_service, category, attributes, entity_id, ignore_empty, is_admin)
    validator.validate()
    return {"is_valid": validator.is_valid, "messages": validator.get_messages()}

@app.post("/validate/attributes/inline/")
def validate_attributes_inline(category: int, attributes: List[AttributeValue], entity_id: int = None, ignore_empty: bool = False, is_admin: bool = False):
    validator = AttributeValidatorInline(attribute_service, category, attributes, entity_id, ignore_empty, is_admin)
    validator.validate()
    return {"is_valid": validator.is_valid, "messages": validator.get_messages()}


