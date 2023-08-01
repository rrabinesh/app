# <?php

# require_once(ROOT_DIR . 'lib/Application/Authorization/PermissionService.php');
# require_once(ROOT_DIR . 'lib/Application/Authorization/PermissionServiceFactory.php');

# class GuestPermissionService implements IPermissionService
# {
#     /**
#      * @param IPermissibleResource $resource
#      * @param UserSession $user
#      * @return bool
#      */
#     public function CanAccessResource(IPermissibleResource $resource, UserSession $user)
#     {
#         return true;
#     }

#     /**
#      * @param IPermissibleResource $resource
#      * @param UserSession $user
#      * @return bool
#      */
#     public function CanBookResource(IPermissibleResource $resource, UserSession $user)
#     {
#         return false;
#     }

#     /**
#      * @param IPermissibleResource $resource
#      * @param UserSession $user
#      * @return bool
#      */
#     public function CanViewResource(IPermissibleResource $resource, UserSession $user)
#     {
#         return true;
#     }
# }

# class GuestPermissionServiceFactory implements IPermissionServiceFactory
# {
#     /**
#      * @return IPermissionService
#      */
#     public function GetPermissionService()
#     {
#         return new GuestPermissionService();
#     }
# }

class IPermissionService:
    def CanAccessResource(self, resource: IPermissibleResource, user: UserSession) -> bool:
        pass

    def CanBookResource(self, resource: IPermissibleResource, user: UserSession) -> bool:
        pass

    def CanViewResource(self, resource: IPermissibleResource, user: UserSession) -> bool:
        pass

class GuestPermissionService(IPermissionService):
    def CanAccessResource(self, resource: IPermissibleResource, user: UserSession) -> bool:
        return True

    def CanBookResource(self, resource: IPermissibleResource, user: UserSession) -> bool:
        return False

    def CanViewResource(self, resource: IPermissibleResource, user: UserSession) -> bool:
        return True

# Dependency to get the permission service
def get_permission_service() -> IPermissionService:
    return GuestPermissionService()

