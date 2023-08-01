# <?php

# class FileExtensionValidator extends ValidatorBase implements IValidator
# {
#     /**
#      * @var string[]
#      */
#     private $validExtensions;

#     /**
#      * @var string
#      */
#     private $fileExtension;

#     /**
#      * @param $validExtensions string|string[]
#      * @param $file UploadedFile
#      */
#     public function __construct($validExtensions, $file)
#     {
#         if (!is_array($validExtensions)) {
#             $validExtensions = [$validExtensions];
#         }
#         $this->validExtensions = $validExtensions;

#         if ($file == null || !is_a($file, 'UploadedFile')) {
#             $this->fileExtension = '';
#         } else {
#             $this->fileExtension = $file->Extension();
#         }
#     }

#     /**
#      * @return void
#      */
#     public function Validate()
#     {
#         $this->isValid = in_array($this->fileExtension, $this->validExtensions);
#     }

#     public function Messages()
#     {
#         return [Resources::GetInstance()->GetString('InvalidAttachmentExtension', implode(',', $this->validExtensions))];
#     }
# }

from fastapi import HTTPException
from starlette.datastructures import UploadFile

class FileExtensionValidator:

    def __init__(self, valid_extensions: list[str], file: UploadFile):
        self.valid_extensions = valid_extensions
        self.file_extension = file.filename.split('.')[-1]

    def validate(self) -> None:
        if self.file_extension not in self.valid_extensions:
            raise HTTPException(
                status_code=400,
                detail="Invalid file extension"
            )
