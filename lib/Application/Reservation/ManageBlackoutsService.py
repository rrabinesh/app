# <?php

# require_once(ROOT_DIR . 'Domain/Access/namespace.php');
# require_once(ROOT_DIR . 'lib/Application/Reservation/Validation/namespace.php');
# require_once(ROOT_DIR . 'lib/Application/Reservation/BlackoutFilter.php');

# interface IManageBlackoutsService
# {
#     /**
#      * @abstract
#      * @param $pageNumber int
#      * @param $pageSize int
#      * @param $sortField string
#      * @param $sortDirection string
#      * @param $filter BlackoutFilter
#      * @param $user UserSession
#      * @return PageableData
#      */
#     public function LoadFiltered($pageNumber, $pageSize, $sortField, $sortDirection, $filter, $user);

#     /**
#      * @param DateRange $blackoutDate
#      * @param array|int[] $resourceIds
#      * @param string $title
#      * @param IReservationConflictResolution $reservationConflictResolution
#      * @param IRepeatOptions $repeatOptions
#      * @return IBlackoutValidationResult
#      */
#     public function Add(DateRange $blackoutDate, $resourceIds, $title, IReservationConflictResolution $reservationConflictResolution, IRepeatOptions $repeatOptions);

#     /**
#      * @param int $blackoutInstanceId
#      * @param DateRange $blackoutDate
#      * @param array|int[] $resourceIds
#      * @param string $title
#      * @param IReservationConflictResolution $reservationConflictResolution
#      * @param IRepeatOptions $repeatOptions
#      * @param SeriesUpdateScope|string $scope
#      * @return IBlackoutValidationResult
#      */
#     public function Update($blackoutInstanceId, DateRange $blackoutDate, $resourceIds, $title, IReservationConflictResolution $reservationConflictResolution, IRepeatOptions $repeatOptions, $scope);

#     /**
#      * @param int $blackoutId
#      * @param string $updateScope
#      */
#     public function Delete($blackoutId, $updateScope);

#     /**
#      * @param int $blackoutId
#      * @param int $userId
#      * @return BlackoutSeries|null
#      */
#     public function LoadBlackout($blackoutId, $userId);
# }

# class ManageBlackoutsService implements IManageBlackoutsService
# {
#     /**
#      * @var IReservationViewRepository
#      */
#     private $reservationViewRepository;

#     /**
#      * @var IBlackoutRepository
#      */
#     private $blackoutRepository;

#     /**
#      * @var IUserRepository
#      */
#     private $userRepository;

#     public function __construct(IReservationViewRepository $reservationViewRepository, IBlackoutRepository $blackoutRepository, IUserRepository $userRepository)
#     {
#         $this->reservationViewRepository = $reservationViewRepository;
#         $this->blackoutRepository = $blackoutRepository;
#         $this->userRepository = $userRepository;
#     }

#     public function LoadFiltered($pageNumber, $pageSize, $sortField, $sortDirection, $filter, $user)
#     {
#         $blackoutFilter = $filter->GetFilter();
#         if (!$user->IsAdmin) {
#             $groups = $this->userRepository->LoadGroups($user->UserId, [RoleLevel::RESOURCE_ADMIN, RoleLevel::SCHEDULE_ADMIN]);
#             $groupIds = [];
#             foreach ($groups as $group) {
#                 $groupIds[] = $group->GroupId;
#             }
#             $adminFilter = new SqlFilterIn(new SqlFilterColumn('r', ColumnNames::RESOURCE_ADMIN_GROUP_ID), $groupIds);
#             $adminFilter->_Or(new SqlFilterIn(new SqlFilterColumn(TableNames::SCHEDULES, ColumnNames::SCHEDULE_ADMIN_GROUP_ID), $groupIds));
#             $blackoutFilter->_And($adminFilter);
#         }

#         return $this->reservationViewRepository->GetBlackoutList($pageNumber, $pageSize, $sortField, $sortDirection, $blackoutFilter);
#     }

#     public function Add(DateRange $blackoutDate, $resourceIds, $title, IReservationConflictResolution $reservationConflictResolution, IRepeatOptions $repeatOptions)
#     {
#         if (!$blackoutDate->GetEnd()->GreaterThan($blackoutDate->GetBegin())) {
#             return new BlackoutDateTimeValidationResult();
#         }

#         $userId = ServiceLocator::GetServer()->GetUserSession()->UserId;

#         $blackoutSeries = BlackoutSeries::Create($userId, $title, $blackoutDate);
#         $blackoutSeries->Repeats($repeatOptions);

#         foreach ($resourceIds as $resourceId) {
#             $blackoutSeries->AddResourceId($resourceId);
#         }

#         $conflictingBlackouts = $this->GetConflictingBlackouts($blackoutSeries);

#         $conflictingReservations = [];
#         if (empty($conflictingBlackouts)) {
#             $conflictingReservations = $this->GetConflictingReservations($blackoutSeries, $reservationConflictResolution);
#         }

#         $blackoutValidationResult = new BlackoutValidationResult($conflictingBlackouts, $conflictingReservations);

#         if ($blackoutValidationResult->CanBeSaved()) {
#             $this->blackoutRepository->Add($blackoutSeries);
#         }

#         return $blackoutValidationResult;
#     }

#     /**
#      * @param BlackoutSeries $blackoutSeries
#      * @param IReservationConflictResolution $reservationConflictResolution
#      * @return array|ReservationItemView[]
#      */
#     private function GetConflictingReservations($blackoutSeries, $reservationConflictResolution)
#     {
#         $conflictingReservations = [];

#         while ($blackout = $blackoutSeries->NextBlackout()) {
#             $existingReservations = $this->reservationViewRepository->GetReservations($blackout->StartDate(), $blackout->EndDate());

#             foreach ($existingReservations as $existingReservation) {
#                 if ($blackoutSeries->ContainsResource($existingReservation->ResourceId) && $blackout->Date()->Overlaps($existingReservation->Date)) {
#                     if (!$reservationConflictResolution->Handle($existingReservation, $blackout)) {
#                         $conflictingReservations[] = $existingReservation;
#                     }
#                 }
#             }
#         }

#         return $conflictingReservations;
#     }

#     /**
#      * @param BlackoutSeries $blackoutSeries
#      * @return array|BlackoutItemView[]
#      */
#     private function GetConflictingBlackouts($blackoutSeries)
#     {
#         $conflictingBlackouts = [];

#         $blackouts = $blackoutSeries->AllBlackouts();
#         foreach ($blackouts as $blackout) {
#             $existingBlackouts = $this->reservationViewRepository->GetBlackoutsWithin($blackout->Date());

#             foreach ($existingBlackouts as $existingBlackout) {
#                 if ($existingBlackout->SeriesId == $blackoutSeries->Id()) {
#                     continue;
#                 }

#                 if ($blackoutSeries->ContainsResource($existingBlackout->ResourceId) && $blackout->Date()->Overlaps($existingBlackout->Date)) {
#                     $conflictingBlackouts[] = $existingBlackout;
#                 }
#             }
#         }

#         return $conflictingBlackouts;
#     }

#     public function Delete($blackoutId, $updateScope)
#     {
#         if ($updateScope == SeriesUpdateScope::FullSeries) {
#             $this->blackoutRepository->DeleteSeries($blackoutId);
#         } else {
#             $this->blackoutRepository->Delete($blackoutId);
#         }
#     }

#     public function LoadBlackout($blackoutId, $userId)
#     {
#         $series = $this->blackoutRepository->LoadByBlackoutId($blackoutId);
#         $user = $this->userRepository->LoadById($userId);

#         foreach ($series->Resources() as $resource) {
#             if (!$user->IsResourceAdminFor($resource)) {
#                 return null;
#             }
#         }

#         return $series;
#     }

#     public function Update($blackoutInstanceId, DateRange $blackoutDate, $resourceIds, $title, IReservationConflictResolution $reservationConflictResolution, IRepeatOptions $repeatOptions, $scope)
#     {
#         if (!$blackoutDate->GetEnd()->GreaterThan($blackoutDate->GetBegin())) {
#             return new BlackoutDateTimeValidationResult();
#         }

#         $userId = ServiceLocator::GetServer()->GetUserSession()->UserId;

#         $blackoutSeries = $this->LoadBlackout($blackoutInstanceId, $userId);

#         if ($blackoutSeries == null) {
#             return new BlackoutSecurityValidationResult();
#         }

#         $blackoutSeries->Update($userId, $scope, $title, $blackoutDate, $repeatOptions, $resourceIds);

#         $conflictingBlackouts = $this->GetConflictingBlackouts($blackoutSeries);

#         $conflictingReservations = [];
#         if (empty($conflictingBlackouts)) {
#             $conflictingReservations = $this->GetConflictingReservations($blackoutSeries, $reservationConflictResolution);
#         }

#         $blackoutValidationResult = new BlackoutValidationResult($conflictingBlackouts, $conflictingReservations);

#         if ($blackoutValidationResult->CanBeSaved()) {
#             $this->blackoutRepository->Update($blackoutSeries);
#         }

#         return $blackoutValidationResult;
#     }
# }


from typing import List
from fastapi import FastAPI

app = FastAPI()

# FastAPI does not have interfaces like PHP, so we'll create a Python class for the service.

class BlackoutFilter:
    # Define your BlackoutFilter class here (assuming it has the required methods and properties).
    pass

class UserSession:
    # Define your UserSession class here (assuming it has the required properties).
    pass

class DateRange:
    # Define your DateRange class here (assuming it has the required methods and properties).
    pass

class IReservationConflictResolution:
    # Define your IReservationConflictResolution class here (assuming it has the required methods).
    pass

class IRepeatOptions:
    # Define your IRepeatOptions class here (assuming it has the required methods).
    pass

class PageableData:
    # Define your PageableData class here (assuming it has the required properties).
    pass

class IManageBlackoutsService:
    def LoadFiltered(self, pageNumber: int, pageSize: int, sortField: str, sortDirection: str, filter: BlackoutFilter, user: UserSession) -> PageableData:
        pass

    def Add(self, blackoutDate: DateRange, resourceIds: List[int], title: str, reservationConflictResolution: IReservationConflictResolution, repeatOptions: IRepeatOptions) -> "IBlackoutValidationResult":
        pass

    def Update(self, blackoutInstanceId: int, blackoutDate: DateRange, resourceIds: List[int], title: str, reservationConflictResolution: IReservationConflictResolution, repeatOptions: IRepeatOptions, scope: str) -> "IBlackoutValidationResult":
        pass

    def Delete(self, blackoutId: int, updateScope: str) -> None:
        pass

    def LoadBlackout(self, blackoutId: int, userId: int) -> "BlackoutSeries":
        pass

# Implement the ManageBlackoutsService class:

class BlackoutSeries:
    @classmethod
    def Create(cls, user_id: int, title: str, blackout_date: DateRange) -> "BlackoutSeries":
        pass

    def Repeats(self, repeat_options: IRepeatOptions) -> None:
        pass

    def AddResourceId(self, resource_id: int) -> None:
        pass

    def NextBlackout(self):
        pass

    def AllBlackouts(self):
        pass

    def ContainsResource(self, resource_id: int) -> bool:
        pass

    def StartDate(self):
        pass

    def EndDate(self):
        pass

    def Date(self):
        pass

    # Other methods for updating, deleting, and handling conflicts can be implemented here.

# Now, create the actual FastAPI endpoints:

@app.get("/load_filtered")
def load_filtered(page_number: int, page_size: int, sort_field: str, sort_direction: str, filter: BlackoutFilter, user: UserSession):
    manage_blackouts = ManageBlackoutsService()
    return manage_blackouts.LoadFiltered(page_number, page_size, sort_field, sort_direction, filter, user)

@app.post("/add")
def add_blackout(blackout_date: DateRange, resource_ids: List[int], title: str, reservation_conflict_resolution: IReservationConflictResolution, repeat_options: IRepeatOptions):
    manage_blackouts = ManageBlackoutsService()
    return manage_blackouts.Add(blackout_date, resource_ids, title, reservation_conflict_resolution, repeat_options)

@app.put("/update")
def update_blackout(blackout_instance_id: int, blackout_date: DateRange, resource_ids: List[int], title: str, reservation_conflict_resolution: IReservationConflictResolution, repeat_options: IRepeatOptions, scope: str):
    manage_blackouts = ManageBlackoutsService()
    return manage_blackouts.Update(blackout_instance_id, blackout_date, resource_ids, title, reservation_conflict_resolution, repeat_options, scope)

@app.delete("/delete")
def delete_blackout(blackout_id: int, update_scope: str):
    manage_blackouts = ManageBlackoutsService()
    return manage_blackouts.Delete(blackout_id, update_scope)

@app.get("/load_blackout")
def load_blackout(blackout_id: int, user_id: int):
    manage_blackouts = ManageBlackoutsService()
    return manage_blackouts.LoadBlackout(blackout_id, user_id)

