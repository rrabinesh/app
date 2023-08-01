# <?php

# class ScheduleItemResponse extends RestResponse
# {
#     public $daysVisible;
#     public $id;
#     public $isDefault;
#     public $name;
#     public $timezone;
#     public $weekdayStart;
#     public $availabilityBegin;
#     public $availabilityEnd;
#     public $maxResourcesPerReservation;
#     public $totalConcurrentReservationsAllowed;

#     public function __construct(IRestServer $server, Schedule $schedule)
#     {
#         $this->daysVisible = $schedule->GetDaysVisible();
#         $this->id = $schedule->GetId();
#         $this->isDefault = $schedule->GetIsDefault();
#         $this->name = $schedule->GetName();
#         $this->timezone = $schedule->GetTimezone();
#         $this->weekdayStart = $schedule->GetWeekdayStart();
#         $this->availabilityBegin = $schedule->GetAvailabilityBegin()->ToIso();
#         $this->availabilityEnd = $schedule->GetAvailabilityBegin()->ToIso();
#         $this->maxResourcesPerReservation = $schedule->GetMaxResourcesPerReservation();
#         $this->totalConcurrentReservationsAllowed = $schedule->GetTotalConcurrentReservations();

#         $this->AddService($server, WebServices::GetSchedule, [WebServiceParams::ScheduleId => $schedule->GetId()]);
#     }

#     public static function Example()
#     {
#         return new ExampleScheduleItemResponse();
#     }
# }

# class ExampleScheduleItemResponse extends ScheduleItemResponse
# {
#     public function __construct()
#     {
#         $this->daysVisible = 5;
#         $this->id = 123;
#         $this->isDefault = true;
#         $this->name = 'schedule name';
#         $this->timezone = 'timezone_name';
#         $this->weekdayStart = 0;
#         $this->availabilityBegin = Date::Now()->ToIso();
#         $this->availabilityEnd = Date::Now()->AddDays(20)->ToIso();
#         $this->maxResourcesPerReservation = 10;
#         $this->totalConcurrentReservationsAllowed = 0;
#     }
# }


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the Pydantic model for ScheduleItemResponse
class ScheduleItemResponse(BaseModel):
    daysVisible: int
    id: int
    isDefault: bool
    name: str
    timezone: str
    weekdayStart: int
    availabilityBegin: str
    availabilityEnd: str
    maxResourcesPerReservation: int
    totalConcurrentReservationsAllowed: int

# Define the ExampleScheduleItemResponse Pydantic model
class ExampleScheduleItemResponse(ScheduleItemResponse):
    daysVisible: int = 5
    id: int = 123
    isDefault: bool = True
    name: str = 'schedule name'
    timezone: str = 'timezone_name'
    weekdayStart: int = 0
    availabilityBegin: str = '2023-07-27T00:00:00Z'  # Replace this with the appropriate ISO format date
    availabilityEnd: str = '2023-08-16T00:00:00Z'  # Replace this with the appropriate ISO format date
    maxResourcesPerReservation: int = 10
    totalConcurrentReservationsAllowed: int = 0

# Define the endpoint to get the example schedule item response
@app.get("/schedule/")
def schedule():
    return ExampleScheduleItemResponse()



