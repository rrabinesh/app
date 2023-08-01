# <?php

# interface IQuotaRepository
# {
#     /**
#      * @abstract
#      * @return array|Quota[]
#      */
#     public function LoadAll();

#     /**
#      * @abstract
#      * @param Quota $quota
#      * @return void
#      */
#     public function Add(Quota $quota);

#     /**
#      * @abstract
#      * @param $quotaId
#      * @return void
#      */
#     public function DeleteById($quotaId);
# }

# interface IQuotaViewRepository
# {
#     /**
#      * @abstract
#      * @return array|QuotaItemView[]
#      */
#     public function GetAll();
# }

# class QuotaRepository implements IQuotaRepository, IQuotaViewRepository
# {
#     public function LoadAll()
#     {
#         $quotas = [];

#         $command = new GetAllQuotasCommand();
#         $reader = ServiceLocator::GetDatabase()->Query($command);

#         while ($row = $reader->GetRow()) {
#             $quotaId = $row[ColumnNames::QUOTA_ID];

#             $limit = Quota::CreateLimit($row[ColumnNames::QUOTA_LIMIT], $row[ColumnNames::QUOTA_UNIT]);
#             $duration = Quota::CreateDuration($row[ColumnNames::QUOTA_DURATION]);

#             $resourceId = $row[ColumnNames::RESOURCE_ID];
#             $groupId = $row[ColumnNames::GROUP_ID];
#             $scheduleId = $row[ColumnNames::SCHEDULE_ID];
#             $enforcedStartTime = $row[ColumnNames::ENFORCED_START_TIME];
#             $enforcedEndTime = $row[ColumnNames::ENFORCED_END_TIME];
#             $enforcedDays = empty($row[ColumnNames::ENFORCED_DAYS]) ? [] : explode(',', $row[ColumnNames::ENFORCED_DAYS]);
#             $scope = Quota::CreateScope($row[ColumnNames::QUOTA_SCOPE]);

#             $quotas[] = new Quota($quotaId, $duration, $limit, $resourceId, $groupId, $scheduleId, $enforcedStartTime, $enforcedEndTime, $enforcedDays, $scope);
#         }
#         $reader->Free();
#         return $quotas;
#     }

#     /**
#      * @return array|QuotaItemView[]
#      */
#     public function GetAll()
#     {
#         $quotas = [];

#         $command = new GetAllQuotasCommand();
#         $reader = ServiceLocator::GetDatabase()->Query($command);

#         while ($row = $reader->GetRow()) {
#             $quotaId = $row[ColumnNames::QUOTA_ID];

#             $limit = $row[ColumnNames::QUOTA_LIMIT];
#             $unit = $row[ColumnNames::QUOTA_UNIT];
#             $duration = $row[ColumnNames::QUOTA_DURATION];
#             $groupName = $row['group_name'];
#             $resourceName = $row['resource_name'];
#             $scheduleName = $row['schedule_name'];
#             $enforcedStartTime = $row[ColumnNames::ENFORCED_START_TIME];
#             $enforcedEndTime = $row[ColumnNames::ENFORCED_END_TIME];
#             $enforcedDays = empty($row[ColumnNames::ENFORCED_DAYS]) ? [] : explode(',', $row[ColumnNames::ENFORCED_DAYS]);
#             $scope = $row[ColumnNames::QUOTA_SCOPE];

#             $quotas[] = new QuotaItemView(
#                 $quotaId,
#                 $limit,
#                 $unit,
#                 $duration,
#                 $groupName,
#                 $resourceName,
#                 $scheduleName,
#                 $enforcedStartTime,
#                 $enforcedEndTime,
#                 $enforcedDays,
#                 $scope
#             );
#         }

#         $reader->Free();
#         return $quotas;
#     }

#     /**
#      * @param Quota $quota
#      * @return void
#      */
#     public function Add(Quota $quota)
#     {
#         $command = new AddQuotaCommand(
#             $quota->GetDuration()->Name(),
#             $quota->GetLimit()->Amount(),
#             $quota->GetLimit()->Name(),
#             $quota->ResourceId(),
#             $quota->GroupId(),
#             $quota->ScheduleId(),
#             $quota->EnforcedStartTime(),
#             $quota->EnforcedEndTime(),
#             $quota->EnforcedDays(),
#             $quota->GetScope()->Name()
#         );

#         ServiceLocator::GetDatabase()->Execute($command);
#     }

#     /**
#      * @param $quotaId
#      * @return void
#      */
#     public function DeleteById($quotaId)
#     {
#         //TODO:  Make this delete a quota instead of the id
#         $command = new DeleteQuotaCommand($quotaId);
#         ServiceLocator::GetDatabase()->Execute($command);
#     }
# }

# class QuotaItemView
# {
#     public $Id;
#     public $Limit;
#     public $Unit;
#     public $Duration;
#     public $GroupName;
#     public $ResourceName;
#     public $ScheduleName;
#     public $AllDay;
#     public $Everyday;
#     public $EnforcedStartTime;
#     public $EnforcedEndTime;
#     public $EnforcedDays;
#     public $Scope;

#     /**
#      * @param int $quotaId
#      * @param decimal $limit
#      * @param string $unit
#      * @param string $duration
#      * @param string $groupName
#      * @param string $resourceName
#      * @param string $scheduleName
#      * @param string|null $enforcedStartTime
#      * @param string|null $enforcedEndTime
#      * @param array|int[] $enforcedDays
#      * @param string $scope
#      */
#     public function __construct(
#         $quotaId,
#         $limit,
#         $unit,
#         $duration,
#         $groupName,
#         $resourceName,
#         $scheduleName,
#         $enforcedStartTime,
#         $enforcedEndTime,
#         $enforcedDays,
#         $scope
#     ) {
#         $this->Id = $quotaId;
#         $this->Limit = $limit;
#         $this->Unit = $unit;
#         $this->Duration = $duration;
#         $this->GroupName = $groupName;
#         $this->ResourceName = $resourceName;
#         $this->ScheduleName = $scheduleName;
#         $this->EnforcedStartTime = empty($enforcedStartTime) ? null : Time::Parse($enforcedStartTime);
#         $this->EnforcedEndTime = empty($enforcedEndTime) ? null : Time::Parse($enforcedEndTime);
#         $this->EnforcedDays = empty($enforcedDays) ? [] : $enforcedDays;
#         $this->AllDay = empty($enforcedStartTime) || empty($enforcedEndTime);
#         $this->Everyday = empty($enforcedDays);
#         $this->Scope = empty($scope) ? QuotaScope::IncludeCompleted : $scope;
#     }
# }

from fastapi import FastAPI
from typing import List

# Placeholder for classes not defined in the provided code
class Quota:
    @staticmethod
    def create_limit(limit, unit):
        pass

    @staticmethod
    def create_duration(duration):
        pass

    @staticmethod
    def create_scope(scope):
        pass

class ServiceLocator:
    @staticmethod
    def get_database():
        pass

class GetAllQuotasCommand:
    pass

class ColumnNames:
    QUOTA_ID = 'quota_id'
    QUOTA_LIMIT = 'quota_limit'
    QUOTA_UNIT = 'quota_unit'
    QUOTA_DURATION = 'quota_duration'
    RESOURCE_ID = 'resource_id'
    GROUP_ID = 'group_id'
    SCHEDULE_ID = 'schedule_id'
    ENFORCED_START_TIME = 'enforced_start_time'
    ENFORCED_END_TIME = 'enforced_end_time'
    ENFORCED_DAYS = 'enforced_days'
    QUOTA_SCOPE = 'quota_scope'

class AddQuotaCommand:
    pass

class DeleteQuotaCommand:
    pass

# Create a FastAPI app
app = FastAPI()

# IQuotaRepository interface (not explicitly needed in FastAPI)

# IQuotaViewRepository interface (not explicitly needed in FastAPI)

# QuotaRepository implementation
class QuotaRepository:
    def load_all(self):
        quotas = []

        command = GetAllQuotasCommand()
        reader = ServiceLocator.get_database().query(command)

        while row := reader.get_row():
            quota_id = row[ColumnNames.QUOTA_ID]

            limit = Quota.create_limit(row[ColumnNames.QUOTA_LIMIT], row[ColumnNames.QUOTA_UNIT])
            duration = Quota.create_duration(row[ColumnNames.QUOTA_DURATION])

            resource_id = row[ColumnNames.RESOURCE_ID]
            group_id = row[ColumnNames.GROUP_ID]
            schedule_id = row[ColumnNames.SCHEDULE_ID]
            enforced_start_time = row[ColumnNames.ENFORCED_START_TIME]
            enforced_end_time = row[ColumnNames.ENFORCED_END_TIME]
            enforced_days = [] if not row[ColumnNames.ENFORCED_DAYS] else row[ColumnNames.ENFORCED_DAYS].split(',')
            scope = Quota.create_scope(row[ColumnNames.QUOTA_SCOPE])

            quotas.append(Quota(quota_id, duration, limit, resource_id, group_id, schedule_id, enforced_start_time, enforced_end_time, enforced_days, scope))
        reader.free()
        return quotas

    def add(self, quota):
        command = AddQuotaCommand(
            quota.get_duration().name(),
            quota.get_limit().amount(),
            quota.get_limit().name(),
            quota.resource_id(),
            quota.group_id(),
            quota.schedule_id(),
            quota.enforced_start_time(),
            quota.enforced_end_time(),
            quota.enforced_days(),
            quota.get_scope().name()
        )

        ServiceLocator.get_database().execute(command)

    def delete_by_id(self, quota_id):
        # TODO: Make this delete a quota instead of the id
        command = DeleteQuotaCommand(quota_id)
        ServiceLocator.get_database().execute(command)

# Create an instance of the QuotaRepository class
quota_repository = QuotaRepository()

# FastAPI route to load all quotas
@app.get("/load_all_quotas/")
async def load_all_quotas():
    quotas = quota_repository.load_all()
    return {"quotas": quotas}

# FastAPI route to add a quota
@app.post("/add_quota/")
async def add_quota(quota: Quota):
    quota_repository.add(quota)
    return {"message": "Quota added successfully"}

# FastAPI route to delete a quota by id
@app.delete("/delete_quota/{quota_id}")
async def delete_quota(quota_id: int):
    quota_repository.delete_by_id(quota_id)
    return {"message": "Quota deleted successfully"}


