# Delete Task

Source: https://marketplace.gohighlevel.com/docs/ghl/contacts/delete-task

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_contacts_delete-task_screenshot.png

---

ContactsTasksDelete Task
Delete Task
DELETE
 https://services.leadconnectorhq.com/contacts/:contactId/tasks/:taskId
Delete Task
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
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
succeded
boolean
Example:true












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
curl -L -X DELETE 'https://services.leadconnectorhq.com/contacts/:contactId/tasks/:taskId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!