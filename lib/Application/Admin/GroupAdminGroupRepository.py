# <?php

# require_once(ROOT_DIR . 'Domain/Access/namespace.php');

# class GroupAdminGroupRepository extends GroupRepository
# {
#     /**
#      * @var IUserRepository
#      */
#     private $userRepository;

#     /**
#      * @var UserSession
#      */
#     private $userSession;

#     public function __construct(IUserRepository $userRepository, UserSession $userSession)
#     {
#         $this->userRepository = $userRepository;
#         $this->userSession = $userSession;
#         parent::__construct();
#     }

#     public function GetList($pageNumber = null, $pageSize = null, $sortField = null, $sortDirection = null, $filter = null)
#     {
#         $user = $this->userRepository->LoadById($this->userSession->UserId);

#         $groupIds = [];
#         $groups = $user->GetAdminGroups();
#         foreach ($groups as $group) {
#             $groupIds[] = $group->GroupId;
#         }
#         $and = new SqlFilterIn(new SqlFilterColumn(TableNames::GROUPS_ALIAS, ColumnNames::GROUP_ID), $groupIds);
#         if ($filter == null) {
#             $filter = $and;
#         } else {
#             $filter->_And($and);
#         }
#         return parent::GetList($pageNumber, $pageSize, $sortField, $sortDirection, $filter);
#     }

#     public function LoadById($groupId)
#     {
#         $user = $this->userRepository->LoadById($this->userSession->UserId);

#         if ($user->IsGroupAdminFor($groupId)) {
#             return parent::LoadById($groupId);
#         }

#         return Group::Null();
#     }

#     public function Add(Group $group)
#     {
#         $id = parent::Add($group);
#         $recalledGroup = parent::LoadById($id);

#         $groups = $this->userRepository->LoadGroups($this->userSession->UserId);
#         foreach ($groups as $userGroup) {
#             if ($userGroup->IsGroupAdmin) {
#                 $recalledGroup->ChangeAdmin($userGroup->GroupId);
#                 break;
#             }
#         }

#         parent::Update($recalledGroup);

#         return $id;
#     }
# }

from fastapi import APIRouter, HTTPException

# Assuming you have defined IUserRepository, UserSession, Group, and other required classes.

router = APIRouter()

class GroupAdminGroupRepository:
    def __init__(self, user_repository: IUserRepository, user_session: UserSession):
        self.user_repository = user_repository
        self.user_session = user_session

    def get_list(self, page_number=None, page_size=None, sort_field=None, sort_direction=None, _filter=None):
        user = self.user_repository.LoadById(self.user_session.UserId)
        group_ids = [group.GroupId for group in user.GetAdminGroups()]

        # Assuming SqlFilterIn, SqlFilterColumn, TableNames, and ColumnNames are defined elsewhere
        _and = SqlFilterIn(SqlFilterColumn(TableNames.GROUPS_ALIAS, ColumnNames.GROUP_ID), group_ids)

        if _filter is None:
            _filter = _and
        else:
            _filter._And(_and)

        # Assuming GetList() exists in the GroupRepository
        groups = GroupRepository.GetList(page_number, page_size, sort_field, sort_direction, _filter)
        return groups

    def load_by_id(self, group_id):
        user = self.user_repository.LoadById(self.user_session.UserId)

        if user.IsGroupAdminFor(group_id):
            # Assuming LoadById() exists in the GroupRepository
            group = GroupRepository.LoadById(group_id)
            return group
        else:
            # Assuming Group.Null() is defined in the Group class
            return Group.Null()

    def add(self, group):
        group_id = GroupRepository.Add(group)
        recalled_group = GroupRepository.LoadById(group_id)

        groups = self.user_repository.LoadGroups(self.user_session.UserId)
        for user_group in groups:
            if user_group.IsGroupAdmin:
                recalled_group.ChangeAdmin(user_group.GroupId)
                break

        GroupRepository.Update(recalled_group)

        return group_id
