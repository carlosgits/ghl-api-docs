# Remove user availability schedule from a calendar

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/remove-calendar-from-schedule

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_remove-calendar-from-schedule_screenshot.png

---

CalendarsAvailabilityRemove user availability schedule from a calendar
Remove user availability schedule from a calendar
DELETE
 https://services.leadconnectorhq.com/calendars/schedules/:id/associations/:calendarId
Removes the association between a team calendar and the given schedule by removing the calendarId from the schedule
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
Unique identifier of the calendar to remove from the schedule
Example: WvVX9LpvlBO6K506xLbp
Responses
200
400
401
404
Calendar successfully removed from schedule
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/calendars/schedules/:id/associations/:calendarId' \
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