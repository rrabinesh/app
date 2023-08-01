# <?php

# require_once(ROOT_DIR . 'lib/WebService/namespace.php');

# class ReminderRequestResponse
# {
#     public $value;
#     public $interval;

#     public function __construct($value, $interval)
#     {
#         $this->value = $value;
#         $this->interval = $interval;
#     }

#     public static function Example()
#     {
#         return new ReminderRequestResponse(15, ReservationReminderInterval::Hours . ' or ' . ReservationReminderInterval::Minutes . ' or ' . ReservationReminderInterval::Days);
#     }
# }


from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

# Define the ReservationReminderInterval Enum
class ReservationReminderInterval(str, Enum):
    Hours = "Hours"
    Minutes = "Minutes"
    Days = "Days"

# Define the ReminderRequestResponse Pydantic model
class ReminderRequestResponse(BaseModel):
    value: int
    interval: str

# Define the ExampleReminderRequestResponse Pydantic model
class ExampleReminderRequestResponse(ReminderRequestResponse):
    pass

# Sample usage of ExampleReminderRequestResponse model
example_response = ExampleReminderRequestResponse(
    value=15,
    interval=f"{ReservationReminderInterval.Hours} or {ReservationReminderInterval.Minutes} or {ReservationReminderInterval.Days}",
)

# Define the endpoint to get reminder request response
@app.get("/reminder/")
def reminder():
    return example_response



