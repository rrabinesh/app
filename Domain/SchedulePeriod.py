# <?php

# class PeriodTypes
# {
#     public const RESERVABLE = 1;
#     public const NONRESERVABLE = 2;
# }

# class SchedulePeriod
# {
#     /**
#      * @var Date
#      */
#     protected $_begin;

#     /**
#      * @var Date
#      */
#     protected $_end;

#     protected $_label;

#     protected $_id;

#     public function __construct(Date $begin, Date $end, $label = null)
#     {
#         $this->_begin = $begin;
#         $this->_end = $end;
#         $this->_label = $label;
#     }

#     /**
#      * @return Time beginning time for this period
#      */
#     public function Begin()
#     {
#         return $this->_begin->GetTime();
#     }

#     /**
#      * @return Time ending time for this period
#      */
#     public function End()
#     {
#         return $this->_end->GetTime();
#     }

#     /**
#      * @return Date
#      */
#     public function BeginDate()
#     {
#         return $this->_begin;
#     }

#     /**
#      * @return Date
#      */
#     public function EndDate()
#     {
#         return $this->_end;
#     }

#     /**
#      * @param Date $dateOverride
#      * @return string
#      */
#     public function Label($dateOverride = null)
#     {
#         if (empty($this->_label)) {
#             $format = Resources::GetInstance()->GetDateFormat('period_time');

#             if (isset($dateOverride) && !$this->_begin->DateEquals($dateOverride)) {
#                 return $dateOverride->Format($format);
#             }
#             return $this->_begin->Format($format);
#         }
#         return $this->_label;
#     }

#     /**
#      * @return string
#      */
#     public function LabelEnd()
#     {
#         if (empty($this->_label)) {
#             $format = Resources::GetInstance()->GetDateFormat('period_time');

#             return $this->_end->Format($format);
#         }
#         return '(' . $this->_label . ')';
#     }

#     /**
#      * @return bool
#      */
#     public function IsReservable()
#     {
#         return true;
#     }

#     public function IsLabelled()
#     {
#         return !empty($this->_label);
#     }

#     public function ToUtc()
#     {
#         return new SchedulePeriod($this->_begin->ToUtc(), $this->_end->ToUtc(), $this->_label);
#     }

#     public function ToTimezone($timezone)
#     {
#         return new SchedulePeriod($this->_begin->ToTimezone($timezone), $this->_end->ToTimezone($timezone), $this->_label);
#     }

#     public function __toString()
#     {
#         return sprintf("Begin: %s End: %s Label: %s", $this->_begin, $this->_end, $this->Label());
#     }

#     /**
#      * Compares the starting datetimes
#      */
#     public function Compare(SchedulePeriod $other)
#     {
#         return $this->_begin->Compare($other->_begin);
#     }

#     public function BeginsBefore(Date $date)
#     {
#         return $this->_begin->DateCompare($date) < 0;
#     }

#     public function IsPastDate()
#     {
#         return ReservationPastTimeConstraint::IsPast($this->BeginDate(), $this->EndDate());
#     }

#     /**
#      * @return string
#      */
#     public function Id()
#     {
#         if (empty($this->_id)) {
#             $this->_id = uniqid($this->_begin->Timestamp());
#         }
#         return $this->_id;
#     }

#     public function Span()
#     {
#         return 1;
#     }
# }

# class NonSchedulePeriod extends SchedulePeriod
# {
#     public function IsReservable()
#     {
#         return false;
#     }

#     public function ToUtc()
#     {
#         return new NonSchedulePeriod($this->_begin->ToUtc(), $this->_end->ToUtc(), $this->_label);
#     }

#     public function ToTimezone($timezone)
#     {
#         return new NonSchedulePeriod($this->_begin->ToTimezone($timezone), $this->_end->ToTimezone($timezone), $this->_label);
#     }
# }


from typing import List, Optional
from pydantic import BaseModel


class Time(BaseModel):
    Hour: int
    Minute: int
    Timezone: str


class PeakTimes(BaseModel):
    allDay: bool = False
    beginTime: Optional[Time] = None
    endTime: Optional[Time] = None
    everyDay: bool = False
    weekdays: List[int] = []
    allYear: bool = False
    beginDay: int = 0
    beginMonth: int = 0
    endDay: int = 0
    endMonth: int = 0


class LayoutPeriod(BaseModel):
    Start: Time
    End: Time
    PeriodType: str
    Label: Optional[str] = None

    def PeriodTypeClass(self):
        if self.PeriodType == "RESERVABLE":
            return "SchedulePeriod"
        return "NonSchedulePeriod"

    def IsReservable(self):
        return self.PeriodType == "RESERVABLE"

    def IsLabelled(self):
        return bool(self.Label)

    def Timezone(self):
        return self.Start.Timezone


class ScheduleLayout(BaseModel):
    periods: List[LayoutPeriod] = []


class LayoutParser:
    def __init__(self, timezone):
        self.layout = ScheduleLayout()
        self.timezone = timezone

    def add_period(self, start, end, label, day_of_week=None):
        period = LayoutPeriod(Start=start, End=end, Label=label)
        self.layout.periods.append(period)

    def add_reservable(self, reservable_slots, day_of_week=None):
        self.parse_slots(reservable_slots, day_of_week, self.add_period)

    def add_blocked(self, blocked_slots, day_of_week=None):
        self.parse_slots(blocked_slots, day_of_week, self.add_period)

    def get_layout(self):
        return self.layout

    def parse_slots(self, all_slots, day_of_week, callback):
        trimmed_slots = all_slots.strip()
        lines = trimmed_slots.splitlines()
        for slot_line in lines:
            parts = slot_line.strip().split(maxsplit=1)
            times = parts[0].split('-')
            start = times[0].strip()
            end = times[1].strip()
            label = parts[1].strip() if len(parts) > 1 else None
            callback(Time(Hour=int(start[:2]), Minute=int(start[3:5]), Timezone=self.timezone),
                     Time(Hour=int(end[:2]), Minute=int(end[3:5]), Timezone=self.timezone),
                     label, day_of_week)


# FastAPI code to interact with the classes
from fastapi import FastAPI

app = FastAPI()

# Example usage
@app.post("/create_layout/")
async def create_layout():
    layout_parser = LayoutParser(timezone="UTC")
    layout_parser.add_reservable("09:00 - 12:00\n13:00 - 17:00", day_of_week=1)
    layout_parser.add_blocked("12:00 - 13:00\n17:00 - 18:00", day_of_week=1)
    layout = layout_parser.get_layout()
    return layout



