# <?php

# class RestServiceLink
# {
#     public $href;
#     public $title;

#     public function __construct($href, $title)
#     {
#         $this->href = $href;
#         $this->title = $title;
#     }
# }

from dataclasses import dataclass

@dataclass
class RestServiceLink:
    href: str
    title: str



