# <?php

# class RequiredEmailDomainValidator extends ValidatorBase implements IValidator
# {
#     private $value;

#     public function __construct($value)
#     {
#         $this->value = $value;
#     }

#     public function Validate()
#     {
#         $this->isValid = true;

#         $domains = Configuration::Instance()->GetSectionKey(ConfigSection::AUTHENTICATION, ConfigKeys::AUTHENTICATION_REQUIRED_EMAIL_DOMAINS);

#         if (empty($domains)) {
#             return;
#         }

#         $allDomains = preg_split('/[\,\s;]/', $domains);

#         $trimmed = trim($this->value);

#         foreach ($allDomains as $d) {
#             $d = str_replace('@', '', trim($d));
#             if (BookedStringHelper::EndsWith($trimmed, '@' . $d)) {
#                 return;
#             }
#         }

#         $this->isValid = false;
#     }
# }

from fastapi import HTTPException

class RequiredEmailDomainValidator:

    def __init__(self, email: str):
        self.email = email

    def validate(self) -> None:
       required_domains = ["example.com", "company.com"] # configurable

       email_domain = self.email.split('@')[-1]
       if email_domain not in required_domains:
           raise HTTPException(status_code=400, detail="Email must be in required domains")

