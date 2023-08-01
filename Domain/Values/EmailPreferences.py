# <?php

# class EmailPreferences implements IEmailPreferences
# {
#     private $preferences = [];

#     private $_added = [];
#     private $_removed = [];

#     public function Add($eventCategory, $eventType)
#     {
#         $key = $this->ToKey($eventCategory, $eventType);
#         $this->preferences[$key] = true;
#     }

#     public function Delete($eventCategory, $eventType)
#     {
#         $key = $this->ToKey($eventCategory, $eventType);
#         unset($this->preferences[$key]);
#     }

#     public function Exists($eventCategory, $eventType)
#     {
#         $key = $this->ToKey($eventCategory, $eventType);
#         return isset($this->preferences[$key]);
#     }

#     private function ToKey($eventCategory, $eventType)
#     {
#         return $eventCategory . '|' . $eventType;
#     }

#     public function AddPreference(IDomainEvent $event)
#     {
#         if (!$this->Exists($event->EventCategory(), $event->EventType())) {
#             $this->Add($event->EventCategory(), $event->EventType());
#             $this->_added[] = $event;
#         }
#     }

#     public function RemovePreference(IDomainEvent $event)
#     {
#         if ($this->Exists($event->EventCategory(), $event->EventType())) {
#             $this->Delete($event->EventCategory(), $event->EventType());
#             $this->_removed[] = $event;
#         }
#     }

#     public function GetAdded()
#     {
#         return $this->_added;
#     }

#     public function GetRemoved()
#     {
#         return $this->_removed;
#     }
# }

# interface IEmailPreferences
# {
#     /**
#      * @abstract
#      * @param EventCategory|string $eventCategory
#      * @param string $eventType
#      * @return bool
#      */
#     public function Exists($eventCategory, $eventType);

#     /**
#      * @abstract
#      * @param IDomainEvent $event
#      */
#     public function AddPreference(IDomainEvent $event);

#     /**
#      * @param IDomainEvent $event
#      */
#     public function RemovePreference(IDomainEvent $event);

#     /**
#      * @abstract
#      * @return array|IDomainEvent[]
#      */
#     public function GetAdded();

#     /**
#      * @abstract
#      * @return array|IDomainEvent[]
#      */
#     public function GetRemoved();
# }


from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EmailPreferences:
    def __init__(self):
        self.preferences = {}
        self._added = []
        self._removed = []

    def add(self, event_category, event_type):
        key = self.to_key(event_category, event_type)
        self.preferences[key] = True

    def delete(self, event_category, event_type):
        key = self.to_key(event_category, event_type)
        if key in self.preferences:
            del self.preferences[key]

    def exists(self, event_category, event_type):
        key = self.to_key(event_category, event_type)
        return key in self.preferences

    def add_preference(self, event):
        if not self.exists(event.event_category, event.event_type):
            self.add(event.event_category, event.event_type)
            self._added.append(event)

    def remove_preference(self, event):
        if self.exists(event.event_category, event.event_type):
            self.delete(event.event_category, event.event_type)
            self._removed.append(event)

    def to_key(self, event_category, event_type):
        return f"{event_category}|{event_type}"

    def get_added(self):
        return self._added

    def get_removed(self):
        return self._removed

class DomainEvent(BaseModel):
    event_category: str
    event_type: str

class EmailPreferencesResponse(BaseModel):
    added: List[DomainEvent]
    removed: List[DomainEvent]

@app.post("/email/preferences/")
async def manage_email_preferences(events: List[DomainEvent]):
    email_preferences = EmailPreferences()
    for event in events:
        email_preferences.add_preference(event)

    return EmailPreferencesResponse(added=email_preferences.get_added(), removed=email_preferences.get_removed())


