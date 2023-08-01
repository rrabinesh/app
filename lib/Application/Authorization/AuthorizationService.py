# <?php

# interface IRoleService
# {
#     /**
#      * @abstract
#      * @param User $user
#      * @return bool
#      */
#     public function IsApplicationAdministrator(User $user);

#     /**
#      * @abstract
#      * @param User $user
#      * @return bool
#      */
#     public function IsResourceAdministrator(User $user);

#     /**
#      * @abstract
#      * @param User $user
#      * @return bool
#      */
#     public function IsGroupAdministrator(User $user);

#     /**
#      * @abstract
#      * @param User $user
#      * @return bool
#      */
#     public function IsScheduleAdministrator(User $user);

#     /**
#      * @param UserSession $userSession
#      * @param int $otherUserId
#      * @return bool
#      */
#     public function IsAdminFor(UserSession $userSession, $otherUserId);
# }

# interface IAuthorizationService extends IRoleService
# {
#     /**
#      * @abstract
#      * @param UserSession $reserver user who is requesting access to perform action
#      * @return bool
#      */
#     public function CanReserveForOthers(UserSession $reserver);

#     /**
#      * @abstract
#      * @param UserSession $reserver user who is requesting access to perform action
#      * @param int $reserveForId user to reserve for
#      * @return bool
#      */
#     public function CanReserveFor(UserSession $reserver, $reserveForId);

#     /**
#      * @abstract
#      * @param UserSession $approver user who is requesting access to perform action
#      * @param int $approveForId user to approve for
#      * @return bool
#      */
#     public function CanApproveFor(UserSession $approver, $approveForId);

#     /**
#      * @param UserSession $user
#      * @param IResource $resource
#      * @return bool
#      */
#     public function CanEditForResource(UserSession $user, IResource $resource);

#     /**
#      * @param UserSession $user
#      * @param IResource $resource
#      * @return bool
#      */
#     public function CanApproveForResource(UserSession $user, IResource $resource);
# }

# class AuthorizationService implements IAuthorizationService
# {
#     /**
#      * @var IUserRepository
#      */
#     private $userRepository;

#     public function __construct(IUserRepository $userRepository)
#     {
#         $this->userRepository = $userRepository;
#     }

#     /**
#      * @param UserSession $reserver user who is requesting access to perform action
#      * @return bool
#      */
#     public function CanReserveForOthers(UserSession $reserver)
#     {
#         if ($reserver->IsAdmin) {
#             return true;
#         }

#         $user = $this->userRepository->LoadById($reserver->UserId);

#         return $user->IsGroupAdmin();
#     }

#     /**
#      * @param UserSession $reserver user who is requesting access to perform action
#      * @param int $reserveForId user to reserve for
#      * @return bool
#      */
#     public function CanReserveFor(UserSession $reserver, $reserveForId)
#     {
#         if ($reserveForId == $reserver->UserId) {
#             return true;
#         }

#         return $this->IsAdminFor($reserver, $reserveForId);
#     }

#     /**
#      * @param UserSession $approver user who is requesting access to perform action
#      * @param int $approveForId user to approve for
#      * @return bool
#      */
#     public function CanApproveFor(UserSession $approver, $approveForId)
#     {
#         return $this->IsAdminFor($approver, $approveForId);
#     }

#     /**
#      * @param User $user
#      * @return bool
#      */
#     public function IsApplicationAdministrator(User $user)
#     {
#         if (Configuration::Instance()->IsAdminEmail($user->EmailAddress())) {
#             return true;
#         }

#         return $user->IsInRole(RoleLevel::APPLICATION_ADMIN);
#     }

#     /**
#      * @param User $user
#      * @return bool
#      */
#     public function IsResourceAdministrator(User $user)
#     {
#         return $user->IsInRole(RoleLevel::RESOURCE_ADMIN);
#     }

#     /**
#      * @param User $user
#      * @return bool
#      */
#     public function IsGroupAdministrator(User $user)
#     {
#         return $user->IsInRole(RoleLevel::GROUP_ADMIN);
#     }

#     /**
#      * @param User $user
#      * @return bool
#      */
#     public function IsScheduleAdministrator(User $user)
#     {
#         return $user->IsInRole(RoleLevel::SCHEDULE_ADMIN);
#     }

#     /**
#      * @param UserSession $userSession
#      * @param int $otherUserId
#      * @return bool
#      */
#     public function IsAdminFor(UserSession $userSession, $otherUserId)
#     {
#         if ($userSession->IsAdmin) {
#             return true;
#         }

#         if (!$userSession->IsGroupAdmin) {
#             // dont even bother checking if the user isnt a group admin
#             return false;
#         }

#         $user1 = $this->userRepository->LoadById($userSession->UserId);
#         $user2 = $this->userRepository->LoadById($otherUserId);

#         return $user1->IsAdminFor($user2);
#     }

#     /**
#      * @param UserSession $userSession
#      * @param IResource $resource
#      * @return bool
#      */
#     public function CanEditForResource(UserSession $userSession, IResource $resource)
#     {
#         if ($userSession->IsAdmin) {
#             return true;
#         }

#         if (!$userSession->IsResourceAdmin && !$userSession->IsScheduleAdmin) {
#             return false;
#         }

#         $user = $this->userRepository->LoadById($userSession->UserId);

#         return $user->IsResourceAdminFor($resource);
#     }

#     /**
#      * @param UserSession $userSession
#      * @param IResource $resource
#      * @return bool
#      */
#     public function CanApproveForResource(UserSession $userSession, IResource $resource)
#     {
#         if ($userSession->IsAdmin) {
#             return true;
#         }

#         if (!$userSession->IsResourceAdmin) {
#             return false;
#         }

#         $user = $this->userRepository->LoadById($userSession->UserId);

#         return $user->IsResourceAdminFor($resource);
#     }
# }

# class GuestAuthorizationService implements IAuthorizationService
# {
#     public function IsApplicationAdministrator(User $user)
#     {
#         return false;
#     }

#     public function IsResourceAdministrator(User $user)
#     {
#         return false;
#     }

#     public function IsGroupAdministrator(User $user)
#     {
#         return false;
#     }

#     public function IsScheduleAdministrator(User $user)
#     {
#         return false;
#     }

#     public function IsAdminFor(UserSession $userSession, $otherUserId)
#     {
#         return false;
#     }

#     public function CanReserveForOthers(UserSession $reserver)
#     {
#         return false;
#     }

#     public function CanReserveFor(UserSession $reserver, $reserveForId)
#     {
#         return false;
#     }

#     public function CanApproveFor(UserSession $approver, $approveForId)
#     {
#         return false;
#     }

#     public function CanEditForResource(UserSession $user, IResource $resource)
#     {
#         return false;
#     }

#     public function CanApproveForResource(UserSession $user, IResource $resource)
#     {
#         return false;
#     }
# }


from abc import ABC, abstractmethod
from typing import Union

# IRoleService interface
class IRoleService(ABC):
    @abstractmethod
    def IsApplicationAdministrator(self, user: User) -> bool:
        pass

    @abstractmethod
    def IsResourceAdministrator(self, user: User) -> bool:
        pass

    @abstractmethod
    def IsGroupAdministrator(self, user: User) -> bool:
        pass

    @abstractmethod
    def IsScheduleAdministrator(self, user: User) -> bool:
        pass

    @abstractmethod
    def IsAdminFor(self, user_session: UserSession, other_user_id: int) -> bool:
        pass

# IAuthorizationService interface
class IAuthorizationService(IRoleService, ABC):
    @abstractmethod
    def CanReserveForOthers(self, reserver: UserSession) -> bool:
        pass

    @abstractmethod
    def CanReserveFor(self, reserver: UserSession, reserve_for_id: int) -> bool:
        pass

    @abstractmethod
    def CanApproveFor(self, approver: UserSession, approve_for_id: int) -> bool:
        pass

    @abstractmethod
    def CanEditForResource(self, user: UserSession, resource: IResource) -> bool:
        pass

    @abstractmethod
    def CanApproveForResource(self, user: UserSession, resource: IResource) -> bool:
        pass

# AuthorizationService class
class AuthorizationService(IAuthorizationService):
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def CanReserveForOthers(self, reserver: UserSession) -> bool:
        if reserver.IsAdmin:
            return True

        user = self.user_repository.LoadById(reserver.UserId)
        return user.IsGroupAdmin()

    def CanReserveFor(self, reserver: UserSession, reserve_for_id: int) -> bool:
        if reserve_for_id == reserver.UserId:
            return True

        return self.IsAdminFor(reserver, reserve_for_id)

    def CanApproveFor(self, approver: UserSession, approve_for_id: int) -> bool:
        return self.IsAdminFor(approver, approve_for_id)

    def IsApplicationAdministrator(self, user: User) -> bool:
        if Configuration.Instance().IsAdminEmail(user.EmailAddress()):
            return True

        return user.IsInRole(RoleLevel.APPLICATION_ADMIN)

    def IsResourceAdministrator(self, user: User) -> bool:
        return user.IsInRole(RoleLevel.RESOURCE_ADMIN)

    def IsGroupAdministrator(self, user: User) -> bool:
        return user.IsInRole(RoleLevel.GROUP_ADMIN)

    def IsScheduleAdministrator(self, user: User) -> bool:
        return user.IsInRole(RoleLevel.SCHEDULE_ADMIN)

    def IsAdminFor(self, user_session: UserSession, other_user_id: int) -> bool:
        if user_session.IsAdmin:
            return True

        if not user_session.IsGroupAdmin:
            return False

        user1 = self.user_repository.LoadById(user_session.UserId)
        user2 = self.user_repository.LoadById(other_user_id)

        return user1.IsAdminFor(user2)

    def CanEditForResource(self, user_session: UserSession, resource: IResource) -> bool:
        if user_session.IsAdmin:
            return True

        if not user_session.IsResourceAdmin and not user_session.IsScheduleAdmin:
            return False

        user = self.user_repository.LoadById(user_session.UserId)
        return user.IsResourceAdminFor(resource)

    def CanApproveForResource(self, user_session: UserSession, resource: IResource) -> bool:
        if user_session.IsAdmin:
            return True

        if not user_session.IsResourceAdmin:
            return False

        user = self.user_repository.LoadById(user_session.UserId)
        return user.IsResourceAdminFor(resource)

# GuestAuthorizationService class
class GuestAuthorizationService(IAuthorizationService):
    def IsApplicationAdministrator(self, user: User) -> bool:
        return False

    def IsResourceAdministrator(self, user: User) -> bool:
        return False

    def IsGroupAdministrator(self, user: User) -> bool:
        return False

    def IsScheduleAdministrator(self, user: User) -> bool:
        return False

    def IsAdminFor(self, user_session: UserSession, other_user_id: int) -> bool:
        return False

    def CanReserveForOthers(self, reserver: UserSession) -> bool:
        return False

    def CanReserveFor(self, reserver: UserSession, reserve_for_id: int) -> bool:
        return False

    def CanApproveFor(self, approver: UserSession, approve_for_id: int) -> bool:
        return False

    def CanEditForResource(self, user: UserSession, resource: IResource) -> bool:
        return False

    def CanApproveForResource(self, user: UserSession, resource: IResource) -> bool:
        return False


