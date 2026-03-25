# Get Calendars

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/get-calendars

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_get-calendars_screenshot.png

---

CalendarsCalendarsGet Calendars
Get Calendars
GET
 https://services.leadconnectorhq.com/calendars/
Get all calendars in a location.
Requirements
Scope(s)
calendars.readonly
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
QUERY PARAMETERS
locationId
string
REQUIRED
Location Id
Example: ve9EPM428h8vShlRW1KT
groupId
string
Group Id
Example: BqTwX8QFwXzpegMve9EQ
showDrafted
boolean
Show drafted
Default value:true
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
calendars
object[]





























































































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
curl -L 'https://services.leadconnectorhq.com/calendars/' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — query
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!