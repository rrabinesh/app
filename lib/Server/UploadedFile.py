# <?php

# class UploadedFile
# {
#     private $file;

#     public function __construct($file)
#     {
#         $this->file = $file;
#     }

#     /**
#      * @return string
#      */
#     public function OriginalName()
#     {
#         return $this->file['name'];
#     }

#     /**
#      * @return string
#      */
#     public function TemporaryName()
#     {
#         return $this->file['tmp_name'];
#     }

#     /**
#      * @return string
#      */
#     public function MimeType()
#     {
#         return $this->file['type'];
#     }

#     /**
#      * @return int total bytes
#      */
#     public function Size()
#     {
#         return $this->file['size'];
#     }

#     /**
#      * @return string
#      */
#     public function Extension()
#     {
#         $info = pathinfo($this->OriginalName());
#         return $info['extension'];
#     }

#     /**
#      * @return string
#      */
#     public function Contents()
#     {
#         $tmpName = $this->TemporaryName();
#         $fp = fopen($tmpName, 'r');
#         $content = fread($fp, filesize($tmpName));
#         fclose($fp);

#         return trim($content);
#     }

#     public function IsError()
#     {
#         return $this->file['error'] != UPLOAD_ERR_OK;
#     }

#     public function Error()
#     {
#         $messages = [
#             UPLOAD_ERR_OK => '',
#             UPLOAD_ERR_INI_SIZE => 'The uploaded file exceeds the maximum file size',
#             UPLOAD_ERR_FORM_SIZE => 'The uploaded file exceeds the maximum file size',
#             UPLOAD_ERR_PARTIAL => 'The uploaded file was only partially uploaded',
#             UPLOAD_ERR_NO_FILE => 'No file was uploaded',
#             UPLOAD_ERR_NO_TMP_DIR => 'Missing temporary storage folder',
#             UPLOAD_ERR_CANT_WRITE => 'Failed to write file to disk, check folder permissions of configured upload directory'
#         ];

#         return $messages[$this->file['error']];
#     }

#     /**
#      * @static
#      * @return int
#      */
#     public static function GetMaxSize()
#     {
#         $max_upload = (int)(ini_get('upload_max_filesize'));
#         $max_post = (int)(ini_get('post_max_size'));
#         $memory_limit = (int)(ini_get('memory_limit'));
#         return min($max_upload, $max_post, $memory_limit);
#     }

#     /**
#      * @static
#      * @return int
#      */
#     public static function GetMaxUploadCount()
#     {
#         return (int)(ini_get('max_file_uploads'));
#     }
# }

from starlette.datastructures import UploadFile

class UploadedFile:

    def __init__(self, upload_file: UploadFile):
        self.upload_file = upload_file

    @property
    def original_name(self):
        return self.upload_file.filename
    
    @property
    def temporary_name(self):
        return None

    @property
    def mime_type(self):
        return self.upload_file.content_type

    @property
    def size(self):
        return self.upload_file.filesize

    @property
    def extension(self):
        return self.upload_file.filename.split('.')[-1]

    def contents(self):
        return self.upload_file.file.read()

    def is_error(self):
        return self.upload_file.errors

    def error(self):
        # map upload errors
        errors = {
            'success': '',
            'file_too_large': 'The uploaded file exceeds the maximum file size',
            'too_many_files': 'The uploaded file exceeds the maximum file size',
            'incorrect_metadata': 'The uploaded file was only partially uploaded',
            'no_file': 'No file was uploaded',
            'missing_directory': 'Missing temporary storage folder',
            'disk_write': 'Failed to write file to disk, check folder permissions of configured upload directory'
        }
        return errors.get(self.upload_file.errors, self.upload_file.errors)

    @staticmethod
    def get_max_size():
        return 2 * 1024 * 1024 # 2 MB

    @staticmethod
    def get_max_upload_count():
        return 10

