# Update Recurring Task

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/update-recurring-task

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_locations_update-recurring-task_screenshot.png

---

Sub-Account (Formerly location)Recurring TasksUpdate Recurring Task
Update Recurring Task
PUT
 https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id
Update Recurring Task
Requirements
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
id
string
REQUIRED
Recurring Task Id
Example: sx6wyHhbFdRXh302Lunr
locationId
string
REQUIRED
Location Id
Example: sx6wyHhbFdRXh302Lunr
APPLICATION/JSON
BODY
REQUIRED
title
string
Name of the task
Example:Task Name
description
string
Description of the task
Example:Task Description
contactIds
string[]
Contact Id
Example:["sx6wyHhbFdRXh302Lunr"]
owners
string[]
Assigned To
Example:["sx6wyHhbFdRXh302Lunr"]
rruleOptions
object
ignoreTaskCreation
boolean
Create initial task or not
Example:true
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
recurringTask
object































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
curl -L -X PUT 'https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "title": "Task Name",
  "description": "Task Description",
  "contactIds": [
    "sx6wyHhbFdRXh302Lunr"
  ],
  "owners": [
    "sx6wyHhbFdRXh302Lunr"
  ],
  "rruleOptions": {
    "intervalType": "hourly",
    "interval": 1,
    "startDate": "2025-07-23T10:00:00.000Z",
    "dueAfterSeconds": 600
  },
  "ignoreTaskCreation": true
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
id — path
REQUIRED
locationId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "title": "Task Name",
  "description": "Task Description",
  "contactIds": [
    "sx6wyHhbFdRXh302Lunr"
  ],
  "owners": [
    "sx6wyHhbFdRXh302Lunr"
  ],
  "rruleOptions": {
    "intervalType": "hourly",
    "interval": 1,
    "startDate": "2025-07-23T10:00:00.000Z",
    "dueAfterSeconds": 600
  },
  "ignoreTaskCreation": true
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!