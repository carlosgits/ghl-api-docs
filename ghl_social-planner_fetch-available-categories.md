# Get all categories with their queue status

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/fetch-available-categories

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_fetch-available-categories_screenshot.png

---

Social PlannerCategory QueueGet all categories with their queue status
Get all categories with their queue status
GET
 https://services.leadconnectorhq.com/social-media-posting/category/queues/available-categories
Returns categories with status: "available" (no queue), "in_queue" (active/paused queue), or "draft" (queue in draft).
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
QUERY PARAMETERS
locationId
string
REQUIRED
Location ID
Example: 609e126a1c4ae1001291e1b5
skip
string
Number of items to skip
Example: 0
limit
string
Maximum number of items to return
Example: 10
q
string
Search query
Example: Marketing
Responses
200
400
401
422
Available categories fetched successfully.
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/category/queues/available-categories' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
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