# <?php

# require_once(ROOT_DIR . 'lib/WebService/namespace.php');

# class ResourcesResponse extends RestResponse
# {
#     /**
#      * @var array|ResourceResponse[]
#      */
#     public $resources;

#     /**
#      * @param IRestServer $server
#      * @param array|BookableResource[] $resources
#      * @param IEntityAttributeList $attributes
#      */
#     public function __construct(IRestServer $server, $resources, $attributes)
#     {
#         foreach ($resources as $resource) {
#             $this->resources[] = new ResourceResponse($server, $resource, $attributes);
#         }
#     }

#     public static function Example()
#     {
#         return new ExampleResourcesResponse();
#     }
# }

# class ExampleResourcesResponse extends ResourcesResponse
# {
#     public function __construct()
#     {
#         $this->resources = [ResourceResponse::Example()];
#     }
# }


from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define the Pydantic model for CustomAttributeResponse
class CustomAttributeResponse(BaseModel):
    id: int
    label: str
    value: str

# Define the Pydantic model for ResourceResponse
class ResourceResponse(BaseModel):
    resourceId: int
    name: str
    location: str
    contact: str
    notes: str
    minLength: str
    maxLength: str
    requiresApproval: bool
    allowMultiday: bool
    maxParticipants: int
    minNoticeAdd: str
    minNoticeUpdate: str
    minNoticeDelete: str
    maxNotice: str
    description: str
    scheduleId: int
    icsUrl: str = None
    statusId: int
    statusReasonId: int
    customAttributes: List[CustomAttributeResponse] = []
    typeId: int
    groupIds: List[int]
    bufferTime: str
    autoReleaseMinutes: int
    requiresCheckIn: bool
    color: str
    creditsPerSlot: int
    peakCreditsPerSlot: int
    maxConcurrentReservations: int

# Define the Pydantic model for ResourcesResponse
class ResourcesResponse(BaseModel):
    resources: List[ResourceResponse]

# Define the ExampleResourcesResponse Pydantic model
class ExampleResourcesResponse(ResourcesResponse):
    resources: List[ResourceResponse] = [ResourceResponse(
        resourceId=123,
        name='resource name',
        location='location',
        contact='contact',
        notes='notes',
        minLength='1 hour',
        maxLength='2 hours',
        requiresApproval=True,
        allowMultiday=True,
        maxParticipants=10,
        minNoticeAdd='1 hour',
        minNoticeUpdate='1 hour',
        minNoticeDelete='1 hour',
        maxNotice='1 hour',
        description='resource description',
        scheduleId=123,
        statusId=1,
        statusReasonId=3,
        typeId=2,
        bufferTime='1 hour',
        autoReleaseMinutes=15,
        requiresCheckIn=True,
        color='#ffffff',
        creditsPerSlot=3,
        peakCreditsPerSlot=6,
        maxConcurrentReservations=1,
        customAttributes=[CustomAttributeResponse(id=1, label='Attribute1', value='Value1')]
    )]

# Define the endpoint to get the example resources response
@app.get("/resources/")
def resources():
    return ExampleResourcesResponse()


