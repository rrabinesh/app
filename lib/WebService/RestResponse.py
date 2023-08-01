# <?php

# class RestResponse
# {
#     public const OK_CODE = 200;
#     public const CREATED_CODE = 201;
#     public const BAD_REQUEST_CODE = 400;
#     public const UNAUTHORIZED_CODE = 401;
#     public const NOT_FOUND_CODE = 404;
#     public const SERVER_ERROR = 500;

#     /**
#      * @var array|RestServiceLink[]
#      */
#     public $links = [];

#     /**
#      * @var string
#      */
#     public $message = null;

#     /**
#      * @param IRestServer $server
#      * @param string $serviceName
#      * @param array $params
#      * @return void
#      */
#     public function AddService(IRestServer $server, $serviceName, $params = [])
#     {
#         $url = $server->GetFullServiceUrl($serviceName, $params);
#         $this->AddServiceLink(new RestServiceLink($url, $serviceName));
#     }

#     /**
#      * @param string $href
#      * @param string $title
#      * @return void
#      */
#     public function AddLink($href, $title)
#     {
#         $this->AddServiceLink(new RestServiceLink($href, $title));
#     }

#     protected function AddServiceLink(RestServiceLink $link)
#     {
#         $this->links[] = $link;
#     }

#     public static function NotFound()
#     {
#         $response = new RestResponse();
#         $response->message = 'The requested resource was not found';
#         return $response;
#     }

#     public static function Unauthorized()
#     {
#         $response = new RestResponse();
#         $response->message = 'You do not have access to the requested resource';
#         return $response;
#     }
# }

from typing import List, Optional
from fastapi import FastAPI, Depends

class RestServiceLink:
    def __init__(self, href: str, title: str):
        self.href = href
        self.title = title

class RestResponse:
    def __init__(self):
        self.links: List[RestServiceLink] = []
        self.message: Optional[str] = None

    def add_service(self, server: "IRestServer", service_name: str, params: dict = None):
        params = params or {}
        url = server.get_full_service_url(service_name, params)
        self.add_service_link(RestServiceLink(url, service_name))

    def add_link(self, href: str, title: str):
        self.add_service_link(RestServiceLink(href, title))

    def add_service_link(self, link: RestServiceLink):
        self.links.append(link)

app = FastAPI()

class IRestServer:
    def get_full_service_url(self, service_name: str, params: dict = None) -> str:
        # Replace this with the actual implementation of getting the full service URL
        return f"https://example.com/{service_name}"

@app.get("/not_found", response_model=RestResponse)
def not_found(server: IRestServer = Depends(IRestServer)):
    response = RestResponse()
    response.message = 'The requested resource was not found'
    response.add_service(server, "some_service")
    return response

@app.get("/unauthorized", response_model=RestResponse)
def unauthorized(server: IRestServer = Depends(IRestServer)):
    response = RestResponse()
    response.message = 'You do not have access to the requested resource'
    response.add_link("https://example.com/some_page", "Some Page")
    return response

