# <?php

# class ServiceLocator
# {
#     /**
#      * @var Database
#      */
#     private static $_database = null;

#     /**
#      * @var Server
#      */
#     private static $_server = null;

#     /**
#      * @var IEmailService
#      */
#     private static $_emailService = null;

#     /**
#      * @var \Booked\IFileSystem
#      */
#     private static $_fileSystem = null;

#     /**
#      * @return Database
#      */
#     public static function GetDatabase()
#     {
#         require_once(ROOT_DIR . 'lib/Database/namespace.php');

#         if (self::$_database == null) {
#             self::$_database = DatabaseFactory::GetDatabase();
#         }
#         return self::$_database;
#     }

#     public static function SetDatabase(Database $database)
#     {
#         self::$_database = $database;
#     }

#     /**
#      * @return Server
#      */
#     public static function GetServer()
#     {
#         require_once(ROOT_DIR . 'lib/Server/namespace.php');

#         if (self::$_server == null) {
#             self::$_server = new Server();
#         }
#         return self::$_server;
#     }

#     public static function SetServer(Server $server)
#     {
#         self::$_server = $server;
#     }

#     /**
#      * @static
#      * @return IEmailService
#      */
#     public static function GetEmailService()
#     {
#         require_once(ROOT_DIR . 'lib/Email/namespace.php');

#         if (self::$_emailService == null) {
#             if (Configuration::Instance()->GetKey(ConfigKeys::ENABLE_EMAIL, new BooleanConverter())) {
#                 self::$_emailService = new EmailService();
# //                self::$_emailService = new EmailLogger();
#             } else {
#                 self::$_emailService = new NullEmailService();
#             }
#         }
#         return self::$_emailService;
#     }

#     public static function SetEmailService(IEmailService $emailService)
#     {
#         self::$_emailService = $emailService;
#     }

#     /**
#      * @static
#      * @return \Booked\FileSystem
#      */
#     public static function GetFileSystem()
#     {
#         require_once(ROOT_DIR . 'lib/FileSystem/namespace.php');

#         if (self::$_fileSystem == null) {
#             self::$_fileSystem = new \Booked\FileSystem();
#         }

#         return self::$_fileSystem;
#     }

#     public static function SetFileSystem(\Booked\IFileSystem $fileSystem)
#     {
#         self::$_fileSystem = $fileSystem;
#     }
# }


from fastapi import FastAPI, Depends

app = FastAPI()

class Database:
    pass

class Server:
    pass

class IEmailService:
    pass

class EmailService(IEmailService):
    pass

class EmailLogger(IEmailService):
    pass

class NullEmailService(IEmailService):
    pass

class FileSystem:
    pass

class ServiceLocator:
    _database = None
    _server = None
    _email_service = None
    _file_system = None

    @staticmethod
    def get_database() -> Database:
        if ServiceLocator._database is None:
            ServiceLocator._database = Database()
        return ServiceLocator._database

    @staticmethod
    def get_server() -> Server:
        if ServiceLocator._server is None:
            ServiceLocator._server = Server()
        return ServiceLocator._server

    @staticmethod
    def get_email_service(enable_email: bool = False) -> IEmailService:
        if ServiceLocator._email_service is None:
            if enable_email:
                ServiceLocator._email_service = EmailService()
            else:
                ServiceLocator._email_service = NullEmailService()
        return ServiceLocator._email_service

    @staticmethod
    def get_file_system() -> FileSystem:
        if ServiceLocator._file_system is None:
            ServiceLocator._file_system = FileSystem()
        return ServiceLocator._file_system

# Dependency functions
def get_database():
    return ServiceLocator.get_database()

def get_server():
    return ServiceLocator.get_server()

def get_email_service(enable_email: bool = False):
    return ServiceLocator.get_email_service(enable_email)

def get_file_system():
    return ServiceLocator.get_file_system()


