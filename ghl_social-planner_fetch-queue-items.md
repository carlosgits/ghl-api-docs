# Fetch items from a queue

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/fetch-queue-items

Screenshot: images/ghl_social-planner_fetch-queue-items_screenshot.png

---

Social PlannerCategory QueueFetch items from a queue
Fetch items from a queue
POST
 https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items
Returns paginated queue items. Pass sessionId to get draft items from an edit session instead of live items.
Requirements
Scope(s)
socialplanner/category.readonly
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
sessionId
string
Edit session ID
Example:60af88475f1b2c001f5d5f4b
skip
number
Number of items to skip
Example:0
limit
number
Maximum number of items to return
Example:10
errorFilter
boolean
To return only queue items with errors
Example:true
itemId
string
Item ID to center the response around. When provided, the response will position this item in the center with items above and below based on limit. The skip parameter is ignored when itemId is provided.
Example:60af88475f1b2c001f5d5f4b
Responses
201
400
401
422
Queue items fetched successfully.
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/items' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "609e126a1c4ae1001291e1b5",
  "sessionId": "60af88475f1b2c001f5d5f4b",
  "skip": 0,
  "limit": 10,
  "errorFilter": true,
  "itemId": "60af88475f1b2c001f5d5f4b"
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
  "sessionId": "60af88475f1b2c001f5d5f4b",
  "skip": 0,
  "limit": 10,
  "errorFilter": true,
  "itemId": "60af88475f1b2c001f5d5f4b"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!