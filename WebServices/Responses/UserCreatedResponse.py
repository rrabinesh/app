# <!-- <?php

# require_once(ROOT_DIR . 'lib/WebService/namespace.php');

# class UserCreatedResponse extends RestResponse
# {
#     public $userId;

#     public function __construct(IRestServer $server, $userId)
#     {
#         $this->userId = $userId;
#         $this->AddService($server, WebServices::GetUser, [WebServiceParams::UserId => $userId]);
#         $this->AddService($server, WebServices::UpdateUser, [WebServiceParams::UserId => $userId]);
#     }

#     public static function Example()
#     {
#         return new ExampleUserCreatedResponse();
#     }
# }

# class ExampleUserCreatedResponse extends UserCreatedResponse
# {
#     public function __construct()
#     {
#         $this->AddLink('http://url/to/user', WebServices::GetUser);
#         $this->AddLink('http://url/to/update/user', WebServices::UpdateUser);
#     }
# } -->

from pydantic import BaseModel

# Simplified versions of the models for demonstration purposes

class UserCreatedResponse(BaseModel):
    userId: int

    def __init__(self, server, user_id):
        self.userId = user_id
        self.add_service(server, "http://url/to/user", "GetUser", {"userId": user_id})
        self.add_service(server, "http://url/to/update/user", "UpdateUser", {"userId": user_id})

    def add_service(self, server, url, service_name, params):
        # Placeholder method to add service information to the response
        pass


# FastAPI route
from fastapi import FastAPI

app = FastAPI()

@app.get("/user_created/{user_id}", response_model=UserCreatedResponse)
def user_created(user_id: int):
    # Simulated data (replace with real data from your application)
    example_user_created = ExampleUserCreatedResponse(user_id)
    return example_user_created


# Simulated classes for the Example data

class WebServices:
    GetUser = "GetUser"
    UpdateUser = "UpdateUser"

class WebServiceParams:
    UserId = "userId"

class IRestServer:
    pass


class ExampleUserCreatedResponse(UserCreatedResponse):
    def __init__(self, user_id):
        super().__init__(server=None, user_id=user_id)

    def add_service(self, server, url, service_name, params):
        # Simulated method to add service information to the response
        pass

    @classmethod
    def Example(cls):
        return cls()


# Note: The implementation of the actual `add_service` method in `UserCreatedResponse` and its corresponding logic,
# as well as the `WebServiceParams`, `WebServices`, and `IRestServer` classes, are not provided in the code above.
# These are placeholders for demonstration purposes. You need to replace them with your actual implementation and
# logic from your application.


