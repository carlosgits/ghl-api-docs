# Fetch slot information for queue items

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/fetch-slots

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_fetch-slots_screenshot.png

---

Social PlannerCategory QueueFetch slot information for queue items
Fetch slot information for queue items
POST
 https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/slots
Returns paginated slot information (scheduledDateTime, isSkipped) for queue items. Pass sessionId to get slots for draft items, or omit for live items. Call this after mutations to refresh slot data.
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
The location ID
Example:abc123
sessionId
string
Session ID for edit mode. If not provided, calculates slots for live items.
Example:507f1f77bcf86cd799439011
skip
number
Number of items to skip
Default value: 0
Example:0
limit
number
Number of items to return
Default value: 20
Example:20
Responses
201
400
401
422
Slots fetched successfully.
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/slots' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "abc123",
  "sessionId": "507f1f77bcf86cd799439011",
  "skip": 0,
  "limit": 20
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
  "locationId": "abc123",
  "sessionId": "507f1f77bcf86cd799439011",
  "skip": 0,
  "limit": 20
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!