# Get event calendar availability schedule

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/get-calendar-schedule

Screenshot: images/ghl_calendars_get-calendar-schedule_screenshot.png

---

CalendarsAvailabilityGet event calendar availability schedule
Get event calendar availability schedule
GET
 https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId
Retrieve the availability schedule for a specific event calendar. Returns the schedule associated with the calendar ID provided in the path.
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
Unique identifier of the event calendar
Example: WvVX9LpvlBO6K506xLbp
Responses
200
400
401
404
Schedule retrieved successfully for the event calendar
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
schedule
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
curl -L 'https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId' \
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
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!