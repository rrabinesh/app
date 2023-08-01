# <?php

# class BlackoutFilter
# {
#     private $startDate = null;
#     private $endDate = null;
#     private $scheduleId = null;
#     private $resourceId = null;

#     /**
#      * @param Date $startDate
#      * @param Date $endDate
#      * @param int $scheduleId
#      * @param int $resourceId
#      */
#     public function __construct($startDate = null, $endDate = null, $scheduleId = null, $resourceId = null)
#     {
#         $this->startDate = $startDate;
#         $this->endDate = $endDate;
#         $this->scheduleId = $scheduleId;
#         $this->resourceId = $resourceId;
#     }

#     public function GetFilter()
#     {
#         $filter = new SqlFilterNull();

#         if (!empty($this->startDate)) {
#             $filter->_And(new SqlFilterGreaterThan(new SqlFilterColumn(TableNames::BLACKOUT_INSTANCES_ALIAS, ColumnNames::RESERVATION_START), $this->startDate->ToDatabase()));
#         }
#         if (!empty($this->endDate)) {
#             $filter->_And(new SqlFilterLessThan(new SqlFilterColumn(TableNames::BLACKOUT_INSTANCES_ALIAS, ColumnNames::RESERVATION_END), $this->endDate->ToDatabase()));
#         }
#         if (!empty($this->scheduleId)) {
#             $filter->_And(new SqlFilterEquals(new SqlFilterColumn(TableNames::SCHEDULES, ColumnNames::SCHEDULE_ID), $this->scheduleId));
#         }
#         if (!empty($this->resourceId)) {
#             $filter->_And(new SqlFilterEquals(new SqlFilterColumn(TableNames::RESOURCES_ALIAS, ColumnNames::RESOURCE_ID), $this->resourceId));
#         }

#         return $filter;
#     }
# }


from datetime import datetime

class BlackoutFilter:
    def __init__(self, start_date=None, end_date=None, schedule_id=None, resource_id=None):
        self.start_date = start_date
        self.end_date = end_date
        self.schedule_id = schedule_id
        self.resource_id = resource_id

    def get_filter(self):
        # Assuming SqlFilterNull, SqlFilterGreaterThan, SqlFilterLessThan, SqlFilterColumn, SqlFilterEquals,
        # TableNames, and ColumnNames classes are properly implemented
        filter = SqlFilterNull()

        if self.start_date:
            filter._And(SqlFilterGreaterThan(SqlFilterColumn(TableNames.BLACKOUT_INSTANCES_ALIAS, ColumnNames.RESERVATION_START), self.start_date.to_database()))

        if self.end_date:
            filter._And(SqlFilterLessThan(SqlFilterColumn(TableNames.BLACKOUT_INSTANCES_ALIAS, ColumnNames.RESERVATION_END), self.end_date.to_database()))

        if self.schedule_id:
            filter._And(SqlFilterEquals(SqlFilterColumn(TableNames.SCHEDULES, ColumnNames.SCHEDULE_ID), self.schedule_id))

        if self.resource_id:
            filter._And(SqlFilterEquals(SqlFilterColumn(TableNames.RESOURCES_ALIAS, ColumnNames.RESOURCE_ID), self.resource_id))

        return filter

# Example usage:
class SqlFilterNull:
    pass

class SqlFilterGreaterThan:
    pass

class SqlFilterLessThan:
    pass

class SqlFilterColumn:
    pass

class SqlFilterEquals:
    pass

class TableNames:
    BLACKOUT_INSTANCES_ALIAS = "blackout_instances_alias"
    SCHEDULES = "schedules"
    RESOURCES_ALIAS = "resources_alias"

class ColumnNames:
    RESERVATION_START = "reservation_start"
    RESERVATION_END = "reservation_end"
    SCHEDULE_ID = "schedule_id"
    RESOURCE_ID = "resource_id"
