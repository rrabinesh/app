# <?php

# class LayoutValidator extends ValidatorBase implements IValidator
# {
#     /**
#      * @var string|string[]
#      */
#     private $reservableSlots;

#     /**
#      * @var string|string[]
#      */
#     private $blockedSlots;

#     /**
#      * @var bool
#      */
#     private $validateSingle;

#     /**
#      * @param string|string[] $reservableSlots
#      * @param string|string[] $blockedSlots
#      * @param bool $validateSingle
#      */
#     public function __construct($reservableSlots, $blockedSlots, $validateSingle = true)
#     {
#         $this->reservableSlots = $reservableSlots;
#         $this->blockedSlots = $blockedSlots;
#         $this->validateSingle = $validateSingle;
#     }

#     /**
#      * @return void
#      */
#     public function Validate()
#     {
#         try {
#             $this->isValid = true;

#             $days = [null];

#             if (!$this->validateSingle) {
#                 Log::Debug('Validating daily layout');
#                 if (count($this->reservableSlots) != DayOfWeek::NumberOfDays || count($this->blockedSlots) != DayOfWeek::NumberOfDays) {
#                     $this->isValid = false;
#                     return;
#                 }
#                 $layout = ScheduleLayout::ParseDaily('UTC', $this->reservableSlots, $this->blockedSlots);
#                 $days = DayOfWeek::Days();
#             } else {
#                 Log::Debug('Validating single layout');
#                 $layout = ScheduleLayout::Parse('UTC', $this->reservableSlots, $this->blockedSlots);
#             }

#             foreach ($days as $day) {
#                 if (is_null($day)) {
#                     $day = 0;
#                 }
#                 $slots = $layout->GetLayout(Date::Now()->AddDays($day)->ToUtc());

#                 /** @var $firstDate Date */
#                 $firstDate = $slots[0]->BeginDate();
#                 /** @var $lastDate Date */
#                 $lastDate = $slots[count($slots) - 1]->EndDate();
#                 if (!$firstDate->IsMidnight() || !$lastDate->IsMidnight()) {
#                     Log::Debug('Dates are not midnight');
#                     $this->isValid = false;
#                 }

#                 if (count($slots) == 0 && $slots[0]->BeginDate()->IsMidnight() && $slots[0]->EndDate()->IsMidnight()) {
#                     Log::Debug('Both dates are midnight');
#                     $this->isValid = true;
#                     return;
#                 }

#                 for ($i = 0; $i < count($slots) - 1; $i++) {
#                     if (!$slots[$i]->EndDate()->Equals($slots[$i + 1]->BeginDate())) {
#                         $this->isValid = false;
#                     }
#                 }
#             }
#         } catch (Exception $ex) {
#             Log::Error('Error during LayoutValidator %s', $ex);
#             $this->isValid = false;
#         }
#     }
# }

from fastapi import HTTPException
from datetime import date, datetime
from enum import Enum

class DayOfWeek(Enum):
   SUNDAY = 0
   #...

class LayoutValidator:

    def __init__(self, reservable_slots, blocked_slots, validate_single=True):
        self.reservable_slots = reservable_slots 
        self.blocked_slots = blocked_slots
        self.validate_single = validate_single

    def validate(self) -> None:
        try:
            is_valid = True
            
            if not self.validate_single:
                # validate daily layout
                days = [DayOfWeek]
                
                if len(self.reservable_slots) != len(days) or len(self.blocked_slots) != len(days):
                    is_valid = False
                    return
                    
                # parse daily layout
                
            else:
                # validate single layout
               
                # parse single layout
                pass
            for day in days:
                slots = layout.get_layout(date.today() + timedelta(days=day))
                
                start = slots[0].start_time 
                end = slots[-1].end_time
                
                if not start.time() == datetime.min.time() or not end.time() == datetime.max.time():
                    is_valid = False
                   
                # additional slot validations
                
            self.is_valid = is_valid
                
        except Exception as e:
            self.is_valid = False

