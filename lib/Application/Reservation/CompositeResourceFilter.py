# <?php

# class CompositeResourceFilter implements IResourceFilter
# {
#     /**
#      * @var array|IResourceFilter[]
#      */
#     private $filters = [];

#     public function Add(IResourceFilter $filter)
#     {
#         $this->filters[] = $filter;
#     }

#     /**
#      * @param IResource $resource
#      * @return bool
#      */
#     public function ShouldInclude($resource)
#     {
#         foreach ($this->filters as $filter) {
#             if (!$filter->ShouldInclude($resource)) {
#                 return false;
#             }
#         }

#         return true;
#     }
# }


from abc import ABC, abstractmethod

class IResourceFilter(ABC):
    @abstractmethod
    def should_include(self, resource):
        pass

class CompositeResourceFilter:
    def __init__(self):
        self.filters = []

    def add(self, filter_obj: IResourceFilter):
        self.filters.append(filter_obj)

    def should_include(self, resource):
        for filter_obj in self.filters:
            if not filter_obj.should_include(resource):
                return False

        return True

# Create a sample ResourceFilter class that implements IResourceFilter
class ResourceFilter(IResourceFilter):
    def should_include(self, resource):
        # Add your custom resource filtering logic here
        return True 
