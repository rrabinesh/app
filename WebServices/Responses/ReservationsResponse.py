# <?php

# require_once(ROOT_DIR . 'lib/WebService/namespace.php');
# require_once(ROOT_DIR . 'WebServices/Responses/ReservationItemResponse.php');

# class ReservationsResponse extends RestResponse
# {
#     /**
#      * @var array|ReservationItemResponse[]
#      */
#     public $reservations = [];
#     public $startDateTime;
#     public $endDateTime;

#     /**
#      * @param IRestServer $server
#      * @param array|ReservationItemView[] $reservations
#      * @param IPrivacyFilter $privacyFilter
#      * @param Date $minDate
#      * @param Date $maxDate
#      */
#     public function __construct(IRestServer $server, $reservations, IPrivacyFilter $privacyFilter, Date $minDate, Date $maxDate)
#     {
#         $user = $server->GetSession();
#         foreach ($reservations as $reservation) {
#             $showUser = $privacyFilter->CanViewUser($user, null, $reservation->UserId);
#             $showDetails = $privacyFilter->CanViewDetails($user, null, $reservation->UserId);

#             $this->reservations[] = new ReservationItemResponse($reservation, $server, $showUser, $showDetails);
#             $this->startDateTime = $minDate->ToIso();
#             $this->endDateTime = $maxDate->ToIso();
#         }
#     }

#     public static function Example()
#     {
#         return new ExampleReservationsResponse();
#     }
# }

# class ExampleReservationsResponse extends ReservationsResponse
# {
#     public function __construct()
#     {
#         $this->reservations = [ReservationItemResponse::Example()];
#     }
# }


from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI()

# Define the Pydantic model for ReservationItemResponse
class ReservationItemResponse(BaseModel):
    referenceNumber: str
    startDate: datetime
    endDate: datetime
    title: str
    description: str
    requiresApproval: bool
    isRecurring: bool
    scheduleId: int
    userId: int
    resourceId: int
    duration: str
    bufferTime: str
    bufferedStartDate: datetime
    bufferedEndDate: datetime
    participants: List[str]
    invitees: List[str]
    startReminder: int
    endReminder: int
    color: str
    textColor: str
    checkInDate: datetime
    checkOutDate: datetime
    originalEndDate: datetime
    isCheckInEnabled: bool
    autoReleaseMinutes: int
    resourceStatusId: int
    creditsConsumed: int

# Define the Pydantic model for ReservationsResponse
class ReservationsResponse(BaseModel):
    reservations: List[ReservationItemResponse]
    startDateTime: datetime
    endDateTime: datetime

# Define the ExampleReservationsResponse Pydantic model
class ExampleReservationsResponse(ReservationsResponse):
    pass


