# Get scheduled posts calendar view

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/fetch-calendar-list

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_fetch-calendar-list_screenshot.png

---

Social PlannerCategory QueueGet scheduled posts calendar view
Get scheduled posts calendar view
POST
 https://services.leadconnectorhq.com/social-media-posting/category/queues/list/calendar
Returns scheduled posts from active queues within a date range. Supports filtering by categories and accounts.
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
categoryIds
string[]
Category Id
Example:["64e431dcaf507c4b26dbdf8b"]
accountIds
string[]
Filter by Account IDs. If not provided or empty, returns all posts.
Example:["aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"]
Responses
201
400
401
422
Calendar list fetched successfully.
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/category/queues/list/calendar' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "609e126a1c4ae1001291e1b5",
  "startDate": "2023-10-01T00:00:00.000Z",
  "endDate": "2023-10-31T23:59:59.999Z",
  "categoryIds": [
    "64e431dcaf507c4b26dbdf8b"
  ],
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
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "locationId": "609e126a1c4ae1001291e1b5",
  "startDate": "2023-10-01T00:00:00.000Z",
  "endDate": "2023-10-31T23:59:59.999Z",
  "categoryIds": [
    "64e431dcaf507c4b26dbdf8b"
  ],
  "accountIds": [
    "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!