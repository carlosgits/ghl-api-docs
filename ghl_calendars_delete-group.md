# Delete Group

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/delete-group

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_delete-group_screenshot.png

---

CalendarsCalendar GroupsDelete Group
Delete Group
DELETE
 https://services.leadconnectorhq.com/calendars/groups/:groupId
Delete Group
Requirements
Scope(s)
calendars/groups.write
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
Possible values: [2021-04-15]
API Version
PATH PARAMETERS
groupId
string
REQUIRED
Group Id
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
success
boolean
Success
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/calendars/groups/:groupId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
groupId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!