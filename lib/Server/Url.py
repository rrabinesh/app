# <?php

# class Url
# {
#     /**
#      * @var string
#      */
#     private $url = '';

#     /**
#      * @var bool
#      */
#     private $hasQuestionMark = false;

#     /**
#      * @param string $url
#      */
#     public function __construct($url)
#     {
#         $this->url = $url;
#         $this->hasQuestionMark = BookedStringHelper::Contains($url, '?');
#     }

#     /**
#      * @param $urlFragment string
#      * @return Url
#      */
#     public function Add($urlFragment)
#     {
#         if (!BookedStringHelper::EndsWith($this->url, '/')) {
#             $this->url .= '/';
#         }

#         $this->url .= urlencode($urlFragment);

#         return $this;
#     }

#     /**
#      * @param string $name
#      * @param string $value
#      * @return Url
#      */
#     public function AddQueryString($name, $value)
#     {
#         $char = '?';
#         if ($this->hasQuestionMark) {
#             $char = '&';
#         }

#         $this->hasQuestionMark = true;
#         $this->url .= sprintf("$char%s=%s", $name, urlencode($value));

#         return $this;
#     }

#     /**
#      * @return string
#      */
#     public function ToString()
#     {
#         return $this->__toString();
#     }

#     public function __toString()
#     {
#         return $this->url;
#     }

#     /**
#      * @return Url
#      */
#     public function Copy()
#     {
#         return new Url($this->ToString());
#     }
# }


from urllib.parse import urlencode

class Url:

    def __init__(self, url):
        self.url = url
        self.has_query = '?' in url
    
    def add(self, url_fragment):
        if not self.url.endswith('/'):
            self.url += '/'
        self.url += urlencode(url_fragment)
        return self
    
    def add_query_param(self, name, value):
        char = '?' if not self.has_query else '&'
        self.has_query = True
        self.url += f'{char}{name}={urlencode(value)}'
        return self
    
    def __str__(self):
        return self.url
    
    def copy(self):
        return Url(self.url)
