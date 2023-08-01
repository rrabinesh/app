# <!-- <?php

# require_once(ROOT_DIR . 'lib/Common/Date.php');
# require_once(ROOT_DIR . 'lib/Common/Helpers/String.php');

# class Cookie
# {
#     public $Name;
#     public $Value;
#     public $Expiration;
#     public $Path;

#     public function __construct($name, $value, $expiration = null, $path = null)
#     {
#         if (is_null($expiration)) {
#             $expiration = Date::Now()->AddDays(30)->TimeStamp();
#         }

#         if (is_null($path)) {
#             $path = Configuration::Instance()->GetScriptUrl();
#         }

#         if (BookedStringHelper::StartsWith($path, 'http')) {
#             $parts = parse_url($path);
#             $path = isset($parts['path']) ? $parts['path'] : '';
#         }

#         $this->Name = $name;
#         $this->Value = $value;
#         $this->Expiration = $expiration;    // date(DATE_COOKIE, $expiration);
#         $this->Path = $path;
#     }

#     public function Delete()
#     {
#         $this->Expiration = date(DATE_COOKIE, Date::Now()->AddDays(-30)->Timestamp());
#     }

#     public function __toString()
#     {
#         return sprintf('%s %s %s %s', $this->Name, $this->Value, $this->Expiration, $this->Path);
#     }
# } -->

from fastapi import FastAPI
from datetime import datetime, timedelta
from urllib.parse import urlparse

app = FastAPI()

class Cookie:
    def __init__(self, name, value, expiration=None, path=None):
        if expiration is None:
            expiration = datetime.now() + timedelta(days=30)

        if path is None:
            # Replace 'Configuration::Instance()->GetScriptUrl()' with the actual script URL if needed
            path = "/"

        if path.startswith("http"):
            parsed_url = urlparse(path)
            path = parsed_url.path

        self.Name = name
        self.Value = value
        self.Expiration = expiration.strftime("%a, %d %b %Y %H:%M:%S GMT")
        self.Path = path

    def delete(self):
        self.Expiration = (datetime.now() - timedelta(days=30)).strftime("%a, %d %b %Y %H:%M:%S GMT")

    def __str__(self):
        return f"{self.Name}={self.Value}; Expires={self.Expiration}; Path={self.Path}"

# Sample route to demonstrate setting and deleting cookies
@app.get("/")
def set_and_delete_cookie():
    cookie_name = "my_cookie"
    cookie_value = "Hello, FastAPI!"

    # Create a new cookie and set it in the response
    cookie = Cookie(cookie_name, cookie_value)
    response = {"message": "Cookie set successfully!"}
    response.set_cookie(cookie.Name, cookie.Value, expires=cookie.Expiration, path=cookie.Path)

    # Delete the cookie by setting its expiration to the past and removing it from the response
    cookie.delete()
    response.delete_cookie(cookie.Name)

    return response



