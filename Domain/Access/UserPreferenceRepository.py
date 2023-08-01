# <?php

# require_once(ROOT_DIR . 'Domain/User.php');

# interface IUserPreferenceRepository
# {
#     /**
#      * @abstract
#      * @param $userId int
#      * @return array|string[] values, indexed by name
#      */
#     public function GetAllUserPreferences($userId);

#     /**
#      * @abstract
#      * @param $userId int
#      * @param $preferenceName string
#      * @return string|null
#      */
#     public function GetUserPreference($userId, $preferenceName);

#     /**
#      * @abstract
#      * @param $userId int
#      * @param $preferenceName string
#      * @param $preferenceValue string
#      * @return void
#      */
#     public function SetUserPreference($userId, $preferenceName, $preferenceValue);
# }

# class UserPreferenceRepository implements IUserPreferenceRepository
# {
#     /**
#      * @param $userId int
#      * @return array|string[] values, indexed by name
#      */
#     public function GetAllUserPreferences($userId)
#     {
#         $reader = ServiceLocator::GetDatabase()->Query(new GetUserPreferencesCommand($userId));

#         $rv = [];
#         while ($row = $reader->GetRow()) {
#             $rv[$row[ColumnNames::PREFERENCE_NAME]] = $row[ColumnNames::PREFERENCE_VALUE];
#         }

#         $reader->Free();
#         return $rv;
#     }

#     /**
#      * @param $userId int
#      * @param $preferenceName string
#      * @return string|null
#      */
#     public function GetUserPreference($userId, $preferenceName)
#     {
#         $reader = ServiceLocator::GetDatabase()->Query(new GetUserPreferenceCommand($userId, $preferenceName));

#         if ($row = $reader->GetRow()) {
#             $reader->Free();
#             return $row[ColumnNames::PREFERENCE_VALUE];
#         }

#         $reader->Free();
#         return null;
#     }

#     /**
#      * @param $userId int
#      * @param $preferenceName string
#      * @param $preferenceValue string
#      * @return void
#      */
#     public function SetUserPreference($userId, $preferenceName, $preferenceValue)
#     {
#         $db = ServiceLocator::GetDatabase();

#         $existingValue = self::GetUserPreference($userId, $preferenceName);
#         if (is_null($existingValue)) {
#             $db->ExecuteInsert(new AddUserPreferenceCommand($userId, $preferenceName, $preferenceValue));
#         } elseif ($existingValue != $preferenceValue) {
#             $db->Execute(new UpdateUserPreferenceCommand($userId, $preferenceName, $preferenceValue));
#         }
#     }
# }



from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI()

# Dummy data for demonstration purposes
class UserPreference(BaseModel):
    userId: int
    preferenceName: str
    preferenceValue: str


# FastAPI UserPreferenceRepository equivalent (dummy implementation)
class UserPreferenceRepository:
    def get_all_user_preferences(self, user_id: int) -> Dict[str, str]:
        # Replace this with your actual database query operation
        # For demonstration purposes, we'll return dummy data
        return {"preference1": "value1", "preference2": "value2"}

    def get_user_preference(self, user_id: int, preference_name: str) -> Optional[str]:
        # Replace this with your actual database query operation
        # For demonstration purposes, we'll return a dummy value
        return "value1"

    def set_user_preference(self, user_id: int, preference_name: str, preference_value: str):
        # Replace this with your actual database insert/update operation
        # For demonstration purposes, we'll return a success message
        return {"message": f"Preference '{preference_name}' set to '{preference_value}'."}


# Route to get all user preferences (GET request)
@app.get("/user/preferences/{user_id}", response_model=Dict[str, str])
def get_all_user_preferences(user_id: int):
    user_pref_repo = UserPreferenceRepository()
    return user_pref_repo.get_all_user_preferences(user_id)


# Route to get a user preference (GET request)
@app.get("/user/preferences/{user_id}/{preference_name}", response_model=UserPreference)
def get_user_preference(user_id: int, preference_name: str):
    user_pref_repo = UserPreferenceRepository()
    preference_value = user_pref_repo.get_user_preference(user_id, preference_name)
    return UserPreference(userId=user_id, preferenceName=preference_name, preferenceValue=preference_value)


# Route to set a user preference (PUT request)
@app.put("/user/preferences/{user_id}/{preference_name}/{preference_value}", response_model=dict)
def set_user_preference(user_id: int, preference_name: str, preference_value: str):
    user_pref_repo = UserPreferenceRepository()
    user_pref_repo.set_user_preference(user_id, preference_name, preference_value)
    return {"message": "Preference set successfully."}



