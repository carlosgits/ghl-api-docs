# Delete Note

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/delete-appointment-note

Screenshot: images/ghl_calendars_delete-appointment-note_screenshot.png

---

CalendarsAppointment NotesDelete Note
Delete Note
DELETE
 https://services.leadconnectorhq.com/calendars/appointments/:appointmentId/notes/:noteId
Delete Note
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
appointmentId
string
REQUIRED
Appointment ID
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/calendars/appointments/:appointmentId/notes/:noteId' \
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
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!