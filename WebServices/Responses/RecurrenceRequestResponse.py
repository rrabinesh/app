# <?php

# require_once(ROOT_DIR . 'lib/WebService/namespace.php');

# class RecurrenceRequestResponse
# {
#     public $type;
#     public $interval;
#     public $monthlyType;
#     public $weekdays;
#     public $repeatTerminationDate;

#     public function __construct($type, $interval, $monthlyType, $weekdays, $repeatTerminationDate)
#     {
#         $this->type = $type;
#         $this->interval = $interval;
#         $this->monthlyType = $monthlyType;
#         $this->weekdays = $weekdays;
#         $this->repeatTerminationDate = $repeatTerminationDate;
#     }

#     public static function Example()
#     {
#         return new ExampleRecurrenceRequestResponse();
#     }

#     /**
#      * @return RecurrenceRequestResponse
#      */
#     public static function null()
#     {
#         return new RecurrenceRequestResponse(RepeatType::None, null, null, [], null);
#     }
# }

# class ExampleRecurrenceRequestResponse extends RecurrenceRequestResponse
# {
#     public function __construct()
#     {
#         $this->interval = 3;
#         $this->monthlyType = RepeatMonthlyType::DayOfMonth . '|' . RepeatMonthlyType::DayOfWeek . '|null';
#         $this->type = RepeatType::Daily . '|' . RepeatType::Monthly . '|' . RepeatType::None . '|' . RepeatType::Weekly . '|' . RepeatType::Yearly;
#         $this->weekdays = [0, 1, 2, 3, 4, 5, 6];
#         $this->repeatTerminationDate = Date::Now()->ToIso();
#     }
# }


from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

# Define the RepeatType Enum
class RepeatType(str, Enum):
    Daily = "Daily"
    Monthly = "Monthly"
    None_ = "None"
    Weekly = "Weekly"
    Yearly = "Yearly"

# Define the RepeatMonthlyType Enum
class RepeatMonthlyType(str, Enum):
    DayOfMonth = "DayOfMonth"
    DayOfWeek = "DayOfWeek"

# Define the RecurrenceRequestResponse Pydantic model
class RecurrenceRequestResponse(BaseModel):
    type: RepeatType
    interval: int
    monthlyType: RepeatMonthlyType
    weekdays: list[int]
    repeatTerminationDate: str

# Define the ExampleRecurrenceRequestResponse Pydantic model
class ExampleRecurrenceRequestResponse(RecurrenceRequestResponse):
    pass

# Sample usage of ExampleRecurrenceRequestResponse model
example_response = ExampleRecurrenceRequestResponse(
    interval=3,
    monthlyType=f"{RepeatMonthlyType.DayOfMonth}|{RepeatMonthlyType.DayOfWeek}|null",
    type=f"{RepeatType.Daily}|{RepeatType.Monthly}|{RepeatType.None_}|{RepeatType.Weekly}|{RepeatType.Yearly}",
    weekdays=[0, 1, 2, 3, 4, 5, 6],
    repeatTerminationDate="2023-07-27T12:00:00Z",
)

# Define the endpoint to get recurrence request response
@app.get("/recurrence/")
def recurrence():
    return example_response



