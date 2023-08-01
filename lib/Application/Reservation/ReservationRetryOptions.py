# <?php

# interface IReservationRetryOptions
# {
#     /**
#      * @param ReservationSeries $series
#      * @param ReservationRetryParameter[] $retryParameters
#      */
#     public function AdjustReservation(ReservationSeries $series, $retryParameters);
# }

# class ReservationRetryOptions implements IReservationRetryOptions
# {
#     /**
#      * @var IReservationConflictIdentifier
#      */
#     private $conflictIdentifier;
#     /**
#      * @var IScheduleRepository
#      */
#     private $scheduleRepository;

#     public function __construct(IReservationConflictIdentifier $conflictIdentifier, IScheduleRepository $scheduleRepository)
#     {
#         $this->conflictIdentifier = $conflictIdentifier;
#         $this->scheduleRepository = $scheduleRepository;
#     }

#     public function AdjustReservation(ReservationSeries $series, $retryParameters)
#     {
#         $shouldSkipConflicts = ReservationRetryParameter::GetValue(ReservationRetryParameter::$SKIP_CONFLICTS, $retryParameters, new BooleanConverter()) == true;
#         if (!$shouldSkipConflicts) {
#             return;
#         }

#         $conflicts = $this->conflictIdentifier->GetConflicts($series);

#         foreach ($conflicts->Conflicts() as $conflict) {
#             $series->RemoveInstance($conflict->Reservation);
#         }

#         $series->CalculateCredits($this->scheduleRepository->GetLayout($series->ScheduleId(), new ScheduleLayoutFactory($series->CurrentInstance()->StartDate()->Timezone())));
#     }
# }


from abc import ABC, abstractmethod

class IReservationRetryOptions(ABC):
    @abstractmethod
    def adjust_reservation(self, series: ReservationSeries, retry_parameters: List[ReservationRetryParameter]):
        pass

class ReservationRetryOptions(IReservationRetryOptions):
    def __init__(self, conflict_identifier: IReservationConflictIdentifier, schedule_repository: IScheduleRepository):
        self.conflict_identifier = conflict_identifier
        self.schedule_repository = schedule_repository

    def adjust_reservation(self, series: ReservationSeries, retry_parameters: List[ReservationRetryParameter]):
        should_skip_conflicts = ReservationRetryParameter.get_value(ReservationRetryParameter.SKIP_CONFLICTS, retry_parameters, BooleanConverter()) == True
        if not should_skip_conflicts:
            return

        conflicts = self.conflict_identifier.get_conflicts(series)

        for conflict in conflicts.conflicts():
            series.remove_instance(conflict.reservation)

        series.calculate_credits(self.schedule_repository.get_layout(
            series.schedule_id(), ScheduleLayoutFactory(series.current_instance().start_date().timezone())
        ))



