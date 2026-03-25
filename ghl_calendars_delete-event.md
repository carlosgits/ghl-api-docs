# Delete Event

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/delete-event

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_delete-event_screenshot.png

---

CalendarsCalendar EventsDelete Event
Delete Event
DELETE
 https://services.leadconnectorhq.com/calendars/events/:eventId
Delete event by ID
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
object
Responses
201
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
succeeded
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/calendars/events/:eventId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{}'
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
{}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!