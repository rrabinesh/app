# <?php

# if (file_exists(ROOT_DIR . 'vendor/autoload.php')) { 
#     require_once ROOT_DIR . 'vendor/autoload.php';
# }

# interface ICaptchaService {
#     /**
#      * @abstract
#      * @return string
#      */
#     public function GetImageUrl();

#     /**
#      * @abstract
#      * @param string $captchaValue
#      * @return bool
#      */
#     public function IsCorrect($captchaValue);
# }

# class NullCaptchaService implements ICaptchaService
# {
#     /**
#      * @return string
#      */
#     public function GetImageUrl()
#     {
#         return '';
#     }

#     /**
#      * @param string $captchaValue
#      * @return bool
#      */
#     public function IsCorrect($captchaValue)
#     {
#         return true;
#     }
# }

# class CaptchaService implements ICaptchaService
# {
#     private function __construct()
#     {
#     }

#     public function GetImageUrl()
#     {
#         $url = new Url(Configuration::Instance()->GetScriptUrl() . '/Services/Authentication/show-captcha.php');
#         $url->AddQueryString('show', 'true');
#         return $url->__toString();
#     }

#     public function IsCorrect($captchaValue)
#     {
#         $isValid = $captchaValue == $_SESSION['phrase'];

#         Log::Debug('Checking captcha value. Value entered: %s. Correct value: %s.  IsValid: %s', $captchaValue,$_SESSION['phrase'] , (int)$isValid);

#         return $isValid;
#     }

#     /**
#      * @static
#      * @return ICaptchaService
#      */
#     public static function Create()
#     {
#         if (Configuration::Instance()->GetKey(ConfigKeys::REGISTRATION_ENABLE_CAPTCHA, new BooleanConverter()) ||
#             (Configuration::Instance()->GetSectionKey(ConfigSection::AUTHENTICATION, ConfigKeys::AUTHENTICATION_CAPTCHA_ON_LOGIN, new BooleanConverter()))
#         ) {
#             if (Configuration::Instance()->GetSectionKey(
#                 ConfigSection::RECAPTCHA,
#                 ConfigKeys::RECAPTCHA_ENABLED,
#                 new BooleanConverter()
#             )
#             ) {
#                 //				Log::Debug('Using ReCaptchaService');
#                 return new ReCaptchaService();
#             }
#             //			Log::Debug('Using CaptchaService');
#             return new CaptchaService();
#         }

#         return new NullCaptchaService();
#     }
# }

# class ReCaptchaService implements ICaptchaService
# {
#     /**
#      * @return string
#      */
#     public function GetImageUrl()
#     {
#         return '';
#     }

#     /**
#      * @param string $captchaValue
#      * @return bool
#      */
#     public function IsCorrect($captchaValue)
#     {
#         $server = ServiceLocator::GetServer();

#         $privatekey = Configuration::Instance()->GetSectionKey(ConfigSection::RECAPTCHA, ConfigKeys::RECAPTCHA_PRIVATE_KEY);
 
#         $recap = new \ReCaptcha\ReCaptcha($privatekey);
#         $resp = $recap->verify($server->GetForm('g-recaptcha-response'),$server->GetRemoteAddress());

#         Log::Debug('ReCaptcha IsValid: %s', $resp->isSuccess());

#         return $resp->isSuccess();
#     }
# }


from fastapi import APIRouter

router = APIRouter()

class ICaptchaService:
    def get_image_url(self) -> str:
        raise NotImplementedError()

    def is_correct(self, captcha_value: str) -> bool:
        raise NotImplementedError()

class NullCaptchaService(ICaptchaService):
    def get_image_url(self) -> str:
        return ''

    def is_correct(self, captcha_value: str) -> bool:
        return True

# You'll need to install the 'requests' library for the ReCaptchaService to work.
# You can install it using: pip install requests
import requests

class ReCaptchaService(ICaptchaService):
    def get_image_url(self) -> str:
        return ''

    def is_correct(self, captcha_value: str) -> bool:
        server = get_server()  # Assuming you have implemented the get_server() function.

        private_key = get_recaptcha_private_key()  # Assuming you have implemented the get_recaptcha_private_key() function.

        response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': private_key,
                'response': captcha_value,
                'remoteip': server.get_remote_address()
            }
        )

        return response.json().get('success', False)

# Define the endpoints for captcha service

@router.get("/captcha/image-url")
def get_captcha_image_url():
    # Assuming you have an instance of CaptchaService or ReCaptchaService.
    captcha_service = CaptchaService.Create()
    return {"image_url": captcha_service.get_image_url()}

@router.post("/captcha/verify")
def verify_captcha(captcha_value: str):
    # Assuming you have an instance of CaptchaService or ReCaptchaService.
    captcha_service = CaptchaService.Create()
    is_correct = captcha_service.is_correct(captcha_value)
    return {"is_correct": is_correct}

def get_recaptcha_private_key():
    # Implement your logic to fetch the ReCaptcha private key from configuration or environment.
    # Replace 'your_recaptcha_private_key' with the actual private key.
    return 'your_recaptcha_private_key'




