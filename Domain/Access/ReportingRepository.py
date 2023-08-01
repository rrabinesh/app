# <?php

# require_once(ROOT_DIR . 'Domain/Access/namespace.php');
# require_once(ROOT_DIR . 'Domain/Access/ReportCommandBuilder.php');
# require_once(ROOT_DIR . 'Domain/SavedReport.php');

# interface IReportingRepository
# {
#     /**
#      * @param ReportCommandBuilder $commandBuilder
#      * @return array
#      */
#     public function GetCustomReport(ReportCommandBuilder $commandBuilder);

#     /**
#      * @param SavedReport $savedReport
#      */
#     public function SaveCustomReport(SavedReport $savedReport);

#     /**
#      * @param int $userId
#      * @return array|SavedReport[]
#      */
#     public function LoadSavedReportsForUser($userId);

#     /**
#      * @param int $reportId
#      * @param int $userId
#      * @return SavedReport
#      */
#     public function LoadSavedReportForUser($reportId, $userId);

#     /**
#      * @param int $reportId
#      * @param int $userId
#      */
#     public function DeleteSavedReport($reportId, $userId);
# }

# class ReportingRepository implements IReportingRepository
# {
#     /**
#      * @param ReportCommandBuilder $commandBuilder
#      * @return array
#      */
#     public function GetCustomReport(ReportCommandBuilder $commandBuilder)
#     {
#         $query = $commandBuilder->Build();
#         $reader = ServiceLocator::GetDatabase()->Query($query);
#         $rows = [];
#         while ($row = $reader->GetRow()) {
#             $row[ColumnNames::DURATION_HOURS] = round($row[ColumnNames::DURATION_ALIAS] / 3600, 2);
#             $rows[] = $row;
#         }
#         $reader->Free();

#         return $rows;
#     }

#     public function SaveCustomReport(SavedReport $report)
#     {
#         $serialized = ReportSerializer::Serialize($report);
#         ServiceLocator::GetDatabase()->ExecuteInsert(new AddSavedReportCommand($report->ReportName(), $report->OwnerId(), $report->DateCreated(), $serialized));
#     }

#     /**
#      * @param $userId
#      * @return array|SavedReport[]
#      */
#     public function LoadSavedReportsForUser($userId)
#     {
#         $reader = ServiceLocator::GetDatabase()->Query(new GetAllSavedReportsForUserCommand($userId));
#         $reports = [];
#         while ($row = $reader->GetRow()) {
#             $reports[] = SavedReport::FromDatabase(
#                 $row[ColumnNames::REPORT_NAME],
#                 $row[ColumnNames::USER_ID],
#                 Date::FromDatabase($row[ColumnNames::DATE_CREATED]),
#                 $row[ColumnNames::REPORT_DETAILS],
#                 $row[ColumnNames::REPORT_ID]
#             );
#         }
#         $reader->Free();

#         return $reports;
#     }

#     /**
#      * @param int $reportId
#      * @param int $userId
#      * @return SavedReport
#      */
#     public function LoadSavedReportForUser($reportId, $userId)
#     {
#         $reader = ServiceLocator::GetDatabase()->Query(new GetSavedReportForUserCommand($reportId, $userId));

#         if ($row = $reader->GetRow()) {
#             $reader->Free();
#             return SavedReport::FromDatabase(
#                 $row[ColumnNames::REPORT_NAME],
#                 $row[ColumnNames::USER_ID],
#                 Date::FromDatabase($row[ColumnNames::DATE_CREATED]),
#                 $row[ColumnNames::REPORT_DETAILS],
#                 $row[ColumnNames::REPORT_ID]
#             );
#         }
#         $reader->Free();
#         return null;
#     }

#     public function DeleteSavedReport($reportId, $userId)
#     {
#         ServiceLocator::GetDatabase()->Execute(new DeleteSavedReportCommand($reportId, $userId));
#     }
# }

class SavedReport(Base):
    __tablename__ = 'saved_reports'

    id = Column(Integer, primary_key=True, index=True)
    report_name = Column(String, index=True)
    user_id = Column(Integer, index=True)
    date_created = Column(DateTime)
    report_details = Column(String)

# Pydantic models
class SavedReportInDB(BaseModel):
    id: int
    report_name: str
    user_id: int
    date_created: str
    report_details: str

class ReportCommandBuilder(BaseModel):
    # Add the necessary fields from the original PHP class here
    pass

# Database functions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)

# API Endpoints
@app.post("/custom_report/", response_model=List[SavedReportInDB])
def get_custom_report(command_builder: ReportCommandBuilder):
    # Implement the logic for fetching custom reports from the database using the provided 'command_builder'
    # Replace this dummy data with the actual database query and logic
    reports = [
        SavedReportInDB(id=1, report_name="Report 1", user_id=1, date_created="2023-07-25 12:00:00", report_details="Details 1"),
        SavedReportInDB(id=2, report_name="Report 2", user_id=1, date_created="2023-07-25 13:00:00", report_details="Details 2"),
    ]
    return reports

@app.post("/save_report/", response_model=SavedReportInDB)
def save_custom_report(report: SavedReport):
    # Implement the logic to save the custom report in the database
    # Replace this dummy data with the actual database insert and logic
    saved_report = SavedReportInDB(
        id=1,
        report_name=report.report_name,
        user_id=report.user_id,
        date_created=report.date_created,
        report_details=report.report_details
    )
    return saved_report

@app.get("/reports/{user_id}/", response_model=List[SavedReportInDB])
def load_saved_reports_for_user(user_id: int, db=Depends(get_db)):
    # Implement the logic to load saved reports for the given user from the database
    # Replace this dummy data with the actual database query and logic
    reports = [
        SavedReportInDB(id=1, report_name="Report 1", user_id=user_id, date_created="2023-07-25 12:00:00", report_details="Details 1"),
        SavedReportInDB(id=2, report_name="Report 2", user_id=user_id, date_created="2023-07-25 13:00:00", report_details="Details 2"),
    ]
    return reports

@app.get("/report/{report_id}/{user_id}", response_model=SavedReportInDB)
def load_saved_report_for_user(report_id: int, user_id: int, db=Depends(get_db)):
    # Implement the logic to load a saved report by report_id and user_id from the database
    # Replace this dummy data with the actual database query and logic
    report = SavedReportInDB(id=1, report_name="Report 1", user_id=user_id, date_created="2023-07-25 12:00:00", report_details="Details 1")
    return report

@app.delete("/report/{report_id}/{user_id}")
def delete_saved_report(report_id: int, user_id: int, db=Depends(get_db)):
    # Implement the logic to delete a saved report by report_id and user_id from the database
    # Replace this dummy data with the actual database delete and logic
    pass

