# <?php

# require_once(ROOT_DIR . 'Domain/CustomAttribute.php');

# interface IAttributeRepository
# {
#     /**
#      * @abstract
#      * @param CustomAttribute $attribute
#      * @return int
#      */
#     public function Add(CustomAttribute $attribute);

#     /**
#      * @abstract
#      * @param $attributeId int
#      * @return CustomAttribute
#      */
#     public function LoadById($attributeId);

#     /**
#      * @abstract
#      * @param CustomAttribute $attribute
#      */
#     public function Update(CustomAttribute $attribute);

#     /**
#      * @abstract
#      * @param $attributeId int
#      * @return void
#      */
#     public function DeleteById($attributeId);

#     /**
#      * @abstract
#      * @param int|CustomAttributeCategory $category
#      * @return array|CustomAttribute[]
#      */
#     public function GetByCategory($category);

#     /**
#      * @abstract
#      * @param int|CustomAttributeCategory $category
#      * @param array|int[] $entityIds if null is passed, get all entity values
#      * @return array|AttributeEntityValue[]
#      */
#     public function GetEntityValues($category, $entityIds = null);
# }

# class AttributeRepository implements IAttributeRepository
# {
#     /**
#      * @var DomainCache
#      */
#     private $cache;

#     public function __construct()
#     {
#         $this->cache = new DomainCache();
#     }

#     public function Add(CustomAttribute $attribute)
#     {
#         $id = ServiceLocator::GetDatabase()->ExecuteInsert(
#             new AddAttributeCommand(
#                 $attribute->Label(),
#                 $attribute->Type(),
#                 $attribute->Category(),
#                 $attribute->Regex(),
#                 $attribute->Required(),
#                 $attribute->PossibleValues(),
#                 $attribute->SortOrder(),
#                 $attribute->AdminOnly(),
#                 $attribute->SecondaryCategory(),
#                 $attribute->SecondaryEntityIds(),
#                 $attribute->IsPrivate()
#             )
#         );

#         foreach ($attribute->EntityIds() as $entityId) {
#             ServiceLocator::GetDatabase()->ExecuteInsert(new AddAttributeEntityCommand($id, $entityId));
#         }

#         return $id;
#     }

#     /**
#      * @param int|CustomAttributeCategory $category
#      * @return array|CustomAttribute[]
#      */
#     public function GetByCategory($category)
#     {
#         if (!$this->cache->Exists($category)) {
#             $reader = ServiceLocator::GetDatabase()->Query(new GetAttributesByCategoryCommand($category));

#             $attributes = [];
#             while ($row = $reader->GetRow()) {
#                 $attributes[] = CustomAttribute::FromRow($row);
#             }

#             $this->cache->Add($category, $attributes);
#             $reader->Free();
#         }

#         return $this->cache->Get($category);
#     }

#     /**
#      * @param $attributeId int
#      * @return CustomAttribute
#      */
#     public function LoadById($attributeId)
#     {
#         $reader = ServiceLocator::GetDatabase()->Query(new GetAttributeByIdCommand($attributeId));

#         $attribute = null;
#         if ($row = $reader->GetRow()) {
#             $attribute = CustomAttribute::FromRow($row);
#         }

#         $reader->Free();
#         return $attribute;
#     }

#     /**
#      * @param CustomAttribute $attribute
#      */
#     public function Update(CustomAttribute $attribute)
#     {
#         $db = ServiceLocator::GetDatabase();
#         $db->Execute(new UpdateAttributeCommand(
#             $attribute->Id(),
#             $attribute->Label(),
#             $attribute->Type(),
#             $attribute->Category(),
#             $attribute->Regex(),
#             $attribute->Required(),
#             $attribute->PossibleValues(),
#             $attribute->SortOrder(),
#             $attribute->AdminOnly(),
#             $attribute->SecondaryCategory(),
#             $attribute->SecondaryEntityIds(),
#             $attribute->IsPrivate()
#         ));

#         foreach ($attribute->RemovedEntityIds() as $entityId) {
#             $db->Execute(new RemoveAttributeEntityCommand($attribute->Id(), $entityId));
#         }

#         foreach ($attribute->AddedEntityIds() as $entityId) {
#             $db->Execute(new AddAttributeEntityCommand($attribute->Id(), $entityId));
#         }
#     }

#     /**
#      * @param int|CustomAttributeCategory $category
#      * @param array|int[] $entityIds
#      * @return array|AttributeEntityValue[]
#      */
#     public function GetEntityValues($category, $entityIds = null)
#     {
#         $values = [];

#         if (!is_array($entityIds) && !empty($entityIds)) {
#             $entityIds = [$entityIds];
#         }

#         if (empty($entityIds)) {
#             $reader = ServiceLocator::GetDatabase()
#                                     ->Query(new GetAttributeAllValuesCommand($category));
#         } else {
#             $reader = ServiceLocator::GetDatabase()
#                                     ->Query(new GetAttributeMultipleValuesCommand($category, $entityIds));
#         }
#         $attribute = null;
#         while ($row = $reader->GetRow()) {
#             $values[] = new AttributeEntityValue(
#                 $row[ColumnNames::ATTRIBUTE_ID],
#                 $row[ColumnNames::ATTRIBUTE_ENTITY_ID],
#                 $row[ColumnNames::ATTRIBUTE_VALUE]
#             );
#         }

#         $reader->Free();
#         return $values;
#     }

#     public function DeleteById($attributeId)
#     {
#         ServiceLocator::GetDatabase()->Execute(new DeleteAttributeCommand($attributeId));
#         ServiceLocator::GetDatabase()->Execute(new DeleteAttributeValuesCommand($attributeId));
#         ServiceLocator::GetDatabase()->Execute(new DeleteAttributeColorRulesCommand($attributeId));
#     }
# }


from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Replace the database URL with your actual database connection string
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Define the SQLAlchemy model for CustomAttribute
class CustomAttribute(Base):
    __tablename__ = "custom_attributes"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, index=True)
    type = Column(String)
    category = Column(String)
    regex = Column(String)
    required = Column(String)
    possible_values = Column(String)
    sort_order = Column(Integer)
    admin_only = Column(String)
    secondary_category = Column(String)
    secondary_entity_ids = Column(String)
    is_private = Column(String)

# Add your database models and table definitions here, if needed
# class AttributeEntityValue(Base):
#     __tablename__ = "attribute_entity_values"
#     ...

# ...

# Add your database CRUD operations here, using the SessionLocal provided above
# For example, to add an attribute to the database:
def add_attribute(attribute: CustomAttribute):
    db = SessionLocal()
    db.add(attribute)
    db.commit()
    db.refresh(attribute)
    return attribute

# ...

# FastAPI endpoints for CRUD operations
@app.post("/attributes/", response_model=CustomAttribute)
def create_attribute(attribute: CustomAttribute):
    db_attribute = add_attribute(attribute)
    return db_attribute

@app.get("/attributes/{attribute_id}", response_model=CustomAttribute)
def get_attribute(attribute_id: int):
    db = SessionLocal()
    attribute = db.query(CustomAttribute).filter(CustomAttribute.id == attribute_id).first()
    if attribute is None:
        raise HTTPException(status_code=404, detail="Attribute not found")
    return attribute

# Add other endpoints for updating, deleting, and fetching attributes based on category/entity IDs
# ...

# Run the FastAPI application with uvicorn
# uvicorn main:app --reload

