# <?php

# class ResourceImportCsvRow
# {
#     public $name;
#     public $status;
#     public $schedule;
#     public $resourceType;
#     public $sortOrder = 0;
#     public $location;
#     public $contact;
#     public $description;
#     public $notes;
#     public $resourceAdministrator;
#     public $color;
#     public $resourceGroups = [];
#     public $autoAssign = true;
#     public $approvalRequired = false;
#     public $capacity;
#     public $minLength;
#     public $maxLength;
#     public $buffer;
#     public $crossDay = false;
#     public $addNotice;
#     public $updateNotice;
#     public $deleteNotice;
#     public $checkIn = false;
#     public $autoreleaseMinutes;
#     public $credits;
#     public $creditsPeak;
#     public $maximumConcurrent;
#     public $attributes = [];

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

#         $this->name = $this->valueOrDefault('name');
#         $this->status = strtolower($this->valueOrDefault('status'));
#         $this->schedule = strtolower($this->valueOrDefault('schedule'));
#         $this->resourceType = strtolower($this->valueOrDefault('resourceType'));
#         $this->sortOrder = $this->valueOrDefault('sortOrder');
#         $this->location = $this->valueOrDefault('location');
#         $this->contact = $this->valueOrDefault('contact');
#         $this->description = $this->valueOrDefault('description');
#         $this->notes = $this->valueOrDefault('notes');
#         $this->resourceAdministrator = strtolower($this->valueOrDefault('resourceAdministrator'));
#         $this->color = $this->valueOrDefault('color');
#         $this->resourceGroups = (!array_key_exists('resourceGroups', $this->indexes) || $indexes['resourceGroups'] === false) ? []
#                 : array_map('trim', explode(',', htmlspecialchars($values[$indexes['resourceGroups']])));
#         $this->autoAssign = strtolower($this->valueOrDefault('autoAssign'));
#         $this->approvalRequired = strtolower($this->valueOrDefault('approvalRequired'));
#         $this->capacity = $this->valueOrDefault('capacity');
#         $this->minLength = $this->valueOrDefault('minLength');
#         $this->maxLength = $this->valueOrDefault('maxLength');
#         $this->buffer = $this->valueOrDefault('buffer');
#         $this->crossDay = $this->valueOrDefault('crossDay');
#         $this->addNotice = $this->valueOrDefault('addNotice');
#         $this->updateNotice = $this->valueOrDefault('updateNotice');
#         $this->deleteNotice = $this->valueOrDefault('deleteNotice');
#         $this->checkIn = $this->valueOrDefault('checkIn');
#         $this->autoreleaseMinutes = $this->valueOrDefault('autoreleaseMinutes');
#         $this->credits = $this->valueOrDefault('credits');
#         $this->creditsPeak = $this->valueOrDefault('creditsPeak');
#         $this->maximumConcurrent = $this->valueOrDefault('concurrentReservations');

#         foreach ($attributes as $label => $attribute) {
#             $this->attributes[$label] = $this->valueOrDefault($label);
#         }
#     }

#     public function IsValid()
#     {
#         $isValid = !empty($this->name);
#         if (!$isValid) {
#             Log::Debug('Resource import row is not valid. Missing name');
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
#         if (!in_array('name', $values) && !in_array('name', $values)) {
#             return false;
#         }

#         $indexes['name'] = self::indexOrFalse('name', $values);
#         $indexes['status'] = self::indexOrFalse('status', $values);
#         $indexes['schedule'] = self::indexOrFalse('schedule', $values);
#         $indexes['resourceType'] = self::indexOrFalse('resource type', $values);
#         $indexes['sortOrder'] = self::indexOrFalse('sort order', $values);
#         $indexes['location'] = self::indexOrFalse('location', $values);
#         $indexes['contact'] = self::indexOrFalse('contact', $values);
#         $indexes['description'] = self::indexOrFalse('description', $values);
#         $indexes['notes'] = self::indexOrFalse('notes', $values);
#         $indexes['resourceAdministrator'] = self::indexOrFalse('resource administrator', $values);
#         $indexes['color'] = self::indexOrFalse('resource color', $values);
#         $indexes['resourceGroups'] = self::indexOrFalse('resource groups', $values);
#         $indexes['autoAssign'] = self::indexOrFalse('permission is automatically granted', $values);
#         $indexes['approvalRequired'] = self::indexOrFalse('reservations must be approved', $values);
#         $indexes['capacity'] = self::indexOrFalse('capacity', $values);
#         $indexes['minLength'] = self::indexOrFalse('reservation minimum length', $values);
#         $indexes['maxLength'] = self::indexOrFalse('reservation maximum length', $values);
#         $indexes['buffer'] = self::indexOrFalse('buffer time', $values);
#         $indexes['crossDay'] = self::indexOrFalse('reservations can be made across days', $values);
#         $indexes['addNotice'] = self::indexOrFalse('reservation add minimum notice', $values);
#         $indexes['updateNotice'] = self::indexOrFalse('reservation update minimum notice', $values);
#         $indexes['deleteNotice'] = self::indexOrFalse('reservation delete minimum notice', $values);
#         $indexes['checkIn'] = self::indexOrFalse('requires check in/out', $values);
#         $indexes['autoreleaseMinutes'] = self::indexOrFalse('autorelease minutes', $values);
#         $indexes['credits'] = self::indexOrFalse('credits (off peak)', $values);
#         $indexes['creditsPeak'] = self::indexOrFalse('credits (peak)', $values);
#         $indexes['concurrentReservations'] = self::indexOrFalse('maximum concurrent reservations', $values);

#         foreach ($attributes as $label => $attribute) {
#             $escapedLabel = str_replace('\'', '\\\\', $label);
#             $indexes[$label] = self::indexOrFalse($escapedLabel, $values);
#         }

#         return $indexes;
#     }

#     private static function indexOrFalse($columnName, $values)
#     {
#         $values = array_map('strtolower', $values);
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
#         return ($this->indexes[$column] === false ||
#                 !array_key_exists($this->indexes[$column], $this->values)) ? ''
#                 : htmlspecialchars(trim($this->values[$this->indexes[$column]]));
#     }
# }

# class ResourceImportCsv
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
#      * @return ResourceImportCsvRow[]
#      */
#     public function GetRows()
#     {
#         $rows = [];

#         $contents = $this->file->Contents();

#         $contents = $this->RemoveUTF8BOM($contents);
#         $csvRows = preg_split('/\n|\r\n?/', $contents);

#         if (count($csvRows) == 0) {
#             Log::Debug('No rows in resource import file');
#             return $rows;
#         }

#         Log::Debug('%s rows in resource import file', count($csvRows));

#         $headers = ResourceImportCsvRow::GetHeaders(str_getcsv($csvRows[0]), $this->attributes);

#         if (!$headers) {
#             Log::Debug('No headers in resource import file.');
#             if (count($csvRows) > 0) {
#                 Log::Debug('Header row: %s', var_export(str_getcsv($csvRows[0]), true));
#             }
#             return $rows;
#         }

#         for ($i = 1; $i < count($csvRows); $i++) {
#             $values = str_getcsv($csvRows[$i]);

#             $row = new ResourceImportCsvRow($values, $headers, $this->attributes);

#             if ($row->IsValid()) {
#                 $rows[] = $row;
#             } else {
#                 Log::Error('Skipped import of resource row %s. Values %s', $i, print_r($values, true));
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

from fastapi import FastAPI, File, UploadFile

# Assume you have defined the necessary Pydantic models and FastAPI dependencies.
# You can add them here or import them from other modules.

# Create a FastAPI app
app = FastAPI()

# Sample CustomAttribute class (you may need to define this properly)
class CustomAttribute:
    pass

# ResourceImportCsvRow
class ResourceImportCsvRow:
    def __init__(self, values, indexes, attributes):
        self.values = values
        self.indexes = indexes

        self.name = self.value_or_default('name')
        self.status = self.value_or_default('status').lower()
        self.schedule = self.value_or_default('schedule').lower()
        self.resourceType = self.value_or_default('resourceType').lower()
        self.sortOrder = self.value_or_default('sortOrder')
        self.location = self.value_or_default('location')
        self.contact = self.value_or_default('contact')
        self.description = self.value_or_default('description')
        self.notes = self.value_or_default('notes')
        self.resourceAdministrator = self.value_or_default('resourceAdministrator').lower()
        self.color = self.value_or_default('color')
        self.resourceGroups = (
            []
            if not self.indexes.get('resourceGroups') or self.indexes['resourceGroups'] is False
            else [val.strip() for val in self.values[self.indexes['resourceGroups']].split(',')]
        )
        self.autoAssign = self.value_or_default('autoAssign').lower() == "true"
        self.approvalRequired = self.value_or_default('approvalRequired').lower() == "true"
        self.capacity = self.value_or_default('capacity')
        self.minLength = self.value_or_default('minLength')
        self.maxLength = self.value_or_default('maxLength')
        self.buffer = self.value_or_default('buffer')
        self.crossDay = self.value_or_default('crossDay').lower() == "true"
        self.addNotice = self.value_or_default('addNotice')
        self.updateNotice = self.value_or_default('updateNotice')
        self.deleteNotice = self.value_or_default('deleteNotice')
        self.checkIn = self.value_or_default('checkIn').lower() == "true"
        self.autoreleaseMinutes = self.value_or_default('autoreleaseMinutes')
        self.credits = self.value_or_default('credits')
        self.creditsPeak = self.value_or_default('creditsPeak')
        self.maximumConcurrent = self.value_or_default('concurrentReservations')

        self.attributes = {}
        for label, attribute in attributes.items():
            self.attributes[label] = self.value_or_default(label)

    def is_valid(self):
        is_valid = bool(self.name)
        if not is_valid:
            print('Resource import row is not valid. Missing name')
        return is_valid

    def value_or_default(self, column):
        return self.values[self.indexes[column]] if self.indexes.get(column, False) else ""

# ResourceImportCsv
class ResourceImportCsv:
    def __init__(self, file: UploadFile, attributes):
        self.file = file
        self.attributes = attributes

    def get_rows(self):
        rows = []

        contents = self.file.file.read().decode("utf-8")

        contents = self.remove_utf8_bom(contents)
        csv_rows = contents.splitlines()

        if not csv_rows:
            print('No rows in resource import file')
            return rows

        print(f'{len(csv_rows)} rows in resource import file')

        headers = ResourceImportCsvRow.get_headers(csv_rows[0], self.attributes)

        if not headers:
            print('No headers in resource import file.')
            if len(csv_rows) > 0:
                print(f'Header row: {csv_rows[0]}')
            return rows

        for i, csv_row in enumerate(csv_rows[1:], 1):
            values = csv_row.split(',')
            row = ResourceImportCsvRow(values, headers, self.attributes)

            if row.is_valid():
                rows.append(row)
            else:
                print(f'Skipped import of resource row {i}. Values {values}')
                # You may want to log the skipped rows here or handle them differently.

        return rows

    def get_skipped_row_numbers(self):
        return []  # As FastAPI does not support global log/debug, we can return an empty list here.

    def remove_utf8_bom(self, text):
        return text.replace("\ufeff", "")


# FastAPI endpoint for importing resources from CSV
@app.post("/import_resources/")
async def import_resources(
    file: UploadFile = File(...),
    attributes: dict = ...  # Define a Pydantic model or custom type to accept the attributes here
):
    resource_importer = ResourceImportCsv(file, attributes)
    rows = resource_importer.get_rows()
    skipped_row_numbers = resource_importer.get_skipped_row_numbers()

    # You can process the imported rows and save them in your database or perform other operations here.
    # Example: saving the rows in a list and returning the count of imported rows.
    imported_count = len(rows)

    return {"imported_count": imported_count, "skipped_row_numbers": skipped_row_numbers}


