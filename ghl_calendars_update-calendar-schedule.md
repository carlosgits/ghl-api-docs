# Update event calendar availability schedule

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/update-calendar-schedule

Screenshot: images/ghl_calendars_update-calendar-schedule_screenshot.png

---

CalendarsAvailabilityUpdate event calendar availability schedule
Update event calendar availability schedule
PUT
 https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId
Update the availability schedule for a specific event calendar. Only provided fields will be updated. The calendar ID is provided in the path.
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
calendarId
string
REQUIRED
Unique identifier of the event calendar
Example: WvVX9LpvlBO6K506xLbp
APPLICATION/JSON
BODY
REQUIRED
rules
object[]
timezone
string
Updated timezone for the schedule (IANA timezone identifier)
Possible values: Value must match regular expression ^[A-Za-z_]+/[A-Za-z_]+$
Example:America/Los_Angeles
Responses
200
400
401
404
422
Schedule updated successfully for the event calendar
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
curl -L -X PUT 'https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "rules": [
    {
      "type": "wday",
      "day": "monday",
      "intervals": [
        {
          "from": "08:00",
          "to": "18:00"
        }
      ]
    }
  ],
  "timezone": "America/Los_Angeles"
}'
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
Body
 REQUIRED
{
  "rules": [
    {
      "type": "wday",
      "day": "monday",
      "intervals": [
        {
          "from": "08:00",
          "to": "18:00"
        }
      ]
    }
  ],
  "timezone": "America/Los_Angeles"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!