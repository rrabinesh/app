# <?php

# interface IReservationAuthorization
# {
#     /**
#      * @param UserSession $currentUser
#      * @return bool
#      */
#     public function CanChangeUsers(UserSession $currentUser);

#     /**
#      * @param ReservationView $reservationView
#      * @param UserSession $currentUser
#      * @return bool
#      */
#     public function CanEdit(ReservationView $reservationView, UserSession $currentUser);

#     /**
#      * @param ReservationView $reservationView
#      * @param UserSession $currentUser
#      * @return bool
#      */
#     public function CanApprove(ReservationView $reservationView, UserSession $currentUser);

#     /**
#      * @param ReservationView $reservationView
#      * @param UserSession $currentUser
#      * @return bool
#      */
#     public function CanViewDetails(ReservationView $reservationView, UserSession $currentUser);
# }

# class ReservationAuthorization implements IReservationAuthorization
# {
#     /**
#      * @var \IAuthorizationService
#      */
#     private $authorizationService;

#     public function __construct(IAuthorizationService $authorizationService)
#     {
#         $this->authorizationService = $authorizationService;
#     }

#     public function CanEdit(ReservationView $reservationView, UserSession $currentUser)
#     {
#         if ($currentUser->IsAdmin) {
#             return true;
#         }

#         $startTimeConstraint = Configuration::Instance()->GetSectionKey(ConfigSection::RESERVATION, ConfigKeys::RESERVATION_START_TIME_CONSTRAINT);
#         $allowedForAdmin = $reservationView->EndDate->GreaterThanOrEqual(Date::Now());

#         $adminForUser = $this->authorizationService->IsAdminFor($currentUser, $reservationView->OwnerId);
#         $adminForResource = false;
#         foreach ($reservationView->Resources as $resource) {
#             if ($this->authorizationService->CanEditForResource($currentUser, $resource)) {
#                 $adminForResource = true;
#             }
#         }

#         if ($allowedForAdmin && ($adminForUser || $adminForResource) && $startTimeConstraint !== ReservationStartTimeConstraint::NONE) {
#             return $adminForUser || $adminForResource;
#         }

#         $ongoingReservation = true;

#         if ($startTimeConstraint == ReservationStartTimeConstraint::CURRENT) {
#             $ongoingReservation = Date::Now()->LessThan($reservationView->EndDate);
#         }

#         if ($startTimeConstraint == ReservationStartTimeConstraint::FUTURE) {
#             $ongoingReservation = Date::Now()->LessThan($reservationView->StartDate);
#         }

#         if ($ongoingReservation) {
#             if ($this->IsAccessibleTo($reservationView, $currentUser)) {
#                 return true;
#             }
#         }

#         return $currentUser->IsAdmin;    // only admins can edit reservations that have ended
#     }

#     public function CanChangeUsers(UserSession $currentUser)
#     {
#         return $currentUser->IsAdmin || $this->authorizationService->CanReserveForOthers($currentUser);
#     }

#     public function CanApprove(ReservationView $reservationView, UserSession $currentUser)
#     {
#         if (!$reservationView->RequiresApproval()) {
#             return false;
#         }

#         if ($currentUser->IsAdmin) {
#             return true;
#         }

#         $canReserveForUser = $this->authorizationService->CanApproveFor($currentUser, $reservationView->OwnerId);
#         if ($canReserveForUser) {
#             return true;
#         }

#         foreach ($reservationView->Resources as $resource) {
#             if ($this->authorizationService->CanApproveForResource($currentUser, $resource)) {
#                 return true;
#             }
#         }

#         return false;
#     }

#     public function CanViewDetails(ReservationView $reservationView, UserSession $currentUser)
#     {
#         return $this->IsAccessibleTo($reservationView, $currentUser);
#     }

#     /**
#      * @param ReservationView $reservationView
#      * @param UserSession $currentUser
#      * @return bool
#      */
#     private function IsAccessibleTo(ReservationView $reservationView, UserSession $currentUser)
#     {
#         if ($reservationView->OwnerId == $currentUser->UserId || $currentUser->IsAdmin) {
#             return true;
#         } else {
#             $canReserveForUser = $this->authorizationService->CanReserveFor($currentUser, $reservationView->OwnerId);
#             if ($canReserveForUser) {
#                 return true;
#             }

#             foreach ($reservationView->Resources as $resource) {
#                 if ($this->authorizationService->CanEditForResource($currentUser, $resource)) {
#                     return true;
#                 }
#             }
#         }

#         return false;
#     }
# }


from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import List, Optional

# Assuming you have a User model and a Reservation model

class ReservationAuthorization:
    def __init__(self, auth_service: AuthenticationService):
        self.auth_service = auth_service

    def can_edit(self, reservation: Reservation, current_user: User) -> bool:
        if current_user.is_admin:
            return True

        # Implement the logic here to check if the current user has permission to edit the reservation
        # You can use the authentication service to check the user's permissions

        return False

    def can_change_users(self, current_user: User) -> bool:
        if current_user.is_admin:
            return True

        # Implement the logic here to check if the current user can change users for reservations
        # You can use the authentication service to check the user's permissions

        return False

    def can_approve(self, reservation: Reservation, current_user: User) -> bool:
        if not reservation.requires_approval:
            return False

        if current_user.is_admin:
            return True

        # Implement the logic here to check if the current user can approve the reservation
        # You can use the authentication service to check the user's permissions

        return False

    def can_view_details(self, reservation: Reservation, current_user: User) -> bool:
        if reservation.owner_id == current_user.user_id or current_user.is_admin:
            return True

        # Implement the logic here to check if the current user can view the reservation details
        # You can use the authentication service to check the user's permissions

        return False

