# Create Recurring Task

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/create-recurring-task

Screenshot: images/ghl_locations_create-recurring-task_screenshot.png

---

Sub-Account (Formerly location)Recurring TasksCreate Recurring Task
Create Recurring Task
POST
 https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks
Create Recurring Task
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
locationId
string
REQUIRED
APPLICATION/JSON
BODY
REQUIRED
title
string
REQUIRED
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
201
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
curl -L 'https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks' \
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