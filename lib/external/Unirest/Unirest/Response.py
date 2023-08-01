# <?php

# namespace Unirest;

# class Response
# {
#     public $code;
#     public $raw_body;
#     public $body;
#     public $headers;

#     /**
#      * @param int $code response code of the cURL request
#      * @param string $raw_body the raw body of the cURL response
#      * @param string $headers raw header string from cURL response
#      * @param array $json_args arguments to pass to json_decode function
#      */
#     public function __construct($code, $raw_body, $headers, $json_args = array())
#     {
#         $this->code     = $code;
#         $this->headers  = $this->parseHeaders($headers);
#         $this->raw_body = $raw_body;
#         $this->body     = $raw_body;

#         // make sure raw_body is the first argument
#         array_unshift($json_args, $raw_body);

#         if (function_exists('json_decode')) {
#             $json = call_user_func_array('json_decode', $json_args);

#             if (json_last_error() === JSON_ERROR_NONE) {
#                 $this->body = $json;
#             }
#         }
#     }

#     /**
#      * if PECL_HTTP is not available use a fall back function
#      *
#      * thanks to ricardovermeltfoort@gmail.com
#      * http://php.net/manual/en/function.http-parse-headers.php#112986
#      * @param string $raw_headers raw headers
#      * @return array
#      */
#     private function parseHeaders($raw_headers)
#     {
#         if (function_exists('http_parse_headers')) {
#             return http_parse_headers($raw_headers);
#         } else {
#             $key = '';
#             $headers = array();

#             foreach (explode("\n", $raw_headers) as $i => $h) {
#                 $h = explode(':', $h, 2);

#                 if (isset($h[1])) {
#                     if (!isset($headers[$h[0]])) {
#                         $headers[$h[0]] = trim($h[1]);
#                     } elseif (is_array($headers[$h[0]])) {
#                         $headers[$h[0]] = array_merge($headers[$h[0]], array(trim($h[1])));
#                     } else {
#                         $headers[$h[0]] = array_merge(array($headers[$h[0]]), array(trim($h[1])));
#                     }

#                     $key = $h[0];
#                 } else {
#                     if (substr($h[0], 0, 1) == "\t") {
#                         $headers[$key] .= "\r\n\t".trim($h[0]);
#                     } elseif (!$key) {
#                         $headers[0] = trim($h[0]);
#                     }
#                 }
#             }

#             return $headers;
#         }
#     }
# }


from fastapi import Response
import json

class UnirestResponse(Response):
    def __init__(self, code, raw_body, headers, json_args=None):
        super().__init__(content=raw_body, status_code=code, headers=headers)

        self.code = code
        self.headers = self.parse_headers(headers)
        self.raw_body = raw_body
        self.body = raw_body

        if json_args is not None:
            try:
                self.body = json.loads(raw_body, *json_args)
            except json.JSONDecodeError:
                pass

    def parse_headers(self, raw_headers):
        if hasattr(super(), "parse_raw_headers"):
            # Newer versions of FastAPI have a parse_raw_headers method, we use it if available
            return self.parse_raw_headers(raw_headers)
        else:
            # If parse_raw_headers is not available, we manually parse the headers
            key = ''
            headers = {}
            for h in raw_headers.split('\n'):
                h = h.split(':', 1)
                if len(h) == 2:
                    key = h[0].strip()
                    value = h[1].strip()
                    if key not in headers:
                        headers[key] = value
                    else:
                        # If the header is already present, we convert it to a list of values
                        if not isinstance(headers[key], list):
                            headers[key] = [headers[key]]
                        headers[key].append(value)
                else:
                    if key:
                        headers[key] += ' ' + h[0].strip()
                    else:
                        headers[0] = h[0].strip()
            return headers

