# Get user availability schedule

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/get-schedule-by-id

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_get-schedule-by-id_screenshot.png

---

CalendarsAvailabilityGet user availability schedule
Get user availability schedule
GET
 https://services.leadconnectorhq.com/calendars/schedules/:id
Retrieve a specific schedule by its unique identifier. Returns detailed information including rules, timezone, and associated calendars/users.
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
id
string
REQUIRED
Unique identifier of the schedule
Example: IkqiJlXJ7o9h61tCHHod
Responses
200
400
401
404
Schedule found and retrieved successfully
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
curl -L 'https://services.leadconnectorhq.com/calendars/schedules/:id' \
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
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!