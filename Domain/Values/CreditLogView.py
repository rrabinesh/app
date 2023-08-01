# <?php

# require_once(ROOT_DIR . 'Domain/Values/FullName.php');

# class CreditLogView
# {
#     /**
#      * @var Date
#      */
#     public $Date;

#     /**
#      * @var string
#      */
#     public $Note;

#     /**
#      * @var int
#      */
#     public $OriginalCreditCount;

#     /**
#      * @var int
#      */
#     public $CreditCount;

#     /**
#      * @var string
#      */
#     public $UserFullName;

#     public function __construct($date, $note, $originalCount, $count, $userFullName = '')
#     {
#         $this->Date = $date;
#         $this->Note = $note;
#         $this->OriginalCreditCount = $originalCount;
#         $this->CreditCount = $count;
#         $this->UserFullName = $userFullName;
#     }

#     /**
#      * @param array $row
#      * @return CreditLogView
#      */
#     public static function Populate($row)
#     {
#         $userName = '';
#         if (isset($row[ColumnNames::FIRST_NAME])) {
#             $userName = new FullName($row[ColumnNames::FIRST_NAME], $row[ColumnNames::LAST_NAME]);
#         }

#         return new CreditLogView(
#             Date::FromDatabase($row[ColumnNames::DATE_CREATED]),
#             $row[ColumnNames::CREDIT_NOTE],
#             $row[ColumnNames::ORIGINAL_CREDIT_COUNT],
#             $row[ColumnNames::CREDIT_COUNT],
#             $userName->__toString()
#         );
#     }
# }

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()

# Pydantic model to represent the CreditLogView data structure
class CreditLogViewModel(BaseModel):
    Date: date
    Note: str
    OriginalCreditCount: int
    CreditCount: int
    UserFullName: str

# Implement the FullName class functionality (for demo purposes)
class FullName:
    def __init__(self, first_name: str, last_name: str):
        self.full_name = f"{first_name} {last_name}"

    def __str__(self):
        return self.full_name

# FastAPI endpoint to populate the CreditLogView
@app.post("/populate-credit-log-view/", response_model=CreditLogViewModel)
def populate_credit_log_view(credit_log_view_model: CreditLogViewModel):
    # For demo purposes, we'll simply create a FullName object using the provided data
    user_full_name = FullName(credit_log_view_model.UserFullName, "")
    credit_log_view_model.UserFullName = str(user_full_name)
    return credit_log_view_model


