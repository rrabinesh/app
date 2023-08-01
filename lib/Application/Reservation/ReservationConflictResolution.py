# <?php

# require_once(ROOT_DIR . 'Domain/Access/namespace.php');

# interface IReservationConflictResolution
# {
#     /**
#      * @param ReservationItemView $existingReservation
#      * @param Blackout $blackout
#      * @return bool
#      */
#     public function Handle(ReservationItemView $existingReservation, Blackout $blackout);
# }

# abstract class ReservationConflictResolution implements IReservationConflictResolution
# {
#     public const BookAround = 'bookAround';
#     public const Delete = 'delete';
#     public const Notify = 'notify';

#     protected function __construct()
#     {
#     }

#     /**
#      * @param string|ReservationConflictResolution $resolutionType
#      * @return ReservationConflictResolution
#      */
#     public static function Create($resolutionType)
#     {
#         if ($resolutionType == self::Delete) {
#             return new ReservationConflictDelete(new ReservationRepository(), new DeleteReservationNotificationService(new UserRepository(), new AttributeRepository()));
#         }
#         if ($resolutionType == self::BookAround) {
#             return new ReservationConflictBookAround();
#         }
#         return new ReservationConflictNotify();
#     }
# }

# class ReservationConflictNotify extends ReservationConflictResolution
# {
#     public function Handle(ReservationItemView $existingReservation, Blackout $blackout)
#     {
#         return false;
#     }
# }

# class ReservationConflictDelete extends ReservationConflictResolution
# {
#     /**
#      * @var IReservationRepository
#      */
#     private $repository;
#     /**
#      * @var IReservationNotificationService
#      */
#     private $notificationService;

#     public function __construct(IReservationRepository $repository, IReservationNotificationService $notificationService)
#     {
#         $this->repository = $repository;
#         $this->notificationService = $notificationService;
#     }

#     public function Handle(ReservationItemView $existingReservation, Blackout $blackout)
#     {
#         $reservation = $this->repository->LoadById($existingReservation->GetId());
#         $reservation->ApplyChangesTo(SeriesUpdateScope::ThisInstance);
#         $reservation->Delete(ServiceLocator::GetServer()->GetUserSession(), 'Deleting conflicting reservation');
#         $this->repository->Delete($reservation);
#         $this->notificationService->Notify($reservation);

#         return true;
#     }
# }

# class ReservationConflictBookAround extends ReservationConflictResolution
# {
#     public function __construct()
#     {
#         parent::__construct();
#     }

#     public function Handle(ReservationItemView $existingReservation, Blackout $blackout)
#     {
#         $originalStart = $blackout->StartDate();
#         $originalEnd = $blackout->EndDate();
#         $reservationStart = $existingReservation->StartDate;
#         $reservationEnd = $existingReservation->EndDate;
#         $timezone = $blackout->StartDate()->Timezone();

#         if ($originalStart->LessThan($reservationStart) && $originalEnd->GreaterThan($reservationEnd)) {
#             Log::Debug('Blackout around reservation %s start %s end %s', $existingReservation->GetId(), $reservationStart, $reservationEnd);

#             $blackout->SetDate(new DateRange($originalStart, $reservationStart->ToTimezone($timezone)));
#             $blackout->GetSeries()->AddBlackout(new Blackout(new DateRange($reservationEnd->ToTimezone($timezone), $originalEnd)));
#             return true;
#         }

#         if ($originalStart->LessThan($reservationStart) && $originalEnd->GreaterThan($reservationStart) && $originalEnd->LessThanOrEqual($reservationEnd)) {
#             $blackout->SetDate(new DateRange($originalStart, $reservationStart->ToTimezone($timezone)));
#             return true;
#         }

#         if ($originalStart->GreaterThan($reservationStart) && $originalStart->LessThanOrEqual($reservationEnd) && $originalEnd->GreaterThan($reservationEnd)) {
#             $blackout->SetDate(new DateRange($reservationEnd->ToTimezone($timezone), $originalEnd));
#             return true;
#         }

#         if ($originalStart->GreaterThanOrEqual($reservationStart) && $originalEnd->LessThanOrEqual($reservationEnd)) {
#             return $blackout->GetSeries()->Delete($blackout);
#         }

#         return false;
#     }
# }


from fastapi import FastAPI
from datetime import datetime

# You can define your constants here
BOOK_AROUND = 'bookAround'
DELETE = 'delete'
NOTIFY = 'notify'

app = FastAPI()

class ReservationItemView:
    # Define properties and methods as needed
    pass

class Blackout:
    # Define properties and methods as needed
    pass

class IReservationRepository:
    # Define methods as needed
    pass

class IReservationNotificationService:
    # Define methods as needed
    pass

class ReservationConflictResolution:
    def __init__(self):
        pass

    def handle(self, existing_reservation: ReservationItemView, blackout: Blackout):
        return False

class ReservationConflictNotify(ReservationConflictResolution):
    def handle(self, existing_reservation: ReservationItemView, blackout: Blackout):
        return False

class ReservationConflictDelete(ReservationConflictResolution):
    def __init__(self, repository: IReservationRepository, notification_service: IReservationNotificationService):
        self.repository = repository
        self.notification_service = notification_service

    def handle(self, existing_reservation: ReservationItemView, blackout: Blackout):
        reservation = self.repository.load_by_id(existing_reservation.GetId())
        reservation.apply_changes_to(SeriesUpdateScope.ThisInstance)
        reservation.delete(ServiceLocator.GetServer().GetUserSession(), 'Deleting conflicting reservation')
        self.repository.delete(reservation)
        self.notification_service.notify(reservation)

        return True

class ReservationConflictBookAround(ReservationConflictResolution):
    def handle(self, existing_reservation: ReservationItemView, blackout: Blackout):
        original_start = blackout.StartDate()
        original_end = blackout.EndDate()
        reservation_start = existing_reservation.StartDate
        reservation_end = existing_reservation.EndDate
        timezone = blackout.StartDate().Timezone()

        # Implement the rest of the logic for handling conflicts and updating the blackout accordingly
        # ...

        return False

def create_resolution(resolution_type: str) -> ReservationConflictResolution:
    if resolution_type == DELETE:
        return ReservationConflictDelete(IReservationRepository(), IReservationNotificationService())
    elif resolution_type == BOOK_AROUND:
        return ReservationConflictBookAround()
    else:
        return ReservationConflictNotify()

@app.get("/handle_conflict/{resolution_type}")
def handle_conflict(resolution_type: str):
    resolution = create_resolution(resolution_type)
    existing_reservation = ReservationItemView()
    blackout = Blackout()

    return resolution.handle(existing_reservation, blackout)


