# Create Calendar

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/create-calendar

Screenshot: images/ghl_calendars_create-calendar_screenshot.png

---

CalendarsCalendarsCreate Calendar
Create Calendar
POST
 https://services.leadconnectorhq.com/calendars/
Create calendar in a location.
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
APPLICATION/JSON
BODY
REQUIRED
isActive
boolean
Should the created calendar be active or draft
Default value: true
notifications
object[]
DEPRECATED
locationId
string
REQUIRED
Example:ocQHyuzHvysMo5N5VsXc
groupId
string
Group Id
Example:BqTwX8QFwXzpegMve9EQ
teamMembers
object[]
eventType
string
Possible values: [RoundRobin_OptimizeForAvailability, RoundRobin_OptimizeForEqualDistribution]
Default value: RoundRobin_OptimizeForAvailability
name
string
REQUIRED
Example:test calendar
description
string
Example:this is used for testing
slug
string
Example:test1
widgetSlug
string
Example:test1
calendarType
string
Possible values: [round_robin, event, class_booking, collective, service_booking, personal]
widgetType
string
Calendar widget type. Choose "default" for "neo" and "classic" for "classic" layout.
Possible values: [default, classic]
Default value: classic
Example:classic
eventTitle
string
Default value: {{contact.name}}
eventColor
string
Default value: #039be5
locationConfigurations
object[]
slotDuration
number
This controls the duration of the meeting
Default value: 30
slotDurationUnit
string
Unit for slot duration.
Possible values: [mins, hours]
slotInterval
number
Slot interval reflects the amount of time the between booking slots that will be shown in the calendar.
Default value: 30
slotIntervalUnit
string
Unit for slot interval.
Possible values: [mins, hours]
slotBuffer
number
Slot-Buffer is additional time that can be added after an appointment, allowing for extra time to wrap up
slotBufferUnit
string
Unit for slot buffer.
Possible values: [mins, hours]
preBuffer
number
Pre-Buffer is additional time that can be added before an appointment, allowing for extra time to get ready
preBufferUnit
string
Unit for pre-buffer.
Possible values: [mins, hours]
appoinmentPerSlot
number
Maximum bookings per slot (per user). Maximum seats per slot in case of Class Booking Calendar.
Default value: 1
appoinmentPerDay
number
Number of appointments that can be booked for a given day
allowBookingAfter
number
Minimum scheduling notice for events
allowBookingAfterUnit
string
Unit for minimum scheduling notice
Possible values: [hours, days, weeks, months, mins]
Example:days
allowBookingFor
number
Minimum number of days/weeks/months for which to allow booking events
allowBookingForUnit
string
Unit for controlling the duration for which booking would be allowed for
Possible values: [days, weeks, months]
Example:days
openHours
object[]
DEPRECATED
enableRecurring
boolean
Enable recurring appointments for the calendars. Please note that only one member should be added in the calendar to enable this
Default value: false
recurring
object
formId
string
stickyContact
boolean
isLivePaymentMode
boolean
autoConfirm
boolean
Default value: true
shouldSendAlertEmailsToAssignedMember
boolean
alertEmail
string
googleInvitationEmails
boolean
Default value: false
allowReschedule
boolean
Default value: true
allowCancellation
boolean
Default value: true
shouldAssignContactToTeamMember
boolean
shouldSkipAssigningContactForExisting
boolean
notes
string
pixelId
string
formSubmitType
string
Possible values: [RedirectURL, ThankYouMessage]
Default value: ThankYouMessage
formSubmitRedirectURL
string
formSubmitThanksMessage
string
availabilityType
number
DEPRECATED
While we will support this property for backward compatibility, it is not required anymore.
Possible values: [0, 1]
availabilities
object[]
DEPRECATED
guestType
string
Possible values: [count_only, collect_detail]
consentLabel
string
calendarCoverImage
string
Example:https://path-to-image.com
lookBusyConfig
object
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
calendar
object
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
curl -L 'https://services.leadconnectorhq.com/calendars/' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "isActive": true,
  "locationId": "ocQHyuzHvysMo5N5VsXc",
  "groupId": "BqTwX8QFwXzpegMve9EQ",
  "teamMembers": [
    {
      "userId": "ocQHyuzHvysMo5N5VsXc",
      "priority": 0.5,
      "isPrimary": true,
      "locationConfigurations": [
        {
          "kind": "custom",
          "location": "string"
        }
      ]
    }
  ],
  "eventType": "RoundRobin_OptimizeForAvailability",
  "name": "test calendar",
  "description": "this is used for testing",
  "slug": "test1",
  "widgetSlug": "test1",
  "calendarType": "round_robin",
  "widgetType": "classic",
  "eventTitle": "{{contact.name}}",
  "eventColor": "#039be5",
  "locationConfigurations": [
    {
      "kind": "custom",
      "location": "string"
    }
  ],
  "slotDuration": 30,
  "slotDurationUnit": "mins",
  "slotInterval": 30,
  "slotIntervalUnit": "mins",
  "slotBuffer": 0,
  "slotBufferUnit": "mins",
  "preBuffer": 0,
  "preBufferUnit": "mins",
  "appoinmentPerSlot": 1,
  "appoinmentPerDay": 0,
  "allowBookingAfter": 0,
  "allowBookingAfterUnit": "days",
  "allowBookingFor": 0,
  "allowBookingForUnit": "days",
  "enableRecurring": false,
  "recurring": {
    "freq": "DAILY",
    "count": 0,
    "bookingOption": "skip",
    "bookingOverlapDefaultStatus": "confirmed"
  },
  "formId": "string",
  "stickyContact": true,
  "isLivePaymentMode": true,
  "autoConfirm": true,
  "shouldSendAlertEmailsToAssignedMember": true,
  "alertEmail": "string",
  "googleInvitationEmails": false,
  "allowReschedule": true,
  "allowCancellation": true,
  "shouldAssignContactToTeamMember": true,
  "shouldSkipAssigningContactForExisting": true,
  "notes": "string",
  "pixelId": "string",
  "formSubmitType": "ThankYouMessage",
  "formSubmitRedirectURL": "string",
  "formSubmitThanksMessage": "string",
  "guestType": "count_only",
  "consentLabel": "string",
  "calendarCoverImage": "https://path-to-image.com",
  "lookBusyConfig": {
    "enabled": true,
    "LookBusyPercentage": 0
  }
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
Body
 REQUIRED
{
  "isActive": true,
  "locationId": "ocQHyuzHvysMo5N5VsXc",
  "groupId": "BqTwX8QFwXzpegMve9EQ",
  "teamMembers": [
    {
      "userId": "ocQHyuzHvysMo5N5VsXc",
      "priority": 0.5,
      "isPrimary": true,
      "locationConfigurations": [
        {
          "kind": "custom",
          "location": "string"
        }
      ]
    }
  ],
  "eventType": "RoundRobin_OptimizeForAvailability",
  "name": "test calendar",
  "description": "this is used for testing",
  "slug": "test1",
  "widgetSlug": "test1",
  "calendarType": "round_robin",
  "widgetType": "classic",
  "eventTitle": "{{contact.name}}",
  "eventColor": "#039be5",
  "locationConfigurations": [
    {
      "kind": "custom",
      "location": "string"
    }
  ],
  "slotDuration": 30,
  "slotDurationUnit": "mins",
  "slotInterval": 30,
  "slotIntervalUnit": "mins",
  "slotBuffer": 0,
  "slotBufferUnit": "mins",
  "preBuffer": 0,
  "preBufferUnit": "mins",
  "appoinmentPerSlot": 1,
  "appoinmentPerDay": 0,
  "allowBookingAfter": 0,
  "allowBookingAfterUnit": "days",
  "allowBookingFor": 0,
  "allowBookingForUnit": "days",
  "enableRecurring": false,
  "recurring": {
    "freq": "DAILY",
    "count": 0,
    "bookingOption": "skip",
    "bookingOverlapDefaultStatus": "confirmed"
  },
  "formId": "string",
  "stickyContact": true,
  "isLivePaymentMode": true,
  "autoConfirm": true,
  "shouldSendAlertEmailsToAssignedMember": true,
  "alertEmail": "string",
  "googleInvitationEmails": false,
  "allowReschedule": true,
  "allowCancellation": true,
  "shouldAssignContactToTeamMember": true,
  "shouldSkipAssigningContactForExisting": true,
  "notes": "string",
  "pixelId": "string",
  "formSubmitType": "ThankYouMessage",
  "formSubmitRedirectURL": "string",
  "formSubmitThanksMessage": "string",
  "guestType": "count_only",
  "consentLabel": "string",
  "calendarCoverImage": "https://path-to-image.com",
  "lookBusyConfig": {
    "enabled": true,
    "LookBusyPercentage": 0
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!