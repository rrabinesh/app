# <?php

# class AttributeFormElement
# {
#     /**
#      * @var int
#      */
#     public $Id;

#     /**
#      * @var mixed
#      */
#     public $Value;

#     public function __construct($id, $value)
#     {
#         $this->Id = $id;
#         $this->Value = $value;
#     }
# }

# class AttributeFormParser
# {
#     /**
#      * @static
#      * @param $attributes string|string[]|null The result of $this->GetForm(FormKeys::ATTRIBUTE_PREFIX)
#      * @return array|AttributeFormElement[]
#      */
#     public static function GetAttributes($attributes)
#     {
#         if (is_array($attributes)) {
#             $af = [];

#             foreach ($attributes as $id => $value) {
#                 $af[] = new AttributeFormElement($id, $value);
#             }

#             return $af;
#         }

#         return [];
#     }
# }



from typing import List, Union

class AttributeFormElement:
    def __init__(self, _id: int, value: Union[str, int]):
        self.Id = _id
        self.Value = value

class AttributeFormParser:
    @staticmethod
    def get_attributes(attributes: Union[str, List[str], None]) -> List[AttributeFormElement]:
        if isinstance(attributes, list):
            af = []

            for index, value in enumerate(attributes):
                af.append(AttributeFormElement(index, value))

            return af

        return []