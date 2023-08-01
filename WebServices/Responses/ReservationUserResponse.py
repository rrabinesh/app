# <?php

# require_once(ROOT_DIR . 'lib/WebService/namespace.php');

# class ReservationUserResponse extends RestResponse
# {
#     public $userId;
#     public $firstName;
#     public $lastName;
#     public $emailAddress;

#     public function __construct(IRestServer $server, $userId, $firstName, $lastName, $emailAddress)
#     {
#         $this->userId = $userId;
#         $this->firstName = $firstName;
#         $this->lastName = $lastName;
#         $this->emailAddress = $emailAddress;
#         $this->AddService($server, WebServices::GetUser, [WebServiceParams::UserId => $userId]);
#     }

#     public static function Masked()
#     {
#         return new MaskedReservationUserResponse();
#     }

#     public static function Example()
#     {
#         return new ExampleReservationUserResponse();
#     }
# }

# class MaskedReservationUserResponse extends ReservationUserResponse
# {
#     public function __construct()
#     {
#         $this->userId = null;
#         $this->firstName = 'Private';
#         $this->lastName = 'Private';
#         $this->emailAddress = 'Private';
#     }
# }

# class ExampleReservationUserResponse extends ReservationUserResponse
# {
#     public function __construct()
#     {
#         $this->userId = 123;
#         $this->firstName = 'first';
#         $this->lastName = 'last';
#         $this->emailAddress = 'email@address.com';
#     }
# }


from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()

# Define the Pydantic model for ReservationUserResponse
class ReservationUserResponse(BaseModel):
    userId: Optional[int]
    firstName: str
    lastName: str
    emailAddress: EmailStr

# Define the MaskedReservationUserResponse Pydantic model
class MaskedReservationUserResponse(ReservationUserResponse):
    userId: Optional[int] = None
    firstName: str = "Private"
    lastName: str = "Private"
    emailAddress: EmailStr = "Private"

# Define the ExampleReservationUserResponse Pydantic model
class ExampleReservationUserResponse(ReservationUserResponse):
    userId: int = 123
    firstName: str = "first"
    lastName: str = "last"
    emailAddress: EmailStr = "email@address.com"

# Define the endpoint to get the example reservation user response
@app.get("/reservation_user/")
def reservation_user():
    return ExampleReservationUserResponse()



