# <?php

# class AuthorizationServiceFactory
# {
#     /**
#      * @return IAuthorizationService
#      */
#     public static function GetAuthorizationService()
#     {
#         return PluginManager::Instance()->LoadAuthorization();
#     }
# }


from your_plugin_manager_module import PluginManager  # Replace with the actual import for PluginManager
from your_authorization_service_module import IAuthorizationService  # Replace with the actual import for IAuthorizationService

class AuthorizationServiceFactory:
    @staticmethod
    def GetAuthorizationService() -> IAuthorizationService:
        return PluginManager.Instance().LoadAuthorization()

