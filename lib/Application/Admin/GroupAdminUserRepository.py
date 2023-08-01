# <?php

# require_once(ROOT_DIR . 'Domain/Access/namespace.php');

# class GroupAdminUserRepository extends UserRepository
# {
#     /**
#      * @var IGroupViewRepository
#      */
#     private $groupRepository;

#     /**
#      * @var UserSession
#      */
#     private $userSession;

#     public function __construct(IGroupViewRepository $groupRepository, UserSession $userSession)
#     {
#         $this->groupRepository = $groupRepository;
#         $this->userSession = $userSession;
#         parent::__construct();
#     }

#     public function GetList($pageNumber, $pageSize, $sortField = null, $sortDirection = null, $filter = null, $accountStatus = AccountStatus::ALL)
#     {
#         if (empty($accountStatus)) {
#             $accountStatus = AccountStatus::ALL;
#         }

#         $user = parent::LoadById($this->userSession->UserId);

#         $groupIds = [];

#         foreach ($user->GetAdminGroups() as $group) {
#             $groupIds[] = $group->GroupId;
#         }

#         return $this->groupRepository->GetUsersInGroup($groupIds, $pageNumber, $pageSize, $filter, $accountStatus);
#     }

#     /**
#      * @param int $userId
#      * @return User|void
#      */
#     public function LoadById($userId)
#     {
#         $user = parent::LoadById($userId);
#         $me = parent::LoadById($this->userSession->UserId);

#         if ($userId == $this->userSession->UserId || $me->IsAdminFor($user)) {
#             return $user;
#         }

#         return User::Null();
#     }
# }

# Assuming you have defined IGroupViewRepository, UserSession, User, AccountStatus, and other required classes.

class GroupAdminUserRepository:
    def __init__(self, group_repository: IGroupViewRepository, user_session: UserSession):
        self.group_repository = group_repository
        self.user_session = user_session

    def get_list(self, page_number, page_size, sort_field=None, sort_direction=None, _filter=None, account_status=AccountStatus.ALL):
        if not account_status:
            account_status = AccountStatus.ALL

        user = self.load_by_id(self.user_session.UserId)
        group_ids = [group.GroupId for group in user.GetAdminGroups()]

        return self.group_repository.GetUsersInGroup(group_ids, page_number, page_size, _filter, account_status)

    def load_by_id(self, user_id):
        user = super().load_by_id(user_id)
        me = self.load_by_id(self.user_session.UserId)

        if user_id == self.user_session.UserId or me.IsAdminFor(user):
            return user

        return User.Null()



