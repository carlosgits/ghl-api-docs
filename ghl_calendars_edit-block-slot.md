# Update Block Slot

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/edit-block-slot

Screenshot: images/ghl_calendars_edit-block-slot_screenshot.png

---

CalendarsCalendar EventsUpdate Block Slot
Update Block Slot
PUT
 https://services.leadconnectorhq.com/calendars/events/block-slots/:eventId
Update block slot by ID
Requirements
Scope(s)
calendars/events.write
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
eventId
string
REQUIRED
Event Id or Instance id. For recurring appointments send masterEventId to modify original series.
Examples:
example1
example2
Event ID
Example:ocQHyuzHvysMo5N5VsXc
APPLICATION/JSON
BODY
REQUIRED
title
string
Title
Example:Test Event
calendarId
string
REQUIRED
Either calendarId or assignedUserId can be set, not both.
Example:CVokAlI8fgw4WYWoCtQz
assignedUserId
string
Either calendarId or assignedUserId can be set, not both.
Example:CVokAlI8fgw4WYWoCtQz
locationId
string
REQUIRED
Location Id
Example:C2QujeCh8ZnC7al2InWR
startTime
string
Start Time
Example:2021-06-23T03:30:00+05:30
endTime
string
End Time
Example:2021-06-23T04:30:00+05:30
Responses
201
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
id
string
REQUIRED
Id
Example:0TkCdp9PfvLeWKYRRvIz
locationId
string
REQUIRED
Location Id
Example:C2QujeCh8ZnC7al2InWR
title
string
REQUIRED
Title
Example:My event
startTime
object
REQUIRED
Start Time
Example:2021-06-23T03:30:00+05:30
endTime
object
REQUIRED
End Time
Example:2021-06-23T04:30:00+05:30
calendarId
string
Calendar id
Example:CVokAlI8fgw4WYWoCtQz
assignedUserId
string
Assigned User Id
Example:0007BWpSzSwfiuSl0tR2


















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
curl -L -X PUT 'https://services.leadconnectorhq.com/calendars/events/block-slots/:eventId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "title": "Test Event",
  "calendarId": "CVokAlI8fgw4WYWoCtQz",
  "assignedUserId": "CVokAlI8fgw4WYWoCtQz",
  "locationId": "C2QujeCh8ZnC7al2InWR",
  "startTime": "2021-06-23T03:30:00+05:30",
  "endTime": "2021-06-23T04:30:00+05:30"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
eventId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "title": "Test Event",
  "calendarId": "CVokAlI8fgw4WYWoCtQz",
  "assignedUserId": "CVokAlI8fgw4WYWoCtQz",
  "locationId": "C2QujeCh8ZnC7al2InWR",
  "startTime": "2021-06-23T03:30:00+05:30",
  "endTime": "2021-06-23T04:30:00+05:30"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!