# <?php

# class StringBuilder
# {
#     private $_string = [];

#     public function Append($string)
#     {
#         $this->_string[] = $string;
#     }

#     public function AppendLine($string = '')
#     {
#         $this->_string[] = $string . "\n";
#     }

#     public function PrependLine($string = '')
#     {
#         array_unshift($this->_string, $string . "\n");
#     }

#     public function Count()
#     {
#         return count($this->_string);
#     }

#     public function ToString($glue = '')
#     {
#         return join($glue, $this->_string);
#     }
# }

from fastapi import FastAPI
from typing import List

app = FastAPI()

class StringBuilder:
    def __init__(self):
        self._string = []

    def append(self, string: str):
        self._string.append(string)

    def append_line(self, string: str = ''):
        self._string.append(string + "\n")

    def prepend_line(self, string: str = ''):
        self._string.insert(0, string + "\n")

    def count(self) -> int:
        return len(self._string)

    def to_string(self, glue: str = '') -> str:
        return glue.join(self._string)



