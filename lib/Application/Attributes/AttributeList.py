# <?php

# interface IEntityAttributeList
# {
#     /**
#      * @return array|string[]
#      */
#     public function GetLabels();

#     /**
#      * @param null $entityId
#      * @return array|CustomAttribute[]
#      */
#     public function GetDefinitions($entityId = null);

#     /**
#      * @param $entityId int|null
#      * @return array|Attribute[]
#      */
#     public function GetAttributes($entityId = null);
# }

# class AttributeList implements IEntityAttributeList
# {
#     /**
#      * @var array|string[]
#      */
#     private $labels = [];

#     /**
#      * @var array|string[]
#      */
#     private $values = [];

#     /**
#      * @var array|int
#      */
#     private $attribute_order = [];

#     /**
#      * @var CustomAttribute[]|array
#      */
#     private $definitions = [];

#     /**
#      * @var CustomAttribute[][]|array
#      */
#     private $entityDefinitions = [];

#     /**
#      * @var array|int[]
#      */
#     private $entityAttributes = [];

#     public function AddDefinition(CustomAttribute $attribute)
#     {
#         $this->labels[] = $attribute->Label();
#         $this->attribute_order[$attribute->Id()] = 1;
#         if ($attribute->UniquePerEntity()) {
#             $entityIds = $attribute->EntityIds();
#             foreach ($entityIds as $entityId) {
#                 $this->entityDefinitions[$entityId][$attribute->Id()] = $attribute;
#             }
#             $this->entityAttributes[$attribute->Id()] = 1;
#         //			Log::Debug('Adding custom attribute definition for entityId=%s, label=%s', $attribute->EntityId(), $attribute->Label());
#         } else {
#             $this->definitions[$attribute->Id()] = $attribute;
#             //			Log::Debug('Adding custom attribute definition label=%s', $attribute->Label());
#         }
#     }

#     /**
#      * @return array|string[]
#      */
#     public function GetLabels()
#     {
#         return $this->labels;
#     }

#     /**
#      * @param null $entityId
#      * @return array|CustomAttribute[]
#      */
#     public function GetDefinitions($entityId = null)
#     {
#         if (empty($entityId) || !array_key_exists($entityId, $this->entityDefinitions)) {
#             return $this->definitions;
#         }

#         return array_merge($this->definitions, $this->entityDefinitions[$entityId]);
#     }

#     /**
#      * @param $attributeEntityValue AttributeEntityValue
#      */
#     public function AddValue($attributeEntityValue)
#     {
#         $entityId = $attributeEntityValue->EntityId;
#         $attributeId = $attributeEntityValue->AttributeId;

#         if ($this->AttributeExistsAndIsNotEntity($attributeId, $entityId)) {
#             Log::Debug('Adding custom attribute value for entityId=%s, attributeId=%s', $entityId, $attributeId);
#             $this->values[$entityId][$attributeId] = new LBAttribute($this->definitions[$attributeId], $attributeEntityValue->Value);
#         } elseif ($this->EntityAttributeExists($attributeId, $entityId)) {
#             Log::Debug(
#                 'Adding entity specific custom attribute value for entityId=%s, attributeId=%s',
#                 $entityId,
#                 $attributeId
#             );
#             $this->values[$entityId][$attributeId] = new LBAttribute($this->entityDefinitions[$entityId][$attributeId], $attributeEntityValue->Value);
#         }
#     }

#     public function GetAttributes($entityId = null)
#     {
#         $attributes = [];
#         foreach ($this->attribute_order as $attributeId => $placeholder) {
#             $definition = null;
#             if ($this->AttributeExistsAndIsNotEntity($attributeId, $entityId)) {
#                 $definition = $this->definitions[$attributeId];
#             } elseif (!empty($entityId) && $this->EntityAttributeExists($attributeId, $entityId)) {
#                 $definition = $this->entityDefinitions[$entityId][$attributeId];
#             }

#             if ($definition != null) {
#                 if (empty($entityId) || !array_key_exists($entityId, $this->values) || !array_key_exists(
#                     $attributeId,
#                     $this->values[$entityId]
#                 )
#                 ) {
#                     $attributes[] = new LBAttribute($definition);
#                 } else {
#                     $attributes[] = $this->values[$entityId][$definition->Id()];
#                 }
#             }
#         }

#         Log::Debug('Found %s attributes for entityId %s', count($attributes), $entityId);

#         return $attributes;
#     }

#     /**
#      * @param $attributeId int
#      * @param $entityId int
#      * @return bool
#      */
#     private function AttributeExistsAndIsNotEntity($attributeId, $entityId)
#     {
#         return array_key_exists($attributeId, $this->definitions) && !$this->IsEntityAttribute($attributeId, $entityId);
#     }

#     /**
#      * @param $attributeId int
#      * @param $entityId int
#      * @return bool
#      */
#     private function EntityAttributeExists($attributeId, $entityId)
#     {
#         return $this->IsEntityAttribute($attributeId, $entityId) &&
#         array_key_exists($entityId, $this->entityDefinitions) && array_key_exists($attributeId, $this->entityDefinitions[$entityId]);
#     }

#     /**
#      * @param $attributeId int
#      * @param $entityId int
#      * @return bool
#      */
#     private function IsEntityAttribute($attributeId, $entityId)
#     {
#         return array_key_exists($attributeId, $this->entityAttributes) && ($entityId != null && array_key_exists($entityId, $this->entityDefinitions));
#     }
# }

from typing import List, Union

class CustomAttribute:
    # Define the CustomAttribute class as needed
    # You can include the required methods and properties
    pass

class LBAttribute:
    # Define the LBAttribute class as needed
    # You can include the required methods and properties
    pass

class AttributeEntityValue:
    # Define the AttributeEntityValue class as needed
    # You can include the required methods and properties
    pass

class Log:
    # Implement Log class as needed
    # This is a placeholder here as the provided PHP Log class is not included
    pass
class IEntityAttributeList:
    def get_labels(self) -> List[str]:
        pass

    def get_definitions(self, entity_id: Union[None, int] = None) -> List[CustomAttribute]:
        pass

    def get_attributes(self, entity_id: Union[None, int] = None) -> List[LBAttribute]:
        pass

class AttributeList(IEntityAttributeList):
    def __init__(self):
        self.labels = []
        self.values = {}
        self.attribute_order = {}
        self.definitions = {}
        self.entity_definitions = {}
        self.entity_attributes = {}

    def add_definition(self, attribute: CustomAttribute):
        self.labels.append(attribute.Label())
        self.attribute_order[attribute.Id()] = 1
        if attribute.UniquePerEntity():
            entity_ids = attribute.EntityIds()
            for entity_id in entity_ids:
                self.entity_definitions.setdefault(entity_id, {})[attribute.Id()] = attribute
            self.entity_attributes[attribute.Id()] = 1
            # Log::Debug('Adding custom attribute definition for entityId=%s, label=%s', attribute->EntityId(), attribute->Label())
        else:
            self.definitions[attribute.Id()] = attribute
            # Log::Debug('Adding custom attribute definition label=%s', attribute->Label())

    def get_labels(self) -> List[str]:
        return self.labels

    def get_definitions(self, entity_id: Union[None, int] = None) -> List[CustomAttribute]:
        if entity_id is None or entity_id not in self.entity_definitions:
            return list(self.definitions.values())
        return list(self.definitions.values()) + list(self.entity_definitions[entity_id].values())

    def add_value(self, attribute_entity_value: AttributeEntityValue):
        entity_id = attribute_entity_value.EntityId
        attribute_id = attribute_entity_value.AttributeId

        if self._attribute_exists_and_is_not_entity(attribute_id, entity_id):
            Log.Debug('Adding custom attribute value for entityId=%s, attributeId=%s', entity_id, attribute_id)
            self.values.setdefault(entity_id, {})[attribute_id] = LBAttribute(self.definitions[attribute_id], attribute_entity_value.Value)
        elif self._entity_attribute_exists(attribute_id, entity_id):
            Log.Debug(
                'Adding entity specific custom attribute value for entityId=%s, attributeId=%s',
                entity_id,
                attribute_id
            )
            self.values.setdefault(entity_id, {})[attribute_id] = LBAttribute(self.entity_definitions[entity_id][attribute_id], attribute_entity_value.Value)

    def get_attributes(self, entity_id: Union[None, int] = None) -> List[LBAttribute]:
        attributes = []
        for attribute_id, _ in self.attribute_order.items():
            definition = None
            if self._attribute_exists_and_is_not_entity(attribute_id, entity_id):
                definition = self.definitions[attribute_id]
            elif entity_id is not None and self._entity_attribute_exists(attribute_id, entity_id):
                definition = self.entity_definitions[entity_id][attribute_id]

            if definition is not None:
                if entity_id is None or (entity_id in self.values and attribute_id not in self.values[entity_id]):
                    attributes.append(LBAttribute(definition))
                else:
                    attributes.append(self.values[entity_id][definition.Id()])

        Log.Debug('Found %s attributes for entityId %s', len(attributes), entity_id)
        return attributes

    def _attribute_exists_and_is_not_entity(self, attribute_id, entity_id):
        return attribute_id in self.definitions and not self._is_entity_attribute(attribute_id, entity_id)

    def _entity_attribute_exists(self, attribute_id, entity_id):
        return self._is_entity_attribute(attribute_id, entity_id) and entity_id in self.entity_definitions and attribute_id in self.entity_definitions[entity_id]

    def _is_entity_attribute(self, attribute_id, entity_id):
        return attribute_id in self.entity_attributes and (entity_id is not None and entity_id in self.entity_definitions)
