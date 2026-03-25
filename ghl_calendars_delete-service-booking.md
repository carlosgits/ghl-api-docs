# Delete Service Booking

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/delete-service-booking

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_delete-service-booking_screenshot.png

---

CalendarsService BookingsDelete Service Booking
Delete Service Booking
DELETE
 https://services.leadconnectorhq.com/calendars/services/bookings/:bookingId
Delete a service booking by ID
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
Booking deleted successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Indicates if the deletion was successful
Example:true
message
string
REQUIRED
Response message
Example:Service booking deleted successfully













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
curl -L -X DELETE 'https://services.leadconnectorhq.com/calendars/services/bookings/:bookingId' \
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