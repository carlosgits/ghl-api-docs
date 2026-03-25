# Delete an active post and schedule the next one

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/delete-current-active-post-and-schedule-next

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_delete-current-active-post-and-schedule-next_screenshot.png

---

Social PlannerCategory QueueDelete an active post and schedule the next one
Delete an active post and schedule the next one
DELETE
 https://services.leadconnectorhq.com/social-media-posting/category/queues/:postId/active-post
Deletes a post that is currently scheduled and automatically triggers the scheduling of the next available post in the queue.
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
postId
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
Successfully deleted the active post and scheduled the next one.
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:postId/active-post' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
postId — path
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