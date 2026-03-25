# Create Service Booking

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/create-service-booking

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_create-service-booking_screenshot.png

---

CalendarsService BookingsCreate Service Booking
Create Service Booking
POST
 https://services.leadconnectorhq.com/calendars/services/bookings
Create a new service booking
Requirements
Scope(s)
calendars/events.write
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
overrideAvailability
boolean
If true the time slot validation would be avoided for any booking creation/update (even the skipSchedulingNotice)
Default value:false
skipSchedulingNotice
boolean
If set to true, the minimum scheduling notice and date range would be ignored
Default value:false
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
Location ID
Example:0007BWpSzSwfiuSl0tR2
contactId
string
REQUIRED
Contact ID
Example:9NkT25Vor1v4aQatFsv2
startTime
string
REQUIRED
Start Time
Example:2021-06-23T03:30:00+05:30
endTime
string
REQUIRED
End Time
Example:2023-09-25T16:30:00+05:30
timezone
string
REQUIRED
Timezone
Example:America/New_York
services
object[]
REQUIRED
serviceLocationId
string
Service Location ID (If not provided, then the default service location will be used)
Example:65e5f6dfacf123513228d384
title
string
Service Booking Title
Example:Service Appointment
status
string
Status. (If not provided, the status configured in Service Global Settings will be used.)
Possible values: [confirmed, new]
Example:confirmed
Responses
201
400
401
Booking created successfully
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
curl -L 'https://services.leadconnectorhq.com/calendars/services/bookings' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "0007BWpSzSwfiuSl0tR2",
  "contactId": "9NkT25Vor1v4aQatFsv2",
  "startTime": "2021-06-23T03:30:00+05:30",
  "endTime": "2023-09-25T16:30:00+05:30",
  "timezone": "America/New_York",
  "services": [
    {
      "id": "a3b4c5d6e7f8901234567890",
      "staffId": "8MkU36Wps2w5bRbuGtw3",
      "position": 0,
      "addOns": [
        {
          "id": "6985f6dfacf123513228d384",
          "quantity": 2,
          "duration": 30
        }
      ]
    }
  ],
  "serviceLocationId": "65e5f6dfacf123513228d384",
  "title": "Service Appointment",
  "status": "confirmed"
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
Show optional parameters
Body
 REQUIRED
{
  "locationId": "0007BWpSzSwfiuSl0tR2",
  "contactId": "9NkT25Vor1v4aQatFsv2",
  "startTime": "2021-06-23T03:30:00+05:30",
  "endTime": "2023-09-25T16:30:00+05:30",
  "timezone": "America/New_York",
  "services": [
    {
      "id": "a3b4c5d6e7f8901234567890",
      "staffId": "8MkU36Wps2w5bRbuGtw3",
      "position": 0,
      "addOns": [
        {
          "id": "6985f6dfacf123513228d384",
          "quantity": 2,
          "duration": 30
        }
      ]
    }
  ],
  "serviceLocationId": "65e5f6dfacf123513228d384",
  "title": "Service Appointment",
  "status": "confirmed"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!