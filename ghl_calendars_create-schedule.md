# Create user availability schedule

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/create-schedule

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_create-schedule_screenshot.png

---

CalendarsAvailabilityCreate user availability schedule
Create user availability schedule
POST
 https://services.leadconnectorhq.com/calendars/schedules
Create new schedule with specified rules, timezone, location, user and calendar associations.
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
APPLICATION/JSON
BODY
REQUIRED
rules
object[]
timezone
string
REQUIRED
Timezone for the schedule (IANA timezone identifier)
Possible values: Value must match regular expression ^[A-Za-z_]+/[A-Za-z_]+$
Example:America/New_York
locationId
string
REQUIRED
Location ID where this schedule applies
Example:IkqiJlXJ7o9h61tCHHod
name
string
REQUIRED
Human-readable name for the schedule
Example:Business Hours Schedule
userId
string
REQUIRED
User ID associated with the schedule
Example:IkqiJlXJ7o9h61tCHHod
calendarIds
string[]
Calendar IDs associated with the schedule
Example:["WvVX9LpvlBO6K506xLbp","XyZ8MnQrStUvWxYzAbCdEf"]
Responses
201
400
401
422
Schedule created successfully
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
curl -L 'https://services.leadconnectorhq.com/calendars/schedules' \
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
  "timezone": "America/New_York",
  "locationId": "IkqiJlXJ7o9h61tCHHod",
  "name": "Business Hours Schedule",
  "userId": "IkqiJlXJ7o9h61tCHHod",
  "calendarIds": [
    "WvVX9LpvlBO6K506xLbp",
    "XyZ8MnQrStUvWxYzAbCdEf"
  ]
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
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
  "timezone": "America/New_York",
  "locationId": "IkqiJlXJ7o9h61tCHHod",
  "name": "Business Hours Schedule",
  "userId": "IkqiJlXJ7o9h61tCHHod",
  "calendarIds": [
    "WvVX9LpvlBO6K506xLbp",
    "XyZ8MnQrStUvWxYzAbCdEf"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!