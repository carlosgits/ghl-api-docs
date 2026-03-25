# Delete Notification

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/delete-event-notification

Screenshot: images/ghl_calendars_delete-event-notification_screenshot.png

---

CalendarsCalendar NotificationsDelete Notification
Delete Notification
DELETE
 https://services.leadconnectorhq.com/calendars/:calendarId/notifications/:notificationId
Delete notification
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
calendarId
string
REQUIRED
notificationId
string
REQUIRED
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
message
string
REQUIRED
Result of delete/update operation












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
curl -L -X DELETE 'https://services.leadconnectorhq.com/calendars/:calendarId/notifications/:notificationId' \
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
notificationId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!