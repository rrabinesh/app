# <?php

# class GroupImportCsvRow
# {
#     private $values = [];
#     private $indexes = [];

#     /**
#      * @var string
#      */
#     public $name;
#     /**
#      * @var bool
#      */
#     public $autoAdd;
#     /**
#      * @var string
#      */
#     public $groupAdministrator;
#     /**
#      * @var bool
#      */
#     public $isAdmin;
#     /**
#      * @var bool
#      */
#     public $isGroupAdmin;
#     /**
#      * @var bool
#      */
#     public $isResourceAdmin;
#     /**
#      * @var bool
#      */
#     public $isScheduleAdmin;
#     /**
#      * @var string[]
#      */
#     public $members;
#     /**
#      * @var string[]
#      */
#     public $permissionsFull;
#     /**
#      * @var string[]
#      */
#     public $permissionsRead;

#     /**
#      * @param $values array
#      * @param $indexes array
#      */
#     public function __construct($values, $indexes)
#     {
#         $this->values = $values;
#         $this->indexes = $indexes;

#         $this->name = $this->valueOrDefault('name');
#         $this->autoAdd = $this->valueOrFalse('autoAdd');
#         $this->groupAdministrator = $this->valueOrDefault('groupAdministrator');
#         $this->isAdmin = $this->valueOrFalse('isAdmin');
#         $this->isGroupAdmin = $this->valueOrFalse('isGroupAdmin');
#         $this->isResourceAdmin = $this->valueOrFalse('isResourceAdmin');
#         $this->isScheduleAdmin = $this->valueOrFalse('isScheduleAdmin');
#         $this->members = $this->asArray('members');
#         $this->permissionsFull = $this->asArray('permissionsFull');
#         $this->permissionsRead = $this->asArray('permissionsRead');
#     }

#     public function IsValid()
#     {
#         $isValid = !empty($this->name);
#         if (!$isValid) {
#             Log::Debug('Group import row is not valid. Name %s', $this->name);
#         }
#         return $isValid;
#     }

#     /**
#      * @param string[] $values
#      * @return bool|string[]
#      */
#     public static function GetHeaders($values)
#     {
#         $values = array_map('strtolower', $values);

#         if (!in_array('name', $values)) {
#             return false;
#         }

#         $indexes['name'] = self::indexOrFalse('name', $values);
#         $indexes['autoAdd'] = self::indexOrFalse('is auto add', $values);
#         $indexes['groupAdministrator'] = self::indexOrFalse('group administrator', $values);
#         $indexes['isAdmin'] = self::indexOrFalse('is application admin', $values);
#         $indexes['isGroupAdmin'] = self::indexOrFalse('is group admin', $values);
#         $indexes['isResourceAdmin'] = self::indexOrFalse('is resource admin', $values);
#         $indexes['isScheduleAdmin'] = self::indexOrFalse('is schedule admin', $values);
#         $indexes['members'] = self::indexOrFalse('members', $values);
#         $indexes['permissionsFull'] = self::indexOrFalse('full permissions', $values);
#         $indexes['permissionsRead'] = self::indexOrFalse('read only permissions', $values);

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

#     /**
#      * @param $column string
#      * @return bool
#      */
#     private function valueOrFalse($column)
#     {
#         $value = $this->valueOrDefault($column);

#         return $value == "true";
#     }

#     private function tryToGetEscapedValue($v)
#     {
#         $value = htmlspecialchars(trim($v));
#         if (!$value) {
#             return trim($v);
#         }

#         return $value;
#     }

#     private function asArray($column)
#     {
#         return (!array_key_exists($column, $this->indexes) || $this->indexes[$column] === false) ? [] : array_map('trim', explode(',', htmlspecialchars($this->values[$this->indexes[$column]])));
#     }
# }

# class GroupImportCsv
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
#      * @param UploadedFile $file
#      */
#     public function __construct(UploadedFile $file)
#     {
#         $this->file = $file;
#     }

#     /**
#      * @return GroupImportCsvRow[]
#      */
#     public function GetRows()
#     {
#         $rows = [];

#         $contents = $this->file->Contents();

#         $contents = $this->RemoveUTF8BOM($contents);
#         $csvRows = preg_split('/\n|\r\n?/', $contents);

#         if (count($csvRows) == 0) {
#             Log::Debug('No rows in group import file');
#             return $rows;
#         }

#         Log::Debug('%s rows in group import file', count($csvRows));

#         $headers = GroupImportCsvRow::GetHeaders(str_getcsv($csvRows[0]));

#         if (!$headers) {
#             Log::Debug('No headers in group import file');
#             return $rows;
#         }

#         for ($i = 1; $i < count($csvRows); $i++) {
#             $values = str_getcsv($csvRows[$i]);

#             $row = new GroupImportCsvRow($values, $headers);

#             if ($row->IsValid()) {
#                 $rows[] = $row;
#             } else {
#                 Log::Error('Skipped import of group row %s. Values %s', $i, print_r($values, true));
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

# Import the required libraries
import csv

class GroupImportCsvRow:
    def __init__(self, values, indexes):
        self.values = values
        self.indexes = indexes

        self.name = self.value_or_default('name')
        self.auto_add = self.value_or_false('autoAdd')
        self.group_administrator = self.value_or_default('groupAdministrator')
        self.is_admin = self.value_or_false('isAdmin')
        self.is_group_admin = self.value_or_false('isGroupAdmin')
        self.is_resource_admin = self.value_or_false('isResourceAdmin')
        self.is_schedule_admin = self.value_or_false('isScheduleAdmin')
        self.members = self.as_array('members')
        self.permissions_full = self.as_array('permissionsFull')
        self.permissions_read = self.as_array('permissionsRead')

    def is_valid(self):
        is_valid = bool(self.name)
        if not is_valid:
            print(f'Group import row is not valid. Name: {self.name}')
        return is_valid

    @staticmethod
    def get_headers(values):
        values = [value.lower() for value in values]

        if 'name' not in values:
            return False

        indexes = {
            'name': GroupImportCsvRow.index_or_false('name', values),
            'autoAdd': GroupImportCsvRow.index_or_false('is auto add', values),
            'groupAdministrator': GroupImportCsvRow.index_or_false('group administrator', values),
            'isAdmin': GroupImportCsvRow.index_or_false('is application admin', values),
            'isGroupAdmin': GroupImportCsvRow.index_or_false('is group admin', values),
            'isResourceAdmin': GroupImportCsvRow.index_or_false('is resource admin', values),
            'isScheduleAdmin': GroupImportCsvRow.index_or_false('is schedule admin', values),
            'members': GroupImportCsvRow.index_or_false('members', values),
            'permissionsFull': GroupImportCsvRow.index_or_false('full permissions', values),
            'permissionsRead': GroupImportCsvRow.index_or_false('read only permissions', values),
        }

        return indexes

    @staticmethod
    def index_or_false(column_name, values):
        index = next((i for i, value in enumerate(values) if value == column_name), False)
        return int(index) if index is not False else False

    def value_or_default(self, column):
        index = self.indexes.get(column, False)
        return self.try_to_get_escaped_value(self.values[index]) if index is not False and index < len(self.values) else ''

    def value_or_false(self, column):
        value = self.value_or_default(column)
        return value.lower() == 'true' if value else False

    def try_to_get_escaped_value(self, v):
        value = v.strip()
        return value if value else v

    def as_array(self, column):
        index = self.indexes.get(column, False)
        value = self.values[index] if index is not False and index < len(self.values) else ''
        return [item.strip() for item in value.split(',')]

class GroupImportCsv:
    def __init__(self, file):
        self.file = file
        self.skipped_row_numbers = []

    def get_rows(self):
        rows = []

        # Assuming file_contents contains the contents of the CSV file
        with open(self.file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            csv_rows = list(csvreader)

            if len(csv_rows) == 0:
                print('No rows in group import file')
                return rows

            headers = GroupImportCsvRow.get_headers(csv_rows[0])

            if not headers:
                print('No headers in group import file')
                return rows

            for i in range(1, len(csv_rows)):
                values = csv_rows[i]

                row = GroupImportCsvRow(values, headers)

                if row.is_valid():
                    rows.append(row)
                else:
                    print(f'Skipped import of group row {i}. Values: {values}')
                    self.skipped_row_numbers.append(i)

        return rows

    def get_skipped_row_numbers(self):
        return self.skipped_row_numbers


