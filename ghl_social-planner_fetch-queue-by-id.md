# Fetch a category queue by ID

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/fetch-queue-by-id

Screenshot: images/ghl_social-planner_fetch-queue-by-id_screenshot.png

---

Social PlannerCategory QueueFetch a category queue by ID
Fetch a category queue by ID
GET
 https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId
Retrieves the details of a single category queue by its unique ID. The response includes a count of posts within the queue that have errors.
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
QUERY PARAMETERS
locationId
string
REQUIRED
Location ID
Example: 609e126a1c4ae1001291e1b5
Responses
200
400
401
422
Successfully retrieved the category queue.
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId' \
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
locationId — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!