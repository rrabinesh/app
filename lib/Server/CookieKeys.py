#  <?php

# class CookieKeys
# {
#     private function __construct()
#     {
#     }

#     public const LANGUAGE = 'language';
#     public const PERSIST_LOGIN = 'persist_login';
# } 

from fastapi import FastAPI

app = FastAPI()

class CookieKeys:
    LANGUAGE = 'language'
    PERSIST_LOGIN = 'persist_login'
