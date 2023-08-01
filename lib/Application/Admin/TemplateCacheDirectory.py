# <?php

# class TemplateCacheDirectory
# {
#     public function Flush()
#     {
#         try {
#             $dirName = $this->GetDirectory();
#             $cacheDir = opendir($dirName);
#             while (false !== ($file = readdir($cacheDir))) {
#                 if ($file != "." && $file != "..") {
#                     unlink($dirName . $file);
#                 }
#             }
#             closedir($cacheDir);
#         } catch (Exception $ex) {
#             Log::Error('Could not flush template cache directory: %s', $ex);
#         }
#     }

#     public function GetDirectory()
#     {
#         return ROOT_DIR . 'tpl_c/';
#     }
# }

from fastapi import FastAPI, HTTPException
import os

# Create a FastAPI app
app = FastAPI()

# Replace with the appropriate ROOT_DIR path in your system
ROOT_DIR = "/path/to/your/root/directory/"

# TemplateCacheDirectory
class TemplateCacheDirectory:
    def flush(self):
        try:
            dir_name = self.get_directory()
            for file in os.listdir(dir_name):
                file_path = os.path.join(dir_name, file)
                if os.path.isfile(file_path):
                    os.unlink(file_path)
        except Exception as ex:
            raise HTTPException(status_code=500, detail=f"Could not flush template cache directory: {ex}")

    def get_directory(self):
        return os.path.join(ROOT_DIR, 'tpl_c/')

# FastAPI endpoint to flush the template cache directory
@app.post("/flush_template_cache/")
async def flush_template_cache():
    template_cache_dir = TemplateCacheDirectory()
    template_cache_dir.flush()
    return {"message": "Template cache directory flushed successfully."}


