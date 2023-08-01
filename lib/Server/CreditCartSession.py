# <?php

# class CreditCartSession
# {
#     public $Quantity;
#     public $CostPerCredit;
#     public $Currency;
#     public $Id;
#     public $UserId;

#     /**
#      * @param float $creditQuantity
#      * @param float $costPerCredit
#      * @param string $currency
#      * @param int $userId
#      */
#     public function __construct($creditQuantity, $costPerCredit, $currency, $userId)
#     {
#         $this->Quantity = $creditQuantity;
#         $this->CostPerCredit = $costPerCredit;
#         $this->Currency = $currency;
#         $this->Id = BookedStringHelper::Random();
#         $this->UserId = $userId;
#     }

#     /**
#      * @return float
#      */
#     public function Total()
#     {
#         return $this->CostPerCredit * $this->Quantity;
#     }

#     /**
#      * @return string
#      */
#     public function Id()
#     {
#         return $this->Id;
#     }
# }

from pydantic import BaseModel

class CreditCartSession(BaseModel):
    quantity: float
    cost_per_credit: float
    currency: str
    id: str
    user_id: int

    def __init__(self, credit_quantity, cost_per_credit, currency, user_id):
        self.quantity = credit_quantity
        self.cost_per_credit = cost_per_credit
        self.currency = currency
        self.id = self.random_id()
        self.user_id = user_id

    def total(self):
        return self.cost_per_credit * self.quantity

    def random_id(self):
        import random
        import string
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


