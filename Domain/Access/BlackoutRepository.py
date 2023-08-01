# <?php

# require_once(ROOT_DIR . 'Domain/Blackout.php');

# interface IBlackoutRepository
# {
#     /**
#      * @param BlackoutSeries $blackoutSeries
#      * @return int
#      */
#     public function Add(BlackoutSeries $blackoutSeries);

#     /**
#      * @param BlackoutSeries $blackoutSeries
#      */
#     public function Update(BlackoutSeries $blackoutSeries);

#     /**
#      * @param int $blackoutId
#      */
#     public function Delete($blackoutId);

#     /**
#      * @param int $blackoutId
#      */
#     public function DeleteSeries($blackoutId);

#     /**
#      * @param int $blackoutId
#      * @return BlackoutSeries
#      */
#     public function LoadByBlackoutId($blackoutId);
# }

# class BlackoutRepository implements IBlackoutRepository
# {
#     /**
#      * @param BlackoutSeries $blackoutSeries
#      * @return int
#      */
#     public function Add(BlackoutSeries $blackoutSeries)
#     {
#         $seriesId = $this->AddSeries($blackoutSeries);
#         foreach ($blackoutSeries->AllBlackouts() as $blackout) {
#             ServiceLocator::GetDatabase()->ExecuteInsert(new AddBlackoutInstanceCommand($seriesId, $blackout->StartDate(), $blackout->EndDate()));
#         }

#         return $seriesId;
#     }

#     private function AddSeries(BlackoutSeries $blackoutSeries)
#     {
#         $db = ServiceLocator::GetDatabase();
#         $seriesId = $db->ExecuteInsert(new AddBlackoutCommand(
#             $blackoutSeries->OwnerId(),
#             $blackoutSeries->Title(),
#             $blackoutSeries->RepeatType(),
#             $blackoutSeries->RepeatConfigurationString()
#         ));

#         foreach ($blackoutSeries->ResourceIds() as $resourceId) {
#             $db->ExecuteInsert(new AddBlackoutResourceCommand($seriesId, $resourceId));
#         }

#         return $seriesId;
#     }

#     /**
#      * @param int $blackoutId
#      */
#     public function Delete($blackoutId)
#     {
#         ServiceLocator::GetDatabase()->Execute(new DeleteBlackoutInstanceCommand($blackoutId));
#     }

#     /**
#      * @param int $blackoutId
#      */
#     public function DeleteSeries($blackoutId)
#     {
#         ServiceLocator::GetDatabase()->Execute(new DeleteBlackoutSeriesCommand($blackoutId));
#     }

#     /**
#      * @param int $blackoutId
#      * @return BlackoutSeries
#      */
#     public function LoadByBlackoutId($blackoutId)
#     {
#         $db = ServiceLocator::GetDatabase();
#         $reader = $db->Query(new GetBlackoutSeriesByBlackoutIdCommand($blackoutId));

#         if ($row = $reader->GetRow()) {
#             $series = BlackoutSeries::FromRow($row);

#             $result = $db->Query(new GetBlackoutInstancesCommand($series->Id()));

#             while ($row = $result->GetRow()) {
#                 $instance = new Blackout(new DateRange(
#                     Date::FromDatabase($row[ColumnNames::BLACKOUT_START]),
#                     Date::FromDatabase($row[ColumnNames::BLACKOUT_END])
#                 ));
#                 $instance->WithId($row[ColumnNames::BLACKOUT_INSTANCE_ID]);
#                 $series->AddBlackout($instance);
#             }
#             $result->Free();

#             $result = $db->Query(new GetBlackoutResourcesCommand($series->Id()));

#             while ($row = $result->GetRow()) {
#                 $series->AddResource(new BlackoutResource(
#                     $row[ColumnNames::RESOURCE_ID],
#                     $row[ColumnNames::RESOURCE_NAME],
#                     $row[ColumnNames::SCHEDULE_ID],
#                     $row[ColumnNames::RESOURCE_ADMIN_GROUP_ID],
#                     $row[ColumnNames::SCHEDULE_ADMIN_GROUP_ID_ALIAS],
#                     $row[ColumnNames::RESOURCE_STATUS_ID]
#                 ));
#             }

#             $result->Free();
#             $reader->Free();
#             return $series;
#         }

#         $reader->Free();
#         return null;
#     }

#     /**
#      * @param BlackoutSeries $blackoutSeries
#      */
#     public function Update(BlackoutSeries $blackoutSeries)
#     {
#         if ($blackoutSeries->IsNew()) {
#             $seriesId = $this->AddSeries($blackoutSeries);
#             $db = ServiceLocator::GetDatabase();
#             $start = $blackoutSeries->CurrentBlackout()->StartDate();
#             $end = $blackoutSeries->CurrentBlackout()->EndDate();
#             $db->Execute(new UpdateBlackoutInstanceCommand($blackoutSeries->CurrentBlackoutInstanceId(), $seriesId, $start, $end));
#         } else {
#             $this->DeleteSeries($blackoutSeries->CurrentBlackoutInstanceId());
#             $this->Add($blackoutSeries);
#         }
#     }
# }

class BlackoutSeries(Base):
    __tablename__ = "blackout_series"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer)
    title = Column(String)
    repeat_type = Column(String)
    repeat_configuration_string = Column(String)

    blackouts = relationship("Blackout", back_populates="series")
    resources = relationship("BlackoutResource", back_populates="series")

class Blackout(Base):
    __tablename__ = "blackouts"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(String)
    end_date = Column(String)
    series_id = Column(Integer, ForeignKey("blackout_series.id"))

    series = relationship("BlackoutSeries", back_populates="blackouts")

class BlackoutResource(Base):
    __tablename__ = "blackout_resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    schedule_id = Column(Integer)
    resource_admin_group_id = Column(Integer)
    schedule_admin_group_id_alias = Column(Integer)
    resource_status_id = Column(Integer)
    series_id = Column(Integer, ForeignKey("blackout_series.id"))

    series = relationship("BlackoutSeries", back_populates="resources")

# Create the database tables
Base.metadata.create_all(bind=engine)

# Add your database CRUD operations here using the SessionLocal provided above
# For example, to add a blackout series to the database:
def add_blackout_series(blackout_series: BlackoutSeries):
    db = SessionLocal()
    db.add(blackout_series)
    db.commit()
    db.refresh(blackout_series)
    return blackout_series

# ...

# FastAPI endpoints for CRUD operations
class BlackoutSeriesCreate(BaseModel):
    owner_id: int
    title: str
    repeat_type: str
    repeat_configuration_string: str

class BlackoutCreate(BaseModel):
    start_date: str
    end_date: str


