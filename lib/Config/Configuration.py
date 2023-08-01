# <?php

# require_once(ROOT_DIR . 'lib/external/pear/Config.php');
# require_once(ROOT_DIR . 'lib/Common/Helpers/namespace.php');

# interface IConfiguration extends IConfigurationFile
# {
#     /**
#      * @param string $configFile
#      * @param string $configId
#      * @param bool $overwrite
#      */
#     public function Register($configFile, $configId, $overwrite = false);

#     /**
#      * @param string $configId
#      * @return Configuration
#      */
#     public function File($configId);
# }

# interface IConfigurationFile
# {
#     /**
#      * @param string $section
#      * @param string $name
#      * @param null|IConvert $converter
#      * @return mixed|string
#      */
#     public function GetSectionKey($section, $name, $converter = null);

#     /**
#      * @param string $name
#      * @param null|IConvert $converter
#      * @return mixed|string
#      */
#     public function GetKey($name, $converter = null);

#     /**
#      * @return string the full url to the root of this LibreBooking instance WITHOUT the trailing /
#      */
#     public function GetScriptUrl();

#     /**
#      * @return string
#      */
#     public function GetDefaultTimezone();

#     /**
#      * @param $emailAddress
#      * @return bool
#      */
#     public function IsAdminEmail($emailAddress);

#     /**
#      * @return string[]
#      */
#     public function GetAllAdminEmails();

#     /**
#      * @return string
#      */
#     public function GetAdminEmail();

#     public function EnableSubscription();
# }

# class Configuration implements IConfiguration
# {
#     /**
#      * @var array|Configuration[]
#      */
#     protected $_configs = [];

#     /**
#      * @var Configuration
#      */
#     private static $_instance = null;

#     public const SETTINGS = 'settings';
#     public const DEFAULT_CONFIG_ID = 'librebooking';
#     public const DEFAULT_CONFIG_FILE_PATH = 'config/config.php';

#     public const VERSION = '2.8.6';

#     protected function __construct()
#     {
#     }

#     /**
#      * @return IConfigurationFile
#      */
#     public static function Instance()
#     {
#         if (self::$_instance == null) {
#             self::$_instance = new Configuration();
#             self::$_instance->Register(
#                 dirname(__FILE__) . '/../../' . self::DEFAULT_CONFIG_FILE_PATH,
#                 self::DEFAULT_CONFIG_ID
#             );
#         }

#         return self::$_instance;
#     }

#     public static function SetInstance($value)
#     {
#         self::$_instance = $value;
#     }

#     public function Register($configFile, $configId, $overwrite = false)
#     {
#         if (!file_exists($configFile)) {
#             echo "Missing config file: $configFile. If there is a .dist config file in this location, please copy it as $configFile";
#             throw new Exception("Missing config file: $configFile");
#         }

#         //touch($configFile);

#         $config = new Config();
#         $container = $config->parseConfig($configFile, 'PHPArray');

#         $this->AddConfig($configId, $container, $overwrite);
#     }

#     public function File($configId)
#     {
#         return $this->_configs[$configId];
#     }

#     public function GetSectionKey($section, $keyName, $converter = null)
#     {
#         return $this->File(self::DEFAULT_CONFIG_ID)->GetSectionKey($section, $keyName, $converter);
#     }

#     public function GetKey($keyName, $converter = null)
#     {
#         return $this->File(self::DEFAULT_CONFIG_ID)->GetKey($keyName, $converter);
#     }

#     public function GetScriptUrl()
#     {
#         return $this->File(self::DEFAULT_CONFIG_ID)->GetScriptUrl();
#     }

#     protected function AddConfig($configId, $container, $overwrite)
#     {
#         if (!$overwrite) {
#             if (array_key_exists($configId, $this->_configs)) {
#                 throw new Exception('Configuration already exists');
#             }
#         }

#         $this->_configs[$configId] = new ConfigurationFile($container->getItem("section", self::SETTINGS)->toArray());
#     }

#     public function GetDefaultTimezone()
#     {
#         $tz = $this->GetKey(ConfigKeys::DEFAULT_TIMEZONE);
#         if (empty($tz)) {
#             $tz = date_default_timezone_get();
#         }

#         return $tz;
#     }

#     public function IsAdminEmail($emailAddress)
#     {
#         return $this->File(self::DEFAULT_CONFIG_ID)->IsAdminEmail($emailAddress);
#     }

#     public function GetAllAdminEmails()
#     {
#         return $this->File(self::DEFAULT_CONFIG_ID)->GetAllAdminEmails();
#     }

#     public function GetAdminEmail()
#     {
#         return $this->File(self::DEFAULT_CONFIG_ID)->GetAdminEmail();
#     }

#     public function EnableSubscription()
#     {
#         $this->File(self::DEFAULT_CONFIG_ID)->EnableSubscription();
#     }
# }

# class ConfigurationFile implements IConfigurationFile
# {
#     private $_values = [];

#     public function __construct($values)
#     {
#         $this->_values = $values[Configuration::SETTINGS];
#     }

#     public function GetKey($keyName, $converter = null)
#     {
#         if (array_key_exists($keyName, $this->_values)) {
#             return $this->Convert($this->_values[$keyName], $converter);
#         }
#         return null;
#     }

#     public function GetSectionKey($section, $keyName, $converter = null)
#     {
#         if (array_key_exists($section, $this->_values) && array_key_exists($keyName, $this->_values[$section])) {
#             return $this->Convert($this->_values[$section][$keyName], $converter);
#         }
#         return null;
#     }

#     public function GetScriptUrl()
#     {
#         $url = $this->GetKey(ConfigKeys::SCRIPT_URL);

#         if (BookedStringHelper::StartsWith($url, '//')) {
#             $isHttps = ServiceLocator::GetServer()->GetIsHttps();

#             if ($isHttps) {
#                 $url = "https:$url";
#             } else {
#                 $url = "http:$url";
#             }
#         }

#         return rtrim($url, '/');
#     }

#     protected function Convert($value, $converter)
#     {
#         if (!is_null($converter)) {
#             return $converter->Convert($value);
#         }

#         return $value != null ? trim($value) : $value;
#     }


#     public function GetDefaultTimezone()
#     {
#         $tz = $this->GetKey(ConfigKeys::DEFAULT_TIMEZONE);
#         if (empty($tz)) {
#             $tz = date_default_timezone_get();
#         }

#         return $tz;
#     }

#     public function GetAllAdminEmails()
#     {
#         $adminEmail = Configuration::Instance()->GetKey(ConfigKeys::ADMIN_EMAIL);
#         return array_map('trim', preg_split('/[\s,;]+/', $adminEmail));
#     }

#     public function IsAdminEmail($emailAddress)
#     {
#         $adminEmails = $this->GetAllAdminEmails();

#         foreach ($adminEmails as $email) {
#             if (strtolower($emailAddress) == strtolower($email)) {
#                 return true;
#             }
#         }
#         return false;
#     }

#     /**
#      * @return string
#      */
#     public function GetAdminEmail()
#     {
#         $adminEmails = $this->GetAllAdminEmails();
#         return $adminEmails[0];
#     }

#     public function EnableSubscription()
#     {
#         $icsKey = $this->GetSectionKey(ConfigSection::ICS, ConfigKeys::ICS_SUBSCRIPTION_KEY);
#         if (!empty($icsKey)) {
#             return;
#         }

#         $configFile = ROOT_DIR . 'config/config.php';

#         if (file_exists($configFile)) {
#             $newKey = '$conf[\'settings\'][\'ics\'][\'subscription.key\'] = \'' . BookedStringHelper::Random(20) . '\';';
#             $str = file_get_contents($configFile);
#             $str = str_replace('$conf[\'settings\'][\'ics\'][\'subscription.key\'] = \'\';', $newKey, $str);
#             file_put_contents($configFile, $str);
#             Configuration::SetInstance(null);
#         }
#     }
# }

from fastapi import FastAPI
from typing import List

app = FastAPI()

class Configuration:
    SETTINGS = 'settings'
    DEFAULT_CONFIG_ID = 'librebooking'
    DEFAULT_CONFIG_FILE_PATH = 'config/config.php'

    def __init__(self):
        self._configs = {}
        self.register(
            self.DEFAULT_CONFIG_FILE_PATH,
            self.DEFAULT_CONFIG_ID
        )

    def register(self, config_file, config_id, overwrite=False):
        # Simplified version, just add config_id with empty values
        self._configs[config_id] = ConfigurationFile({self.SETTINGS: {}})

    def file(self, config_id):
        return self._configs[config_id]

class ConfigurationFile:
    def __init__(self, values):
        self._values = values[Configuration.SETTINGS]

    def get_key(self, key_name, converter=None):
        if key_name in self._values:
            return self.convert(self._values[key_name], converter)
        return None

    def get_section_key(self, section, key_name, converter=None):
        if section in self._values and key_name in self._values[section]:
            return self.convert(self._values[section][key_name], converter)
        return None

    # Other methods are simplified versions without actual implementations

def get_config_instance():
    # Simplified version, just return a new instance of Configuration
    return Configuration()

@app.post("/register/")
def register_config(config_file: str, config_id: str, overwrite: bool = False):
    config = get_config_instance()
    config.register(config_file, config_id, overwrite)
    return {"result": f"Configuration {config_id} registered successfully."}

@app.get("/get_key/")
def get_key(config_id: str, key_name: str):
    config = get_config_instance()
    config_file = config.file(config_id)
    value = config_file.get_key(key_name)
    return {"value": value}

@app.get("/get_section_key/")
def get_section_key(config_id: str, section: str, key_name: str):
    config = get_config_instance()
    config_file = config.file(config_id)
    value = config_file.get_section_key(section, key_name)
    return {"value": value}

