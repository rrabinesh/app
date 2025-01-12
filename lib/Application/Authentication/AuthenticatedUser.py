# <!-- <?php

# class AuthenticatedUser
# {
#     /**
#      * @var string
#      */
#     private $username;

#     /**
#      * @var string
#      */
#     private $email;

#     /**
#      * @var string
#      */
#     private $fname;

#     /**
#      * @var string
#      */
#     private $lname;

#     /**
#      * @var string
#      */
#     private $password;

#     /**
#      * @var string
#      */
#     private $languageCode;

#     /**
#      * @var string
#      */
#     private $timezoneName;

#     /**
#      * @var string
#      */
#     private $phone;

#     /**
#      * @var string
#      */
#     private $organization;

#     /**
#      * @var string
#      */
#     private $title;

#     /**
#      * @var string[]|null
#      */
#     private $groups = null;

#     /**
#      * @param string $username
#      * @param string $email
#      * @param string $fname
#      * @param string $lname
#      * @param string $password
#      * @param string $languageCode
#      * @param string $timezoneName
#      * @param string $phone
#      * @param string $organization
#      * @param string $title
#      * @param string[]|null $groups
#      */
#     public function __construct($username, $email, $fname, $lname, $password, $languageCode, $timezoneName, $phone, $organization, $title, $groups = null)
#     {
#         $this->username = $username;
#         $this->email = $email;
#         $this->fname = $fname;
#         $this->lname = $lname;
#         $this->password = $password;
#         $this->languageCode = empty($languageCode) ? Configuration::Instance()->GetKey(ConfigKeys::LANGUAGE) : $languageCode;
#         $this->timezoneName = $timezoneName;
#         $this->phone = $phone;
#         $this->organization = $organization;
#         $this->title = $title;
#         $this->groups = is_null($groups) ? [] : $groups;
#         ;
#     }

#     /**
#      * @return string
#      */
#     public function Email()
#     {
#         return $this->EnsureNull($this->email);
#     }

#     /**
#      * @return string
#      */
#     public function FirstName()
#     {
#         return $this->EnsureNull($this->fname);
#     }

#     /**
#      * @return string
#      */
#     public function LanguageCode()
#     {
#         return $this->EnsureNull($this->languageCode);
#     }

#     /**
#      * @return string
#      */
#     public function LastName()
#     {
#         return $this->EnsureNull($this->lname);
#     }

#     /**
#      * @return string
#      */
#     public function Organization()
#     {
#         return $this->EnsureNull($this->organization);
#     }

#     /**
#      * @return string
#      */
#     public function Password()
#     {
#         return $this->password;
#     }

#     /**
#      * @return string
#      */
#     public function Phone()
#     {
#         return $this->EnsureNull($this->phone);
#     }

#     /**
#      * @return string
#      */
#     public function TimezoneName()
#     {
#         return $this->timezoneName;
#     }

#     /**
#      * @return string
#      */
#     public function Title()
#     {
#         return $this->EnsureNull($this->title);
#     }

#     /**
#      * @return string
#      */
#     public function Username()
#     {
#         return $this->username;
#     }

#     private function EnsureNull($value)
#     {
#         $value = trim($value);
#         if (empty($value)) {
#             return null;
#         }

#         return trim($value);
#     }

#     /**
#      * @return string[]|null
#      */
#     public function GetGroups()
#     {
#         return $this->groups;
#     }
# } -->

from pydantic import BaseModel
from typing import Optional, List

class AuthenticatedUser(BaseModel):
    username: str
    email: Optional[str]
    fname: Optional[str]
    lname: Optional[str]
    password: str
    languageCode: Optional[str]
    timezoneName: str
    phone: Optional[str]
    organization: Optional[str]
    title: Optional[str]
    groups: List[str] = []

    def ensure_null(self, value):
        value = value.strip()
        if not value:
            return None

        return value.strip()

    def Email(self):
        return self.ensure_null(self.email)

    def FirstName(self):
        return self.ensure_null(self.fname)

    def LanguageCode(self):
        return self.ensure_null(self.languageCode)

    def LastName(self):
        return self.ensure_null(self.lname)

    def Organization(self):
        return self.ensure_null(self.organization)

    def Phone(self):
        return self.ensure_null(self.phone)

    def TimezoneName(self):
        return self.timezoneName

    def Title(self):
        return self.ensure_null(self.title)

    def Username(self):
        return self.username

    class Config:
        allow_mutation = False



