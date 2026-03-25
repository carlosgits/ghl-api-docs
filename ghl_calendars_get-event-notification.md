# Get notifications

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/get-event-notification

Screenshot: images/ghl_calendars_get-event-notification_screenshot.png

---

CalendarsCalendar NotificationsGet notifications
Get notifications
GET
 https://services.leadconnectorhq.com/calendars/:calendarId/notifications
Get calendar notifications based on query
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
calendarId
string
REQUIRED
QUERY PARAMETERS
isActive
boolean
deleted
boolean
limit
number
Number of records to return
Default value:100
skip
number
Number of records to skip
Default value:0
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
Array [
_id
string
Notification ID
receiverType
string
Possible values: [contact, guest, assignedUser, emails, phoneNumbers, business]
Example:contact
additionalEmailIds
string[]
Example:["example1@email.com","example2@email.com"]
additionalPhoneNumbers
string[]
Example:["+919876744444","+919876744445"]
channel
string
Possible values: [email, inApp, sms, whatsapp]
Example:email
notificationType
string
Possible values: [booked, confirmation, cancellation, reminder, followup, reschedule]
Example:confirmation
isActive
boolean
Example:true
additionalWhatsappNumbers
string[]
Example:["+919876744444","+919876744445"]
templateId
string
Example:0as9d8as0d
body
string
Example:This is a test notification
subject
string
Example:Test Notification
afterTime
object[]
beforeTime
object[]
selectedUsers
string[]
Example:["user1","user2"]
deleted
boolean
Example:false
]


















































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
curl -L 'https://services.leadconnectorhq.com/calendars/:calendarId/notifications' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!