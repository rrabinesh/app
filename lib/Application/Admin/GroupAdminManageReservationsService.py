# <?php

# require_once(ROOT_DIR . 'Domain/Access/namespace.php');
# require_once(ROOT_DIR . 'Domain/Access/namespace.php');

# class GroupAdminManageReservationsService extends ManageReservationsService implements IManageReservationsService
# {
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

#         $this->userRepository = $userRepository;
#     }

#     /**
#      * @param $pageNumber int
#      * @param $pageSize int
#      * @param null|string $sortField
#      * @param null|string $sortDirection
#      * @param $filter ReservationFilter
#      * @param $userSession UserSession
#      * @return PageableData|ReservationItemView[]
#      */
#     public function LoadFiltered($pageNumber, $pageSize, $sortField, $sortDirection, $filter, $userSession)
#     {
#         $user = $this->userRepository->LoadById($userSession->UserId);

#         $adminGroups = $user->GetAdminGroups();
#         $groupIds = [];
#         foreach ($adminGroups as $group) {
#             $groupIds[] = $group->GroupId;
#         }

#         $command = new GetFullGroupReservationListCommand($groupIds);

#         if ($filter != null) {
#             $command = new FilterCommand($command, $filter->GetFilter());
#         }

#         $builder = ['ReservationItemView', 'Populate'];
#         return PageableDataStore::GetList($command, $builder, $pageNumber, $pageSize, $sortField, $sortDirection);
#     }
# }

# Assuming you have defined IReservationViewRepository, IUserRepository, IReservationAuthorization,
# IReservationHandler, IUpdateReservationPersistenceService, PageableData, ReservationItemView,
# ReservationFilter, UserSession, and other required classes.

class GroupAdminManageReservationsService:
    def __init__(
        self,
        reservation_view_repository: IReservationViewRepository,
        user_repository: IUserRepository,
        authorization: IReservationAuthorization,
        reservation_handler: IReservationHandler = None,
        persistence_service: IUpdateReservationPersistenceService = None
    ):
        self.reservation_view_repository = reservation_view_repository
        self.user_repository = user_repository
        self.authorization = authorization
        self.reservation_handler = reservation_handler
        self.persistence_service = persistence_service

    def load_filtered(self, page_number, page_size, sort_field, sort_direction, _filter, user_session):
        user = self.user_repository.LoadById(user_session.UserId)

        admin_groups = user.GetAdminGroups()
        group_ids = [group.GroupId for group in admin_groups]

        command = GetFullGroupReservationListCommand(group_ids)

        if _filter is not None:
            command = FilterCommand(command, _filter.GetFilter())

        builder = ['ReservationItemView', 'Populate']
        return PageableDataStore.GetList(command, builder, page_number, page_size, sort_field, sort_direction)


