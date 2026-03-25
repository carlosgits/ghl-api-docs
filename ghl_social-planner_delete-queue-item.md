# Delete an item from a queue

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/delete-queue-item

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_delete-queue-item_screenshot.png

---

Social PlannerCategory QueueDelete an item from a queue
Delete an item from a queue
DELETE
 https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId
Deletes an item from a specific category queue.
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
QUERY PARAMETERS
locationId
string
REQUIRED
Location ID
Example: 609e126a1c4ae1001291e1b5
sessionId
string
Edit session ID
Example: 60af88475f1b2c001f5d5f4b
Responses
200
400
401
422
The queue item has been successfully deleted.
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items/:itemId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
locationId — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!