# <?php

# class FileTypeValidator extends ValidatorBase implements IValidator
# {
#     /**
#      * @var null|UploadedFile
#      */
#     private $file;

#     /**
#      * @var array|string[]
#      */
#     private $allowedTypes;

#     /**
#      * @param UploadedFile|null $file
#      * @param array|string|string[] $allowedTypes
#      */
#     public function __construct($file, $allowedTypes = [])
#     {
#         $this->file = $file;
#         if (!is_array($allowedTypes)) {
#             $this->allowedTypes = [$allowedTypes];
#         } else {
#             $this->allowedTypes = $allowedTypes;
#         }
#     }

#     public function Validate()
#     {
#         if ($this->file == null) {
#             return;
#         }
#         $this->isValid = in_array($this->file->Extension(), $this->allowedTypes);
#         if (!$this->IsValid()) {
#             $this->AddMessage(Resources::GetInstance()->GetString('InvalidAttachmentExtension', [implode(',', $this->allowedTypes)]));
#         }
#     }
# }


from fastapi import HTTPException
from starlette.datastructures import UploadFile

class FileTypeValidator:

    def __init__(self, file: UploadFile, allowed_types: list[str]):
        self.file = file
        self.allowed_types = allowed_types

    def validate(self) -> None:
        if not self.file:
            return
        
        file_type = self.file.filename.split('.')[-1]
        if file_type not in self.allowed_types:
            raise HTTPException(
                status_code=400, 
                detail="Invalid file type. Allowed types: {allowed_types}"
            )
