# Update user availability schedule

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/update-schedule

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_update-schedule_screenshot.png

---

CalendarsAvailabilityUpdate user availability schedule
Update user availability schedule
PUT
 https://services.leadconnectorhq.com/calendars/schedules/:id
Modify an existing schedule by updating its rules, timezone, and name All fields are optional - only provided fields will be updated.
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
Unique identifier of the schedule to update
Example: sch123def456ghi789
APPLICATION/JSON
BODY
REQUIRED
name
string
Human-readable name for the schedule
Example:Updated Business Hours
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
Schedule updated successfully
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
curl -L -X PUT 'https://services.leadconnectorhq.com/calendars/schedules/:id' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "name": "Updated Business Hours",
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
id — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "name": "Updated Business Hours",
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