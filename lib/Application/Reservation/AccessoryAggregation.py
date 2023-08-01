# <?php

# class AccessoryAggregation
# {
#     private $knownAccessoryIds = [];

#     /**
#      * @var \DateRange
#      */
#     private $duration;

#     /**
#      * @var string[]
#      */
#     private $addedReservations = [];

#     private $accessoryQuantity = [];

#     /**
#      * @param array|AccessoryToCheck[] $accessories
#      * @param DateRange $duration
#      */
#     public function __construct($accessories, $duration)
#     {
#         foreach ($accessories as $a) {
#             $this->knownAccessoryIds[$a->GetId()] = 1;
#         }

#         $this->duration = $duration;
#     }

#     /**
#      * @param AccessoryReservation $accessoryReservation
#      */
#     public function Add(AccessoryReservation $accessoryReservation)
#     {
#         if ($accessoryReservation->GetStartDate()->GreaterThanOrEqual($this->duration->GetEnd()) || $accessoryReservation->GetEndDate()->LessThanOrEqual($this->duration->GetBegin())) {
#             return;
#         }

#         $accessoryId = $accessoryReservation->GetAccessoryId();

#         $key = $accessoryReservation->GetReferenceNumber() . $accessoryId;

#         if (array_key_exists($key, $this->addedReservations)) {
#             return;
#         }

#         $this->addedReservations[$key] = true;

#         if (array_key_exists($accessoryId, $this->accessoryQuantity)) {
#             $this->accessoryQuantity[$accessoryId] += $accessoryReservation->QuantityReserved();
#         } else {
#             $this->accessoryQuantity[$accessoryId] = $accessoryReservation->QuantityReserved();
#         }
#     }

#     /**
#      * @param int $accessoryId
#      * @return int
#      */
#     public function GetQuantity($accessoryId)
#     {
#         if (array_key_exists($accessoryId, $this->accessoryQuantity)) {
#             return $this->accessoryQuantity[$accessoryId];
#         }
#         return 0;
#     }
# }


from datetime import datetime

class AccessoryAggregation:
    def __init__(self, accessories, duration):
        self.knownAccessoryIds = {a.GetId(): 1 for a in accessories}
        self.duration = duration
        self.addedReservations = {}
        self.accessoryQuantity = {}

    def add(self, accessory_reservation):
        if (
            accessory_reservation.GetStartDate() >= self.duration.GetEnd()
            or accessory_reservation.GetEndDate() <= self.duration.GetBegin()
        ):
            return

        accessory_id = accessory_reservation.GetAccessoryId()

        key = f"{accessory_reservation.GetReferenceNumber()}{accessory_id}"

        if key in self.addedReservations:
            return

        self.addedReservations[key] = True

        if accessory_id in self.accessoryQuantity:
            self.accessoryQuantity[accessory_id] += accessory_reservation.QuantityReserved()
        else:
            self.accessoryQuantity[accessory_id] = accessory_reservation.QuantityReserved()

    def get_quantity(self, accessory_id):
        return self.accessoryQuantity.get(accessory_id, 0)

# Example usage:
class AccessoryToCheck:
    def __init__(self, accessory_id):
        self.accessory_id = accessory_id

class AccessoryReservation:
    def __init__(self, accessory_id, start_date, end_date, reference_number, quantity_reserved):
        self.accessory_id = accessory_id
        self.start_date = start_date
        self.end_date = end_date
        self.reference_number = reference_number
        self.quantity_reserved = quantity_reserved
