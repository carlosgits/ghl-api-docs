# Get Service Bookings

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/get-service-bookings

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_get-service-bookings_screenshot.png

---

CalendarsService BookingsGet Service Bookings
Get Service Bookings
GET
 https://services.leadconnectorhq.com/calendars/services/bookings
Retrieve service bookings for a location within a given date range, with an optional service location filter.
Requirements
Scope(s)
calendars/events.readonly
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
Location ID
Example: 0007BWpSzSwfiuSl0tR2
startTime
string
REQUIRED
Start Time (timestamp in milliseconds as string)
Example: 1704110400000
endTime
string
REQUIRED
End Time (timestamp in milliseconds as string)
Example: 1704114000000
timezone
string
Timezone
Example: America/New_York
serviceLocationId
string
Service Location ID
Example: 65e5f6dfacf123513228d384
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
bookings
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
curl -L 'https://services.leadconnectorhq.com/calendars/services/bookings' \
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
startTime — query
REQUIRED
endTime — query
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