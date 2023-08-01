# <?php

# require_once(ROOT_DIR . 'Domain/Announcement.php');

# class AnnouncementRepository implements IAnnouncementRepository
# {
#     public function GetFuture($displayPage = -1)
#     {
#         $announcements = [];

#         $reader = ServiceLocator::GetDatabase()->Query(new GetDashboardAnnouncementsCommand(Date::Now(), $displayPage));

#         while ($row = $reader->GetRow()) {
#             $announcements[] = Announcement::FromRow($row);
#         }

#         $reader->Free();

#         return $announcements;
#     }

#     public function GetAll($sortField = null, $sortDirection = null)
#     {
#         $announcements = [];

#         $command = new GetAllAnnouncementsCommand();

#         if (!empty($sortField)) {
#             $command = new SortCommand($command, $sortField, $sortDirection);
#         }

#         $reader = ServiceLocator::GetDatabase()->Query($command);

#         while ($row = $reader->GetRow()) {
#             $announcements[] = Announcement::FromRow($row);
#         }

#         $reader->Free();

#         return $announcements;
#     }

#     /**
#      * @param Announcement $announcement
#      */
#     public function Add(Announcement $announcement)
#     {
#         $db = ServiceLocator::GetDatabase();
#         $announcementId = $db->ExecuteInsert(
#             new AddAnnouncementCommand(
#                 $announcement->Text(),
#                 $announcement->Start(),
#                 $announcement->End(),
#                 $announcement->Priority(),
#                 $announcement->DisplayPage()
#             )
#         );

#         foreach ($announcement->GroupIds() as $groupId) {
#             $db->ExecuteInsert(new AddAnnouncementGroupCommand($announcementId, $groupId));
#         }

#         foreach ($announcement->ResourceIds() as $resourceId) {
#             $db->ExecuteInsert(new AddAnnouncementResourceCommand($announcementId, $resourceId));
#         }
#     }

#     /**
#      * @param int $announcementId
#      */
#     public function Delete($announcementId)
#     {
#         ServiceLocator::GetDatabase()->Execute(new DeleteAnnouncementCommand($announcementId));
#     }

#     /**
#      * @param int $announcementId
#      * @return Announcement
#      */
#     public function LoadById($announcementId)
#     {
#         $announcement = null;
#         $reader = ServiceLocator::GetDatabase()->Query(new GetAnnouncementByIdCommand($announcementId));

#         if ($row = $reader->GetRow()) {
#             $announcement = Announcement::FromRow($row);
#         }

#         $reader->Free();
#         return $announcement;
#     }

#     public function Update(Announcement $announcement)
#     {
#         $this->Delete($announcement->Id());
#         $this->Add($announcement);
#     }
# }

# interface IAnnouncementRepository
# {
#     /**
#      * Gets all announcements to be displayed for the user
#      * @param int $page
#      * @return Announcement[]
#      */
#     public function GetFuture($page);

#     /**
#      * @param null|string $sortField
#      * @param null|string $sortDirection
#      * @return Announcement[]|array
#      */
#     public function GetAll($sortField = null, $sortDirection = null);

#     /**
#      * @param Announcement $announcement
#      */
#     public function Add(Announcement $announcement);

#     /**
#      * @param Announcement $announcement
#      */
#     public function Update(Announcement $announcement);

#     /**
#      * @param int $announcementId
#      */
#     public function Delete($announcementId);

#     /**
#      * @param int $announcementId
#      * @return Announcement
#      */
#     public function LoadById($announcementId);
# }


from fastapi import FastAPI, HTTPException
from sqlalchemy import Column, Integer, String, DateTime, create_engine, MetaData, Table, desc, asc
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import List, Optional

app = FastAPI()

# Assuming you have defined Announcement table in the database
# and created an SQLAlchemy engine named 'engine'
Base = declarative_base()
metadata = MetaData(bind=engine)

class Announcement(Base):
    __table__ = Table('announcement', metadata, autoload=True)

class IAnnouncementRepository:
    def get_future(self, page: int = -1) -> List[Announcement]:
        pass

    def get_all(self, sort_field: Optional[str] = None, sort_direction: Optional[str] = None) -> List[Announcement]:
        pass

    def add(self, announcement: Announcement) -> None:
        pass

    def update(self, announcement: Announcement) -> None:
        pass

    def delete(self, announcement_id: int) -> None:
        pass

    def load_by_id(self, announcement_id: int) -> Announcement:
        pass

class AnnouncementRepository(IAnnouncementRepository):
    def get_future(self, page: int = -1) -> List[Announcement]:
        session = sessionmaker(bind=engine)()
        announcements = (
            session.query(Announcement)
            .filter(Announcement.start >= datetime.now())
            .limit(page)
            .all()
        )
        session.close()
        return announcements

    def get_all(self, sort_field: Optional[str] = None, sort_direction: Optional[str] = None) -> List[Announcement]:
        session = sessionmaker(bind=engine)()
        query = session.query(Announcement)

        if sort_field:
            column = getattr(Announcement, sort_field)
            if sort_direction == 'desc':
                query = query.order_by(desc(column))
            else:
                query = query.order_by(asc(column))

        announcements = query.all()
        session.close()
        return announcements

    def add(self, announcement: Announcement) -> None:
        session = sessionmaker(bind=engine)()
        session.add(announcement)
        session.commit()
        session.close()

    def update(self, announcement: Announcement) -> None:
        session = sessionmaker(bind=engine)()
        session.merge(announcement)
        session.commit()
        session.close()

    def delete(self, announcement_id: int) -> None:
        session = sessionmaker(bind=engine)()
        announcement = session.query(Announcement).filter_by(id=announcement_id).first()
        if announcement:
            session.delete(announcement)
            session.commit()
        session.close()

    def load_by_id(self, announcement_id: int) -> Announcement:
        session = sessionmaker(bind=engine)()
        announcement = session.query(Announcement).filter_by(id=announcement_id).first()
        session.close()
        return announcement

# Create an instance of the AnnouncementRepository
announcement_repository = AnnouncementRepository()

@app.get("/announcements/future/")
def get_future_announcements(page: int = -1):
    announcements = announcement_repository.get_future(page)
    return announcements

@app.get("/announcements/")
def get_all_announcements(sort_field: Optional[str] = None, sort_direction: Optional[str] = None):
    announcements = announcement_repository.get_all(sort_field, sort_direction)
    return announcements

# Implement other endpoints for adding, updating, and deleting announcements if needed


