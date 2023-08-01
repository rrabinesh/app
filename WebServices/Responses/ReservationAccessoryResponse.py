# <?php

# require_once(ROOT_DIR . 'lib/WebService/namespace.php');

# class ReservationAccessoryResponse extends RestResponse
# {
#     public $id;
#     public $name;
#     public $quantityAvailable;
#     public $quantityReserved;

#     public function __construct(IRestServer $server, $id, $name, $quantityReserved, $quantityAvailable)
#     {
#         $this->id = $id;
#         $this->name = $name;
#         $this->quantityReserved = $quantityReserved;
#         $this->quantityAvailable = $quantityAvailable;

#         $this->AddService($server, WebServices::GetAccessory, [WebServiceParams::AccessoryId => $id]);
#     }

#     public static function Example()
#     {
#         return new ExampleReservationAccessoryResponse();
#     }
# }

# class ExampleReservationAccessoryResponse extends ReservationAccessoryResponse
# {
#     public function __construct()
#     {
#         $this->id = 1;
#         $this->name = 'Example';
#         $this->quantityAvailable = 12;
#         $this->quantityReserved = 3;
#     }
# }



from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the ReservationAccessoryResponse Pydantic model
class ReservationAccessoryResponse(BaseModel):
    id: int
    name: str
    quantityAvailable: int
    quantityReserved: int

# Define the ExampleReservationAccessoryResponse Pydantic model
class ExampleReservationAccessoryResponse(ReservationAccessoryResponse):
    pass

# Sample usage of ExampleReservationAccessoryResponse model
example_response = ExampleReservationAccessoryResponse(
    id=1,
    name="Example",
    quantityAvailable=12,
    quantityReserved=3,
)

# Define the endpoint to get reservation accessory response
@app.get("/reservation_accessory/")
def reservation_accessory():
    return example_response



