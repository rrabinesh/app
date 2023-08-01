# <?php

# interface IPermissionService
# {
#     /**
#      * @param IPermissibleResource $resource
#      * @param UserSession $user
#      * @return bool
#      */
#     public function CanAccessResource(IPermissibleResource $resource, UserSession $user);

#     /**
#      * @param IPermissibleResource $resource
#      * @param UserSession $user
#      * @return bool
#      */
#     public function CanBookResource(IPermissibleResource $resource, UserSession $user);

#     /**
#      * @param IPermissibleResource $resource
#      * @param UserSession $user
#      * @return bool
#      */
#     public function CanViewResource(IPermissibleResource $resource, UserSession $user);
# }

# class PermissionService implements IPermissionService
# {
#     /**
#      * @var IResourcePermissionStore
#      */
#     private $_store;

#     private $_allowedResourceIds;

#     private $_bookableResourceIds;

#     private $_viewOnlyResourceIds;


#     /**
#      * @param IResourcePermissionStore $store
#      */
#     public function __construct(IResourcePermissionStore $store)
#     {
#         $this->_store = $store;
#     }

#     /**
#      * @param IPermissibleResource $resource
#      * @param UserSession $user
#      * @return bool
#      */
#     public function CanAccessResource(IPermissibleResource $resource, UserSession $user)
#     {
#         if ($user->IsAdmin) {
#             return true;
#         }

#         if ($this->_allowedResourceIds == null) {
#             $this->_allowedResourceIds = $this->_store->GetAllResources($user->UserId);
#         }

#         return in_array($resource->GetResourceId(), $this->_allowedResourceIds);
#     }

#     /**
#      * @param IPermissibleResource $resource
#      * @param UserSession $user
#      * @return bool
#      */
#     public function CanBookResource(IPermissibleResource $resource, UserSession $user)
#     {
#         if ($user->IsAdmin) {
#             return true;
#         }

#         if ($this->_bookableResourceIds == null) {
#             $this->_bookableResourceIds = $this->_store->GetBookableResources($user->UserId);
#         }

#         return in_array($resource->GetResourceId(), $this->_bookableResourceIds);
#     }

#     /**
#      * @param IPermissibleResource $resource
#      * @param UserSession $user
#      * @return bool
#      */
#     public function CanViewResource(IPermissibleResource $resource, UserSession $user)
#     {
#         if ($user->IsAdmin) {
#             return true;
#         }

#         if ($this->_viewOnlyResourceIds == null) {
#             $this->_viewOnlyResourceIds = $this->_store->GetViewOnlyResources($user->UserId);
#         }

#         return in_array($resource->GetResourceId(), $this->_viewOnlyResourceIds);
#     }
# }


class IPermissionService:
    def CanAccessResource(self, resource: IPermissibleResource, user: UserSession) -> bool:
        pass

    def CanBookResource(self, resource: IPermissibleResource, user: UserSession) -> bool:
        pass

    def CanViewResource(self, resource: IPermissibleResource, user: UserSession) -> bool:
        pass

class PermissionService(IPermissionService):
    def __init__(self, store: IResourcePermissionStore):
        self._store = store
        self._allowed_resource_ids = None
        self._bookable_resource_ids = None
        self._view_only_resource_ids = None

    def CanAccessResource(self, resource: IPermissibleResource, user: UserSession) -> bool:
        if user.IsAdmin:
            return True

        if self._allowed_resource_ids is None:
            self._allowed_resource_ids = self._store.GetAllResources(user.UserId)

        return resource.GetResourceId() in self._allowed_resource_ids

    def CanBookResource(self, resource: IPermissibleResource, user: UserSession) -> bool:
        if user.IsAdmin:
            return True

        if self._bookable_resource_ids is None:
            self._bookable_resource_ids = self._store.GetBookableResources(user.UserId)

        return resource.GetResourceId() in self._bookable_resource_ids

    def CanViewResource(self, resource: IPermissibleResource, user: UserSession) -> bool:
        if user.IsAdmin:
            return True

        if self._view_only_resource_ids is None:
            self._view_only_resource_ids = self._store.GetViewOnlyResources(user.UserId)

        return resource.GetResourceId() in self._view_only_resource_ids

# Dependency to get the permission service
def get_permission_service(store: IResourcePermissionStore) -> IPermissionService:
    return PermissionService(store)


