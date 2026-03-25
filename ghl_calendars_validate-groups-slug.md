# Validate group slug

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/validate-groups-slug

Screenshot: images/ghl_calendars_validate-groups-slug_screenshot.png

---

CalendarsCalendar GroupsValidate group slug
Validate group slug
POST
 https://services.leadconnectorhq.com/calendars/groups/validate-slug
Validate if group slug is available or not.
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
Location Id
Example:ve9EPM428h8vShlRW1KT
slug
string
REQUIRED
Slug
Example:calendar-1
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
available
boolean
REQUIRED












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
curl -L 'https://services.leadconnectorhq.com/calendars/groups/validate-slug' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "slug": "calendar-1"
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
  "locationId": "ve9EPM428h8vShlRW1KT",
  "slug": "calendar-1"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!