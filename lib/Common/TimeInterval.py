# <?php

# class TimeInterval
# {
#     /**
#      * @var DateDiff
#      */
#     private $interval = null;

#     /**
#      * @param int $seconds
#      */
#     public function __construct($seconds)
#     {
#         $this->interval = null;

#         if (!empty($seconds)) {
#             $this->interval = new DateDiff($seconds);
#         }
#     }

#     /**
#      * @static
#      * @param string|int $interval string interval in format: #d#h#m ie: 22d4h12m or total seconds
#      * @return TimeInterval
#      */
#     public static function Parse($interval)
#     {
#         if (is_a($interval, 'TimeInterval')) {
#             return $interval;
#         }

#         if (empty($interval)) {
#             return new TimeInterval(0);
#         }

#         if (!is_numeric($interval)) {
#             $seconds = DateDiff::FromTimeString($interval)->TotalSeconds();
#         } else {
#             $seconds = $interval;
#         }

#         return new TimeInterval($seconds);
#     }

#     /**
#      * @param $minutes
#      * @return TimeInterval
#      */
#     public static function FromMinutes($minutes)
#     {
#         return TimeInterval::Parse($minutes * 60);
#     }

#     /**
#      * @param $hours
#      * @return TimeInterval
#      */
#     public static function FromHours($hours)
#     {
#         return TimeInterval::Parse($hours * 60 * 60);
#     }

#     /**
#      * @param $days
#      * @return TimeInterval
#      */
#     public static function FromDays($days)
#     {
#         return TimeInterval::Parse($days * 60 * 60 * 24);
#     }

#     /**
#      * @return TimeInterval
#      */
#     public static function None()
#     {
#         return new TimeInterval(0);
#     }

#     /**
#      * @return int
#      */
#     public function Days()
#     {
#         return $this->Interval()->Days();
#     }

#     /**
#      * @return int
#      */
#     public function Hours()
#     {
#         return $this->Interval()->Hours();
#     }

#     /**
#      * @return int
#      */
#     public function Minutes()
#     {
#         return $this->Interval()->Minutes();
#     }

#     /**
#      * @return DateDiff
#      */
#     public function Interval()
#     {
#         return $this->Diff();
#     }

#     /**
#      * @return DateDiff
#      */
#     public function Diff()
#     {
#         if ($this->interval != null) {
#             return $this->interval;
#         }

#         return DateDiff::Null();
#     }

#     /**
#      * @return null|int
#      */
#     public function ToDatabase()
#     {
#         if ($this->interval != null && !$this->interval->IsNull()) {
#             return $this->interval->TotalSeconds();
#         }

#         return null;
#     }

#     /**
#      * @return int
#      */
#     public function TotalSeconds()
#     {
#         if ($this->interval != null) {
#             return $this->interval->TotalSeconds();
#         }
#         return 0;
#     }

#     /**
#      * @return string
#      */
#     public function __toString()
#     {
#         if ($this->interval != null) {
#             return $this->interval->__toString();
#         }

#         return '';
#     }

#     /**
#      * @return string
#      */
#     public function ToShortString()
#     {
#         if ($this->interval != null) {
#             return $this->interval->ToString(true);
#         }

#         return '';
#     }

#     /**
#      * @param bool $includeTotalHours
#      * @return string
#      */
#     public function ToString($includeTotalHours)
#     {
#         if ($includeTotalHours) {
#             return $this->__toString() . ' (' . $this->TotalSeconds() / 3600 . 'h)';
#         }

#         return $this->__toString();
#     }
# }

from fastapi import FastAPI

app = FastAPI()

class DateDiff:
    # Placeholder DateDiff class (implement your own logic for handling date differences)
    pass
def create_date_diff(seconds):
    # Placeholder function for creating a DateDiff object with given seconds
    return DateDiff(seconds)

class TimeInterval:
    def __init__(self, seconds):
        self._interval = None

        if seconds:
            self._interval = create_date_diff(seconds)

    @classmethod
    def parse(cls, interval):
        if isinstance(interval, TimeInterval):
            return interval

        if not interval:
            return TimeInterval(0)

        if not interval.isnumeric():
            seconds = DateDiff.from_time_string(interval).total_seconds()
        else:
            seconds = int(interval)

        return TimeInterval(seconds)

    @classmethod
    def from_minutes(cls, minutes):
        return TimeInterval.parse(minutes * 60)

    @classmethod
    def from_hours(cls, hours):
        return TimeInterval.parse(hours * 60 * 60)

    @classmethod
    def from_days(cls, days):
        return TimeInterval.parse(days * 60 * 60 * 24)

    @classmethod
    def none(cls):
        return TimeInterval(0)

    def days(self):
        return self.interval().days()

    def hours(self):
        return self.interval().hours()

    def minutes(self):
        return self.interval().minutes()

    def interval(self):
        return self.diff()

    def diff(self):
        if self._interval:
            return self._interval

        return DateDiff.null()

    def to_database(self):
        if self._interval and not self._interval.is_null():
            return self._interval.total_seconds()

        return None

    def total_seconds(self):
        if self._interval:
            return self._interval.total_seconds()

        return 0

    def __str__(self):
        if self._interval:
            return str(self._interval)

        return ''

    def to_short_string(self):
        if self._interval:
            return self._interval.to_string(True)

        return ''

    def to_string(self, include_total_hours):
        if include_total_hours:
            return f"{self} ({self.total_seconds() / 3600}h)"

        return str(self)

# FastAPI route to use the TimeInterval class
@app.get("/time_interval/")
async def get_time_interval(interval_str: str = "22d4h12m"):
    time_interval_obj = TimeInterval.parse(interval_str)
    return {"time_interval": time_interval_obj.to_string(True)}

@app.get("/null_time_interval/")
async def get_null_time_interval():
    null_time_interval_obj = TimeInterval.none()
    return {"null_time_interval": null_time_interval_obj.to_string()}



