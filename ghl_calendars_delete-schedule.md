# Delete user availability schedule

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/delete-schedule

Screenshot: images/ghl_calendars_delete-schedule_screenshot.png

---

CalendarsAvailabilityDelete user availability schedule
Delete user availability schedule
DELETE
 https://services.leadconnectorhq.com/calendars/schedules/:id
Permanently remove a schedule and all its associated rules. This action cannot be undone.
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
Unique identifier of the schedule to delete
Example: sch123def456ghi789
Responses
200
400
401
404
Schedule deleted successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
Whether the deletion was successful
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/calendars/schedules/:id' \
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