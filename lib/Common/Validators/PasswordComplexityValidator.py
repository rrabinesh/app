# <?php

# class PasswordComplexityValidator extends ValidatorBase implements IValidator
# {
#     private $password;

#     public function __construct($passwordPlainText)
#     {
#         $this->password = $passwordPlainText;
#     }

#     public function Validate()
#     {
#         $caseRequirements = Configuration::Instance()->GetSectionKey(ConfigSection::PASSWORD, ConfigKeys::PASSWORD_UPPER_AND_LOWER, new BooleanConverter());
#         $letters = Configuration::Instance()->GetSectionKey(ConfigSection::PASSWORD, ConfigKeys::PASSWORD_LETTERS, new IntConverter());
#         $numbers = Configuration::Instance()->GetSectionKey(ConfigSection::PASSWORD, ConfigKeys::PASSWORD_NUMBERS, new IntConverter());

#         $passwordNumbers = preg_match_all("/[^a-zA-Z]/", $this->password, $m1);
#         $passwordUpper = preg_match_all("/[A-Z]/", $this->password, $m2);
#         $passwordLower = preg_match_all("/[a-z]/", $this->password, $m3);
#         $passwordLetters = strlen($this->password);

#         if (empty($letters)) {
#             $letters = 6;
#         }

#         $this->isValid = $passwordNumbers >= $numbers && $passwordLetters >= $letters;

#         if ($caseRequirements) {
#             $this->isValid = $this->isValid && $passwordUpper > 0 && $passwordLower > 0;
#         }

#         if (!$this->IsValid()) {
#             if (!$caseRequirements) {
#                 $this->AddMessage(Resources::GetInstance()->GetString('PasswordError', [$letters, $numbers]));
#             } else {
#                 $this->AddMessage(Resources::GetInstance()->GetString('PasswordErrorRequirements', [$letters, $numbers]));
#             }
#         }
#     }
# }


from fastapi import HTTPException
import re

class PasswordComplexityValidator:

    def __init__(self, password: str):
        self.password = password

    def validate(self) -> None:
        min_letters = 6 # configurable
        min_numbers = 1 # configurable
        require_upper_lower = True # configurable

        has_digits = len(re.findall(r"\d", self.password)) >= min_numbers
        has_letters = len(self.password) >= min_letters
        has_upper = re.search(r"[A-Z]", self.password)
        has_lower = re.search(r"[a-z]", self.password)

        is_valid = has_digits and has_letters
        if require_upper_lower:
            is_valid = is_valid and has_upper and has_lower

        if not is_valid:
            raise HTTPException(status_code=400, detail="Password does not meet complexity requirements")
