# Get Appointment

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/get-appointment

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_get-appointment_screenshot.png

---

CalendarsCalendar EventsGet Appointment
Get Appointment
GET
 https://services.leadconnectorhq.com/calendars/events/appointments/:eventId
Get appointment by ID
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
eventId
string
REQUIRED
Event Id or Instance id. For recurring appointments send masterEventId to modify original series.
Examples:
example1
example2
Event ID
Example:ocQHyuzHvysMo5N5VsXc
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
event
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
curl -L 'https://services.leadconnectorhq.com/calendars/events/appointments/:eventId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!