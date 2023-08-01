# <?php

# class AvailableLanguage
# {
#     /**
#      * @var string
#      */
#     public $LanguageCode;

#     /**
#      * @var string
#      */
#     public $LanguageFile;

#     /**
#      * @var string
#      */
#     public $DisplayName;

#     /**
#      * @var string
#      */
#     public $LanguageClass;

#     /**
#      * @return string
#      */
#     public function GetDisplayName()
#     {
#         return $this->DisplayName;
#     }

#     /**
#      * @return string
#      */
#     public function GetLanguageCode()
#     {
#         return $this->LanguageCode;
#     }

#     /**
#      * @param string $languageCode
#      * @param string $languageFile
#      * @param string $displayName
#      */
#     public function __construct($languageCode, $languageFile, $displayName)
#     {
#         $this->LanguageCode = $languageCode;
#         $this->LanguageFile = $languageFile;
#         $this->DisplayName = $displayName;
#         $this->LanguageClass = str_replace('.php', '', $languageFile);
#     }
# }

from pydantic import BaseModel

class AvailableLanguage(BaseModel):
    LanguageCode: str
    LanguageFile: str
    DisplayName: str
    LanguageClass: str

    def get_display_name(self):
        return self.DisplayName

    def get_language_code(self):
        return self.LanguageCode

    def __init__(self, language_code: str, language_file: str, display_name: str):
        super().__init__(LanguageCode=language_code, LanguageFile=language_file, DisplayName=display_name)
        self.LanguageClass = language_file.replace('.php', '')

# Usage example:
language = AvailableLanguage(language_code="en", language_file="english.php", display_name="English")
print(language.dict())



