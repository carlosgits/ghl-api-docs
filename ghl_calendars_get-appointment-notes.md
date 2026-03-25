# Get Notes

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/get-appointment-notes

Screenshot: images/ghl_calendars_get-appointment-notes_screenshot.png

---

CalendarsAppointment NotesGet Notes
Get Notes
GET
 https://services.leadconnectorhq.com/calendars/appointments/:appointmentId/notes
Get Appointment Notes
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
PATH PARAMETERS
appointmentId
string
REQUIRED
Appointment ID
QUERY PARAMETERS
limit
number
REQUIRED
Possible values: <= 20
Limit of notes to fetch
Example: 10
offset
number
REQUIRED
Offset of notes to fetch
Example: 0
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
notes
object[]
hasMore
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
curl -L 'https://services.leadconnectorhq.com/calendars/appointments/:appointmentId/notes' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
appointmentId — path
REQUIRED
limit — query
REQUIRED
offset — query
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!