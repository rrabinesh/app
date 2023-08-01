# <?php

# class CaptchaValidator extends ValidatorBase implements IValidator
# {
#     private $captchaValue;
#     private $captchaService;

#     public function __construct($captchaValue, ICaptchaService $captchaService)
#     {
#         $this->captchaValue = $captchaValue;
#         $this->captchaService = $captchaService;
#     }

#     public function Validate()
#     {
#         $this->isValid = $this->captchaService->IsCorrect($this->captchaValue);
#     }
# }

from abc import ABC, abstractmethod

class IValidator(ABC):
    @abstractmethod
    def validate(self) -> bool:
        pass

class ICaptchaService(ABC):
    @abstractmethod
    def is_correct(self, value: str) -> bool:
        pass
        
class CaptchaValidator(IValidator):

    def __init__(self, captcha_value: str, captcha_service: ICaptchaService):
        self.captcha_value = captcha_value
        self.captcha_service = captcha_service
        
    def validate(self) -> bool:
        self.is_valid = self.captcha_service.is_correct(self.captcha_value)
        return self.is_valid
