# Create Calendar Group

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/create-calendar-group

Screenshot: images/ghl_calendars_create-calendar-group_screenshot.png

---

CalendarsCalendar GroupsCreate Calendar Group
Create Calendar Group
POST
 https://services.leadconnectorhq.com/calendars/groups
Create Calendar Group
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
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
Example:ocQHyuzHvysMo5N5VsXc
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
isActive
boolean
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
curl -L 'https://services.leadconnectorhq.com/calendars/groups' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "ocQHyuzHvysMo5N5VsXc",
  "name": "group a",
  "description": "group description",
  "slug": "15-mins",
  "isActive": true
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
2021-04-15
Body
 REQUIRED
{
  "locationId": "ocQHyuzHvysMo5N5VsXc",
  "name": "group a",
  "description": "group description",
  "slug": "15-mins",
  "isActive": true
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!