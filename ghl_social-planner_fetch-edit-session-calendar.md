# Fetch calendar view for an edit session

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/fetch-edit-session-calendar

Screenshot: images/ghl_social-planner_fetch-edit-session-calendar_screenshot.png

---

Social PlannerCategory QueueFetch calendar view for an edit session
Fetch calendar view for an edit session
POST
 https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/edit/calendar
Retrieves a calendar preview of scheduled posts based on draft items within an edit session. This shows how posts would be scheduled if changes were saved.
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
REQUIRED
Edit session ID
Example:60af88475f1b2c001f5d5f4b
startDate
string
REQUIRED
Start Date in ISO format
Example:2023-10-01T00:00:00.000Z
endDate
string
REQUIRED
End Date in ISO format
Example:2023-10-31T23:59:59.999Z
accountIds
string[]
Filter by Account IDs. If not provided or empty, returns all posts.
Example:["aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"]
Responses
201
400
401
422
Edit session calendar fetched successfully.
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/edit/calendar' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "609e126a1c4ae1001291e1b5",
  "sessionId": "60af88475f1b2c001f5d5f4b",
  "startDate": "2023-10-01T00:00:00.000Z",
  "endDate": "2023-10-31T23:59:59.999Z",
  "accountIds": [
    "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"
  ]
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
  "startDate": "2023-10-01T00:00:00.000Z",
  "endDate": "2023-10-31T23:59:59.999Z",
  "accountIds": [
    "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!