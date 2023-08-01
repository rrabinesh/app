# <?php

# require_once(ROOT_DIR . 'Domain/Access/namespace.php');

# class TermsOfServiceValidator extends ValidatorBase implements IValidator
# {
#     /**
#      * @var ITermsOfServiceRepository
#      */
#     private $termsOfServiceRepository;
#     /**
#      * @var bool
#      */
#     private $hasAcknowledged;

#     /**
#      * @param ITermsOfServiceRepository $termsOfServiceRepository
#      * @param bool $hasAcknowledged
#      */
#     public function __construct(ITermsOfServiceRepository $termsOfServiceRepository, $hasAcknowledged)
#     {
#         $this->termsOfServiceRepository = $termsOfServiceRepository;
#         $this->hasAcknowledged = $hasAcknowledged;
#     }

#     public function Validate()
#     {
#         $this->isValid = true;

#         $terms = $this->termsOfServiceRepository->Load();

#         if ($terms != null && $terms->AppliesToRegistration()) {
#             $this->isValid = $this->hasAcknowledged;
#         }
#     }
# }

from fastapi import HTTPException

from tos_repository import TermsOfServiceRepository

class TermsOfServiceValidator:

    def __init__(self, repo: TermsOfServiceRepository, acknowledged: bool):
        self.repo = repo
        self.acknowledged = acknowledged

    def validate(self) -> None:
        terms = self.repo.get_current()
        if terms and terms.applies_to_registration:
           if not self.acknowledged:
               raise HTTPException(status_code=400, detail="Terms of Service must be acknowledged")
