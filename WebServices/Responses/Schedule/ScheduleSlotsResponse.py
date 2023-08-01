# <?php

# class ScheduleSlotResponse extends RestResponse
# {
#     /**
#      * @var string
#      */
#     public $date;

#     /**
#      * @var ScheduleSlotResourceResponse[]
#      */
#     public $resources;

#     public function __construct(IRestServer $server, Date $date)
#     {
#         $this->date = $date->ToIso();
#     }

#     public function AddResource(ScheduleSlotResourceResponse $scheduleResource)
#     {
#         $this->resources[] = $scheduleResource;
#     }
# }

# class ScheduleSlotDetailsResponse extends RestResponse
# {
#     /**
#      * @var int
#      */
#     public $slotSpan;

#     /**
#      * @var bool
#      */
#     public $isReserved;

#     /**
#      * @var string
#      */
#     public $label;

#     /**
#      * @var bool
#      */
#     public $isReservable;

#     /**
#      * @var string
#      */
#     public $color;

#     /**
#      * @var string
#      */
#     public $startDateTime;

#     /**
#      * @var string
#      */
#     public $endDateTime;

#     /**
#      * @var ReservationItemResponse|null
#      */
#     public $reservation;

#     public function __construct(IRestServer $server, IReservationSlot $slot, IPrivacyFilter $privacyFilter)
#     {
#         $user = $server->GetSession();

#         $this->slotSpan = $slot->PeriodSpan();
#         $this->isReserved = $slot->IsReserved();
#         $this->label = $slot->Label();
#         $this->isReservable = $slot->IsReservable();
#         $this->color = $slot->Color();
#         $this->startDateTime = $slot->BeginDate()->ToIso();
#         $this->endDateTime = $slot->EndDate()->ToIso();

#         if ($slot->IsReserved()) {
#             /** @var ReservationSlot $slot */
#             $reservation = $slot->Reservation();
#             $showUser = $privacyFilter->CanViewUser($user, null, $reservation->UserId);
#             $showDetails = $privacyFilter->CanViewDetails($user, null, $reservation->UserId);
#             $this->reservation = new ReservationItemResponse($reservation, $server, $showUser, $showDetails);
#         }
#     }
# }

# class ScheduleSlotResourceResponse extends RestResponse
# {
#     public $slots = [];

#     /**
#      * @var IRestServer
#      */
#     private $server;

#     /**
#      * @var IPrivacyFilter
#      */
#     private $privacyFilter;
#     /**
#      * @var int
#      */
#     public $resourceId;
#     /**
#      * @var string
#      */
#     public $resourceName;

#     public function __construct(IRestServer $server, ResourceDto $resource, IPrivacyFilter $privacyFilter)
#     {
#         $this->server = $server;
#         $this->privacyFilter = $privacyFilter;

#         $this->AddService($server, WebServices::GetResource, [WebServiceParams::ResourceId => $resource->GetId()]);

#         $this->resourceId = $resource->GetId();
#         $this->resourceName = $resource->GetName();
#     }

#     public function AddSlot(IReservationSlot $slot)
#     {
#         $this->slots[] = new ScheduleSlotDetailsResponse($this->server, $slot, $this->privacyFilter);
#     }
# }

# class ScheduleSlotsResponse extends RestResponse
# {
#     public $dates = [];
#     /**
#      * @var int
#      */
#     private $scheduleId;

#     /**
#      * @param IRestServer $server
#      * @param int $scheduleId
#      * @param IDailyLayout $dailyLayout
#      * @param DateRange $dates
#      * @param ResourceDto[] $resources
#      * @param IPrivacyFilter $privacyFilter
#      */
#     public function __construct(IRestServer $server, $scheduleId, IDailyLayout $dailyLayout, DateRange $dates, $resources, IPrivacyFilter $privacyFilter)
#     {
#         $this->scheduleId = $scheduleId;
#         $this->AddService($server, WebServices::GetSchedule, [WebServiceParams::ScheduleId => $scheduleId]);

#         foreach ($dates->Dates() as $date) {
#             $scheduleDate = new ScheduleSlotResponse($server, $date);

#             foreach ($resources as $resource) {
#                 $scheduleResource = new ScheduleSlotResourceResponse($server, $resource, $privacyFilter);
#                 $slots = $dailyLayout->GetLayout($date, $resource->GetId());
#                 foreach ($slots as $slot) {
#                     $scheduleResource->AddSlot($slot);
#                 }

#                 $scheduleDate->AddResource($scheduleResource);
#             }

#             $this->dates[] = $scheduleDate;
#         }
#     }

#     public static function Example()
#     {
#         return new ExampleScheduleSlotsResponse();
#     }
# }

# class ExampleScheduleSlotsResponse extends ScheduleSlotsResponse
# {
#     public function __construct()
#     {
#         $this->dates = [new ExampleScheduleSlotResponse()];
#     }
# }

# class ExampleScheduleSlotResponse extends ScheduleSlotResponse
# {
#     public function __construct()
#     {
#         $this->date = Date::Now()->ToIso();
#         $this->resources = [new ExampleScheduleSlotResourceResponse()];
#     }
# }

# class ExampleScheduleSlotResourceResponse extends ScheduleSlotResourceResponse
# {
#     public function __construct()
#     {
#         $this->resourceId = 1;
#         $this->resourceName = 'resourcename';
#         $this->slots = [new ExampleScheduleSlotDetailsResponse()];
#     }
# }

# class ExampleScheduleSlotDetailsResponse extends ScheduleSlotDetailsResponse
# {
#     public function __construct()
#     {
#         $this->color = '#ffffff';
#         $this->endDateTime = Date::Now()->ToIso();
#         $this->isReservable = false;
#         $this->isReserved = true;
#         $this->label = 'username';
#         $this->reservation = ReservationItemResponse::Example();
#         $this->slotSpan = 4;
#         $this->startDateTime = Date::Now()->ToIso();
#     }
# }


from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

app = FastAPI()

class ReservationItemResponse(BaseModel):
    # fields
    
    @staticmethod
    def example():
        return ReservationItemResponse(...)
        
class ScheduleSlotDetailsResponse(BaseModel):
    slotSpan: int 
    isReserved: bool
    label: str
    isReservable: bool
    color: str
    startDateTime: datetime
    endDateTime: datetime
    reservation: Optional[ReservationItemResponse]

    @staticmethod
    def example():
        return ScheduleSlotDetailsResponse(
            slotSpan=4,
            isReserved=True,
            label='username',
            isReservable=False,
            color='#ffffff',
            startDateTime=datetime.now(),
            endDateTime=datetime.now(),
            reservation=ReservationItemResponse.example(),
        )
        
class ScheduleSlotResourceResponse(BaseModel):
    slots: List[ScheduleSlotDetailsResponse]
    resourceId: int
    resourceName: str
    
    @staticmethod
    def example():
        return ScheduleSlotResourceResponse(
            resourceId=1,
            resourceName='resource',
            slots=[ScheduleSlotDetailsResponse.example()]
        )
        
class ScheduleSlotResponse(BaseModel):
    date: datetime
    resources: List[ScheduleSlotResourceResponse]
    
    @staticmethod
    def example():
        return ScheduleSlotResponse(
            date=datetime.now(),
            resources=[ScheduleSlotResourceResponse.example()]
        )

class ScheduleSlotsResponse(BaseModel):
    dates: List[ScheduleSlotResponse]
    
    @staticmethod
    def example():
        return ScheduleSlotsResponse(
            dates=[ScheduleSlotResponse.example()]
        )

@app.get("/slots")
async def get_slots():
    return ScheduleSlotsResponse.example()
