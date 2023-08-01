# <?php

# interface IResourceAvailabilityStrategy
# {
#     /**
#      * @param Date $startDate
#      * @param Date $endDate
#      * @param int[]|int|null $resourceIds
#      * @return array|IReservedItemView[]
#      */
#     public function GetItemsBetween(Date $startDate, Date $endDate, $resourceIds);
# }

# class ResourceAvailability implements IResourceAvailabilityStrategy
# {
#     /**
#      * @var IReservationViewRepository
#      */
#     protected $_repository;

#     public function __construct(IReservationViewRepository $repository)
#     {
#         $this->_repository = $repository;
#     }

#     public function GetItemsBetween(Date $startDate, Date $endDate, $resourceIds)
#     {
#         $reservations = $this->_repository->GetReservations($startDate, $endDate, null, null, null, $resourceIds);
#         $blackouts = $this->_repository->GetBlackoutsWithin(new DateRange($startDate, $endDate), null, $resourceIds);

#         return array_merge($reservations, $blackouts);
#     }
# }



from datetime import date
from typing import List, Optional

class IReservedItemView:
    # Define the properties of IReservedItemView here as required
    pass

class DateRange:
    def __init__(self, start_date: date, end_date: date):
        self.start_date = start_date
        self.end_date = end_date

class IReservationViewRepository:
    # Define the methods of IReservationViewRepository here as required
    pass

class ResourceAvailability:
    def __init__(self, repository: IReservationViewRepository):
        self._repository = repository

    def get_items_between(self, start_date: date, end_date: date, resource_ids: Optional[List[int]] = None) -> List[IReservedItemView]:
        reservations = self._repository.get_reservations(start_date, end_date, resource_ids)
        blackouts = self._repository.get_blackouts_within(DateRange(start_date, end_date), resource_ids)

        return reservations + blackouts



