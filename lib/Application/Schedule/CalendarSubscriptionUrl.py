# <?php

# class CalendarSubscriptionUrl
# {
#     /**
#      * @var Url
#      */
#     private $url;

#     public const PAGE_TOKEN = '{page}';

#     public function __construct($userPublicId, $schedulePublicId, $resourcePublicId)
#     {
#         $config = Configuration::Instance();
#         $subscriptionKey = $config->GetSectionKey(ConfigSection::ICS, ConfigKeys::ICS_SUBSCRIPTION_KEY);

#         if (empty($subscriptionKey)) {
#             $this->url = new Url('#');
#             return;
#         }

#         $scriptUrl = $config->GetScriptUrl();
#         $scriptUrl .= '/export/' . self::PAGE_TOKEN;
#         $url = new Url($scriptUrl);

#         $url->AddQueryString(QueryStringKeys::USER_ID, $userPublicId);
#         $url->AddQueryString(QueryStringKeys::SCHEDULE_ID, $schedulePublicId);
#         $url->AddQueryString(QueryStringKeys::RESOURCE_ID, $resourcePublicId);
#         $url->AddQueryString(QueryStringKeys::SUBSCRIPTION_KEY, $subscriptionKey);
#         $this->url = $url;
#     }

#     public function GetWebcalUrl()
#     {
#         $scriptUrl = $this->url->ToString();
#         return str_replace(self::PAGE_TOKEN, Pages::CALENDAR_SUBSCRIBE, $scriptUrl);
#     }

#     public function GetAtomUrl()
#     {
#         $scriptUrl = $this->url->ToString();
#         return str_replace(self::PAGE_TOKEN, Pages::CALENDAR_SUBSCRIBE_ATOM, $scriptUrl);
#     }

#     public function __toString()
#     {
#         return $this->GetWebcalUrl();
#     }
# }


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

