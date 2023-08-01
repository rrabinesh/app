# <?php

# class DomainCache
# {
#     private $_cache;

#     public function __construct()
#     {
#         $this->_cache = [];
#     }

#     /**
#      * @param mixed $key
#      * @return bool
#      */
#     public function Exists($key)
#     {
#         return array_key_exists($key, $this->_cache);
#     }

#     /**
#      * @param mixed $key
#      * @return mixed
#      */
#     public function Get($key)
#     {
#         return $this->_cache[$key];
#     }

#     /**
#      * @param mixed $key
#      * @param mixed $object
#      */
#     public function Add($key, $object)
#     {
#         $this->_cache[$key] = $object;
#     }

#     /**
#      * @param mixed $key
#      */
#     public function Remove($key)
#     {
#         unset($this->_cache[$key]);
#     }
# }


from fastapi import FastAPI

app = FastAPI()

# Global cache dictionary to simulate the caching behavior
cache = {}

class DomainCache:
    def __init__(self):
        pass

    def exists(self, key):
        return key in cache

    def get(self, key):
        return cache.get(key)

    def add(self, key, obj):
        cache[key] = obj

    def remove(self, key):
        if key in cache:
            del cache[key]

# Instantiate the DomainCache
domain_cache = DomainCache()

# FastAPI endpoint to simulate the cache operations
@app.get("/cache/{key}")
def get_from_cache(key: str):
    if domain_cache.exists(key):
        return {"key": key, "value": domain_cache.get(key)}
    else:
        return {"key": key, "value": "Not found in cache"}

@app.post("/cache/{key}")
def add_to_cache(key: str, value: str):
    domain_cache.add(key, value)
    return {"key": key, "value": value, "status": "added to cache"}

@app.delete("/cache/{key}")
def remove_from_cache(key: str):
    domain_cache.remove(key)
    return {"key": key, "status": "removed from cache"}



