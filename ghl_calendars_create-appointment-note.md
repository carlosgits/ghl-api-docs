# Create Note

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/create-appointment-note

Screenshot: images/ghl_calendars_create-appointment-note_screenshot.png

---

CalendarsAppointment NotesCreate Note
Create Note
POST
 https://services.leadconnectorhq.com/calendars/appointments/:appointmentId/notes
Create Note
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
APPLICATION/JSON
BODY
REQUIRED
userId
string
Example:GCs5KuzPqTls7vWclkEV
body
string
REQUIRED
Note body
Possible values: <= 5000 characters
Example:lorem ipsum
Responses
201
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
note
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
curl -L 'https://services.leadconnectorhq.com/calendars/appointments/:appointmentId/notes' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "userId": "GCs5KuzPqTls7vWclkEV",
  "body": "lorem ipsum"
}'
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
Body
 REQUIRED
{
  "userId": "GCs5KuzPqTls7vWclkEV",
  "body": "lorem ipsum"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!