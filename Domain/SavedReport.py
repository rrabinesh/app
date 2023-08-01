# <!-- <?php

# interface ISavedReport
# {
#     /**
#      * @return string
#      */
#     public function ReportName();

#     /**
#      * @return int
#      */
#     public function Id();
# }

# class SavedReport implements ISavedReport
# {
#     /**
#      * @var int
#      */
#     private $reportId;
#     /**
#      * @var string
#      */
#     private $reportName;
#     /**
#      * @var int
#      */
#     private $userId;
#     /**
#      * @var Report_Usage
#      */
#     private $usage;
#     /**
#      * @var Report_ResultSelection
#      */
#     private $selection;
#     /**
#      * @var Report_GroupBy
#      */
#     private $groupBy;

#     /**
#      * @var Report_Range
#      */
#     private $range;

#     /**
#      * @var Report_Filter
#      */
#     private $filter;

#     /**
#      * @var Date
#      */
#     private $dateCreated;

#     public function __construct(
#         $reportName,
#         $userId,
#         Report_Usage $usage,
#         Report_ResultSelection $selection,
#         Report_GroupBy $groupBy,
#         Report_Range $range,
#         Report_Filter $filter
#     ) {
#         $this->reportName = $reportName;
#         $this->userId = $userId;
#         $this->usage = $usage;
#         $this->selection = $selection;
#         $this->groupBy = $groupBy;
#         $this->range = $range;
#         $this->filter = $filter;
#         $this->dateCreated = Date::Now();
#     }

#     public function Id()
#     {
#         return $this->reportId;
#     }

#     /**
#      * @return Date
#      */
#     public function DateCreated()
#     {
#         return $this->dateCreated;
#     }

#     /**
#      * @return Report_Usage
#      */
#     public function Usage()
#     {
#         return $this->usage;
#     }

#     /**
#      * @return Report_ResultSelection
#      */
#     public function Selection()
#     {
#         return $this->selection;
#     }

#     /**
#      * @return Report_GroupBy
#      */
#     public function GroupBy()
#     {
#         return $this->groupBy;
#     }

#     /**
#      * @return Report_Range
#      */
#     public function Range()
#     {
#         return $this->range;
#     }

#     /**
#      * @return Report_Filter
#      */
#     public function Filter()
#     {
#         return $this->filter;
#     }

#     /**
#      * @return Date
#      */
#     public function RangeStart()
#     {
#         return $this->range->Start();
#     }

#     /**
#      * @return Date
#      */
#     public function RangeEnd()
#     {
#         return $this->range->End();
#     }

#     /**
#      * @return int[]|null
#      */
#     public function ResourceIds()
#     {
#         return $this->filter->ResourceIds();
#     }

#     /**
#      * @return int[]|null
#      */
#     public function ResourceTypeIds()
#     {
#         return $this->filter->ResourceTypeIds();
#     }

#     /**
#      * @return int[]|null
#      */
#     public function ScheduleIds()
#     {
#         return $this->filter->ScheduleIds();
#     }

#     /**
#      * @return int|null
#      */
#     public function UserId()
#     {
#         return $this->filter->UserId();
#     }

#     /**
#      * @return int|null
#      */
#     public function ParticipantId()
#     {
#         return $this->filter->ParticipantId();
#     }

#     /**
#      * @return int[]|null
#      */
#     public function GroupIds()
#     {
#         return $this->filter->GroupIds();
#     }

#     /**
#      * @return int[]|null
#      */
#     public function AccessoryIds()
#     {
#         return $this->filter->AccessoryIds();
#     }

#     /**
#      * @return bool
#      */
#     public function IncludeDeleted()
#     {
#         return $this->filter->IncludeDeleted();
#     }

#     /**
#      * @return string
#      */
#     public function ReportName()
#     {
#         return $this->reportName;
#     }

#     /**
#      * @return int
#      */
#     public function OwnerId()
#     {
#         return $this->userId;
#     }

#     /**
#      * @param Date $date
#      */
#     public function WithDateCreated(Date $date)
#     {
#         $this->dateCreated = $date;
#     }

#     /**
#      * @param int $reportId
#      */
#     public function WithId($reportId)
#     {
#         $this->reportId = $reportId;
#     }

#     /**
#      * @return bool
#      */
#     public function IsScheduled()
#     {
#         return false;
#     }

#     /**
#      * @static
#      * @param string $reportName
#      * @param int $userId
#      * @param Date $dateCreated
#      * @param string $serialized
#      * @param int $reportId
#      * @return SavedReport
#      */
#     public static function FromDatabase($reportName, $userId, Date $dateCreated, $serialized, $reportId)
#     {
#         $savedReport = ReportSerializer::Deserialize($reportName, $userId, $serialized);
#         $savedReport->WithDateCreated($dateCreated);
#         $savedReport->WithId($reportId);
#         return $savedReport;
#     }
# }

# class ReportSerializer
# {
#     /**
#      * @static
#      * @param SavedReport $report
#      * @return string
#      */
#     public static function Serialize(SavedReport $report)
#     {
#         $template = 'usage=%s;selection=%s;groupby=%s;range=%s;range_start=%s;range_end=%s;resourceid=%s;scheduleid=%s;userid=%s;groupid=%s;accessoryid=%s;participantid=%s;deleted=%s;resourceTypeId=%s';

#         return sprintf(
#             $template,
#             $report->Usage(),
#             $report->Selection(),
#             $report->GroupBy(),
#             $report->Range(),
#             $report->RangeStart()->ToDatabase(),
#             $report->RangeEnd()->ToDatabase(),
#             implode('|', $report->ResourceIds()),
#             implode('|', $report->ScheduleIds()),
#             $report->UserId(),
#             implode('|', $report->GroupIds()),
#             implode('|', $report->AccessoryIds()),
#             $report->ParticipantId(),
#             $report->IncludeDeleted(),
#             implode('|', $report->ResourceTypeIds())
#         );
#     }

#     /**
#      * @static
#      * @param string $reportName
#      * @param int $userId
#      * @param string $serialized
#      * @return SavedReport
#      */
#     public static function Deserialize($reportName, $userId, $serialized)
#     {
#         $values = [];
#         $pairs = explode(';', $serialized);
#         foreach ($pairs as $pair) {
#             $keyValue = explode('=', $pair);

#             if (count($keyValue) == 2) {
#                 $values[$keyValue[0]] = $keyValue[1];
#             }
#         }

#         return new SavedReport(
#             $reportName,
#             $userId,
#             self::GetUsage($values),
#             self::GetSelection($values),
#             self::GetGroupBy($values),
#             self::GetRange($values),
#             self::GetFilter($values)
#         );
#     }

#     /**
#      * @static
#      * @param array $values
#      * @return Report_Usage
#      */
#     private static function GetUsage($values)
#     {
#         if (array_key_exists('usage', $values)) {
#             return new Report_Usage($values['usage']);
#         } else {
#             return new Report_Usage(Report_Usage::RESOURCES);
#         }
#     }

#     /**
#      * @static
#      * @param array $values
#      * @return Report_ResultSelection
#      */
#     private static function GetSelection($values)
#     {
#         if (array_key_exists('selection', $values)) {
#             return new Report_ResultSelection($values['selection']);
#         } else {
#             return new Report_ResultSelection(Report_ResultSelection::FULL_LIST);
#         }
#     }

#     /**
#      * @static
#      * @param array $values
#      * @return Report_GroupBy
#      */
#     private static function GetGroupBy($values)
#     {
#         if (array_key_exists('groupby', $values)) {
#             return new Report_GroupBy($values['groupby']);
#         } else {
#             return new Report_GroupBy(Report_GroupBy::NONE);
#         }
#     }

#     /**
#      * @static
#      * @param array $values
#      * @return Report_Range
#      */
#     private static function GetRange($values)
#     {
#         if (array_key_exists('range', $values)) {
#             $start = $values['range_start'];
#             $end = $values['range_end'];

#             return new Report_Range($values['range'], $start, $end, 'UTC');
#         } else {
#             return Report_Range::AllTime();
#         }
#     }

#     /**
#      * @static
#      * @param array $values
#      * @return Report_Filter
#      */
#     private static function GetFilter($values)
#     {
#         $resourceIds = isset($values['resourceid']) ? explode('|', $values['resourceid']) : [];
#         $scheduleIds = isset($values['scheduleid']) ? explode('|', $values['scheduleid']) : [];
#         $userId = isset($values['userid']) ? $values['userid'] : '';
#         $groupIds = isset($values['groupid']) ? explode('|', $values['groupid']) : [];
#         $accessoryIds = isset($values['accessoryid']) ? explode('|', $values['accessoryid']) : [];
#         $participantId = isset($values['participantid']) ? $values['participantid'] : [];
#         $deleted = isset($values['deleted']) ? intval($values['deleted']) : false;
#         $resourceTypeIds = isset($values['resourceTypeId']) ? explode('|', $values['resourceTypeId']) : [];

#         return new Report_Filter($resourceIds, $scheduleIds, $userId, $groupIds, $accessoryIds, $participantId, $deleted, $resourceTypeIds);
#     }
# } -->

from enum import Enum
from typing import List, Union
from fastapi import FastAPI

app = FastAPI()

class ReportUsage(str, Enum):
    RESOURCES = "resources"
    # Add other usage types here if needed

class ReportResultSelection(str, Enum):
    FULL_LIST = "full_list"
    # Add other result selection types here if needed

class ReportGroupBy(str, Enum):
    NONE = "none"
    # Add other group by types here if needed

class ReportRange:
    def __init__(self, range_type: str, start: str, end: str, timezone: str):
        self.range_type = range_type
        self.start = start
        self.end = end
        self.timezone = timezone

class ReportFilter:
    def __init__(
        self,
        resource_ids: List[int],
        schedule_ids: List[int],
        user_id: Union[int, None],
        group_ids: List[int],
        accessory_ids: List[int],
        participant_id: Union[int, None],
        include_deleted: bool,
        resource_type_ids: List[int]
    ):
        self.resource_ids = resource_ids
        self.schedule_ids = schedule_ids
        self.user_id = user_id
        self.group_ids = group_ids
        self.accessory_ids = accessory_ids
        self.participant_id = participant_id
        self.include_deleted = include_deleted
        self.resource_type_ids = resource_type_ids

class SavedReport:
    def __init__(
        self,
        report_name: str,
        user_id: int,
        usage: ReportUsage,
        selection: ReportResultSelection,
        group_by: ReportGroupBy,
        report_range: ReportRange,
        report_filter: ReportFilter
    ):
        self.report_name = report_name
        self.user_id = user_id
        self.usage = usage
        self.selection = selection
        self.group_by = group_by
        self.report_range = report_range
        self.report_filter = report_filter

@app.get("/reports/{report_id}")
def get_report(report_id: int):
    # Replace this placeholder with your actual database retrieval logic
    # For demonstration purposes, we'll return a sample report
    report = SavedReport(
        report_name="Sample Report",
        user_id=1,
        usage=ReportUsage.RESOURCES,
        selection=ReportResultSelection.FULL_LIST,
        group_by=ReportGroupBy.NONE,
        report_range=ReportRange("weekly", "2023-07-01", "2023-07-07", "UTC"),
        report_filter=ReportFilter([], [], 1, [], [], None, False, [])
    )
    return report

# If you want to add other endpoints to create and manipulate reports, define appropriate functions for them.

# To run the FastAPI application:
# uvicorn main:app --reload


