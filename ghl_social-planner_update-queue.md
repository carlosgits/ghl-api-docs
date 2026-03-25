# Update queue settings or status

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/update-queue

Screenshot: images/ghl_social-planner_update-queue_screenshot.png

---

Social PlannerCategory QueueUpdate queue settings or status
Update queue settings or status
PUT
 https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId
Updates queue status (active/paused/deleted), time slots, or skip dates.
Requirements
Scope(s)
socialplanner/category.write
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
Example: 2021-07-28
PATH PARAMETERS
queueId
string
REQUIRED
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
Location ID
Example:609e126a1c4ae1001291e1b5
skipLegacyWatermark
boolean
Skip legacy watermark cleanup when rescheduling posts
Example:false
status
object
Status of the Queue
Example:paused
skipDateTime
string
Skip Date Time in ISO format
Example:2023-10-05T14:48:00.000Z
timeSlots
object[]
enableFuturePosts
boolean
Enable posting future content. Automatically Queue any New Posts Created in this Category.
Example:true
prioritizeNewContent
boolean
Prioritize new content over older content. When true, new items added via directToQueue will be placed at the top of the queue.
Example:false
Responses
200
400
401
422
Queue updated successfully.
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Example:true
statusCode
number
REQUIRED
Example:200
results
object
REQUIRED
traceId
string

















































Share your feedback
★
★
★
★
★
AUTHORIZATION: AUTHORIZATION
CURL
NODEJS
PYTHON
PHP
JAVA
GO
RUBY
POWERSHELL
CURL
curl -L -X PUT 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "609e126a1c4ae1001291e1b5",
  "skipLegacyWatermark": false,
  "status": "paused",
  "skipDateTime": "2023-10-05T14:48:00.000Z",
  "timeSlots": [
    {
      "dayOfWeek": 0,
      "time": "09:00"
    }
  ],
  "enableFuturePosts": true,
  "prioritizeNewContent": false
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
queueId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "locationId": "609e126a1c4ae1001291e1b5",
  "skipLegacyWatermark": false,
  "status": "paused",
  "skipDateTime": "2023-10-05T14:48:00.000Z",
  "timeSlots": [
    {
      "dayOfWeek": 0,
      "time": "09:00"
    }
  ],
  "enableFuturePosts": true,
  "prioritizeNewContent": false
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!