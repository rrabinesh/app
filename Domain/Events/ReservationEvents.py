# <?php

# class SeriesEventPriority
# {
#     public const Highest = 10;
#     public const High = 7;
#     public const Normal = 5;
#     public const Low = 3;
#     public const Lowest = 1;
# }

# abstract class SeriesEvent
# {
#     /**
#      * @var int
#      */
#     private $priority;

#     /**
#      * @var \ReservationSeries
#      */
#     protected $series;

#     /**
#      * @var string
#      */
#     protected $id;

#     /**
#      * @param int|SeriesEventPriority $priority
#      * @return void
#      */
#     protected function SetPriority($priority)
#     {
#         $this->priority = $priority;
#     }

#     /**
#      * @return int|SeriesEventPriority
#      */
#     public function GetPriority()
#     {
#         return $this->priority;
#     }

#     /**
#      * @return ReservationSeries
#      */
#     public function Series()
#     {
#         return $this->series;
#     }

#     /**
#      * @return int
#      */
#     public function SeriesId()
#     {
#         return $this->series->SeriesId();
#     }

#     /**
#      * @param ReservationSeries $series
#      * @param int|SeriesEventPriority $priority
#      */
#     public function __construct(ReservationSeries $series, $priority = SeriesEventPriority::Normal)
#     {
#         $this->priority = $priority;
#         $this->series = $series;
#         $this->id = $this->series->SeriesId();
#     }

#     public function __toString()
#     {
#         return sprintf("%s-%s", get_class($this), $this->id);
#     }

#     public static function Compare(SeriesEvent $event1, SeriesEvent $event2)
#     {
#         if ($event1->GetPriority() == $event2->GetPriority()) {
#             return 0;
#         }

#         // higher priority should be at the top
#         return ($event1->GetPriority() > $event2->GetPriority()) ? -1 : 1;
#     }
# }

# class InstanceAddedEvent extends SeriesEvent
# {
#     /**
#      * @var Reservation
#      */
#     private $instance;

#     /**
#      * @return Reservation
#      */
#     public function Instance()
#     {
#         return $this->instance;
#     }

#     public function __construct(Reservation $reservationInstance, ExistingReservationSeries $series)
#     {
#         $this->instance = $reservationInstance;
#         parent::__construct($series, SeriesEventPriority::Lowest);
#     }

#     public function __toString()
#     {
#         return sprintf("%s%s", get_class($this), $this->instance->ReferenceNumber());
#     }
# }

# class InstanceRemovedEvent extends SeriesEvent
# {
#     /**
#      * @var Reservation
#      */
#     private $instance;

#     /**
#      * @return Reservation
#      */
#     public function Instance()
#     {
#         return $this->instance;
#     }

#     public function __construct(Reservation $reservationInstance, ExistingReservationSeries $series)
#     {
#         $this->instance = $reservationInstance;
#         parent::__construct($series, SeriesEventPriority::Highest);
#     }

#     public function __toString()
#     {
#         return sprintf("%s%s", get_class($this), $this->instance->ReferenceNumber());
#     }
# }

# class InstanceUpdatedEvent extends SeriesEvent
# {
#     /**
#      * @var Reservation
#      */
#     private $instance;

#     /**
#      * @return Reservation
#      */
#     public function Instance()
#     {
#         return $this->instance;
#     }

#     public function __construct(Reservation $reservationInstance, ExistingReservationSeries $series)
#     {
#         $this->instance = $reservationInstance;
#         parent::__construct($series, SeriesEventPriority::Low);
#     }

#     public function __toString()
#     {
#         return sprintf("%s%s", get_class($this), $this->instance->ReferenceNumber());
#     }
# }

# class SeriesBranchedEvent extends SeriesEvent
# {
#     public function __construct(ReservationSeries $series)
#     {
#         parent::__construct($series);
#     }

#     public function __toString()
#     {
#         return sprintf("%s%s", get_class($this), $this->series->SeriesId());
#     }
# }

# class SeriesDeletedEvent extends SeriesEvent
# {
#     public function __construct(ExistingReservationSeries $series)
#     {
#         parent::__construct($series, SeriesEventPriority::Highest);
#     }

#     /**
#      * @return ExistingReservationSeries
#      */
#     public function Series()
#     {
#         return $this->series;
#     }

#     public function __toString()
#     {
#         return sprintf("%s%s", get_class($this), $this->series->SeriesId());
#     }
# }

# class ResourceRemovedEvent extends SeriesEvent
# {
#     /**
#      * @var BookableResource
#      */
#     private $resource;

#     public function __construct(BookableResource $resource, ExistingReservationSeries $series)
#     {
#         $this->resource = $resource;

#         parent::__construct($series, SeriesEventPriority::Highest);
#     }

#     /**
#      * @return BookableResource
#      */
#     public function Resource()
#     {
#         return $this->resource;
#     }

#     /**
#      * @return int
#      */
#     public function ResourceId()
#     {
#         return $this->resource->GetResourceId();
#     }

#     /**
#      * @return ExistingReservationSeries
#      */
#     public function Series()
#     {
#         return $this->series;
#     }

#     public function __toString()
#     {
#         return sprintf("%s%s%s", get_class($this), $this->ResourceId(), $this->series->SeriesId());
#     }
# }

# class ResourceAddedEvent extends SeriesEvent
# {
#     /**
#      * @var BookableResource
#      */
#     private $resource;

#     /**
#      * @var int|ResourceLevel
#      */
#     private $resourceLevel;

#     /**
#      * @param BookableResource $resource
#      * @param int|ResourceLevel $resourceLevel
#      * @param ExistingReservationSeries $series
#      */
#     public function __construct(BookableResource $resource, $resourceLevel, ExistingReservationSeries $series)
#     {
#         $this->resource = $resource;
#         $this->resourceLevel = $resourceLevel;

#         parent::__construct($series, SeriesEventPriority::Low);
#     }

#     /**
#      * @return BookableResource
#      */
#     public function Resource()
#     {
#         return $this->resource;
#     }

#     public function ResourceId()
#     {
#         return $this->resource->GetResourceId();
#     }

#     /**
#      * @return ExistingReservationSeries
#      */
#     public function Series()
#     {
#         return $this->series;
#     }

#     public function __toString()
#     {
#         return sprintf("%s%s%s", get_class($this), $this->ResourceId(), $this->series->SeriesId());
#     }

#     public function ResourceLevel()
#     {
#         return $this->resourceLevel;
#     }
# }

# class SeriesApprovedEvent extends SeriesEvent
# {
#     public function __construct(ExistingReservationSeries $series)
#     {
#         parent::__construct($series);
#     }

#     public function __toString()
#     {
#         return sprintf("%s%s", get_class($this), $this->series->SeriesId());
#     }
# }

# class AccessoryAddedEvent extends SeriesEvent
# {
#     /**
#      * @return int
#      */
#     public function AccessoryId()
#     {
#         return $this->accessory->AccessoryId;
#     }

#     /**
#      * @return int
#      */
#     public function Quantity()
#     {
#         return $this->accessory->QuantityReserved;
#     }

#     /**
#      * @var \ReservationAccessory
#      */
#     private $accessory;

#     public function __construct(ReservationAccessory $accessory, ExistingReservationSeries $series)
#     {
#         $this->accessory = $accessory;

#         parent::__construct($series, SeriesEventPriority::Low);
#     }

#     public function __toString()
#     {
#         return sprintf("%s%s", get_class($this), $this->accessory->__toString());
#     }
# }

# class AccessoryRemovedEvent extends SeriesEvent
# {
#     /**
#      * @return int
#      */
#     public function AccessoryId()
#     {
#         return $this->accessory->AccessoryId;
#     }

#     /**
#      * @var \ReservationAccessory
#      */
#     private $accessory;

#     public function __construct(ReservationAccessory $accessory, ExistingReservationSeries $series)
#     {
#         $this->accessory = $accessory;

#         parent::__construct($series, SeriesEventPriority::Highest);
#     }

#     public function __toString()
#     {
#         return sprintf("%s%s", get_class($this), $this->accessory->__toString());
#     }
# }

# class AttributeAddedEvent extends SeriesEvent
# {
#     /**
#      * @return int
#      */
#     public function AttributeId()
#     {
#         return $this->attribute->AttributeId;
#     }

#     /**
#      * @return mixed
#      */
#     public function Value()
#     {
#         return $this->attribute->Value;
#     }

#     /**
#      * @var \AttributeValue
#      */
#     private $attribute;

#     public function __construct(AttributeValue $attribute, ExistingReservationSeries $series)
#     {
#         $this->attribute = $attribute;

#         parent::__construct($series, SeriesEventPriority::Low);
#     }

#     public function __toString()
#     {
#         return sprintf("%s%s", get_class($this), $this->attribute->__toString());
#     }
# }

# class AttributeRemovedEvent extends SeriesEvent
# {
#     /**
#      * @return int
#      */
#     public function AttributeId()
#     {
#         return $this->attribute->AttributeId;
#     }

#     /**
#      * @var \AttributeValue
#      */
#     private $attribute;

#     public function __construct(AttributeValue $attribute, ExistingReservationSeries $series)
#     {
#         $this->attribute = $attribute;

#         parent::__construct($series, SeriesEventPriority::Highest);
#     }

#     public function __toString()
#     {
#         return sprintf("%s%s", get_class($this), $this->attribute->__toString());
#     }
# }

# class OwnerChangedEvent extends SeriesEvent
# {
#     /**
#      * @var int
#      */
#     private $oldOwnerId;

#     /**
#      * @var int
#      */
#     private $newOwnerId;

#     /**
#      * @param ExistingReservationSeries $series
#      * @param int $oldOwnerId
#      * @param int $newOwnerId
#      */
#     public function __construct(ExistingReservationSeries $series, $oldOwnerId, $newOwnerId)
#     {
#         $this->series = $series;
#         $this->oldOwnerId = $oldOwnerId;
#         $this->newOwnerId = $newOwnerId;
#     }

#     /**
#      * @return ExistingReservationSeries
#      */
#     public function Series()
#     {
#         return $this->series;
#     }

#     /**
#      * @return int
#      */
#     public function OldOwnerId()
#     {
#         return $this->oldOwnerId;
#     }

#     /**
#      * @return int
#      */
#     public function NewOwnerId()
#     {
#         return $this->newOwnerId;
#     }

#     public function __toString()
#     {
#         return sprintf(
#             "%s%s%s%s",
#             get_class($this),
#             $this->OldOwnerId(),
#             $this->NewOwnerId(),
#             $this->series->SeriesId()
#         );
#     }
# }

# class AttachmentRemovedEvent extends SeriesEvent
# {
#     /**
#      * @var int
#      */
#     private $fileId;

#     /**
#      * @var string
#      */
#     private $extension;

#     /**
#      * @param ExistingReservationSeries $series
#      * @param int $fileId
#      * @param string $extension
#      */
#     public function __construct(ExistingReservationSeries $series, $fileId, $extension)
#     {
#         parent::__construct($series, SeriesEventPriority::Lowest);

#         $this->fileId = $fileId;
#         $this->extension = $extension;
#     }

#     /**
#      * @return int
#      */
#     public function FileId()
#     {
#         return $this->fileId;
#     }

#     /**
#      * return string
#      */
#     public function FileName()
#     {
#         return $this->fileId . '.' . $this->extension;
#     }

#     public function __toString()
#     {
#         return sprintf("%s%s%s", get_class($this), $this->FileId(), $this->series->SeriesId());
#     }
# }

# class ReminderAddedEvent extends SeriesEvent
# {
#     private $minutesPrior;
#     private $reminderType;

#     /**
#      * @param ExistingReservationSeries $series
#      * @param int $minutesPrior
#      * @param ReservationReminderType|int $reminderType
#      */
#     public function __construct(ExistingReservationSeries $series, $minutesPrior, $reminderType)
#     {
#         $this->series = $series;
#         $this->minutesPrior = $minutesPrior;
#         $this->reminderType = $reminderType;
#     }

#     public function __toString()
#     {
#         return sprintf(
#             "%s%s%s%s",
#             get_class($this),
#             $this->MinutesPrior(),
#             $this->ReminderType(),
#             $this->series->SeriesId()
#         );
#     }

#     /**
#      * @return int
#      */
#     public function MinutesPrior()
#     {
#         return $this->minutesPrior;
#     }

#     /**
#      * @return ReservationReminderType
#      */
#     public function ReminderType()
#     {
#         return $this->reminderType;
#     }
# }

# class ReminderRemovedEvent extends SeriesEvent
# {
#     /**
#      * @var int|ReservationReminderType
#      */
#     private $reminderType;

#     /**
#      * @return ReservationReminderType
#      */
#     public function ReminderType()
#     {
#         return $this->reminderType;
#     }

#     /**
#      * @param ExistingReservationSeries $series
#      * @param int|ReservationReminderType $reminderType
#      */
#     public function __construct(ExistingReservationSeries $series, $reminderType)
#     {
#         $this->series = $series;
#         $this->reminderType = $reminderType;
#     }

#     public function __toString()
#     {
#         return sprintf(
#             "%s%s%s",
#             get_class($this),
#             $this->ReminderType(),
#             $this->series->SeriesId()
#         );
#     }
# }

from fastapi import FastAPI
from enum import IntEnum

app = FastAPI()

class SeriesEventPriority(IntEnum):
    Highest = 10
    High = 7
    Normal = 5
    Low = 3
    Lowest = 1

class SeriesEvent:
    def __init__(self, series, priority=SeriesEventPriority.Normal):
        self.priority = priority
        self.series = series
        self.id = self.series.SeriesId()

    def SetPriority(self, priority):
        self.priority = priority

    def GetPriority(self):
        return self.priority

    def Series(self):
        return self.series

    def SeriesId(self):
        return self.series.SeriesId()

    def __toString(self):
        return f"{type(self).__name__}-{self.id}"

    @staticmethod
    def Compare(event1, event2):
        if event1.GetPriority() == event2.GetPriority():
            return 0

        return -1 if event1.GetPriority() > event2.GetPriority() else 1

class InstanceAddedEvent(SeriesEvent):
    def __init__(self, reservation_instance, series):
        self.instance = reservation_instance
        super().__init__(series, SeriesEventPriority.Lowest)

    def Instance(self):
        return self.instance

    def __toString(self):
        return f"{type(self).__name__}{self.instance.ReferenceNumber()}"

class InstanceRemovedEvent(SeriesEvent):
    def __init__(self, reservation_instance, series):
        self.instance = reservation_instance
        super().__init__(series, SeriesEventPriority.Highest)

    def Instance(self):
        return self.instance

    def __toString(self):
        return f"{type(self).__name__}{self.instance.ReferenceNumber()}"

class InstanceUpdatedEvent(SeriesEvent):
    def __init__(self, reservation_instance, series):
        self.instance = reservation_instance
        super().__init__(series, SeriesEventPriority.Low)

    def Instance(self):
        return self.instance

    def __toString(self):
        return f"{type(self).__name__}{self.instance.ReferenceNumber()}"

class SeriesBranchedEvent(SeriesEvent):
    def __init__(self, series):
        super().__init__(series)

    def __toString(self):
        return f"{type(self).__name__}{self.series.SeriesId()}"

class SeriesDeletedEvent(SeriesEvent):
    def __init__(self, series):
        super().__init__(series, SeriesEventPriority.Highest)

    def Series(self):
        return self.series

    def __toString(self):
        return f"{type(self).__name__}{self.series.SeriesId()}"
