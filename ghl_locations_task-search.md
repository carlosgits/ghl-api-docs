# Task Search Filter

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/task-search

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_locations_task-search_screenshot.png

---

Sub-Account (Formerly location)Tasks SearchTask Search Filter
Task Search Filter
POST
 https://services.leadconnectorhq.com/locations/:locationId/tasks/search
Task Search
Requirements
Scope(s)
locations/tasks.readonly
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
PATH PARAMETERS
locationId
string
REQUIRED
Location Id
Example: ve9EPM428h8vShlRW1KT
APPLICATION/JSON
BODY
REQUIRED
contactId
string[]
Contact Ids
Example:["dSMo5jnqkJyh8YeGXM7k","j5WESpmRj816VtyUuWwh"]
completed
boolean
Task Completed Or Pending
Example:true
assignedTo
string[]
Assigned User Ids
Example:["0004Mtfsd11SBU1mBPgd"]
query
string
Search Value
Example:Task Name
limit
number
Limit To Api
Default value: 25
Example:10
skip
number
Number Of Tasks To Skip
Default value: 0
Example:10
businessId
string
Bussiness Id
Example:6348240b98722079e5417332
Responses
200
400
401
422
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
tasks
array[]























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
curl -L 'https://services.leadconnectorhq.com/locations/:locationId/tasks/search' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "contactId": [
    "dSMo5jnqkJyh8YeGXM7k",
    "j5WESpmRj816VtyUuWwh"
  ],
  "completed": true,
  "assignedTo": [
    "0004Mtfsd11SBU1mBPgd"
  ],
  "query": "Task Name",
  "limit": 10,
  "skip": 10,
  "businessId": "6348240b98722079e5417332"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "contactId": [
    "dSMo5jnqkJyh8YeGXM7k",
    "j5WESpmRj816VtyUuWwh"
  ],
  "completed": true,
  "assignedTo": [
    "0004Mtfsd11SBU1mBPgd"
  ],
  "query": "Task Name",
  "limit": 10,
  "skip": 10,
  "businessId": "6348240b98722079e5417332"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!