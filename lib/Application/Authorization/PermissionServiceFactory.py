# <?php

# interface IPermissionServiceFactory
# {
#     /**
#      * @return IPermissionService
#      */
#     public function GetPermissionService();
# }

# class PermissionServiceFactory implements IPermissionServiceFactory
# {
#     /**
#      * @return IPermissionService
#      */
#     public function GetPermissionService()
#     {
#         return PluginManager::Instance()->LoadPermission();
#     }
# }


from fastapi import FastAPI, Depends

# Define your IPermissionService and PluginManager classes or data models here

app = FastAPI()

class IPermissionServiceFactory:
    def GetPermissionService(self) -> IPermissionService:
        pass

class PermissionServiceFactory(IPermissionServiceFactory):
    def GetPermissionService(self) -> IPermissionService:
        return PluginManager.Instance().LoadPermission()

# Dependency to get the permission service factory
def get_permission_service_factory() -> IPermissionServiceFactory:
    return PermissionServiceFactory()

# Dependency to get the permission service
def get_permission_service(permission_service_factory: IPermissionServiceFactory = Depends(get_permission_service_factory)) -> IPermissionService:
    return permission_service_factory.GetPermissionService()

