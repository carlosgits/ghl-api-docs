# Discard edit session changes

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/discard-edit-session

Screenshot: images/ghl_social-planner_discard-edit-session_screenshot.png

---

Social PlannerCategory QueueDiscard edit session changes
Discard edit session changes
POST
 https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/edit/discard
Cancels the edit session and deletes all staged changes without affecting the live queue.
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
sessionId
string
REQUIRED
Edit session ID
Example:60af88475f1b2c001f5d5f4b
keepInDraft
boolean
If true, keeps the queue in DRAFT state after saving instead of automatically activating it. Only applicable when the queue is currently in DRAFT status.
Default value: false
Example:false
Responses
200
400
401
422
Edit session discarded successfully.
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/edit/discard' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "609e126a1c4ae1001291e1b5",
  "sessionId": "60af88475f1b2c001f5d5f4b",
  "keepInDraft": false
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
  "keepInDraft": false
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!