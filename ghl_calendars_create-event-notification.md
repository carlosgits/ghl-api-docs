# Create notification

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/create-event-notification

Screenshot: images/ghl_calendars_create-event-notification_screenshot.png

---

CalendarsCalendar NotificationsCreate notification
Create notification
POST
 https://services.leadconnectorhq.com/calendars/:calendarId/notifications
Create Calendar notifications, either one or multiple. All notification settings must be for single calendar only
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
APPLICATION/JSON
BODY ARRAY
REQUIRED
Array [
receiverType
string
REQUIRED
notification recipient type
Possible values: [contact, guest, assignedUser, emails, phoneNumbers, business]
channel
string
REQUIRED
Notification channel
Possible values: [email, inApp, sms, whatsapp]
notificationType
string
REQUIRED
Notification type
Possible values: [booked, confirmation, cancellation, reminder, followup, reschedule]
isActive
boolean
Is the notification active
Default value: true
templateId
string
Template ID for email notification. Not necessary for in-App notification
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
fromAddress
string
from address for email notification
fromName
string
from name for email/sms notification
fromNumber
string
from number for sms notification
]
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
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '[
  {
    "receiverType": "contact",
    "channel": "email",
    "notificationType": "booked",
    "isActive": true,
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
    "fromAddress": "string",
    "fromName": "string",
    "fromNumber": "string"
  }
]'
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
Body
 REQUIRED
[
  {
    "receiverType": "contact",
    "channel": "email",
    "notificationType": "booked",
    "isActive": true,
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
    "fromAddress": "string",
    "fromName": "string",
    "fromNumber": "string"
  }
]
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!