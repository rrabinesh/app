# <?php

# class CsvImportResult
# {
#     public $importCount = 0;
#     public $skippedRows = [];
#     public $messages = [];

#     /**
#      * @param $imported int
#      * @param $skippedRows int[]
#      * @param $messages string|string[]
#      */
#     public function __construct($imported, $skippedRows, $messages)
#     {
#         $this->importCount = $imported;
#         $this->skippedRows = $skippedRows;
#         $this->messages = is_array($messages) ? $messages : [$messages];
#     }
# }

from typing import List, Union
from pydantic import BaseModel

class CsvImportResult(BaseModel):
    importCount: int = 0
    skippedRows: List[int] = []
    messages: List[str] = []

    # Constructor to initialize the model from the input data
    def __init__(self, imported: int, skippedRows: List[int], messages: Union[str, List[str]]):
        super().__init__(importCount=imported, skippedRows=skippedRows, messages=messages)

# Example usage:
imported_data_count = 100
skipped_rows_list = [10, 15, 25]
messages_list = ["Row 5: Invalid data", "Row 20: Missing field"]

csv_import_result = CsvImportResult(imported=imported_data_count, skippedRows=skipped_rows_list, messages=messages_list)
print(csv_import_result.dict())


