# <?php

# class ScheduleAdminManageReservationsService extends ManageReservationsService implements IManageReservationsService
# {
#     /**
#      * @var IReservationViewRepository
#      */
#     private $reservationViewRepository;

#     /**
#      * @var IUserRepository
#      */
#     private $userRepository;

#     /**
#      * @param IReservationViewRepository $reservationViewRepository
#      * @param IUserRepository $userRepository
#      * @param IReservationAuthorization $authorization
#      * @param IReservationHandler|null $reservationHandler
#      * @param IUpdateReservationPersistenceService|null $persistenceService
#      */
#     public function __construct(
#         IReservationViewRepository $reservationViewRepository,
#         IUserRepository $userRepository,
#         IReservationAuthorization $authorization,
#         $reservationHandler = null,
#         $persistenceService = null
#     ) {
#         parent::__construct($reservationViewRepository, $authorization, $reservationHandler, $persistenceService);

#         $this->reservationViewRepository = $reservationViewRepository;
#         $this->userRepository = $userRepository;
#     }

#     /**
#      * @param $pageNumber int
#      * @param $pageSize int
#      * @param null|string $sortField
#      * @param null|string $sortDirection
#      * @param $filter ReservationFilter
#      * @param $user UserSession
#      * @return PageableData|ReservationItemView[]
#      */
#     public function LoadFiltered($pageNumber, $pageSize, $sortField, $sortDirection, $filter, $user)
#     {
#         $groupIds = [];
#         $groups = $this->userRepository->LoadGroups($user->UserId, RoleLevel::SCHEDULE_ADMIN);
#         foreach ($groups as $group) {
#             $groupIds[] = $group->GroupId;
#         }

#         $filter->_And(new SqlFilterIn(new SqlFilterColumn(TableNames::SCHEDULES, ColumnNames::SCHEDULE_ADMIN_GROUP_ID), $groupIds));
#         return $this->reservationViewRepository->GetList($pageNumber, $pageSize, $sortField, $sortDirection, $filter->GetFilter());
#     }
# }


from fastapi import FastAPI

# Assume you have defined the necessary Pydantic models and FastAPI dependencies.
# You can add them here or import them from other modules.

# Create a FastAPI app
app = FastAPI()

# Sample IReservationViewRepository, IUserRepository, IReservationAuthorization
# You may need to define these interfaces properly.
class IReservationViewRepository:
    pass

class IUserRepository:
    pass

class IReservationAuthorization:
    pass

# Sample ReservationFilter and ReservationItemView
# You may need to define these models properly.
class ReservationFilter:
    pass

class ReservationItemView:
    pass

# ScheduleAdminManageReservationsService
class ScheduleAdminManageReservationsService:
    def __init__(
        self,
        reservation_view_repository: IReservationViewRepository,
        user_repository: IUserRepository,
        authorization: IReservationAuthorization,
        reservation_handler=None,
        persistence_service=None,
    ):
        self.reservation_view_repository = reservation_view_repository
        self.user_repository = user_repository
        self.authorization = authorization
        self.reservation_handler = reservation_handler
        self.persistence_service = persistence_service

    def load_filtered(self, page_number, page_size, sort_field, sort_direction, filter, user):
        group_ids = []
        groups = self.user_repository.LoadGroups(user.UserId, RoleLevel.SCHEDULE_ADMIN)
        for group in groups:
            group_ids.append(group.GroupId)

        filter._And(SqlFilterIn(SqlFilterColumn(TableNames.SCHEDULES, ColumnNames.SCHEDULE_ADMIN_GROUP_ID), group_ids))
        return self.reservation_view_repository.GetList(page_number, page_size, sort_field, sort_direction, filter.GetFilter())



