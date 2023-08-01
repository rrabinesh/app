# <?php

# require_once(ROOT_DIR . 'lib/WebService/RestResponse.php');
# require_once(ROOT_DIR . 'Domain/Values/WebService/WebServiceUserSession.php');

# interface IRestServer
# {
#     /**
#      * @return mixed
#      */
#     public function GetRequest();

#     /**
#      * @param RestResponse $restResponse
#      * @param int $statusCode
#      * @return void
#      */
#     public function WriteResponse(RestResponse $restResponse, $statusCode = 200);

#     /**
#      * @param string $serviceName
#      * @param array $params
#      * @return string
#      */
#     public function GetServiceUrl($serviceName, $params = []);

#     /**
#      * @return string
#      */
#     public function GetUrl();

#     /**
#      * @param string $serviceName
#      * @param array $params
#      * @return string
#      */
#     public function GetFullServiceUrl($serviceName, $params = []);

#     /**
#      * @param string $headerName
#      * @return string|null
#      */
#     public function GetHeader($headerName);

#     /**
#      * @param WebServiceUserSession $session
#      * @return void
#      */
#     public function SetSession(WebServiceUserSession $session);

#     /**
#      * @return WebServiceUserSession|null
#      */
#     public function GetSession();

#     /**
#      * @param string $queryStringKey
#      * @return string|null
#      */
#     public function GetQueryString($queryStringKey);
# }

from abc import ABC, abstractmethod
from fastapi import FastAPI, Request, Response

app = FastAPI()

class RestResponse:
    def __init__(self):
        self.links = []
        self.message = None

    def add_service(self, server, service_name, params=None):
        params = params or {}
        url = server.get_full_service_url(service_name, params)
        self.add_service_link(RestServiceLink(url, service_name))

    def add_link(self, href, title):
        self.add_service_link(RestServiceLink(href, title))

    def add_service_link(self, link):
        self.links.append(link)

class RestServiceLink:
    def __init__(self, href, title):
        self.href = href
        self.title = title

class WebServiceUserSession:
    pass  # Define your WebServiceUserSession class if needed

class IRestServer(ABC):
    @abstractmethod
    def get_request(self) -> Request:
        pass

    @abstractmethod
    def write_response(self, rest_response: RestResponse, status_code: int = 200) -> Response:
        pass

    @abstractmethod
    def get_service_url(self, service_name: str, params: dict = None) -> str:
        pass

    @abstractmethod
    def get_url(self) -> str:
        pass

    @abstractmethod
    def get_full_service_url(self, service_name: str, params: dict = None) -> str:
        pass

    @abstractmethod
    def get_header(self, header_name: str) -> str:
        pass

    @abstractmethod
    def set_session(self, session: WebServiceUserSession) -> None:
        pass

    @abstractmethod
    def get_session(self) -> WebServiceUserSession:
        pass

    @abstractmethod
    def get_query_string(self, query_string_key: str) -> str:
        pass

