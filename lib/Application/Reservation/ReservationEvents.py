# <?php

# require_once(ROOT_DIR . 'Domain/Events/IDomainEvent.php');

# class EventCategory
# {
#     public const Reservation = 'reservation';
# }

# class ReservationEvent
# {
#     public const Approved = 'approved';
#     public const Created = 'created';
#     public const Updated = 'updated';
#     public const Deleted = 'deleted';
#     public const SeriesEnding = 'series_ending';
#     public const ParticipationChanged = 'participation_changed';

#     /**
#      * @static
#      * @return array|IDomainEvent[]
#      */
#     public static function AllEvents()
#     {
#         return [
#             new ReservationApprovedEvent(),
#             new ReservationCreatedEvent(),
#             new ReservationUpdatedEvent(),
#             new ReservationDeletedEvent(),
#             new ReservationSeriesEndingEvent(),
#             new ParticipationChangedEvent(),
#         ];
#     }
# }

# class ReservationCreatedEvent implements IDomainEvent
# {
#     public function EventType()
#     {
#         return ReservationEvent::Created;
#     }

#     public function EventCategory()
#     {
#         return EventCategory::Reservation;
#     }
# }

# class ReservationUpdatedEvent implements IDomainEvent
# {
#     public function EventType()
#     {
#         return ReservationEvent::Updated;
#     }

#     public function EventCategory()
#     {
#         return EventCategory::Reservation;
#     }
# }

# class ReservationDeletedEvent implements IDomainEvent
# {
#     public function EventType()
#     {
#         return ReservationEvent::Deleted;
#     }

#     public function EventCategory()
#     {
#         return EventCategory::Reservation;
#     }
# }

# class ReservationApprovedEvent implements IDomainEvent
# {
#     public function EventType()
#     {
#         return ReservationEvent::Approved;
#     }

#     public function EventCategory()
#     {
#         return EventCategory::Reservation;
#     }
# }

# class ReservationSeriesEndingEvent implements IDomainEvent
# {
#     public function EventType()
#     {
#         return ReservationEvent::SeriesEnding;
#     }

#     public function EventCategory()
#     {
#         return EventCategory::Reservation;
#     }
# }

# class ParticipationChangedEvent implements IDomainEvent
# {
#     public function EventType()
#     {
#         return ReservationEvent::ParticipationChanged;
#     }

#     public function EventCategory()
#     {
#         return EventCategory::Reservation;
#     }
# }


from fastapi import FastAPI

app = FastAPI()

class EventCategory:
    Reservation = 'reservation'

class ReservationEvent:
    Approved = 'approved'
    Created = 'created'
    Updated = 'updated'
    Deleted = 'deleted'
    SeriesEnding = 'series_ending'
    ParticipationChanged = 'participation_changed'

    @staticmethod
    def all_events():
        return [
            ReservationApprovedEvent(),
            ReservationCreatedEvent(),
            ReservationUpdatedEvent(),
            ReservationDeletedEvent(),
            ReservationSeriesEndingEvent(),
            ParticipationChangedEvent(),
        ]

class IDomainEvent:
    def event_type(self):
        pass

    def event_category(self):
        pass

class ReservationCreatedEvent(IDomainEvent):
    def event_type(self):
        return ReservationEvent.Created

    def event_category(self):
        return EventCategory.Reservation

class ReservationUpdatedEvent(IDomainEvent):
    def event_type(self):
        return ReservationEvent.Updated

    def event_category(self):
        return EventCategory.Reservation

class ReservationDeletedEvent(IDomainEvent):
    def event_type(self):
        return ReservationEvent.Deleted

    def event_category(self):
        return EventCategory.Reservation

class ReservationApprovedEvent(IDomainEvent):
    def event_type(self):
        return ReservationEvent.Approved

    def event_category(self):
        return EventCategory.Reservation

class ReservationSeriesEndingEvent(IDomainEvent):
    def event_type(self):
        return ReservationEvent.SeriesEnding

    def event_category(self):
        return EventCategory.Reservation

class ParticipationChangedEvent(IDomainEvent):
    def event_type(self):
        return ReservationEvent.ParticipationChanged

    def event_category(self):
        return EventCategory.Reservation

@app.get("/all_events")
def all_events():
    events = [event.event_type() for event in ReservationEvent.all_events()]
    return {"events": events}


