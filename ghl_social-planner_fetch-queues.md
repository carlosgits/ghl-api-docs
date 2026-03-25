# Fetch category queues for a location

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/fetch-queues

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_fetch-queues_screenshot.png

---

Social PlannerCategory QueueFetch category queues for a location
Fetch category queues for a location
POST
 https://services.leadconnectorhq.com/social-media-posting/category/queues/list
Retrieves a paginated list of all category queues for a given location, excluding any that have been marked as deleted.
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
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
Location ID
Example:609e126a1c4ae1001291e1b5
skip
number
Number of items to skip
Example:0
limit
number
Maximum number of items to return
Example:10
Responses
201
400
401
422
Successfully retrieved category queues.
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/category/queues/list' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "609e126a1c4ae1001291e1b5",
  "skip": 0,
  "limit": 10
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "locationId": "609e126a1c4ae1001291e1b5",
  "skip": 0,
  "limit": 10
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!