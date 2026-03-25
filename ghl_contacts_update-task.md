# Update Task

Source: https://marketplace.gohighlevel.com/docs/ghl/contacts/update-task

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_contacts_update-task_screenshot.png

---

ContactsTasksUpdate Task
Update Task
PUT
 https://services.leadconnectorhq.com/contacts/:contactId/tasks/:taskId
Update Task
Requirements
Scope(s)
contacts.write
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
contactId
string
REQUIRED
Contact Id
Example: sx6wyHhbFdRXh302LLNR
taskId
string
REQUIRED
Task Id
Example: ocQHyuzHvysMo5N5VsXc
APPLICATION/JSON
BODY
REQUIRED
title
string
Example:First Task
body
string
Example:loram ipsum
dueDate
string
Example:2020-10-25T11:00:00Z
completed
boolean
Example:true
assignedTo
string
Example:hxHGVRb1YJUscrCB8eXK
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
task
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
curl -L -X PUT 'https://services.leadconnectorhq.com/contacts/:contactId/tasks/:taskId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "title": "First Task",
  "body": "loram ipsum",
  "dueDate": "2020-10-25T11:00:00Z",
  "completed": true,
  "assignedTo": "hxHGVRb1YJUscrCB8eXK"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
contactId — path
REQUIRED
taskId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "title": "First Task",
  "body": "loram ipsum",
  "dueDate": "2020-10-25T11:00:00Z",
  "completed": true,
  "assignedTo": "hxHGVRb1YJUscrCB8eXK"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!