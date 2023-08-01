# <?php

# namespace Booked {
#     require_once(ROOT_DIR . 'lib/Common/Resources.php');
#     require_once(ROOT_DIR . 'lib/Common/Resources.php');

#     use NumberFormatter;
#     use Resources;

#     class Currency
#     {
#         private $currencies = [];

#         /**
#          * @var string
#          */
#         private $currencyCode;

#         /**
#          * @var CurrencyDefinition
#          */
#         private $currency;

#         /**
#          * @param string $currencyCode
#          */
#         public function __construct($currencyCode)
#         {
#             $this->currencyCode = $currencyCode;
#             $this->currencies = self::Currencies();

#             $this->currency = $this->currencies[0];
#             foreach ($this->currencies as $currency) {
#                 if ($currency->IsoCode() == $currencyCode) {
#                     $this->currency = $currency;
#                     break;
#                 }
#             }
#         }

#         /**
#          * @return CurrencyDefinition[]
#          */
#         public static function Currencies()
#         {
#             return [
#                     new CurrencyDefinition('USD'),
#                     new CurrencyDefinition('GBP'),
#                     new CurrencyDefinition('AUD'),
#                     new CurrencyDefinition('BRL'),
#                     new CurrencyDefinition('CAD'),
#                     new CurrencyDefinition('CZK'),
#                     new CurrencyDefinition('DKK'),
#                     new CurrencyDefinition('EUR'),
#                     new CurrencyDefinition('HKD'),
#                     new CurrencyDefinition('HUF'),
#                     new CurrencyDefinition('ILS'),
#                     new CurrencyDefinition('JPY', true),
#                     new CurrencyDefinition('MYR'),
#                     new CurrencyDefinition('MXN'),
#                     new CurrencyDefinition('NOK'),
#                     new CurrencyDefinition('NZD'),
#                     new CurrencyDefinition('PHP'),
#                     new CurrencyDefinition('PLN'),
#                     new CurrencyDefinition('SGD'),
#                     new CurrencyDefinition('SEK'),
#                     new CurrencyDefinition('CHF'),
#                     new CurrencyDefinition('TWD'),
#                     new CurrencyDefinition('THB'),
#             ];
#         }

#         /**
#          * @param string $currencyCode
#          * @return Currency
#          */
#         public static function Create($currencyCode)
#         {
#             return new Currency($currencyCode);
#         }

#         /**
#          * @param float $amount
#          * @return string
#          */
#         public function Format($amount)
#         {
#             if (!class_exists('NumberFormatter')) {
#                 if ($this->currencyCode == 'USD') {
#                     return '$' . floatval($amount) . 'USD';
#                 } else {
#                     return 'We cannot format this currency. <a href="http://php.net/manual/en/book.intl.php">You must enable internationalization</a>.';
#                 }
#             } else {
#                 $fmt = new NumberFormatter(Resources::GetInstance()->CurrentLanguage, NumberFormatter::CURRENCY);
#                 return $fmt->formatCurrency($amount, $this->currencyCode);
#             }
#         }

#         /**
#          * @param float $amount
#          * @return float
#          */
#         public function ToStripe($amount)
#         {
#             if ($this->IsZeroDecimal()) {
#                 return $amount;
#             }

#             return $amount * 100;
#         }

#         /**
#          * @param float $amount
#          * @return float
#          */
#         public function FromStripe($amount)
#         {
#             if ($this->IsZeroDecimal()) {
#                 return $amount;
#             }

#             return $amount / 100;
#         }

#         public function IsZeroDecimal()
#         {
#             return $this->currency->IsZeroDecimal();
#         }
#     }

#     class CurrencyDefinition
#     {
#         /**
#          * @var string
#          */
#         private $isoCode;

#         /**
#          * @var bool
#          */
#         private $isZeroDecimal;

#         /**
#          * @param string $isoCode
#          * @param bool $isZeroDecimal
#          */
#         public function __construct($isoCode, $isZeroDecimal = false)
#         {
#             $this->isoCode = $isoCode;
#             $this->isZeroDecimal = $isZeroDecimal;
#         }

#         public function __toString()
#         {
#             return $this->isoCode;
#         }

#         /**
#          * @return string
#          */
#         public function IsoCode()
#         {
#             return $this->isoCode;
#         }

#         /**
#          * @return bool
#          */
#         public function IsZeroDecimal()
#         {
#             return $this->isZeroDecimal;
#         }
#     }
# }


from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class CurrencyDefinition(BaseModel):
    iso_code: str
    is_zero_decimal: bool

class Currency(BaseModel):
    currency_code: str
    currency: CurrencyDefinition

@app.get("/currencies/", response_model=List[Currency])
async def get_currencies():
    currencies = [
        Currency(currency_code="USD", currency=CurrencyDefinition(iso_code="USD")),
        Currency(currency_code="GBP", currency=CurrencyDefinition(iso_code="GBP")),
        Currency(currency_code="AUD", currency=CurrencyDefinition(iso_code="AUD")),
        Currency(currency_code="BRL", currency=CurrencyDefinition(iso_code="BRL")),
        Currency(currency_code="CAD", currency=CurrencyDefinition(iso_code="CAD")),
        # Add more currencies here as needed...
    ]
    return currencies

@app.get("/currency/{currency_code}", response_model=Currency)
async def get_currency(currency_code: str):
    currencies = {
        "USD": Currency(currency_code="USD", currency=CurrencyDefinition(iso_code="USD")),
        "GBP": Currency(currency_code="GBP", currency=CurrencyDefinition(iso_code="GBP")),
        "AUD": Currency(currency_code="AUD", currency=CurrencyDefinition(iso_code="AUD")),
        "BRL": Currency(currency_code="BRL", currency=CurrencyDefinition(iso_code="BRL")),
        "CAD": Currency(currency_code="CAD", currency=CurrencyDefinition(iso_code="CAD")),
        # Add more currencies here as needed...
    }
    return currencies.get(currency_code, {"currency_code": "Unknown", "currency": {"iso_code": "Unknown"}})

