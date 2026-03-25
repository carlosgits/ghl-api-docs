# List user availability schedule

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/get-all-schedules

Screenshot: images/ghl_calendars_get-all-schedules_screenshot.png

---

CalendarsAvailabilityList user availability schedule
List user availability schedule
GET
 https://services.leadconnectorhq.com/calendars/schedules/search
Retrieve user availability schedules based on various filters including location, calendar, and user. Supports pagination.
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
QUERY PARAMETERS
locationId
string
REQUIRED
Location ID to filter schedules by
Example: IkqiJlXJ7o9h61tCHHod
userId
string
REQUIRED
User ID to filter schedules by specific user
Example: IkqiJlXJ7o9h61tCHHod
calendarId
string
Calendar ID for filtering schedules by specific calendar
Example: WvVX9LpvlBO6K506xLbp
skip
number
Number of items to skip for pagination
Default value:0
Example: 0
limit
number
Possible values: >= 1 and <= 500
Maximum number of items to return (max 500)
Default value:50
Example: 50
Responses
200
400
401
Schedules retrieved successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
schedules
object[]
REQUIRED







































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
curl -L 'https://services.leadconnectorhq.com/calendars/schedules/search' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — query
REQUIRED
userId — query
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!