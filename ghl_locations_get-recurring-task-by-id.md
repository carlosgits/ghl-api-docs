# Get Recurring Task By Id

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/get-recurring-task-by-id

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_locations_get-recurring-task-by-id_screenshot.png

---

Sub-Account (Formerly location)Recurring TasksGet Recurring Task By Id
Get Recurring Task By Id
GET
 https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id
Get Recurring Task By Id
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
curl -L 'https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!