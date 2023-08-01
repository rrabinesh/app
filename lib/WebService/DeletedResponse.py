# <?php

# class DeletedResponse extends RestResponse
# {
#     public function __construct()
#     {
#         $this->message = 'The item was deleted';
#     }

#     public static function Example()
#     {
#         return new DeletedResponse();
#     }
# }

from fastapi import FastAPI

class DeletedResponse:
    def __init__(self):
        self.message = 'The item was deleted'

    @staticmethod
    def example():
        return DeletedResponse()

app = FastAPI()

@app.get("/delete", response_model=DeletedResponse)
def delete_item():
    return DeletedResponse.example()

