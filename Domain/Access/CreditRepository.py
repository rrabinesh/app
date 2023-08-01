# <?php

# require_once(ROOT_DIR . 'Domain/Values/CreditLogView.php');
# require_once(ROOT_DIR . 'Domain/Access/PageableDataStore.php');

# interface ICreditRepository
# {
#     /**
#      * @param int $pageNumber
#      * @param int $pageSize
#      * @param int $userId
#      * @param string $sortField
#      * @param string $sortDirection
#      * @param ISqlFilter $filter
#      * @return PageableData|CreditLogView[]
#      */
#     public function GetList($pageNumber, $pageSize, $userId = -1, $sortField = null, $sortDirection = null, $filter = null);
# }

# class CreditRepository implements ICreditRepository
# {
#     public function GetList($pageNumber, $pageSize, $userId = -1, $sortField = null, $sortDirection = null, $filter = null)
#     {
#         $command = new GetAllCreditLogsCommand($userId);

#         if ($filter != null) {
#             $command = new FilterCommand($command, $filter);
#         }

#         $builder = ['CreditLogView', 'Populate'];
#         return PageableDataStore::GetList($command, $builder, $pageNumber, $pageSize, $sortField, $sortDirection);
#     }
# }

from fastapi import FastAPI, Query
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

# Define the CreditLogView model
class CreditLogView(BaseModel):
    Date: str
    Note: str
    OriginalCreditCount: int
    CreditCount: int
    UserFullName: str

# Define the PageableData model
class PageableData(BaseModel):
    Results: List[CreditLogView]
    PageInfo: dict


