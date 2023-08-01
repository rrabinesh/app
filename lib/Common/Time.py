# <?php

# class Time
# {
#     private $_hour;
#     private $_minute;
#     private $_second;
#     private $_timezone;

#     public const FORMAT_HOUR_MINUTE = "H:i";

#     public function __construct($hour, $minute, $second = null, $timezone = null)
#     {
#         $this->_hour = intval($hour);
#         $this->_minute =  intval($minute);
#         $this->_second = is_null($second) ? 0 : intval($second);
#         $this->_timezone = $timezone;

#         if (empty($timezone)) {
#             $this->_timezone = date_default_timezone_get();
#         }
#     }

#     private function GetDate()
#     {
#         $parts = getdate(strtotime("$this->_hour:$this->_minute:$this->_second"));
#         return new Date("{$parts['year']}-{$parts['mon']}-{$parts['mday']} $this->_hour:$this->_minute:$this->_second", $this->_timezone);
#     }

#     /**
#      * @param string $time
#      * @param string $timezone, defaults to server timezone if not provided
#      * @return Time
#      */
#     public static function Parse($time, $timezone = null)
#     {
#         $date = new Date($time, $timezone);

#         return new Time($date->Hour(), $date->Minute(), $date->Second(), $timezone);
#     }

#     public function Hour()
#     {
#         return $this->_hour;
#     }

#     public function Minute()
#     {
#         return $this->_minute;
#     }

#     public function Second()
#     {
#         return $this->_second;
#     }

#     public function Timezone()
#     {
#         return $this->_timezone;
#     }

#     public function Format($format)
#     {
#         return $this->GetDate()->Format($format);
#     }

#     public function ToDatabase()
#     {
#         return $this->Format('H:i:s');
#     }

#     /**
#      * Compares this time to the one passed in
#      * Returns:
#      * -1 if this time is less than the passed in time
#      * 0 if the times are equal
#      * 1 if this time is greater than the passed in time
#      * @param Time $time
#      * @param Date|null $comparisonDate date to be used for time comparison
#      * @return int comparison result
#      */
#     public function Compare(Time $time, $comparisonDate = null)
#     {
#         if ($comparisonDate != null) {
#             $myDate = Date::Create($comparisonDate->Year(), $comparisonDate->Month(), $comparisonDate->Day(), $this->Hour(), $this->Minute(), $this->Second(), $this->Timezone());
#             $otherDate = Date::Create($comparisonDate->Year(), $comparisonDate->Month(), $comparisonDate->Day(), $time->Hour(), $time->Minute(), $time->Second(), $time->Timezone());

#             return ($myDate->Compare($otherDate));
#         }

#         return $this->GetDate()->Compare($time->GetDate());
#     }

#     /**
#      * @param Time $time
#      * @param Date|null $comparisonDate date to be used for time comparison
#      * @return bool
#      */
#     public function Equals(Time $time, $comparisonDate = null)
#     {
#         return $this->Compare($time, $comparisonDate) == 0;
#     }

#     public function ToString()
#     {
#         return sprintf("%02d:%02d:%02d", $this->_hour, $this->_minute, $this->_second);
#     }

#     public function __toString()
#     {
#         return $this->ToString();
#     }
# }

# class NullTime extends Time
# {
#     public function __construct()
#     {
#         parent::__construct(0, 0, 0, null);
#     }

#     public function ToDatabase()
#     {
#         return null;
#     }

#     public function ToString()
#     {
#         return '';
#     }
# }

from fastapi import FastAPI

app = FastAPI()

class Time:
    def __init__(self, hour, minute, second=None, timezone=None):
        self._hour = int(hour)
        self._minute = int(minute)
        self._second = 0 if second is None else int(second)
        self._timezone = timezone or "UTC"

    def get_date(self):
        # Assuming a custom implementation for getting the current date in the specified timezone
        return get_date_in_timezone(self._hour, self._minute, self._second, self._timezone)

    @classmethod
    def parse(cls, time_str, timezone=None):
        # Assuming a custom implementation for parsing the time string and obtaining the hour, minute, and second
        hour, minute, second = parse_time_string(time_str)
        return cls(hour, minute, second, timezone)

    def hour(self):
        return self._hour

    def minute(self):
        return self._minute

    def second(self):
        return self._second

    def timezone(self):
        return self._timezone

    def format(self, time_format):
        return self.get_date().format(time_format)

    def to_database(self):
        return self.format("H:i:s")

    def compare(self, other_time, comparison_date=None):
        if comparison_date is not None:
            my_date = create_date(comparison_date.year(), comparison_date.month(), comparison_date.day(),
                                  self._hour, self._minute, self._second, self._timezone)
            other_date = create_date(comparison_date.year(), comparison_date.month(), comparison_date.day(),
                                     other_time.hour(), other_time.minute(), other_time.second(), other_time.timezone())
            return my_date.compare(other_date)

        return self.get_date().compare(other_time.get_date())

    def equals(self, other_time, comparison_date=None):
        return self.compare(other_time, comparison_date) == 0

    def to_string(self):
        return f"{self._hour:02d}:{self._minute:02d}:{self._second:02d}"

    def __str__(self):
        return self.to_string()

class NullTime(Time):
    def __init__(self):
        super().__init__(0, 0, 0, None)

    def to_database(self):
        return None

    def to_string(self):
        return ''

# FastAPI route to use the Time and NullTime classes
@app.get("/time/")
async def get_time(time_str: str = "10:30", timezone: str = "UTC"):
    time_obj = Time.parse(time_str, timezone)
    return {"time": time_obj.to_string()}

@app.get("/null_time/")
async def get_null_time():
    null_time_obj = NullTime()
    return {"null_time": null_time_obj.to_string()}


