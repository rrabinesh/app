# <?php

# class WebLoginContext implements ILoginContext
# {
#     /**
#      * @var LoginData
#      */
#     private $data;

#     public function __construct(LoginData $data)
#     {
#         $this->data = $data;
#     }

#     /**
#      * @return LoginData
#      */
#     public function GetData()
#     {
#         return $this->data;
#     }
# }

class LoginData(BaseModel):
    field1: str
    field2: int
    # Add other fields as needed


# WebLoginContext class
class WebLoginContext:
    def __init__(self, data: LoginData):
        self.data = data

    def get_data(self) -> LoginData:
        return self.data

