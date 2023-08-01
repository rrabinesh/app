# <?php

# require_once(ROOT_DIR . 'Domain/CreditCost.php');
# require_once(ROOT_DIR . 'Domain/PaymentGateway.php');
# require_once(ROOT_DIR . 'Domain/Values/PayPalPaymentResult.php');
# require_once(ROOT_DIR . 'Domain/Values/TransactionLogView.php');
# require_once(ROOT_DIR . 'Domain/Access/PageableDataStore.php');
# require_once(ROOT_DIR . 'lib/Database/namespace.php');
# require_once(ROOT_DIR . 'lib/Database/Commands/namespace.php');

# interface IPaymentRepository
# {
#     /**
#      * @param CreditCost $credit
#      */
#     public function UpdateCreditCost($credit);

#     /**
#      * @param int $creditCount
#      */
#     public function DeleteCreditCost($creditCount);

#     /**
#      * @return CreditCost[]
#      */
#     public function GetCreditCosts();

#     /**
#      * @param PayPalGateway $gateway
#      */
#     public function UpdatePayPalGateway(PayPalGateway $gateway);

#     /**
#      * @param StripeGateway $gateway
#      */
#     public function UpdateStripeGateway(StripeGateway $gateway);

#     /**
#      * @return PayPalGateway
#      */
#     public function GetPayPalGateway();

#     /**
#      * @return StripeGateway
#      */
#     public function GetStripeGateway();

#     /**
#      * @param int $pageNumber
#      * @param int $pageSize
#      * @param int $userId
#      * @param string $sortField
#      * @param string $sortDirection
#      * @param ISqlFilter $filter
#      * @return PageableData|TransactionLogView[]
#      */
#     public function GetList($pageNumber, $pageSize, $userId = -1, $sortField = null, $sortDirection = null, $filter = null);

#     /**
#      * @param int $transactionLogId
#      * @return TransactionLogView
#      */
#     public function GetTransactionLogView($transactionLogId);
# }

# class PaymentRepository implements IPaymentRepository
# {
#     public function UpdateCreditCost($credit)
#     {
#         $this->DeleteCreditCost($credit->Count()); // In case it already exists: overwrite
#         ServiceLocator::GetDatabase()->Execute(new AddPaymentConfigurationCommand($credit->Count(), $credit->Cost(), $credit->Currency()));
#     }

#     public function DeleteCreditCost($creditCount)
#     {
#         ServiceLocator::GetDatabase()->Execute(new DeletePaymentConfigurationCommand($creditCount));
#     }

#     public function GetCreditCosts()
#     {
#         $reader = ServiceLocator::GetDatabase()->Query(new GetPaymentConfigurationCommand());
#         $res = [];
#         for ($i=0;$i<$reader->NumRows();$i++) {
#             $row = $reader->GetRow();
#             $res[] = new CreditCost($row[ColumnNames::CREDIT_COUNT], $row[ColumnNames::CREDIT_COST], $row[ColumnNames::CREDIT_CURRENCY]);
#         }
#         $reader->Free();

#         if (empty($res)) {
#             $res[] = new CreditCost();
#         }
#         return $res;
#     }

#     public function UpdatePayPalGateway(PayPalGateway $gateway)
#     {
#         $this->UpdateGateway($gateway);
#     }

#     public function UpdateStripeGateway(StripeGateway $gateway)
#     {
#         $this->UpdateGateway($gateway);
#     }

#     private function UpdateGateway(IPaymentGateway $gateway)
#     {
#         ServiceLocator::GetDatabase()->Execute(new DeletePaymentGatewaySettingsCommand($gateway->GetGatewayType()));
#         if ($gateway->IsEnabled()) {
#             foreach ($gateway->Settings() as $gatewaySetting) {
#                 ServiceLocator::GetDatabase()->Execute(new AddPaymentGatewaySettingCommand($gateway->GetGatewayType(), $gatewaySetting->Name(), $gatewaySetting->Value()));
#             }
#         }
#     }

#     public function GetPayPalGateway()
#     {
#         $clientId = null;
#         $secret = null;
#         $environment = null;

#         $reader = ServiceLocator::GetDatabase()->Query(new GetPaymentGatewaySettingsCommand(PaymentGateways::PAYPAL));
#         while ($row = $reader->GetRow()) {
#             if ($row[ColumnNames::GATEWAY_SETTING_NAME] == PayPalGateway::CLIENT_ID) {
#                 $clientId = $row[ColumnNames::GATEWAY_SETTING_VALUE];
#             } elseif ($row[ColumnNames::GATEWAY_SETTING_NAME] == PayPalGateway::SECRET) {
#                 $secret = $row[ColumnNames::GATEWAY_SETTING_VALUE];
#             } elseif ($row[ColumnNames::GATEWAY_SETTING_NAME] == PayPalGateway::ENVIRONMENT) {
#                 $environment = $row[ColumnNames::GATEWAY_SETTING_VALUE];
#             }
#         }

#         $reader->Free();
#         return PayPalGateway::Create($clientId, $secret, $environment);
#     }

#     public function GetStripeGateway()
#     {
#         $publishableKey = null;
#         $secretKey = null;

#         $reader = ServiceLocator::GetDatabase()->Query(new GetPaymentGatewaySettingsCommand(PaymentGateways::STRIPE));
#         while ($row = $reader->GetRow()) {
#             if ($row[ColumnNames::GATEWAY_SETTING_NAME] == StripeGateway::PUBLISHABLE_KEY) {
#                 $publishableKey = $row[ColumnNames::GATEWAY_SETTING_VALUE];
#             } elseif ($row[ColumnNames::GATEWAY_SETTING_NAME] == StripeGateway::SECRET_KEY) {
#                 $secretKey = $row[ColumnNames::GATEWAY_SETTING_VALUE];
#             }
#         }

#         $reader->Free();
#         return StripeGateway::Create($publishableKey, $secretKey);
#     }

#     /**
#      * @param int $pageNumber
#      * @param int $pageSize
#      * @param int $userId
#      * @param string $sortField
#      * @param string $sortDirection
#      * @param ISqlFilter $filter
#      * @return PageableData|TransactionLogView[]
#      */
#     public function GetList($pageNumber, $pageSize, $userId = -1, $sortField = null, $sortDirection = null, $filter = null)
#     {
#         $command = new GetAllTransactionLogsCommand($userId);

#         if ($filter != null) {
#             $command = new FilterCommand($command, $filter);
#         }

#         $builder = ['TransactionLogView', 'Populate'];
#         return PageableDataStore::GetList($command, $builder, $pageNumber, $pageSize, $sortField, $sortDirection);
#     }

#     /**
#      * @param int $transactionLogId
#      * @return TransactionLogView
#      */
#     public function GetTransactionLogView($transactionLogId)
#     {
#         $command = new GetTransactionLogCommand($transactionLogId);
#         $reader = ServiceLocator::GetDatabase()->Query($command);
#         if ($row = $reader->GetRow()) {
#             $reader->Free();
#             return TransactionLogView::Populate($row);
#         }

#         $reader->Free();
#         return null;
#     }
# }


from fastapi import FastAPI, HTTPException
from typing import List

# Create a FastAPI app
app = FastAPI()

# Placeholder for classes not defined in the provided code
class CreditCost:
    pass

class PayPalGateway:
    pass

class StripeGateway:
    pass

class TransactionLogView:
    pass

# IPaymentRepository interface (not explicitly needed in FastAPI)

# PaymentRepository implementation
class PaymentRepository:
    def update_credit_cost(self, credit: CreditCost):
        # Implement the logic to update credit cost
        pass

    def delete_credit_cost(self, credit_count: int):
        # Implement the logic to delete credit cost
        pass

    def get_credit_costs(self) -> List[CreditCost]:
        # Implement the logic to get credit costs
        pass

    def update_paypal_gateway(self, gateway: PayPalGateway):
        # Implement the logic to update PayPal gateway
        pass

    def update_stripe_gateway(self, gateway: StripeGateway):
        # Implement the logic to update Stripe gateway
        pass

    def get_paypal_gateway(self) -> PayPalGateway:
        # Implement the logic to get PayPal gateway
        pass

    def get_stripe_gateway(self) -> StripeGateway:
        # Implement the logic to get Stripe gateway
        pass

    def get_list(
        self,
        page_number: int,
        page_size: int,
        user_id: int = -1,
        sort_field: str = None,
        sort_direction: str = None,
        filter: str = None
    ) -> List[TransactionLogView]:
        # Implement the logic to get a list of transaction logs
        pass

    def get_transaction_log_view(self, transaction_log_id: int) -> TransactionLogView:
        # Implement the logic to get a transaction log view
        pass

# Create an instance of the PaymentRepository class
payment_repository = PaymentRepository()

# FastAPI endpoint to update credit cost
@app.post("/update_credit_cost/")
async def update_credit_cost(credit: CreditCost):
    payment_repository.update_credit_cost(credit)
    return {"message": "Credit cost updated successfully"}

# FastAPI endpoint to delete credit cost
@app.post("/delete_credit_cost/")
async def delete_credit_cost(credit_count: int):
    payment_repository.delete_credit_cost(credit_count)
    return {"message": "Credit cost deleted successfully"}

# FastAPI endpoint to get credit costs
@app.get("/get_credit_costs/")
async def get_credit_costs():
    credit_costs = payment_repository.get_credit_costs()
    return {"credit_costs": credit_costs}

# FastAPI endpoint to update PayPal gateway
@app.post("/update_paypal_gateway/")
async def update_paypal_gateway(gateway: PayPalGateway):
    payment_repository.update_paypal_gateway(gateway)
    return {"message": "PayPal gateway updated successfully"}

# FastAPI endpoint to update Stripe gateway
@app.post("/update_stripe_gateway/")
async def update_stripe_gateway(gateway: StripeGateway):
    payment_repository.update_stripe_gateway(gateway)
    return {"message": "Stripe gateway updated successfully"}

# FastAPI endpoint to get PayPal gateway
@app.get("/get_paypal_gateway/")
async def get_paypal_gateway():
    gateway = payment_repository.get_paypal_gateway()
    return {"gateway": gateway}



