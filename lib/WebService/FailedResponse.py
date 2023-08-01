# <?php

# class FailedResponse extends RestResponse
# {
#     /**
#      * @var array|string[]
#      */
#     public $errors;

#     /**
#      * @param IRestServer $server
#      * @param array|string[] $errors
#      */
#     public function __construct(IRestServer $server, $errors)
#     {
#         $this->message = 'There were errors processing your request';
#         $this->errors = $errors;
#     }
# }

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

class FailedResponse(BaseModel):
    message: str = 'There were errors processing your request'
    errors: List[str]

app = FastAPI()

@app.get("/failed", response_model=FailedResponse)
def process_request():
    errors = ["Error 1", "Error 2"]  # Replace this with the actual errors from your application
    return FailedResponse(errors=errors)
