# <?php

# require_once(ROOT_DIR . 'lib/Server/UserSession.php');

# class Server
# {
#     public function __construct()
#     {
#     }

#     public function SetCookie(Cookie $cookie)
#     {
#         setcookie($cookie->Name, $cookie->Value, $cookie->Expiration, $cookie->Path);
#     }

#     public function DeleteCookie(Cookie $cookie)
#     {
#         setcookie($cookie->Name, '', -1, $cookie->Path);
#     }

#     public function GetCookie($name)
#     {
#         if (isset($_COOKIE[$name])) {
#             return $_COOKIE[$name];
#         }
#         return null;
#     }

#     public const sessionId = 'booked';

#     public function SetSession($name, $value)
#     {
#         if (!$this->IsSessionStarted()) {
#             $parts = parse_url(Configuration::Instance()->GetScriptUrl());
#             $path = isset($parts['path']) ? $parts['path'] : '';
#             $seconds = Configuration::Instance()->GetKey(ConfigKeys::INACTIVITY_TIMEOUT) * 60;
#             ini_set('session.gc_maxlifetime', $seconds);
#             session_set_cookie_params(0, $path);
#             @session_unset();
#             @session_destroy();
#             @session_start();
#         }

#         $_SESSION[self::sessionId][$name] = $value;
#     }

#     public function GetSession($name)
#     {
#         if (!$this->IsSessionStarted()) {
#             $parts = parse_url(Configuration::Instance()->GetScriptUrl());
#             $path = isset($parts['path']) ? $parts['path'] : '';
#             $seconds = Configuration::Instance()->GetKey(ConfigKeys::INACTIVITY_TIMEOUT, new IntConverter()) * 60;
#             ini_set('session.gc_maxlifetime', $seconds);
#             session_set_cookie_params(0, $path);
#             @session_unset();
#             @session_destroy();
#             @session_start();
#         }
#         if (isset($_SESSION[self::sessionId][$name])) {
#             return $_SESSION[self::sessionId][$name];
#         }
#         return null;
#     }

#     public function EndSession($name)
#     {
#         $this->SetSession($name, null);
#         @session_unset();
#         @session_destroy();
#     }

#     /**
#      * @return bool
#      */
#     private function IsSessionStarted()
#     {
#         if (php_sapi_name() !== 'cli') {
#             if (version_compare(phpversion(), '5.4.0', '>=')) {
#                 return session_status() === PHP_SESSION_ACTIVE ? true : false;
#             } else {
#                 return session_id() === '' ? false : true;
#             }
#         }
#         return false;
#     }

#     /**
#      * @param string $name
#      * @return string|null
#      */
#     public function GetQuerystring($name)
#     {
#         if (isset($_GET[$name])) {
#             $value = $_GET[$name];

#             if ($value != '' && $value != null && !is_array($value)) {
#                 return htmlspecialchars(trim($value));
#             } else {
#                 if (is_array($value)) {
#                     array_walk($value, [$this, 'specialchars']);
#                     return $value;
#                 }
#             }

#             return '';
#         }
#         return null;
#     }

#     private static function specialchars(&$val)
#     {
#         $val = htmlspecialchars(trim($val));
#     }

#     /**
#      * @param string $name
#      * @return string|null
#      */
#     public function GetForm($name)
#     {
#         $value = $this->GetRawForm($name);
#         if (!empty($value) && !is_array($value)) {
#             return htmlspecialchars(trim($value));
#         }

#         if (is_array($value)) {
#             array_walk($value, [$this, 'specialchars']);
#             return $value;
#         }

#         return $value;
#     }

#     /**
#      * @param string $name
#      * @return string|null
#      */
#     public function GetRawForm($name)
#     {
#         if (isset($_POST[$name])) {
#             if (is_array($_POST[$name])) {
#                 return $_POST[$name];
#             }

#             return trim($_POST[$name]);
#         }
#         return null;
#     }

#     /**
#      * @param string $name
#      * @return null|UploadedFile
#      */
#     public function GetFile($name)
#     {
#         if (isset($_FILES[$name])) {
#             return new UploadedFile($_FILES[$name]);
#         }
#         return null;
#     }

#     /**
#      * @param string $name
#      * @return array|UploadedFile[]
#      */
#     public function GetFiles($name)
#     {
#         $uploadedFiles = [];

#         if (isset($_FILES[$name])) {
#             $files = $_FILES[$name];
#             if (is_array($files['name'])) {
#                 // convert the files from the weird PHP multi-file array to a normal array of objects
#                 // taken from PHP.net
#                 $file_ary = [];
#                 $file_count = count($files['name']);
#                 $file_keys = array_keys($files);

#                 for ($i = 0; $i < $file_count; $i++) {
#                     foreach ($file_keys as $key) {
#                         $file_ary[$i][$key] = $files[$key][$i];
#                     }

#                     $uploadedFiles[] = new UploadedFile($file_ary[$i]);
#                 }
#             } else {
#                 $uploadedFiles[] = new UploadedFile($_FILES[$name]);
#             }
#         }
#         return $uploadedFiles;
#     }

#     public function GetUrl()
#     {
#         $url = $_SERVER['SCRIPT_NAME'];

#         if (isset($_SERVER['QUERY_STRING'])) {
#             $qs = http_build_query($_GET);
#             $url .= '?' . $qs;
#         }

#         return $url;
#     }

#     /**
#      * @return UserSession
#      */
#     public function GetUserSession()
#     {
#         $userSession = $this->GetSession(SessionKeys::USER_SESSION);

#         if (!empty($userSession)) {
#             return $userSession;
#         }

#         return new NullUserSession();
#     }

#     /**
#      * @param $userSession UserSession
#      * @return void
#      */
#     public function SetUserSession($userSession)
#     {
#         $this->SetSession(SessionKeys::USER_SESSION, $userSession);
#     }

#     /**
#      * @return string
#      */
#     public function GetRequestMethod()
#     {
#         return $this->GetHeader('REQUEST_METHOD');
#     }

#     /**
#      * @return string
#      */
#     public function GetLanguage()
#     {
#         $lang = $this->GetHeader('HTTP_ACCEPT_LANGUAGE');
#         if (strlen($lang) > 4) {
#             return substr(str_replace('-', '_', $lang), 0, 5);
#         }
#         return null;
#     }

#     /**
#      * @param string $headerCode
#      * @return string
#      */
#     public function GetHeader($headerCode)
#     {
#         return $_SERVER[$headerCode];
#     }

#     /**
#      * @return string
#      */
#     public function GetRemoteAddress()
#     {
#         return $this->GetHeader('REMOTE_ADDR');
#     }

#     /**
#      * @return bool
#      */
#     public function GetIsHttps()
#     {
#         $isHttps = $this->GetHeader('HTTPS');
#         return $isHttps == 'on';
#     }

#     /**
#      * @return string
#      */
#     public function GetRequestUri()
#     {
#         return $this->GetUrl();
#         //return $this->GetHeader('REQUEST_URI');
#     }
# }


from fastapi import Request
from starlette.datastructures import UploadFile

class Server:

    def __init__(self, request: Request):
        self.request = request

    def get_query_param(self, name):
        return self.request.query_params.get(name)

    def get_form_field(self, name):
        return self.request.form.get(name)

    def get_file(self, name):
        f = self.request.files.get(name)
        if f:
            return UploadFile(f)
        return None

    def get_files(self, name):
        files = self.request.files.getlist(name)
        return [UploadFile(f) for f in files]

    def get_url(self):
        return str(self.request.url)
    
    def get_method(self):
        return self.request.method

    def get_header(self, name):
        return self.request.headers.get(name)

    def get_remote_addr(self):
        return self.request.client.host

    def get_is_https(self):
        return self.request.url.scheme == 'https'

    def get_path(self):
        return self.request.url.path

    def set_cookie(self, cookie):
        # TODO: implement setting cookies
        pass
    def get_cookie(self, name):
        return self.request.cookies.get(name)

    def set_session(self, name, value):
        # TODO: implement sessions
        pass
    def get_session(self, name):
        # TODO: implement sessions
        pass
    def end_session(self, name):
        # TODO: implement ending sessions
        pass