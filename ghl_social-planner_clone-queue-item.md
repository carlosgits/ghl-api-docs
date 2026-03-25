# Clone a queue item

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/clone-queue-item

Screenshot: images/ghl_social-planner_clone-queue-item_screenshot.png

---

Social PlannerCategory QueueClone a queue item
Clone a queue item
POST
 https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId/clone
Duplicates an existing queue item at a specified order position. Requires an active edit session.
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
itemId
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
sessionId
string
REQUIRED
Edit session ID
Example:60af88475f1b2c001f5d5f4b
order
number
REQUIRED
Order for the cloned item (typically between source and next item)
Example:1.5
Responses
201
400
401
422
Queue item cloned successfully.
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
Example:201
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId/clone' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "609e126a1c4ae1001291e1b5",
  "sessionId": "60af88475f1b2c001f5d5f4b",
  "order": 1.5
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
itemId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "locationId": "609e126a1c4ae1001291e1b5",
  "sessionId": "60af88475f1b2c001f5d5f4b",
  "order": 1.5
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!