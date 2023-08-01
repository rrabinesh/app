# <?php

# require_once(ROOT_DIR . 'Domain/Accessory.php');

# interface IAccessoryRepository
# {
#     /**
#      * @param int $accessoryId
#      * @return Accessory
#      */
#     public function LoadById($accessoryId);

#     /**
#      * @return Accessory[]
#      */
#     public function LoadAll();

#     /**
#      * @param Accessory $accessory
#      * @return int
#      */
#     public function Add(Accessory $accessory);

#     /**
#      * @param Accessory $accessory
#      * @return void
#      */
#     public function Update(Accessory $accessory);

#     /**
#      * @param int $accessoryId
#      * @return void
#      */
#     public function Delete($accessoryId);
# }

# class AccessoryRepository implements IAccessoryRepository
# {
#     /**
#      * @param int $accessoryId
#      * @return Accessory
#      */
#     public function LoadById($accessoryId)
#     {
#         $reader = ServiceLocator::GetDatabase()->Query(new GetAccessoryByIdCommand($accessoryId));

#         if ($row = $reader->GetRow()) {
#             $accessory = new Accessory($row[ColumnNames::ACCESSORY_ID], $row[ColumnNames::ACCESSORY_NAME], $row[ColumnNames::ACCESSORY_QUANTITY]);
#             $arReader = ServiceLocator::GetDatabase()->Query(new GetAccessoryResources($accessoryId));

#             while ($row = $arReader->GetRow()) {
#                 $accessory->AddResource($row[ColumnNames::RESOURCE_ID], $row[ColumnNames::ACCESSORY_MINIMUM_QUANTITY], $row[ColumnNames::ACCESSORY_MAXIMUM_QUANTITY]);
#             }

#             $reader->Free();

#             return $accessory;
#         }

#         return null;
#     }

#     /**
#      * @param Accessory $accessory
#      * @return int
#      */
#     public function Add(Accessory $accessory)
#     {
#         return ServiceLocator::GetDatabase()->ExecuteInsert(new AddAccessoryCommand($accessory->GetName(), $accessory->GetQuantityAvailable()));
#     }

#     /**
#      * @param Accessory $accessory
#      * @return void
#      */
#     public function Update(Accessory $accessory)
#     {
#         ServiceLocator::GetDatabase()->Execute(new UpdateAccessoryCommand($accessory->GetId(), $accessory->GetName(), $accessory->GetQuantityAvailable()));
#         ServiceLocator::GetDatabase()->Execute(new DeleteAcccessoryResourcesCommand($accessory->GetId()));
#         foreach ($accessory->Resources() as $resource) {
#             ServiceLocator::GetDatabase()->Execute(new AddAccessoryResourceCommand($accessory->GetId(), $resource->ResourceId, $resource->MinQuantity, $resource->MaxQuantity));
#         }
#     }

#     /**
#      * @param int $accessoryId
#      * @return void
#      */
#     public function Delete($accessoryId)
#     {
#         ServiceLocator::GetDatabase()->Execute(new DeleteAccessoryCommand($accessoryId));
#     }

#     /**
#      * @return Accessory[]
#      */
#     public function LoadAll()
#     {
#         $reader = ServiceLocator::GetDatabase()->Query(new GetAllAccessoriesCommand());
#         $accessories = [];

#         while ($row = $reader->GetRow()) {
#             $accessory = new Accessory($row[ColumnNames::ACCESSORY_ID], $row[ColumnNames::ACCESSORY_NAME], $row[ColumnNames::ACCESSORY_QUANTITY]);

#             $resourceList = $row[ColumnNames::RESOURCE_ACCESSORY_LIST];
#             if (!empty($resourceList)) {
#                 $pairs = explode('!sep!', $resourceList);

#                 foreach ($pairs as $pair) {
#                     $nv = explode(',', $pair);
#                     $accessory->AddResource($nv[0], $nv[1], $nv[2]);
#                 }
#             }

#             $accessories[] = $accessory;
#         }

#         $reader->Free();
#         return $accessories;
#     }
# }

from sqlalchemy import Column, Integer, String, create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import List

# Assuming you have defined Accessory table in the database
# and created an SQLAlchemy engine named 'engine'
Base = declarative_base()
metadata = MetaData(bind=engine)

class Accessory(Base):
    __table__ = Table('accessory', metadata, autoload=True)

class IAccessoryRepository:
    def load_by_id(self, accessory_id: int) -> Accessory:
        pass

    def load_all(self) -> List[Accessory]:
        pass

    def add(self, accessory: Accessory) -> int:
        pass

    def update(self, accessory: Accessory) -> None:
        pass

    def delete(self, accessory_id: int) -> None:
        pass

class AccessoryRepository(IAccessoryRepository):
    def load_by_id(self, accessory_id: int) -> Accessory:
        # Assuming you have already set up the SQLAlchemy session
        session = sessionmaker(bind=engine)()
        accessory = session.query(Accessory).filter_by(accessory_id=accessory_id).first()
        session.close()
        return accessory

    def load_all(self) -> List[Accessory]:
        session = sessionmaker(bind=engine)()
        accessories = session.query(Accessory).all()
        session.close()
        return accessories

    def add(self, accessory: Accessory) -> int:
        session = sessionmaker(bind=engine)()
        session.add(accessory)
        session.commit()
        session.close()
        return accessory.accessory_id

    def update(self, accessory: Accessory) -> None:
        session = sessionmaker(bind=engine)()
        session.merge(accessory)
        session.commit()
        session.close()

    def delete(self, accessory_id: int) -> None:
        session = sessionmaker(bind=engine)()
        accessory = session.query(Accessory).filter_by(accessory_id=accessory_id).first()
        if accessory:
            session.delete(accessory)
            session.commit()
        session.close()

