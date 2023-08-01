# <?php

# require_once(ROOT_DIR . 'Domain/Values/Currency.php');
# use Booked\Currency;

# class CreditCost
# {
#     /**
#      * @var int
#      */
#     private $count;
#     /**
#      * @var float
#      */
#     private $cost;
#     /**
#      * @var string
#      */
#     private $currency;

#     /**
#      * @param float $cost
#      * @param string $currency
#      */
#     public function __construct($count = 1, $cost = 0.0, $currency = 'USD')
#     {
#         $this->count = $count;
#         $this->cost = $cost;
#         $this->currency = $currency;
#     }

#     /**
#      * @return int
#      */
#     public function Count()
#     {
#         return $this->count;
#     }

#     /**
#      * @return float
#      */
#     public function Cost()
#     {
#         return $this->cost;
#     }

#     /**
#      * @return string
#      */
#     public function Currency()
#     {
#         return $this->currency;
#     }

#     /**
#      * @param float|null $amount
#      * @return string
#      */
#     public function FormatCurrency($amount = null)
#     {
#         $toFormat = is_null($amount) ? $this->Cost() : $amount;
#         $currency = new Currency($this->Currency());
#         return $currency->Format($toFormat);
#     }

#     /**
#      * @param float $quantity
#      * @return float
#      */
#     public function GetTotal($quantity)
#     {
#         return $this->Cost() * $quantity;
#     }

#     /**
#      * @param float $quantity
#      * @return string
#      */
#     public function GetFormattedTotal($quantity)
#     {
#         $total = $this->GetTotal($quantity);
#         return $this->FormatCurrency($total);
#     }
# }

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CreditCost(BaseModel):
    count: int = 1
    cost: float = 0.0
    currency: str = 'USD'

    def format_currency(self, amount=None):
        if amount is None:
            amount = self.cost

        # Implement the currency formatting logic here based on your requirements.
        # You can use a third-party library or a database to store currency formats.
        # For this example, let's assume we return a string with the currency code and amount.
        formatted_amount = f"{self.currency} {amount}"
        return formatted_amount

    def get_total(self, quantity):
        return self.cost * quantity

    def get_formatted_total(self, quantity):
        total = self.get_total(quantity)
        return self.format_currency(total)

