# <?php

# require_once(ROOT_DIR . 'lib/Config/namespace.php');
# require_once(ROOT_DIR . 'lib/Application/Schedule/namespace.php');
# require_once(ROOT_DIR . 'lib/Application/Authorization/namespace.php');
# require_once(ROOT_DIR . 'lib/Server/namespace.php');
# require_once(ROOT_DIR . 'lib/Common/namespace.php');
# require_once(ROOT_DIR . 'Domain/namespace.php');
# require_once(ROOT_DIR . 'Domain/Access/namespace.php');
# require_once(ROOT_DIR . 'Presenters/Schedule/SchedulePageBuilder.php');
# require_once(ROOT_DIR . 'Presenters/ActionPresenter.php');

# interface ISchedulePresenter
# {
#     public function PageLoad(UserSession $user);
# }

# class SchedulePresenter extends ActionPresenter implements ISchedulePresenter
# {
#     /**
#      * @var ISchedulePage
#      */
#     private $_page;

#     /**
#      * @var IScheduleService
#      */
#     private $_scheduleService;

#     /**
#      * @var IResourceService
#      */
#     private $_resourceService;

#     /**
#      * @var ISchedulePageBuilder
#      */
#     private $_builder;

#     /**
#      * @var IReservationService
#      */
#     private $_reservationService;

#     /**
#      * @param ISchedulePage $page
#      * @param IScheduleService $scheduleService
#      * @param IResourceService $resourceService
#      * @param ISchedulePageBuilder $schedulePageBuilder
#      * @param IReservationService $reservationService
#      */
#     public function __construct(
#         ISchedulePage $page,
#         IScheduleService $scheduleService,
#         IResourceService $resourceService,
#         ISchedulePageBuilder $schedulePageBuilder,
#         IReservationService $reservationService
#     ) {
#         parent::__construct($page);
#         $this->_page = $page;
#         $this->_scheduleService = $scheduleService;
#         $this->_resourceService = $resourceService;
#         $this->_builder = $schedulePageBuilder;
#         $this->_reservationService = $reservationService;
#     }

#     public function PageLoad(UserSession $user, $loadReservations = false)
#     {
#         $showInaccessibleResources = $this->_page->ShowInaccessibleResources();

#         $schedules = $this->_scheduleService->GetAll($showInaccessibleResources, $user);

#         if (count($schedules) == 0) {
#             $this->_page->ShowPermissionError(true);
#             return;
#         }

#         $this->_page->ShowPermissionError(false);

#         $currentSchedule = $this->_builder->GetCurrentSchedule($this->_page, $schedules, $user);
#         $targetTimezone = $this->_page->GetDisplayTimezone($user, $currentSchedule);

#         $activeScheduleId = $currentSchedule->GetId();
#         $this->_builder->BindSchedules($this->_page, $schedules, $currentSchedule);

#         $scheduleDates = $this->_builder->GetScheduleDates($user, $currentSchedule, $this->_page);
#         $this->_builder->BindDisplayDates($this->_page, $scheduleDates, $currentSchedule);
#         $this->_builder->BindSpecificDates($user, $this->_page, $this->_page->GetSelectedDates(), $currentSchedule);

#         $resourceGroups = $this->_resourceService->GetResourceGroups($activeScheduleId, $user);
#         $this->_builder->BindResourceGroups($this->_page, $resourceGroups);

#         $resourceTypes = $this->_resourceService->GetResourceTypes();
#         $this->_builder->BindResourceTypes($this->_page, $resourceTypes);

#         $resourceAttributes = $this->_resourceService->GetResourceAttributes();
#         $resourceTypeAttributes = $this->_resourceService->GetResourceTypeAttributes();

#         $filter = $this->_builder->GetResourceFilter($activeScheduleId, $this->_page);
#         $this->_builder->BindResourceFilter($this->_page, $filter, $resourceAttributes, $resourceTypeAttributes);

#         $resources = $this->_resourceService->GetScheduleResources($activeScheduleId, $showInaccessibleResources, $user, $filter);

#         $reservationListing = new EmptyReservationListing();
#         if ($loadReservations) {
#             $rids = [];
#             foreach ($resources as $resource) {
#                 $rids[] = $resource->Id;
#             }
#             $reservationListing = $this->_reservationService->GetReservations($scheduleDates, $activeScheduleId, $targetTimezone, $rids);
#         }

#         $dailyLayout = $this->_scheduleService->GetDailyLayout($activeScheduleId, new ScheduleLayoutFactory($targetTimezone), $reservationListing);

#         $this->_builder->BindReservations($this->_page, $resources, $dailyLayout);
#     }

#     public function GetLayout(UserSession $user)
#     {
#         $scheduleId = $this->_page->GetScheduleId();
#         $layoutDate = $this->_page->GetLayoutDate();

#         $requestedDate = Date::Parse($layoutDate, $user->Timezone);

#         $layout = $this->_scheduleService->GetLayout($scheduleId, new ScheduleLayoutFactory($user->Timezone));
#         $periods = $layout->GetLayout($requestedDate);

#         $this->_page->SetLayoutResponse(new ScheduleLayoutSerializable($periods));
#     }

#     public function LoadReservations()
#     {
#         $filter = $this->_page->GetReservationRequest();
#         $items = $this->_reservationService->Search($filter->DateRange(), $filter->ScheduleId(), $filter->ResourceIds(), $filter->OwnerId(), $filter->ParticipantId());
#         $this->_page->BindReservations($items);
#     }
# }


from fastapi import Depends
from repositories import ScheduleRepository, ResourceRepository
from services import ScheduleService, ReservationService
from models import User
from calendar import Calendar

class SchedulePresenter:

    def __init__(
        self,
        schedule_service: ScheduleService = Depends(),
        resource_service: ResourceRepository = Depends(),
        reservation_service: ReservationService = Depends(),
    ):
        self.schedule_service = schedule_service
        self.resource_service = resource_service
        self.reservation_service = reservation_service

    async def get_schedule(self, user: User):
        schedules = await self.schedule_service.get_all_for_user(user)
        
        if not schedules:
            # handle no permission
            pass
        current_schedule = schedules[0] # placeholder
        
        resources = await self.resource_service.get_for_schedule(current_schedule.id)
        
        dates = Calendar.dates_for_month(date.today())
        
        reservations = await self.reservation_service.get_for_schedule(
            current_schedule.id, dates
        )
        
        return {
            "schedules": schedules,
            "resources": resources,
            "dates": dates,
            "reservations": reservations
        }

    async def get_layout(self, user: User, date: date):
        layout = await self.schedule_service.get_layout(user.timezone, date)
        return ScheduleLayout.from_domain(layout).dict()

    async def load_reservations(self, request: ReservationSearch):
        reservations = await self.reservation_service.search(
            request.schedule_id,
            request.date_range,
            request.resource_ids,
            request.owner_id,
            request.participant_id,
        )
        return reservations
