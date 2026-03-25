# Update notification

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/update-event-notification

Screenshot: images/ghl_calendars_update-event-notification_screenshot.png

---

CalendarsCalendar NotificationsUpdate notification
Update notification
PUT
 https://services.leadconnectorhq.com/calendars/:calendarId/notifications/:notificationId
Update Event notification by id
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
APPLICATION/JSON
BODY
REQUIRED
receiverType
string
Notification recipient type
Possible values: [contact, guest, assignedUser, emails, phoneNumbers, business]
additionalEmailIds
string[]
Additional email addresses to receive notifications.
Example:["example1@email.com","example2@email.com"]
additionalPhoneNumbers
string[]
Additional phone numbers to receive notifications.
Example:["+919876744444","+919876744445"]
selectedUsers
string[]
Selected users for in-App and business email notifications. Supports user IDs and special keyword "sub_account_admin"
Example:["userId1","userId2","sub_account_admin"]
channel
string
Notification channel
Possible values: [email, inApp, sms, whatsapp]
notificationType
string
Notification type
Possible values: [booked, confirmation, cancellation, reminder, followup, reschedule]
isActive
boolean
Is the notification active
Default value: true
deleted
boolean
Marks the notification as deleted (soft delete)
Default value: false
templateId
string
Template ID for email notification
body
string
Body for email notification. Not necessary for in-App notification
subject
string
Subject for email notification. Not necessary for in-App notification
afterTime
object[]
beforeTime
object[]
fromAddress
string
From address for email notification
fromNumber
string
from number for sms notification
fromName
string
From name for email/sms notification
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
curl -L -X PUT 'https://services.leadconnectorhq.com/calendars/:calendarId/notifications/:notificationId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "receiverType": "contact",
  "additionalEmailIds": [
    "example1@email.com",
    "example2@email.com"
  ],
  "additionalPhoneNumbers": [
    "+919876744444",
    "+919876744445"
  ],
  "selectedUsers": [
    "userId1",
    "userId2",
    "sub_account_admin"
  ],
  "channel": "email",
  "notificationType": "booked",
  "isActive": true,
  "deleted": false,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": [
    {
      "timeOffset": 1,
      "unit": "hours"
    }
  ],
  "beforeTime": [
    {
      "timeOffset": 1,
      "unit": "hours"
    }
  ],
  "fromAddress": "string",
  "fromNumber": "string",
  "fromName": "string"
}'
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
Body
 REQUIRED
{
  "receiverType": "contact",
  "additionalEmailIds": [
    "example1@email.com",
    "example2@email.com"
  ],
  "additionalPhoneNumbers": [
    "+919876744444",
    "+919876744445"
  ],
  "selectedUsers": [
    "userId1",
    "userId2",
    "sub_account_admin"
  ],
  "channel": "email",
  "notificationType": "booked",
  "isActive": true,
  "deleted": false,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": [
    {
      "timeOffset": 1,
      "unit": "hours"
    }
  ],
  "beforeTime": [
    {
      "timeOffset": 1,
      "unit": "hours"
    }
  ],
  "fromAddress": "string",
  "fromNumber": "string",
  "fromName": "string"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!