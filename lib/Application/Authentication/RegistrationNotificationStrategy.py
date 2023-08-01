# <?php

# class RegistrationNotificationStrategy implements IRegistrationNotificationStrategy
# {
#     public function NotifyAccountCreated(User $user, $password)
#     {
#         if (Configuration::Instance()->GetKey(ConfigKeys::REGISTRATION_NOTIFY, new BooleanConverter())) {
#             ServiceLocator::GetEmailService()->Send(new AccountCreationEmail(
#                 $user,
#                 ServiceLocator::GetServer()->GetUserSession()
#             ));
#         }
#     }
# }




# User class (Assuming you have a User class)
class User:
    def __init__(self, email):
        self.email = email


# Configuration class (Assuming you have a Configuration class with GetKey method)
class Configuration:
    @staticmethod
    def get_key(config_key, converter):
        # Replace this with the actual implementation to get configuration value based on config_key and converter
        return True


# BooleanConverter class (Assuming you have a BooleanConverter class)
class BooleanConverter:
    pass


# ServiceLocator class (Assuming you have a ServiceLocator class with GetEmailService and GetServer methods)
class ServiceLocator:
    @staticmethod
    def get_email_service():
        # Replace this with the actual implementation to get the EmailService instance
        return EmailService()

    @staticmethod
    def get_server():
        # Replace this with the actual implementation to get the Server instance
        return Server()


# AccountCreationEmail class (Assuming you have an AccountCreationEmail class)
class AccountCreationEmail:
    def __init__(self, user, user_session):
        self.user = user
        self.user_session = user_session

    def send(self):
        # Replace this with the actual implementation to send the account creation email
        print(f"Sending account creation email to {self.user.email}")


# EmailService class (Assuming you have an EmailService class)
class EmailService:
    def send(self, email):
        # Replace this with the actual implementation to send the email
        email.send()


# Server class (Assuming you have a Server class with GetUserSession method)
class Server:
    def get_user_session(self):
        # Replace this with the actual implementation to get the UserSession instance
        return UserSession()


# UserSession class (Assuming you have a UserSession class)
class UserSession:
    pass


# RegistrationNotificationStrategy class (Implementation of IRegistrationNotificationStrategy interface)
class RegistrationNotificationStrategy:
    def notify_account_created(self, user, password):
        if Configuration.get_key("REGISTRATION_NOTIFY", BooleanConverter()):
            email_service = ServiceLocator.get_email_service()
            email_service.send(AccountCreationEmail(user, ServiceLocator.get_server().get_user_session()))

