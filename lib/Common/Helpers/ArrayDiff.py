# <?php

# class ArrayDiff
# {
#     private $_added = [];
#     private $_removed = [];
#     private $_unchanged = [];

#     public function __construct($array1, $array2)
#     {
#         $added = array_diff($array2, $array1);
#         $removed = array_diff($array1, $array2);
#         $unchanged = array_intersect($array1, $array2);

#         if (!empty($added)) {
#             $this->_added = array_merge($added);
#         }
#         if (!empty($removed)) {
#             $this->_removed = array_merge($removed);
#         }
#         if (!empty($unchanged)) {
#             $this->_unchanged = array_merge($unchanged);
#         }
#     }

#     public function AreDifferent()
#     {
#         return !empty($this->_added) || !empty($this->_removed);
#     }

#     public function GetAddedToArray1()
#     {
#         return $this->_added;
#     }

#     public function GetRemovedFromArray1()
#     {
#         return $this->_removed;
#     }

#     public function GetUnchangedInArray1()
#     {
#         return $this->_unchanged;
#     }
# }

from fastapi import FastAPI
from typing import List

app = FastAPI()

class ArrayDiff:
    def __init__(self, array1: List[str], array2: List[str]):
        added = list(set(array2) - set(array1))
        removed = list(set(array1) - set(array2))
        unchanged = list(set(array1) & set(array2))

        self._added = added
        self._removed = removed
        self._unchanged = unchanged

    def are_different(self):
        return bool(self._added) or bool(self._removed)

    def get_added_to_array1(self):
        return self._added

    def get_removed_from_array1(self):
        return self._removed

    def get_unchanged_in_array1(self):
        return self._unchanged

@app.post("/array_diff/")
def array_diff(array1: List[str], array2: List[str]):
    array_diff = ArrayDiff(array1, array2)
    result = {
        "are_different": array_diff.are_different(),
        "added_to_array1": array_diff.get_added_to_array1(),
        "removed_from_array1": array_diff.get_removed_from_array1(),
        "unchanged_in_array1": array_diff.get_unchanged_in_array1(),
    }
    return result

