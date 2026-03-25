# Update Group

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/edit-group

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_edit-group_screenshot.png

---

CalendarsCalendar GroupsUpdate Group
Update Group
PUT
 https://services.leadconnectorhq.com/calendars/groups/:groupId
Update Group by group ID
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
APPLICATION/JSON
BODY
REQUIRED
name
string
REQUIRED
Example:group a
description
string
REQUIRED
Example:group description
slug
string
REQUIRED
Example:15-mins
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
group
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
curl -L -X PUT 'https://services.leadconnectorhq.com/calendars/groups/:groupId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "name": "group a",
  "description": "group description",
  "slug": "15-mins"
}'
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
Body
 REQUIRED
{
  "name": "group a",
  "description": "group description",
  "slug": "15-mins"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!