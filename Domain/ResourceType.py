# <?php

# class ResourceType
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
#      * @var string
#      */
#     private $description;

#     /**
#      * @var array|AttributeValue[]
#      */
#     private $attributeValues = [];

#     public function __construct($id, $name, $description, $attributeList = null)
#     {
#         $this->id = $id;
#         $this->name = $name;
#         $this->description = $description;
#         if (!empty($attributeList)) {
#             $attributes = CustomAttributes::Parse($attributeList);
#             foreach ($attributes->All() as $id => $value) {
#                 $this->WithAttribute(new AttributeValue($id, $value));
#             }
#         }
#     }

#     /**
#      * @param string $name
#      * @param string $description
#      * @return ResourceType
#      */
#     public static function CreateNew($name, $description)
#     {
#         return new ResourceType(0, $name, $description);
#     }

#     /**
#      * @return int
#      */
#     public function Id()
#     {
#         return $this->id;
#     }

#     /**
#      * @return string
#      */
#     public function Name()
#     {
#         return $this->name;
#     }

#     /**
#      * @return string
#      */
#     public function Description()
#     {
#         return $this->description;
#     }

#     /**
#      * @param $name string
#      */
#     public function SetName($name)
#     {
#         $this->name = $name;
#     }

#     /**
#      * @param $description string
#      */
#     public function SetDescription($description)
#     {
#         $this->description = $description;
#     }

#     public function WithAttribute(AttributeValue $attribute)
#     {
#         $this->attributeValues[$attribute->AttributeId] = $attribute;
#     }

#     /**
#      * @var array|AttributeValue[]
#      */
#     private $addedAttributeValues = [];

#     /**
#      * @var array|AttributeValue[]
#      */
#     private $removedAttributeValues = [];

#     /**
#      * @param $attributes AttributeValue[]|array
#      */
#     public function ChangeAttributes($attributes)
#     {
#         $diff = new ArrayDiff($this->attributeValues, $attributes);

#         $added = $diff->GetAddedToArray1();
#         $removed = $diff->GetRemovedFromArray1();

#         /** @var $attribute AttributeValue */
#         foreach ($added as $attribute) {
#             $this->addedAttributeValues[] = $attribute;
#         }

#         /** @var $accessory AttributeValue */
#         foreach ($removed as $attribute) {
#             $this->removedAttributeValues[] = $attribute;
#         }

#         foreach ($attributes as $attribute) {
#             $this->AddAttributeValue($attribute);
#         }
#     }

#     /**
#      * @param $attribute AttributeValue
#      */
#     public function ChangeAttribute($attribute)
#     {
#         $this->removedAttributeValues[] = $attribute;
#         $this->addedAttributeValues[] = $attribute;
#         $this->AddAttributeValue($attribute);
#     }

#     /**
#      * @param $attributeValue AttributeValue
#      */
#     public function AddAttributeValue($attributeValue)
#     {
#         $this->attributeValues[$attributeValue->AttributeId] = $attributeValue;
#     }

#     /**
#      * @return array|AttributeValue[]
#      */
#     public function GetAddedAttributes()
#     {
#         return $this->addedAttributeValues;
#     }

#     /**
#      * @return array|AttributeValue[]
#      */
#     public function GetRemovedAttributes()
#     {
#         return $this->removedAttributeValues;
#     }

#     /**
#      * @param $customAttributeId
#      * @return mixed
#      */
#     public function GetAttributeValue($customAttributeId)
#     {
#         if (array_key_exists($customAttributeId, $this->attributeValues)) {
#             return $this->attributeValues[$customAttributeId]->Value;
#         }

#         return null;
#     }
# }


from typing import List

class AttributeValue:
    def __init__(self, attribute_id: int, value: str):
        self.AttributeId = attribute_id
        self.Value = value

class ResourceType:
    def __init__(self, resource_id: int, name: str, description: str, attribute_list: List[AttributeValue] = None):
        self.id = resource_id
        self.name = name
        self.description = description
        self.attributeValues = {}
        if attribute_list:
            for attribute in attribute_list:
                self.with_attribute(attribute)

    @staticmethod
    def create_new(name: str, description: str):
        return ResourceType(0, name, description)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def set_name(self, name: str):
        self.name = name

    def set_description(self, description: str):
        self.description = description

    def with_attribute(self, attribute: AttributeValue):
        self.attributeValues[attribute.AttributeId] = attribute

    def change_attributes(self, attributes: List[AttributeValue]):
        added_attributes = []
        removed_attributes = []

        for attribute in attributes:
            if attribute.AttributeId not in self.attributeValues:
                added_attributes.append(attribute)

        for existing_attribute in self.attributeValues.values():
            if existing_attribute not in attributes:
                removed_attributes.append(existing_attribute)

        self.addedAttributeValues = added_attributes
        self.removedAttributeValues = removed_attributes

        for attribute in attributes:
            self.add_attribute_value(attribute)

    def change_attribute(self, attribute: AttributeValue):
        self.removedAttributeValues = [attribute]
        self.addedAttributeValues = [attribute]
        self.add_attribute_value(attribute)

    def add_attribute_value(self, attribute: AttributeValue):
        self.attributeValues[attribute.AttributeId] = attribute

    def get_added_attributes(self):
        return self.addedAttributeValues

    def get_removed_attributes(self):
        return self.removedAttributeValues

    def get_attribute_value(self, custom_attribute_id: int):
        if custom_attribute_id in self.attributeValues:
            return self.attributeValues[custom_attribute_id].Value

        return None

