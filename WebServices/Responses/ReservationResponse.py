# <?php

# require_once(ROOT_DIR . 'lib/WebService/namespace.php');
# require_once(ROOT_DIR . 'WebServices/Responses/RecurrenceRequestResponse.php');
# require_once(ROOT_DIR . 'WebServices/Responses/ResourceItemResponse.php');
# require_once(ROOT_DIR . 'WebServices/Responses/ReservationAccessoryResponse.php');
# require_once(ROOT_DIR . 'WebServices/Responses/CustomAttributes/CustomAttributeResponse.php');
# require_once(ROOT_DIR . 'WebServices/Responses/AttachmentResponse.php');
# require_once(ROOT_DIR . 'WebServices/Responses/ReservationUserResponse.php');
# require_once(ROOT_DIR . 'WebServices/Responses/ReminderRequestResponse.php');

# class ReservationResponse extends RestResponse
# {
#     public $referenceNumber;
#     public $startDate;
#     public $endDate;
#     public $title;
#     public $description;
#     public $requiresApproval;
#     public $isRecurring;
#     public $scheduleId;
#     public $resourceId;
#     /**
#      * @var ReservationUserResponse
#      */
#     public $owner;
#     /**
#      * @var array|ReservationUserResponse[]
#      */
#     public $participants = [];
#     /**
#      * @var array|ReservationUserResponse[]
#      */
#     public $invitees = [];
#     /**
#      * @var array|CustomAttributeResponse[]
#      */
#     public $customAttributes = [];
#     /**
#      * @var RecurrenceRequestResponse
#      */
#     public $recurrenceRule;
#     /**
#      * @var array|AttachmentResponse[]
#      */
#     public $attachments = [];
#     /**
#      * @var array|ResourceItemResponse[]
#      */
#     public $resources = [];
#     /**
#      * @var array|ReservationAccessoryResponse[]
#      */
#     public $accessories = [];
#     /**
#      * @var ReminderRequestResponse
#      */
#     public $startReminder;
#     /**
#      * @var ReminderRequestResponse
#      */
#     public $endReminder;
#     /**
#      * @var bool
#      */
#     public $allowParticipation;

#     public $checkInDate;
#     public $checkOutDate;
#     public $originalEndDate;
#     public $isCheckInAvailable;
#     public $isCheckoutAvailable;
#     public $autoReleaseMinutes;

#     /**
#      * @param IRestServer $server
#      * @param ReservationView $reservation
#      * @param IPrivacyFilter $privacyFilter
#      * @param array|CustomAttribute[] $attributes
#      */
#     public function __construct(
#         IRestServer $server,
#         ReservationView $reservation,
#         IPrivacyFilter $privacyFilter,
#         $attributes = []
#     ) {
#         $this->owner = ReservationUserResponse::Masked();

#         $canViewUser = $privacyFilter->CanViewUser($server->GetSession(), $reservation);
#         $canViewDetails = $privacyFilter->CanViewDetails($server->GetSession(), $reservation);

#         $this->referenceNumber = $reservation->ReferenceNumber;
#         $this->startDate = $reservation->StartDate->ToTimezone($server->GetSession()->Timezone)->ToIso();
#         $this->endDate = $reservation->EndDate->ToTimezone($server->GetSession()->Timezone)->ToIso();
#         $this->requiresApproval = $reservation->RequiresApproval();
#         $this->isRecurring = $reservation->IsRecurring();
#         $repeatTerminationDate = $reservation->RepeatTerminationDate != null ? $reservation->RepeatTerminationDate->ToIso() : null;
#         $this->recurrenceRule = new RecurrenceRequestResponse($reservation->RepeatType, $reservation->RepeatInterval, $reservation->RepeatMonthlyType, $reservation->RepeatWeekdays, $repeatTerminationDate);
#         $this->resourceId = $reservation->ResourceId;
#         $this->scheduleId = $reservation->ScheduleId;
#         $this->AddService($server, WebServices::GetSchedule, [WebServiceParams::ScheduleId => $reservation->ScheduleId]);

#         foreach ($reservation->Resources as $resource) {
#             $this->resources[$resource->Id()] = new ResourceItemResponse($server, $resource->Id(), $resource->GetName());
#         }

#         foreach ($reservation->Accessories as $accessory) {
#             $this->accessories[] = new ReservationAccessoryResponse($server, $accessory->AccessoryId, $accessory->Name, $accessory->QuantityReserved, $accessory->QuantityAvailable);
#         }

#         if ($canViewDetails) {
#             $this->title = $reservation->Title;
#             $this->description = $reservation->Description;
#             foreach ($attributes as $attribute) {
#                 $this->customAttributes[] = new CustomAttributeResponse(
#                     $server,
#                     $attribute->Id(),
#                     $attribute->Label(),
#                     $reservation->GetAttributeValue($attribute->Id())
#                 );
#             }
#             foreach ($reservation->Attachments as $attachment) {
#                 $this->attachments[] = new AttachmentResponse($server, $attachment->FileId(), $attachment->FileName(), $reservation->ReferenceNumber);
#             }
#         }

#         if ($canViewUser) {
#             $this->owner = new ReservationUserResponse(
#                 $server,
#                 $reservation->OwnerId,
#                 $reservation->OwnerFirstName,
#                 $reservation->OwnerLastName,
#                 $reservation->OwnerEmailAddress
#             );
#             foreach ($reservation->Participants as $participant) {
#                 $this->participants[] = new ReservationUserResponse(
#                     $server,
#                     $participant->UserId,
#                     $participant->FirstName,
#                     $participant->LastName,
#                     $participant->Email
#                 );
#             }
#             foreach ($reservation->Invitees as $invitee) {
#                 $this->invitees[] = new ReservationUserResponse(
#                     $server,
#                     $invitee->UserId,
#                     $invitee->FirstName,
#                     $invitee->LastName,
#                     $invitee->Email
#                 );
#             }
#         }

#         if ($reservation->StartReminder != null) {
#             $this->startReminder = new ReminderRequestResponse($reservation->StartReminder->GetValue(), $reservation->StartReminder->GetInterval());
#         }
#         if ($reservation->EndReminder != null) {
#             $this->endReminder = new ReminderRequestResponse($reservation->EndReminder->GetValue(), $reservation->EndReminder->GetInterval());
#         }

#         if ($reservation->RequiresApproval()) {
#             $this->AddService($server, WebServices::ApproveReservation, [WebServiceParams::ReferenceNumber => $reservation->ReferenceNumber]);
#         }

#         $this->allowParticipation = $reservation->AllowParticipation;


#         $this->checkInDate = $reservation->CheckinDate->ToIso();
#         $this->checkOutDate = $reservation->CheckoutDate->ToIso();
#         $this->originalEndDate = $reservation->OriginalEndDate->ToIso();
#         $this->isCheckInAvailable = $reservation->IsCheckinAvailable();
#         $this->isCheckoutAvailable = $reservation->IsCheckoutAvailable();
#         $this->autoReleaseMinutes = $reservation->AutoReleaseMinutes();
#     }


#     /**
#      * @return ReservationResponse
#      */
#     public static function Example()
#     {
#         return new ExampleReservationResponse();
#     }
# }

# class ExampleReservationResponse extends ReservationResponse
# {
#     public function __construct()
#     {
#         $this->accessories = [ReservationAccessoryResponse::Example()];
#         $this->attachments = [AttachmentResponse::Example()];
#         $this->customAttributes = [CustomAttributeResponse::Example()];
#         $this->description = 'reservation description';
#         $this->endDate = Date::Now()->ToIso();
#         $this->invitees = [ReservationUserResponse::Example()];
#         $this->isRecurring = true;
#         $this->owner = ReservationUserResponse::Example();
#         $this->participants = [ReservationUserResponse::Example()];
#         $this->recurrenceRule = RecurrenceRequestResponse::Example();
#         $this->referenceNumber = 'refnum';
#         $this->requiresApproval = true;
#         $this->resourceId = 123;
#         $this->resources = [ResourceItemResponse::Example()];
#         $this->scheduleId = 123;
#         $this->startDate = Date::Now()->ToIso();
#         $this->title = 'reservation title';
#         $this->startReminder = ReminderRequestResponse::Example();
#         $this->endReminder = ReminderRequestResponse::Example();
#     }
# }

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

app = FastAPI()

# Define the Pydantic model for ReservationUserResponse
class ReservationUserResponse(BaseModel):
    userId: int
    firstName: str
    lastName: str
    emailAddress: str

# Define the Pydantic model for RecurrenceRequestResponse
class RecurrenceRequestResponse(BaseModel):
    type: str
    interval: int
    monthlyType: str
    weekdays: List[int]
    repeatTerminationDate: Optional[datetime]

# Define the Pydantic model for ResourceItemResponse
class ResourceItemResponse(BaseModel):
    id: int
    name: str

# Define the Pydantic model for ReservationAccessoryResponse
class ReservationAccessoryResponse(BaseModel):
    id: int
    name: str
    quantityReserved: int
    quantityAvailable: int

# Define the Pydantic model for CustomAttributeResponse
class CustomAttributeResponse(BaseModel):
    id: int
    label: str
    value: str

# Define the Pydantic model for AttachmentResponse
class AttachmentResponse(BaseModel):
    url: str

# Define the Pydantic model for ReminderRequestResponse
class ReminderRequestResponse(BaseModel):
    value: int
    interval: str

# Define the Pydantic model for ReservationResponse
class ReservationResponse(BaseModel):
    referenceNumber: str
    startDate: datetime
    endDate: datetime
    title: Optional[str]
    description: Optional[str]
    requiresApproval: bool
    isRecurring: bool
    scheduleId: int
    resourceId: int
    owner: ReservationUserResponse
    participants: List[ReservationUserResponse]
    invitees: List[ReservationUserResponse]
    customAttributes: List[CustomAttributeResponse]
    recurrenceRule: RecurrenceRequestResponse
    attachments: List[AttachmentResponse]
    resources: List[ResourceItemResponse]
    accessories: List[ReservationAccessoryResponse]
    startReminder: Optional[ReminderRequestResponse]
    endReminder: Optional[ReminderRequestResponse]
    allowParticipation: bool
    checkInDate: datetime
    checkOutDate: datetime
    originalEndDate: datetime
    isCheckInAvailable: bool
    isCheckoutAvailable: bool
    autoReleaseMinutes: int

# Define the ExampleReservationResponse Pydantic model
class ExampleReservationResponse(ReservationResponse):
    pass

