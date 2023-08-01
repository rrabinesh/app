# <?php

# class UserImportCsvRow
# {
#     public $username;
#     public $email;
#     public $firstName = 'imported';
#     public $lastName = 'imported';
#     public $password;
#     public $phone;
#     public $organization;
#     public $position;
#     public $timezone;
#     public $language;
#     public $groups = [];
#     public $attributes = [];
#     public $status = 1;
#     public $credits;
#     public $color;

#     private $values = [];
#     private $indexes = [];

#     /**
#      * @param $values array
#      * @param $indexes array
#      * @param $attributes CustomAttribute[]
#      */
#     public function __construct($values, $indexes, $attributes)
#     {
#         $this->values = $values;
#         $this->indexes = $indexes;

#         $this->username = $this->valueOrDefault('username');
#         $this->email = $this->valueOrDefault('email');
#         $this->firstName = $this->valueOrDefault('firstName');
#         $this->lastName = $this->valueOrDefault('lastName');
#         $this->password = $this->valueOrDefault('password');
#         $this->phone = $this->valueOrDefault('phone');
#         $this->organization = $this->valueOrDefault('organization');
#         $this->position = $this->valueOrDefault('position');
#         $this->timezone = $this->valueOrDefault('timezone');
#         $this->language = $this->valueOrDefault('language');
#         $this->status = $this->valueOrDefault('status');
#         $this->credits = $this->valueOrDefault('credits');
#         $this->color = $this->valueOrDefault('color');
#         $this->groups = (!array_key_exists('groups', $this->indexes) || $indexes['groups'] === false) ? [] : array_map('trim', explode(',', htmlspecialchars($values[$indexes['groups']])));
#         foreach ($attributes as $label => $attribute) {
#             $this->attributes[$label] = $this->valueOrDefault($label);
#         }
#     }

#     public function IsValid()
#     {
#         $isValid = !empty($this->username) && !empty($this->email);
#         if (!$isValid) {
#             Log::Debug('User import row is not valid. Username %s, Email %s', $this->username, $this->email);
#         }
#         return $isValid;
#     }

#     /**
#      * @param string[] $values
#      * @param CustomAttribute[] $attributes
#      * @return bool|string[]
#      */
#     public static function GetHeaders($values, $attributes)
#     {
#         $values = array_map('strtolower', $values);

#         if (!in_array('email', $values) && !in_array('username', $values)) {
#             return false;
#         }

#         $indexes['email'] = self::indexOrFalse('email', $values);
#         $indexes['username'] = self::indexOrFalse('username', $values);
#         $indexes['firstName'] = self::indexOrFalse('first name', $values);
#         $indexes['lastName'] = self::indexOrFalse('last name', $values);
#         $indexes['password'] = self::indexOrFalse('password', $values);
#         $indexes['phone'] = self::indexOrFalse('phone', $values);
#         $indexes['organization'] = self::indexOrFalse('organization', $values);
#         $indexes['position'] = self::indexOrFalse('position', $values);
#         $indexes['timezone'] = self::indexOrFalse('timezone', $values);
#         $indexes['language'] = self::indexOrFalse('language', $values);
#         $indexes['groups'] = self::indexOrFalse('groups', $values);
#         $indexes['status'] = self::indexOrFalse('status', $values);
#         $indexes['credits'] = self::indexOrFalse('credits', $values);
#         $indexes['color'] = self::indexOrFalse('color', $values);

#         foreach ($attributes as $label => $attribute) {
#             $label = strtolower($label);
#             $escapedLabel = str_replace('\'', '\\\\', $label);
#             $indexes[$label] = self::indexOrFalse($escapedLabel, $values);
#         }

#         return $indexes;
#     }

#     private static function indexOrFalse($columnName, $values)
#     {
#         $index = array_search($columnName, $values);
#         if ($index === false) {
#             return false;
#         }

#         return intval($index);
#     }

#     /**
#      * @param $column string
#      * @return string
#      */
#     private function valueOrDefault($column)
#     {
#         return ($this->indexes[$column] === false || !array_key_exists($this->indexes[$column], $this->values)) ? '' : $this->tryToGetEscapedValue($this->values[$this->indexes[$column]]);
#     }

#     private function tryToGetEscapedValue($v)
#     {
#         $value = htmlspecialchars(trim($v));
#         if (!$value) {
#             // htmlspecialchars freaked out and couldnt encode
#             return trim($v);
#         }

#         return $value;
#     }
# }

# class UserImportCsv
# {
#     /**
#      * @var UploadedFile
#      */
#     private $file;

#     /**
#      * @var int[]
#      */
#     private $skippedRowNumbers = [];

#     /**
#      * @var CustomAttribute[]
#      */
#     private $attributes;

#     /**
#      * @param UploadedFile $file
#      * @param CustomAttribute[] $attributes
#      */
#     public function __construct(UploadedFile $file, $attributes)
#     {
#         $this->file = $file;
#         $this->attributes = $attributes;
#     }

#     /**
#      * @return UserImportCsvRow[]
#      */
#     public function GetRows()
#     {
#         $rows = [];

#         $contents = $this->file->Contents();

#         $contents = $this->RemoveUTF8BOM($contents);
#         $csvRows = preg_split('/\n|\r\n?/', $contents);

#         if (count($csvRows) == 0) {
#             Log::Debug('No rows in user import file');
#             return $rows;
#         }

#         Log::Debug('%s rows in user import file', count($csvRows));

#         $headers = UserImportCsvRow::GetHeaders(str_getcsv($csvRows[0]), $this->attributes);

#         if (!$headers) {
#             Log::Debug('No headers in user import file');
#             return $rows;
#         }

#         for ($i = 1; $i < count($csvRows); $i++) {
#             $values = str_getcsv($csvRows[$i]);

#             $row = new UserImportCsvRow($values, $headers, $this->attributes);

#             if ($row->IsValid()) {
#                 $rows[] = $row;
#             } else {
#                 Log::Error('Skipped import of user row %s. Values %s', $i, print_r($values, true));
#                 $this->skippedRowNumbers[] = $i;
#             }
#         }

#         return $rows;
#     }

#     /**
#      * @return int[]
#      */
#     public function GetSkippedRowNumbers()
#     {
#         return $this->skippedRowNumbers;
#     }

#     private function RemoveUTF8BOM($text)
#     {
#         return str_replace("\xEF\xBB\xBF", '', $text);
#     }
# }

from fastapi import FastAPI, HTTPException, UploadFile, File
from typing import List

# Create a FastAPI app
app = FastAPI()

# CustomAttribute model (replace it with your actual CustomAttribute model if available)
class CustomAttribute:
    pass

# UserImportCsvRow
class UserImportCsvRow:
    def __init__(self, values, indexes, attributes):
        self.username = self.value_or_default('username', values, indexes)
        self.email = self.value_or_default('email', values, indexes)
        self.firstName = self.value_or_default('firstName', values, indexes, default_value='imported')
        self.lastName = self.value_or_default('lastName', values, indexes, default_value='imported')
        self.password = self.value_or_default('password', values, indexes)
        self.phone = self.value_or_default('phone', values, indexes)
        self.organization = self.value_or_default('organization', values, indexes)
        self.position = self.value_or_default('position', values, indexes)
        self.timezone = self.value_or_default('timezone', values, indexes)
        self.language = self.value_or_default('language', values, indexes)
        self.groups = self.get_list_value('groups', values, indexes)
        self.attributes = {}
        for label, attribute in attributes.items():
            self.attributes[label] = self.value_or_default(label, values, indexes)
        self.status = self.value_or_default('status', values, indexes, default_value=1)
        self.credits = self.value_or_default('credits', values, indexes)
        self.color = self.value_or_default('color', values, indexes)

    def is_valid(self):
        is_valid = bool(self.username) and bool(self.email)
        if not is_valid:
            raise HTTPException(status_code=400, detail=f"User import row is not valid. Username: {self.username}, Email: {self.email}")
        return is_valid

    @staticmethod
    def value_or_default(column, values, indexes, default_value=''):
        index = indexes.get(column)
        return values[index].strip() if index is not None and 0 <= index < len(values) else default_value

    @staticmethod
    def get_list_value(column, values, indexes):
        index = indexes.get(column)
        return [item.strip() for item in values[index].split(',')] if index is not None and 0 <= index < len(values) else []

# FastAPI endpoint to handle user import CSV file
@app.post("/user_import/")
async def user_import(csv_file: UploadFile = File(...)):
    # Replace this with your actual CustomAttribute model if available
    attributes = { "attribute1": CustomAttribute(), "attribute2": CustomAttribute() }

    rows = []
    skipped_row_numbers = []

    contents = await csv_file.read()
    contents = contents.decode('utf-8')
    csv_rows = contents.splitlines()

    if len(csv_rows) == 0:
        raise HTTPException(status_code=400, detail="No rows in user import file")

    headers = UserImportCsvRow.get_headers(csv_rows[0].split(','), attributes)

    if not headers:
        raise HTTPException(status_code=400, detail="No headers in user import file")

    for i, row in enumerate(csv_rows[1:], start=1):
        values = row.split(',')
        user_row = UserImportCsvRow(values, headers, attributes)
        if user_row.is_valid():
            rows.append(user_row)
        else:
            skipped_row_numbers.append(i)

    return {
        "rows": [row.__dict__ for row in rows],
        "skipped_row_numbers": skipped_row_numbers
    }

# Helper function to get headers
def get_headers(values, attributes):
    pass


