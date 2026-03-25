# Get Blocked Slots

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/get-blocked-slots

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_get-blocked-slots_screenshot.png

---

CalendarsCalendar EventsGet Blocked Slots
Get Blocked Slots
GET
 https://services.leadconnectorhq.com/calendars/blocked-slots
Get Blocked Slots
Requirements
Scope(s)
calendars/events.readonly
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
Example: 0007BWpSzSwfiuSl0tR2
userId
string
User Id - Owner of an appointment. Either of userId, groupId or calendarId is required
Example: CVokAlI8fgw4WYWoCtQz
calendarId
string
Either of calendarId, userId or groupId is required
Example: BqTwX8QFwXzpegMve9EQ
groupId
string
Either of groupId, calendarId or userId is required
Example: ocQHyuzHvysMo5N5VsXc
startTime
string
REQUIRED
Start Time (in millis)
Example: 1680373800000
endTime
string
REQUIRED
End Time (in millis)
Example: 1680978599999
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
events
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
curl -L 'https://services.leadconnectorhq.com/calendars/blocked-slots' \
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
startTime — query
REQUIRED
endTime — query
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