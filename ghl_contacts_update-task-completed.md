# Update Task Completed

Source: https://marketplace.gohighlevel.com/docs/ghl/contacts/update-task-completed

Screenshot: images/ghl_contacts_update-task-completed_screenshot.png

---

ContactsTasksUpdate Task Completed
Update Task Completed
PUT
 https://services.leadconnectorhq.com/contacts/:contactId/tasks/:taskId/completed
Update Task Completed
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
completed
boolean
REQUIRED
Example:true
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
curl -L -X PUT 'https://services.leadconnectorhq.com/contacts/:contactId/tasks/:taskId/completed' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "completed": true
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
  "completed": true
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!