# <?php

# class ReservationAction
# {
#     public const Create = 'create';
#     public const Delete = 'delete';
#     public const Update = 'update';
#     public const Approve = 'approve';
#     public const Checkin = 'checkin';
#     public const Checkout = 'checkout';
#     public const WaitList = 'waitlist';
# }


from enum import Enum

class ReservationAction(str, Enum):
    Create = 'create'
    Delete = 'delete'
    Update = 'update'
    Approve = 'approve'
    Checkin = 'checkin'
    Checkout = 'checkout'
    WaitList = 'waitlist'



