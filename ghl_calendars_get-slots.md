# Get Free Slots

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/get-slots

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_get-slots_screenshot.png

---

CalendarsCalendarsGet Free Slots
Get Free Slots
GET
 https://services.leadconnectorhq.com/calendars/:calendarId/free-slots
Get free slots for a calendar between a date range. Optionally a consumer can also request free slots in a particular timezone and also for a particular user.
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
PATH PARAMETERS
calendarId
string
REQUIRED
Calendar Id
Example: ocQHyuzHvysMo5N5VsXc
QUERY PARAMETERS
startDate
number
REQUIRED
Start Date (⚠️ Important: Date range cannot be more than 31 days)
Example: 1548898600000
endDate
number
REQUIRED
End Date (⚠️ Important: Date range cannot be more than 31 days)
Example: 1601490599999
timezone
string
The timezone in which the free slots are returned
Example: America/Chihuahua
userId
string
The user for whom the free slots are returned
Example: 082goXVW3lIExEQPOnd3
userIds
string[]
The users for whom the free slots are returned
Responses
200
400
401
Availability map keyed by date (YYYY-MM-DD)
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
property name*
SlotsSchema























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
curl -L 'https://services.leadconnectorhq.com/calendars/:calendarId/free-slots' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
calendarId — path
REQUIRED
startDate — query
REQUIRED
endDate — query
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