# <?php

# require_once(ROOT_DIR . 'Domain/Reminder.php');
# require_once(ROOT_DIR . 'Domain/ReminderNotice.php');

# class ReminderRepository implements IReminderRepository
# {
#     // select date_sub(start_date,INTERVAL rr.minutes_prior MINUTE) as reminder_date from reservation_instances ri INNER JOIN reservation_reminders rr on ri.series_id = rr.series_id

#     public function GetAll()
#     {
#         $reminders = [];

#         $reader = ServiceLocator::GetDatabase()->Query(new GetAllRemindersCommand());

#         while ($row = $reader->GetRow()) {
#             $reminders[] = Reminder::FromRow($row);
#         }
#         $reader->Free();
#         return $reminders;
#     }

#     /**
#      * @param Reminder $reminder
#      */
#     public function Add(Reminder $reminder)
#     {
#         ServiceLocator::GetDatabase()->ExecuteInsert(new AddReminderCommand(
#             $reminder->UserID(),
#             $reminder->Address(),
#             $reminder->Message(),
#             $reminder->SendTime(),
#             $reminder->RefNumber()
#         ));
#     }

#     /**
#      * @param string $user_id
#      * @return Reminder[]
#      */
#     public function GetByUser($user_id)
#     {
#         $reminders = [];
#         $reader = ServiceLocator::GetDatabase()->Query(new GetReminderByUserCommand($user_id));

#         while ($row = $reader->GetRow()) {
#             $reminders[] = Reminder::FromRow($row);
#         }

#         $reader->Free();
#         return $reminders;
#     }

#     /**
#      * @param string $refnumber
#      * @return Reminder[]
#      */
#     public function GetByRefNumber($refnumber)
#     {
#         $reminders = [];
#         $reader = ServiceLocator::GetDatabase()->Query(new GetReminderByRefNumberCommand($refnumber));

#         if ($row = $reader->GetRow()) {
#             $reminders = Reminder::FromRow($row);
#         }

#         $reader->Free();
#         return $reminders;
#     }

#     /**
#      * @param int $reminder_id
#      */
#     public function DeleteReminder($reminder_id)
#     {
#         ServiceLocator::GetDatabase()->Query(new DeleteReminderCommand($reminder_id));
#     }

#     /**
#      * @param $user_id
#      */
#     public function DeleteReminderByUser($user_id)
#     {
#         ServiceLocator::GetDatabase()->Query(new DeleteReminderByUserCommand($user_id));
#     }

#     /**
#      * @param $user_id
#      */
#     public function DeleteReminderByRefNumber($refnumber)
#     {
#         ServiceLocator::GetDatabase()->Query(new DeleteReminderByRefNumberCommand($refnumber));
#     }

#     /**
#      * @param Date $now
#      * @param ReservationReminderType|int $reminderType
#      * @return ReminderNotice[]|array
#      */
#     public function GetReminderNotices(Date $now, $reminderType)
#     {
#         $reader = ServiceLocator::GetDatabase()->Query(new GetReminderNoticesCommand($now->ToTheMinute(), $reminderType));

#         $notices = [];
#         while ($row = $reader->GetRow()) {
#             $notices[] = ReminderNotice::FromRow($row);
#         }

#         $reader->Free();
#         return $notices;
#     }
# }

# interface IReminderRepository
# {
#     /**
#      * @abstract
#      * @return Reminder[]|array
#      */
#     public function GetAll();

#     /**
#      * @abstract
#      * @param Reminder $reminder
#      */
#     public function Add(Reminder $reminder);

#     /**
#      * @abstract
#      * @param string $user_id
#      * @return Reminder[]|array
#      */
#     public function GetByUser($user_id);

#     /**
#      * @abstract
#      * @param string $refnumber
#      * @return Reminder[]|array
#      */
#     public function GetByRefNumber($refnumber);

#     /**
#      * @abstract
#      * @param int $reminder_id
#      */
#     public function DeleteReminder($reminder_id);

#     /**
#      * @abstract
#      * @param $user_id
#      */
#     public function DeleteReminderByUser($user_id);

#     /**
#      * @abstract
#      * @param $refnumber
#      */
#     public function DeleteReminderByRefNumber($refnumber);
# }


from fastapi import FastAPI
from typing import List

# Placeholder for classes not defined in the provided code
class Reminder:
    @staticmethod
    def from_row(row):
        pass

class ReminderNotice:
    @staticmethod
    def from_row(row):
        pass

class ServiceLocator:
    @staticmethod
    def get_database():
        pass

class GetAllRemindersCommand:
    pass

class AddReminderCommand:
    pass

class GetReminderByUserCommand:
    pass

class GetReminderByRefNumberCommand:
    pass

class DeleteReminderCommand:
    pass

class DeleteReminderByUserCommand:
    pass

class DeleteReminderByRefNumberCommand:
    pass

class GetReminderNoticesCommand:
    pass

# Create a FastAPI app
app = FastAPI()

# IReminderRepository interface (not explicitly needed in FastAPI)

# ReminderRepository implementation
class ReminderRepository:
    def get_all(self):
        reminders = []

        reader = ServiceLocator.get_database().query(GetAllRemindersCommand())

        while row := reader.get_row():
            reminders.append(Reminder.from_row(row))
        reader.free()
        return reminders

    def add(self, reminder):
        ServiceLocator.get_database().execute_insert(AddReminderCommand(
            reminder.user_id(),
            reminder.address(),
            reminder.message(),
            reminder.send_time(),
            reminder.ref_number()
        ))

    def get_by_user(self, user_id):
        reminders = []
        reader = ServiceLocator.get_database().query(GetReminderByUserCommand(user_id))

        while row := reader.get_row():
            reminders.append(Reminder.from_row(row))

        reader.free()
        return reminders

    def get_by_ref_number(self, refnumber):
        reminders = []
        reader = ServiceLocator.get_database().query(GetReminderByRefNumberCommand(refnumber))

        if row := reader.get_row():
            reminders = Reminder.from_row(row)

        reader.free()
        return reminders

    def delete_reminder(self, reminder_id):
        ServiceLocator.get_database().query(DeleteReminderCommand(reminder_id))

    def delete_reminder_by_user(self, user_id):
        ServiceLocator.get_database().query(DeleteReminderByUserCommand(user_id))

    def delete_reminder_by_ref_number(self, refnumber):
        ServiceLocator.get_database().query(DeleteReminderByRefNumberCommand(refnumber))

    def get_reminder_notices(self, now, reminder_type):
        reader = ServiceLocator.get_database().query(GetReminderNoticesCommand(now.to_the_minute(), reminder_type))

        notices = []
        while row := reader.get_row():
            notices.append(ReminderNotice.from_row(row))

        reader.free()
        return notices

# Create an instance of the ReminderRepository class
reminder_repository = ReminderRepository()

# FastAPI route to get all reminders
@app.get("/reminders/")
async def get_all_reminders():
    reminders = reminder_repository.get_all()
    return {"reminders": reminders}

# FastAPI route to add a reminder
@app.post("/add_reminder/")
async def add_reminder(reminder: Reminder):
    reminder_repository.add(reminder)
    return {"message": "Reminder added successfully"}

# FastAPI route to get reminders by user ID
@app.get("/reminders/{user_id}")
async def get_reminders_by_user(user_id: str):
    reminders = reminder_repository.get_by_user(user_id)
    return {"reminders": reminders}

# FastAPI route to get reminders by reference number
@app.get("/reminders/ref/{refnumber}")
async def get_reminders_by_ref_number(refnumber: str):
    reminders = reminder_repository.get_by_ref_number(refnumber)
    return {"reminders": reminders}

# FastAPI route to delete a reminder by ID
@app.delete("/reminders/delete/{reminder_id}")
async def delete_reminder_by_id(reminder_id: int):
    reminder_repository.delete_reminder(reminder_id)
    return {"message": "Reminder deleted successfully"}

# FastAPI route to delete reminders by user ID
@app.delete("/reminders/delete/user/{user_id}")
async def delete_reminders_by_user(user_id: str):
    reminder_repository.delete_reminder_by_user(user_id)
    return {"message": "Reminders for user deleted successfully"}

# FastAPI route to delete reminders by reference number
@app.delete("/reminders/delete/ref/{refnumber}")
async def delete_reminders_by_ref_number(refnumber: str):
    reminder_repository.delete_reminder_by_ref_number(refnumber)
    return {"message": "Reminders for reference number deleted successfully"}

# FastAPI route to get reminder notices
@app.get("/reminders/notices/")
async def get_reminder_notices(now: Date, reminder_type: str):
    notices = reminder_repository.get_reminder_notices(now, reminder_type)
    return {"notices": notices}

