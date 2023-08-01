# <?php

# class SmartyTextbox
# {
#     private $name;
#     private $type;
#     private $id;
#     private $attributes;
#     private $smartyVariable;
#     private $smarty;
#     private $required;

#     public function __construct($formKey, $type, $id, $smartyVariable, $attributes, $required, &$smarty)
#     {
#         $this->name = $this->GetName($formKey);
#         $this->type = empty($type) ? 'text' : $type;
#         $this->id = empty($id) ? $this->GetName($formKey) : $id;
#         $this->attributes = $attributes;
#         $this->smartyVariable = $smartyVariable;
#         $this->required = $required;
#         $this->smarty = $smarty;
#     }

#     public function Html()
#     {
#         $value = $this->GetValue();
#         $style = empty($this->style) ? '' : " style=\"{$this->style}\"";
#         $required = $this->required ? ' required="required" ' : '';

#         return "<input type=\"{$this->GetInputType()}\" name=\"{$this->name}\" id=\"{$this->id}\" value=\"$value\"{$required} $this->attributes />";
#     }

#     protected function GetInputType()
#     {
#         return $this->type;
#     }

#     private function GetName($formKey)
#     {
#         return FormKeys::Evaluate($formKey);
#     }

#     private function GetValue()
#     {
#         $value = $this->GetPostedValue();

#         if (empty($value)) {
#             $value = $this->GetTemplateValue();
#         }

#         if (!empty($value)) {
#             return trim($value);
#         }

#         return '';
#     }

#     private function GetPostedValue()
#     {
#         return ServiceLocator::GetServer()->GetForm($this->name);
#     }

#     private function GetTemplateValue()
#     {
#         $value = '';

#         if (!empty($this->smartyVariable)) {
#             $var = $this->smarty->getTemplateVars($this->smartyVariable);
#             if (!empty($var)) {
#                 $value = $var;
#             }
#         }

#         return $value;
#     }
# }

# class SmartyPasswordbox extends SmartyTextbox
# {
#     protected function GetInputType()
#     {
#         return 'password';
#     }
# }


from fastapi import FastAPI

app = FastAPI()

class SmartyTextbox:
    def __init__(self, form_key, input_type, _id, smarty_variable, attributes, required, smarty):
        self.name = self.get_name(form_key)
        self.type = input_type if input_type else 'text'
        self.id = _id if _id else self.get_name(form_key)
        self.attributes = attributes
        self.smarty_variable = smarty_variable
        self.required = required
        self.smarty = smarty

    def html(self):
        value = self.get_value()
        style = f' style="{self.style}"' if hasattr(self, 'style') else ''
        required = 'required="required"' if self.required else ''

        return f'<input type="{self.get_input_type()}" name="{self.name}" id="{self.id}" value="{value}" {required} {self.attributes} />'

    def get_input_type(self):
        return self.type

    def get_name(self, form_key):
        return FormKeys.evaluate(form_key)

    def get_value(self):
        value = self.get_posted_value()

        if not value:
            value = self.get_template_value()

        if value:
            return value.strip()

        return ''

    def get_posted_value(self):
        return ServiceLocator.get_server().get_form(self.name)

    def get_template_value(self):
        value = ''

        if self.smarty_variable:
            var = self.smarty.get_template_vars(self.smarty_variable)
            if var:
                value = var

        return value

class SmartyPasswordbox(SmartyTextbox):
    def get_input_type(self):
        return 'password'


