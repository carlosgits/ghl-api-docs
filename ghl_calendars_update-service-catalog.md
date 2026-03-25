# Update Service

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/update-service-catalog

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_update-service-catalog_screenshot.png

---

CalendarsServicesUpdate Service
Update Service
PUT
 https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId
Update service by ID.
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
serviceId
string
REQUIRED
Service ID
Example: 65e5f6dfacf123513228d384
APPLICATION/JSON
BODY
REQUIRED
name
string
Service name
Example:Hair Styling
description
string
Service description
Example:Full hair styling session
slug
string
Unique URL-friendly identifier
Example:hair-styling
eventColor
string
Service event color (hex)
Example:#66C61C
coverImage
string
Service cover image URL
Example:https://example.com/cover.jpg
serviceCategoryId
string
Service category ID
Example:65e5f6dfacf123513228d381
payment
object
serviceDuration
number
This controls the duration of the appointment
Example:60
serviceDurationUnit
string
Duration unit
Possible values: [mins, hours]
Example:mins
preBuffer
number
Pre-Buffer is additional time that can be added before an appointment, allowing for extra time to get ready
Example:10
preBufferUnit
string
Pre-buffer unit
Possible values: [mins, hours]
Example:mins
postBuffer
number
Post-buffer: Additional time that can be added after an appointment, allowing for extra time to wrap up
Example:15
postBufferUnit
string
Post-buffer unit
Possible values: [mins, hours]
Example:mins
isPrivate
boolean
Whether service is private (not shown publicly)
Example:false
formId
string
Custom form ID (will be used to display the custom form on the booking page, if only one service is selected)
Example:65e5f6dfacf123513228d390
staff
object[]
variations
object[]
Responses
200
400
401
Service updated successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
service
object
























































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
curl -L -X PUT 'https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "name": "Hair Styling",
  "description": "Full hair styling session",
  "slug": "hair-styling",
  "eventColor": "#66C61C",
  "coverImage": "https://example.com/cover.jpg",
  "serviceCategoryId": "65e5f6dfacf123513228d381",
  "payment": {
    "amount": 50,
    "deposit": 20,
    "depositType": "amount"
  },
  "serviceDuration": 60,
  "serviceDurationUnit": "mins",
  "preBuffer": 10,
  "preBufferUnit": "mins",
  "postBuffer": 15,
  "postBufferUnit": "mins",
  "isPrivate": false,
  "formId": "65e5f6dfacf123513228d390",
  "staff": [
    {
      "id": "65e5f6dfacf123513228d384"
    }
  ],
  "variations": [
    {
      "serviceDuration": 30,
      "serviceDurationUnit": "mins",
      "preBuffer": 10,
      "preBufferUnit": "mins",
      "postBuffer": 15,
      "postBufferUnit": "mins",
      "payment": {
        "amount": 50,
        "deposit": 20,
        "depositType": "amount"
      },
      "id": "65e5f6dfacf123513228d385",
      "name": "Standard Haircut"
    }
  ]
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
serviceId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "name": "Hair Styling",
  "description": "Full hair styling session",
  "slug": "hair-styling",
  "eventColor": "#66C61C",
  "coverImage": "https://example.com/cover.jpg",
  "serviceCategoryId": "65e5f6dfacf123513228d381",
  "payment": {
    "amount": 50,
    "deposit": 20,
    "depositType": "amount"
  },
  "serviceDuration": 60,
  "serviceDurationUnit": "mins",
  "preBuffer": 10,
  "preBufferUnit": "mins",
  "postBuffer": 15,
  "postBufferUnit": "mins",
  "isPrivate": false,
  "formId": "65e5f6dfacf123513228d390",
  "staff": [
    {
      "id": "65e5f6dfacf123513228d384"
    }
  ],
  "variations": [
    {
      "serviceDuration": 30,
      "serviceDurationUnit": "mins",
      "preBuffer": 10,
      "preBufferUnit": "mins",
      "postBuffer": 15,
      "postBufferUnit": "mins",
      "payment": {
        "amount": 50,
        "deposit": 20,
        "depositType": "amount"
      },
      "id": "65e5f6dfacf123513228d385",
      "name": "Standard Haircut"
    }
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!