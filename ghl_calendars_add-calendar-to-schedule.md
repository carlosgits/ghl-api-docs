# Apply user availability schedule to a calendar

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/add-calendar-to-schedule

Screenshot: images/ghl_calendars_add-calendar-to-schedule_screenshot.png

---

CalendarsAvailabilityApply user availability schedule to a calendar
Apply user availability schedule to a calendar
PUT
 https://services.leadconnectorhq.com/calendars/schedules/:id/associations/:calendarId
Associates a calendar with the given schedule by adding the calendarId to a schedule
Requirements
Scope(s)
calendars.write
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
id
string
REQUIRED
Unique identifier of the schedule
Example: IkqiJlXJ7o9h61tCHHod
calendarId
string
REQUIRED
Unique identifier of the team calendar to add to the schedule
Example: WvVX9LpvlBO6K506xLbp
Responses
200
400
401
404
Calendar successfully added to schedule
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
curl -L -X PUT 'https://services.leadconnectorhq.com/calendars/schedules/:id/associations/:calendarId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
id — path
REQUIRED
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