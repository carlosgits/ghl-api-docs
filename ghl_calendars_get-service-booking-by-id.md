# Get Service Booking by ID

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/get-service-booking-by-id

Screenshot: images/ghl_calendars_get-service-booking-by-id_screenshot.png

---

CalendarsService BookingsGet Service Booking by ID
Get Service Booking by ID
GET
 https://services.leadconnectorhq.com/calendars/services/bookings/:bookingId
Get a specific service booking by ID
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
PATH PARAMETERS
bookingId
string
REQUIRED
Unique Service Booking ID
Example: IkqiJlXJ7o9h61tCHHod
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
bookingId
string
REQUIRED
Booking ID
Example:7NkT25Vor1v4aQatFsv2
locationId
string
REQUIRED
Location ID
Example:0007BWpSzSwfiuSl0tR2
serviceLocationId
string
REQUIRED
Service Location ID
Example:65e5f6dfacf123513228d384
startTime
string
REQUIRED
Start Time
Example:2023-09-25T16:00:00+05:30
endTime
string
REQUIRED
End Time
Example:2023-09-25T16:30:00+05:30
services
object[]
REQUIRED
timezone
string
REQUIRED
Timezone
Example:America/New_York
status
string
REQUIRED
Status
Example:confirmed






































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
curl -L 'https://services.leadconnectorhq.com/calendars/services/bookings/:bookingId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
bookingId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!