# <?php

# class ReservationCreatedResponse extends RestResponse
# {
#     public $referenceNumber;
#     public $isPendingApproval;

#     public function __construct(IRestServer $server, $referenceNumber, $isPendingApproval)
#     {
#         $this->message = 'The reservation was created';
#         $this->referenceNumber = $referenceNumber;
#         $this->isPendingApproval = $isPendingApproval;
#         $this->AddService($server, WebServices::GetReservation, [WebServiceParams::ReferenceNumber => $referenceNumber]);
#         $this->AddService($server, WebServices::UpdateReservation, [WebServiceParams::ReferenceNumber => $referenceNumber]);
#     }

#     public static function Example()
#     {
#         return new ExampleReservationCreatedResponse();
#     }
# }

# class ReservationUpdatedResponse extends RestResponse
# {
#     public $referenceNumber;
#     public $isPendingApproval;

#     public function __construct(IRestServer $server, $referenceNumber, $isPendingApproval)
#     {
#         $this->message = 'The reservation was updated';
#         $this->referenceNumber = $referenceNumber;
#         $this->isPendingApproval = $isPendingApproval;
#         $this->AddService($server, WebServices::GetReservation, [WebServiceParams::ReferenceNumber => $referenceNumber]);
#     }

#     public static function Example()
#     {
#         return new ExampleReservationCreatedResponse();
#     }
# }

# class ReservationApprovedResponse extends RestResponse
# {
#     public $referenceNumber;

#     public function __construct(IRestServer $server, $referenceNumber)
#     {
#         $this->message = 'The reservation was approved';
#         $this->referenceNumber = $referenceNumber;
#         $this->AddService($server, WebServices::GetReservation, [WebServiceParams::ReferenceNumber => $referenceNumber]);
#     }

#     public static function Example()
#     {
#         return new ExampleReservationCreatedResponse();
#     }
# }

# class ReservationCheckedInResponse extends RestResponse
# {
#     public $referenceNumber;

#     public function __construct(IRestServer $server, $referenceNumber)
#     {
#         $this->message = 'The reservation was checked in';
#         $this->referenceNumber = $referenceNumber;
#         $this->AddService($server, WebServices::GetReservation, [WebServiceParams::ReferenceNumber => $referenceNumber]);
#     }

#     public static function Example()
#     {
#         return new ExampleReservationCreatedResponse();
#     }
# }

# class ReservationCheckedOutResponse extends RestResponse
# {
#     public $referenceNumber;

#     public function __construct(IRestServer $server, $referenceNumber)
#     {
#         $this->message = 'The reservation was checked out';
#         $this->referenceNumber = $referenceNumber;
#         $this->AddService($server, WebServices::GetReservation, [WebServiceParams::ReferenceNumber => $referenceNumber]);
#     }

#     public static function Example()
#     {
#         return new ExampleReservationCreatedResponse();
#     }
# }

# class ExampleReservationCreatedResponse extends ReservationCreatedResponse
# {
#     public function __construct()
#     {
#         $this->referenceNumber = 'referenceNumber';
#         $this->isPendingApproval = true;
#         $this->AddLink('http://url/to/reservation', WebServices::GetReservation);
#         $this->AddLink('http://url/to/update/reservation', WebServices::UpdateReservation);
#     }
# }

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the base response Pydantic model
class BaseResponse(BaseModel):
    message: str
    referenceNumber: str

# Define the specific response Pydantic models
class ReservationCreatedResponse(BaseResponse):
    isPendingApproval: bool

class ReservationUpdatedResponse(BaseResponse):
    isPendingApproval: bool

class ReservationApprovedResponse(BaseResponse):
    pass

class ReservationCheckedInResponse(BaseResponse):
    pass

class ReservationCheckedOutResponse(BaseResponse):
    pass

# Define the ExampleReservationCreatedResponse Pydantic model
class ExampleReservationCreatedResponse(ReservationCreatedResponse):
    pass

# Sample usage of ExampleReservationCreatedResponse model
example_response = ExampleReservationCreatedResponse(
    message="The reservation was created",
    referenceNumber="referenceNumber",
    isPendingApproval=True,
)

# Define the endpoint to get the example reservation created response
@app.get("/reservation_created/")
def reservation_created():
    return example_response

# Define the endpoint to get the example reservation updated response
@app.get("/reservation_updated/")
def reservation_updated():
    return example_response

# Define the endpoint to get the example reservation approved response
@app.get("/reservation_approved/")
def reservation_approved():
    return example_response

# Define the endpoint to get the example reservation checked in response
@app.get("/reservation_checked_in/")
def reservation_checked_in():
    return example_response

# Define the endpoint to get the example reservation checked out response
@app.get("/reservation_checked_out/")
def reservation_checked_out():
    return example_response



