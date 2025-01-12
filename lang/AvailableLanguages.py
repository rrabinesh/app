# <?php

# require_once(ROOT_DIR . 'lang/AvailableLanguage.php');

# class AvailableLanguages
# {
#     /**
#      * @return array|AvailableLanguage[]
#      */
#     public static function GetAvailableLanguages()
#     {
#         return [
#             'ar' => new AvailableLanguage('ar', 'ar.php', 'عربى'),
#             'eu_es' => new AvailableLanguage('eu_es', 'eu_es.php', 'Basque'),
#             'bg_bg' => new AvailableLanguage('bg_bg', 'bg_bg.php', 'Bulgarian'),
#             'ca' => new AvailableLanguage('ca', 'ca.php', 'Catalan'),
#             'cz' => new AvailableLanguage('cz', 'cz.php', 'Czech'),
#             'da_da' => new AvailableLanguage('da_da', 'da_da.php', 'Danish'),
#             'de_de' => new AvailableLanguage('de_de', 'de_de.php', 'Deutsch'),
#             'du_be' => new AvailableLanguage('du_be', 'du_be.php', 'Flemisch'),
#             'du_nl' => new AvailableLanguage('du_nl', 'du_nl.php', 'Dutch'),
#             'el_gr' => new AvailableLanguage('el_gr', 'el_gr.php', 'Greek (Ελληνικά'),
#             'en_us' => new AvailableLanguage('en_us', 'en_us.php', 'English US'),
#             'en_gb' => new AvailableLanguage('en_gb', 'en_gb.php', 'English GB'),
#             'es' => new AvailableLanguage('es', 'es.php', 'Espa&ntilde;ol'),
#             'ee_ee' => new AvailableLanguage('ee_ee', 'ee_ee.php', 'Estonian'),
#             'fi_fi' => new AvailableLanguage('fi_fi', 'fi_fi.php', 'Suomi'),
#             'fr_fr' => new AvailableLanguage('fr_fr', 'fr_fr.php', 'Fran&ccedil;ais'),
#             'hr_hr' => new AvailableLanguage('hr_hr', 'hr_hr.php', 'Hrvatski'),
#             'hu_hu' => new AvailableLanguage('hu_hu', 'hu_hu.php', 'Hungarian'),
#             'he' => new AvailableLanguage('he', 'he.php', 'עברית'),
#             'id_id' => new AvailableLanguage('id_id', 'id_id.php', 'Bahasa Indonesia'),
#             'it_it' => new AvailableLanguage('it_it', 'it_it.php', 'Italiano'),
#             'ja_jp' => new AvailableLanguage('ja_jp', 'ja_jp.php', 'Japanese'),
#             'lt' => new AvailableLanguage('lt', 'lt.php', 'Lietuvių'),
#             'no_no' => new AvailableLanguage('no_no', 'no_no.php', 'Norsk bokmål'),
#             'pl' => new AvailableLanguage('pl', 'pl.php', 'Polski'),
#             'pt_pt' => new AvailableLanguage('pt_pt', 'pt_pt.php', 'Portugu&ecirc;s'),
#             'pt_br' => new AvailableLanguage('pt_br', 'pt_br.php', 'Portugu&ecirc;s Brasileiro'),
#             'ru_ru' => new AvailableLanguage('ru_ru', 'ru_ru.php', 'Русский'),
#             'si_si' => new AvailableLanguage('si_si', 'si_si.php', 'Slovenščina'),
#             'sr_sr' => new AvailableLanguage('sr_sr', 'sr_sr.php', 'Serbian'),
#             'ro_ro' => new AvailableLanguage('ro_ro', 'ro_ro.php', 'Romanian'),
#             'th_th' => new AvailableLanguage('th_th', 'th_th.php', 'Thai'),
#             'tr_tr' => new AvailableLanguage('tr_tr', 'tr_tr.php', 'Türkçe'),
#             'sv_sv' => new AvailableLanguage('sv_sv', 'sv_sv.php', 'Swedish'),
#             'vn_vn' => new AvailableLanguage('vn_vn', 'vn_vn.php', 'Tiếng Việt'),
#             'zh_cn' => new AvailableLanguage('zh_cn', 'zh_cn.php', '简体中文'),
#             'zh_tw' => new AvailableLanguage('zh_tw', 'zh_tw.php', '繁體中文'),
#         ];
#     }

#     public static function Contains($language)
#     {
#         $languages = self::GetAvailableLanguages();

#         return array_key_exists(strtolower($language), $languages);
#     }
# }




from typing import Dict

class AvailableLanguage:
    def __init__(self, language_code: str, language_file: str, display_name: str):
        self.LanguageCode = language_code
        self.LanguageFile = language_file
        self.DisplayName = display_name
        self.LanguageClass = language_file.replace('.php', '')

def get_available_languages() -> Dict[str, AvailableLanguage]:
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
        'zh_tw': AvailableLanguage('zh_tw', 'zh_tw.php', '繁體中文'),
    }

def contains(language: str) -> bool:
    languages = get_available_languages()
    return language.lower() in languages


