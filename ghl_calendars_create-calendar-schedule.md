# Create event calendar availability schedule

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/create-calendar-schedule

Screenshot: images/ghl_calendars_create-calendar-schedule_screenshot.png

---

CalendarsAvailabilityCreate event calendar availability schedule
Create event calendar availability schedule
POST
 https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId
Create a new availability schedule specifically for an event calendar. The calendar ID is provided in the path, and schedule rules and timezone are provided in the request body.
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
REQUIRED
timezone
string
REQUIRED
Timezone for the schedule (IANA timezone identifier)
Possible values: Value must match regular expression ^[A-Za-z_]+/[A-Za-z_]+$
Example:America/New_York
Responses
201
400
401
404
422
Schedule created successfully for the event calendar
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
          "from": "09:00",
          "to": "17:00"
        }
      ]
    }
  ],
  "timezone": "America/New_York"
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
          "from": "09:00",
          "to": "17:00"
        }
      ]
    }
  ],
  "timezone": "America/New_York"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!