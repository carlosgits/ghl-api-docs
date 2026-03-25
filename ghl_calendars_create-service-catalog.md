# Create Service

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/create-service-catalog

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_create-service-catalog_screenshot.png

---

CalendarsServicesCreate Service
Create Service
POST
 https://services.leadconnectorhq.com/calendars/services/catalog
Create new service in a location.
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
locationId
string
REQUIRED
Location ID
Example:0007BWpSzSwfiuSl0tR2
name
string
REQUIRED
Service name
Example:Hair Styling
slug
string
REQUIRED
Unique URL-friendly identifier
Example:hair-styling
staff
object[]
REQUIRED
description
string
Service description
Example:Full hair styling session
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
Service category ID (uses default category if not provided)
Example:65e5f6dfacf123513228d381
payment
object
serviceDuration
number
This controls the duration of the appointment
Example:30
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
variations
object[]
Responses
201
400
401
Service created successfully
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
curl -L 'https://services.leadconnectorhq.com/calendars/services/catalog' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "0007BWpSzSwfiuSl0tR2",
  "name": "Hair Styling",
  "slug": "hair-styling",
  "staff": [
    {
      "id": "65e5f6dfacf123513228d384"
    }
  ],
  "description": "Full hair styling session",
  "eventColor": "#66C61C",
  "coverImage": "https://example.com/cover.jpg",
  "serviceCategoryId": "65e5f6dfacf123513228d381",
  "payment": {
    "amount": 50,
    "deposit": 20,
    "depositType": "amount"
  },
  "serviceDuration": 30,
  "serviceDurationUnit": "mins",
  "preBuffer": 10,
  "preBufferUnit": "mins",
  "postBuffer": 15,
  "postBufferUnit": "mins",
  "isPrivate": false,
  "formId": "65e5f6dfacf123513228d390",
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
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "locationId": "0007BWpSzSwfiuSl0tR2",
  "name": "Hair Styling",
  "slug": "hair-styling",
  "staff": [
    {
      "id": "65e5f6dfacf123513228d384"
    }
  ],
  "description": "Full hair styling session",
  "eventColor": "#66C61C",
  "coverImage": "https://example.com/cover.jpg",
  "serviceCategoryId": "65e5f6dfacf123513228d381",
  "payment": {
    "amount": 50,
    "deposit": 20,
    "depositType": "amount"
  },
  "serviceDuration": 30,
  "serviceDurationUnit": "mins",
  "preBuffer": 10,
  "preBufferUnit": "mins",
  "postBuffer": 15,
  "postBufferUnit": "mins",
  "isPrivate": false,
  "formId": "65e5f6dfacf123513228d390",
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
      "name": "Standard Haircut"
    }
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!