# <?php

# require_once(ROOT_DIR . 'lang/AvailableLanguages.php');

# interface IResourceLocalization
# {
#     /**
#      * @abstract
#      * @param $key
#      * @param array|string $args
#      * @return void
#      */
#     public function GetString($key, $args = []);

#     public function GetDateFormat($key);

#     public function GetDays($key);

#     public function GetMonths($key);

#     public function GeneralDateFormat();

#     public function GeneralDateTimeFormat();
# }

# class ResourceKeys
# {
#     public const DATE_GENERAL = 'general_date';
#     public const DATETIME_GENERAL = 'general_datetime';
#     public const DATETIME_SHORT = 'short_datetime';
#     public const DATETIME_SYSTEM = 'system_datetime';
# }

# class Resources implements IResourceLocalization
# {
#     /**
#      * @var string
#      */
#     public $CurrentLanguage;
#     public $LanguageFile;
#     public $CalendarLanguageFile;

#     /**
#      * @var array|AvailableLanguage[]
#      */
#     public $AvailableLanguages = [];

#     /**
#      * @var string
#      */
#     public $Charset;

#     /**
#      * @var string
#      */
#     public $HtmlLang;

#     /**
#      * @var string
#      */
#     public $TextDirection = 'ltr';

#     protected $LanguageDirectory;

#     private static $_instance;

#     private $systemDateKeys = [];

#     /**
#      * @var Language
#      */
#     private $_lang;

#     protected function __construct()
#     {
#         $this->LanguageDirectory = dirname(__FILE__) . '/../../lang/';

#         $this->systemDateKeys['js_general_date'] = 'yy-mm-dd';
#         $this->systemDateKeys['js_general_datetime'] = 'yy-mm-dd HH:mm';
#         $this->systemDateKeys['js_general_time'] = 'HH:mm';
#         $this->systemDateKeys['system_datetime'] = 'Y-m-d H:i:s';
#         $this->systemDateKeys['url'] = 'Y-m-d';
#         $this->systemDateKeys['url_full'] = 'Y-m-d H:i:s';
#         $this->systemDateKeys['ical'] = 'Ymd\THis\Z';
#         $this->systemDateKeys['system'] = 'Y-m-d';
#         $this->systemDateKeys['fullcalendar'] = 'Y-m-d H:i';
#         $this->systemDateKeys['google'] = 'Ymd\\THi00\\Z';

#         $this->LoadAvailableLanguages();
#     }

#     private static function Create()
#     {
#         $resources = new Resources();
#         $resources->SetCurrentLanguage($resources->GetLanguageCode());
#         $resources->LoadOverrides();
#         return $resources;
#     }

#     /**
#      * @return Resources
#      */
#     public static function &GetInstance()
#     {
#         if (is_null(self::$_instance)) {
#             self::$_instance = Resources::Create();
#         }

#         setlocale(LC_ALL, self::$_instance->CurrentLanguage);
#         return self::$_instance;
#     }

#     public static function SetInstance($instance)
#     {
#         self::$_instance = $instance;
#     }

#     /**
#      * @param string $languageCode
#      * @return bool
#      */
#     public function SetLanguage($languageCode)
#     {
#         return $this->SetCurrentLanguage($languageCode);
#     }

#     /**
#      * @param string $languageCode
#      * @return bool
#      */
#     public function IsLanguageSupported($languageCode)
#     {
#         return !empty($languageCode) &&
#         (array_key_exists($languageCode, $this->AvailableLanguages) &&
#                 file_exists($this->LanguageDirectory . $this->AvailableLanguages[$languageCode]->LanguageFile));
#     }

#     public function GetString($key, $args = [])
#     {
#         if (!is_array($args)) {
#             $args = [$args];
#         }

#         $strings = $this->_lang->Strings;

#         if (!isset($strings[$key]) || empty($strings[$key])) {
#             return '?';
#         }

#         if (empty($args)) {
#             return $strings[$key];
#         } else {
#             $sprintf_args = '';

#             for ($i = 0; $i < count($args); $i++) {
#                 $sprintf_args .= "'" . addslashes($args[$i]) . "',";
#             }

#             $sprintf_args = substr($sprintf_args, 0, strlen($sprintf_args) - 1);
#             $string = addslashes($strings[$key]);
#             $return = eval("return sprintf('$string', $sprintf_args);");
#             return $return;
#         }
#     }

#     public function GetDateFormat($key)
#     {
#         if (array_key_exists($key, $this->systemDateKeys)) {
#             return $this->systemDateKeys[$key];
#         }

#         $dates = $this->_lang->Dates;

#         if (!isset($dates[$key]) || empty($dates[$key])) {
#             return '?';
#         }

#         return $dates[$key];
#     }

#     public function GeneralDateFormat()
#     {
#         return $this->GetDateFormat(ResourceKeys::DATE_GENERAL);
#     }

#     public function GeneralDateTimeFormat()
#     {
#         return $this->GetDateFormat(ResourceKeys::DATETIME_GENERAL);
#     }

#     public function ShortDateTimeFormat()
#     {
#         return $this->GetDateFormat(ResourceKeys::DATETIME_SHORT);
#     }

#     public function SystemDateTimeFormat()
#     {
#         return $this->GetDateFormat(ResourceKeys::DATETIME_SYSTEM);
#     }

#     public function GetDays($key)
#     {
#         $days = $this->_lang->Days;

#         if (!isset($days[$key]) || empty($days[$key])) {
#             return '?';
#         }

#         return $days[$key];
#     }

#     public function GetMonths($key)
#     {
#         $months = $this->_lang->Months;

#         if (!isset($months[$key]) || empty($months[$key])) {
#             return '?';
#         }

#         return $months[$key];
#     }

#     /**
#      * @param $languageCode
#      * @return bool
#      */
#     private function SetCurrentLanguage($languageCode)
#     {
#         $languageCode = strtolower($languageCode);

#         if ($languageCode == $this->CurrentLanguage) {
#             return true;
#         }

#         if ($this->IsLanguageSupported($languageCode)) {
#             $languageSettings = $this->AvailableLanguages[$languageCode];
#             $this->LanguageFile = $languageSettings->LanguageFile;

#             require_once($this->LanguageDirectory . $this->LanguageFile);

#             $class = $languageSettings->LanguageClass;
#             $this->_lang = new $class();
#             $this->CurrentLanguage = $languageCode;
#             $this->Charset = $this->_lang->Charset;
#             $this->HtmlLang = $this->_lang->HtmlLang;
#             $this->TextDirection = $this->_lang->TextDirection;

#             setlocale(LC_ALL, $this->CurrentLanguage);

#             return true;
#         }

#         return false;
#     }

#     private function GetLanguageCode()
#     {
#         $cookie = ServiceLocator::GetServer()->GetCookie(CookieKeys::LANGUAGE);
#         if ($cookie != null) {
#             return $cookie;
#         } else {
#             return Configuration::Instance()->GetKey(ConfigKeys::LANGUAGE);
#         }
#     }

#     private function LoadAvailableLanguages()
#     {
#         $this->AvailableLanguages = AvailableLanguages::GetAvailableLanguages();
#     }

#     private function LoadOverrides()
#     {
#         $overrideFile = ROOT_DIR . 'config/lang-overrides.php';
#         if (file_exists($overrideFile)) {
#             global $langOverrides;
#             include_once($overrideFile);
#             $this->_lang->Strings = array_merge($this->_lang->Strings, $langOverrides);
#         }
#     }
# }

from typing import List, Dict

class AvailableLanguage:
    def __init__(self, language_code: str, language_file: str, display_name: str):
        self.LanguageCode = language_code
        self.LanguageFile = language_file
        self.DisplayName = display_name
        self.LanguageClass = language_file.replace('.php', '')

class IResourceLocalization:
    def GetString(self, key: str, args: List[str] = []) -> str:
        raise NotImplementedError

    def GetDateFormat(self, key: str) -> str:
        raise NotImplementedError

    def GetDays(self, key: str) -> str:
        raise NotImplementedError

    def GetMonths(self, key: str) -> str:
        raise NotImplementedError

    def GeneralDateFormat(self) -> str:
        raise NotImplementedError

    def GeneralDateTimeFormat(self) -> str:
        raise NotImplementedError

class ResourceKeys:
    DATE_GENERAL = 'general_date'
    DATETIME_GENERAL = 'general_datetime'
    DATETIME_SHORT = 'short_datetime'
    DATETIME_SYSTEM = 'system_datetime'

class Resources(IResourceLocalization):
    def __init__(self):
        self.CurrentLanguage: str = ""
        self.LanguageFile: str = ""
        self.CalendarLanguageFile: str = ""
        self.AvailableLanguages: Dict[str, AvailableLanguage] = {}
        self.Charset: str = ""
        self.HtmlLang: str = ""
        self.TextDirection: str = 'ltr'
        self.LanguageDirectory: str = ""

        self.systemDateKeys = {
            'js_general_date': 'yy-mm-dd',
            'js_general_datetime': 'yy-mm-dd HH:mm',
            'js_general_time': 'HH:mm',
            'system_datetime': 'Y-m-d H:i:s',
            'url': 'Y-m-d',
            'url_full': 'Y-m-d H:i:s',
            'ical': 'Ymd\\THis\\Z',
            'system': 'Y-m-d',
            'fullcalendar': 'Y-m-d H:i',
            'google': 'Ymd\\THi00\\Z'
        }

        self._lang = None
        self._load_available_languages()
        self._set_instance()

    @staticmethod
    def _set_instance():
        global resources_instance
        resources_instance = Resources()

    @staticmethod
    def get_instance() -> 'Resources':
        return resources_instance

    def _load_available_languages(self):
        self.AvailableLanguages = self._get_available_languages()

    def _get_available_languages(self) -> Dict[str, AvailableLanguage]:
        return {
            'ar': AvailableLanguage('ar', 'ar.php', 'عربى'),
            'eu_es': AvailableLanguage('eu_es', 'eu_es.php', 'Basque'),
            'bg_bg': AvailableLanguage('bg_bg', 'bg_bg.php', 'Bulgarian'),
            'ca': AvailableLanguage('ca', 'ca.php', 'Catalan'),
            'cz': AvailableLanguage('cz', 'cz.php', 'Czech'),
            'da_da': AvailableLanguage('da_da', 'da_da.php', 'Danish'),
            'de_de': AvailableLanguage('de_de', 'de_de.php', 'Deutsch'),
            'du_be': AvailableLanguage('du_be', 'du_be.php', 'Flemisch'),
            'du_nl': AvailableLanguage('du_nl', 'du_nl.php', 'Dutch'),
            'el_gr': AvailableLanguage('el_gr', 'el_gr.php', 'Greek (Ελληνικά'),
            'en_us': AvailableLanguage('en_us', 'en_us.php', 'English US'),
            'en_gb': AvailableLanguage('en_gb', 'en_gb.php', 'English GB'),
            'es': AvailableLanguage('es', 'es.php', 'Espa&ntilde;ol'),
            'ee_ee': AvailableLanguage('ee_ee', 'ee_ee.php', 'Estonian'),
            'fi_fi': AvailableLanguage('fi_fi', 'fi_fi.php', 'Suomi'),
            'fr_fr': AvailableLanguage('fr_fr', 'fr_fr.php', 'Fran&ccedil;ais'),
            'hr_hr': AvailableLanguage('hr_hr', 'hr_hr.php', 'Hrvatski'),
            'hu_hu': AvailableLanguage('hu_hu', 'hu_hu.php', 'Hungarian'),
            'he': AvailableLanguage('he', 'he.php', 'עברית'),
            'id_id': AvailableLanguage('id_id', 'id_id.php', 'Bahasa Indonesia'),
            'it_it': AvailableLanguage('it_it', 'it_it.php', 'Italiano'),
            'ja_jp': AvailableLanguage('ja_jp', 'ja_jp.php', 'Japanese'),
            'lt': AvailableLanguage('lt', 'lt.php', 'Lietuvių'),
            'no_no': AvailableLanguage('no_no', 'no_no.php', 'Norsk bokmål'),
            'pl': AvailableLanguage('pl', 'pl.php', 'Polski'),
            'pt_pt': AvailableLanguage('pt_pt', 'pt_pt.php', 'Portugu&ecirc;s'),
            'pt_br': AvailableLanguage('pt_br', 'pt_br.php', 'Portugu&ecirc;s Brasileiro'),
            'ru_ru': AvailableLanguage('ru_ru', 'ru_ru.php', 'Русский'),
            'si_si': AvailableLanguage('si_si', 'si_si.php', 'Slovenščina'),
            'sr_sr': AvailableLanguage('sr_sr', 'sr_sr.php', 'Serbian'),
            'ro_ro': AvailableLanguage('ro_ro', 'ro_ro.php', 'Romanian'),
            'th_th': AvailableLanguage('th_th', 'th_th.php', 'Thai'),
            'tr_tr': AvailableLanguage('tr_tr', 'tr_tr.php', 'Türkçe'),
            'sv_sv': AvailableLanguage('sv_sv', 'sv_sv.php', 'Swedish'),
            'vn_vn': AvailableLanguage('vn_vn', 'vn_vn.php', 'Tiếng Việt'),
            'zh_cn': AvailableLanguage('zh_cn', 'zh_cn.php', '简体中文'),
            'zh_tw': AvailableLanguage('zh_tw', 'zh_tw.php', '繁體中文')
        }

    def set_language(self, language_code: str) -> bool:
        return self._set_current_language(language_code)

    def is_language_supported(self, language_code: str) -> bool:
        return language_code.lower() in self.AvailableLanguages and \
               self.AvailableLanguages[language_code.lower()].LanguageFile

    def _set_current_language(self, language_code: str) -> bool:
        language_code = language_code.lower()

        if language_code == self.CurrentLanguage:
            return True

        if self.is_language_supported(language_code):
            language_settings = self.AvailableLanguages[language_code]
            self.LanguageFile = language_settings.LanguageFile

            # The following line might need to be adjusted based on how the language class is imported in the language file
            lang_module = __import__(self.LanguageDirectory + self.LanguageFile[:-4], fromlist=[language_settings.LanguageClass])
            self._lang = getattr(lang_module, language_settings.LanguageClass)()

            self.CurrentLanguage = language_code
            self.Charset = self._lang.Charset
            self.HtmlLang = self._lang.HtmlLang
            self.TextDirection = self._lang.TextDirection

            return True

        return False

    def get_string(self, key: str, args: List[str] = []) -> str:
        if not isinstance(args, list):
            args = [args]

        strings = self._lang.Strings

        if key not in strings or not strings[key]:
            return '?'

        if not args:
            return strings[key]
        else:
            return strings[key].format(*args)

    def get_date_format(self, key: str) -> str:
        if key in self.systemDateKeys:
            return self.systemDateKeys[key]

        dates = self._lang.Dates

        if key not in dates or not dates[key]:
            return '?'

        return dates[key]

    def general_date_format(self) -> str:
        return self.get_date_format(ResourceKeys.DATE_GENERAL)

    def general_date_time_format(self) -> str:
        return self.get_date_format(ResourceKeys.DATETIME_GENERAL)

    def short_date_time_format(self) -> str:
        return self.get_date_format(ResourceKeys.DATETIME_SHORT)

    def system_date_time_format(self) -> str:
        return self.get_date_format(ResourceKeys.DATETIME_SYSTEM)

    def get_days(self, key: str) -> str:
        days = self._lang.Days

        if key not in days or not days[key]:
            return '?'

        return days[key]

    def get_months(self, key: str) -> str:
        months = self._lang.Months

        if key not in months or not months[key]:
            return '?'

        return months[key]


