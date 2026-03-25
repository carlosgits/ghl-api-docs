# Create Calendar Resource

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/create-calendar-resource

Screenshot: images/ghl_calendars_create-calendar-resource_screenshot.png

---

CalendarsCalendar Resources: Rooms & EquipmentsCreate Calendar Resource
Create Calendar Resource
POST
 https://services.leadconnectorhq.com/calendars/resources/:resourceType
DEPRECATED
This endpoint has been deprecated and may be replaced or removed in future versions of the API.
Create calendar resource by resource type (Services V1)
Requirements
Scope(s)
calendars/resources.write
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
resourceType
string
REQUIRED
Possible values: [equipments, rooms]
Calendar Resource Type
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
name
string
REQUIRED
description
string
REQUIRED
quantity
number
REQUIRED
Quantity of the equipment.
outOfService
number
REQUIRED
Quantity of the out of service equipment.
capacity
number
REQUIRED
Capacity of the room.
calendarIds
string[]
REQUIRED
Service calendar IDs to be mapped with the resource.
One equipment can only be mapped with one service calendar.
One room can be mapped with multiple service calendars.
Possible values: <= 100
Responses
201
400
401
Calendar resource created
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
locationId
string
REQUIRED
Location ID of the resource
name
string
REQUIRED
Name of the resource
Example:yoga room
resourceType
string
REQUIRED
Possible values: [equipments, rooms]
isActive
boolean
REQUIRED
Whether the resource is active
description
string
Description of the resource
quantity
number
Quantity of the resource
outOfService
number
Indicates if the resource is out of service
Example:0
capacity
number
Capacity of the resource
Example:85
calendarIds
string[]
REQUIRED
Calendar IDs
Example:["Jsj0xnlDDjw0SuvX1J13","oCM5feFC86FAAbcO7lJK"]























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
curl -L 'https://services.leadconnectorhq.com/calendars/resources/:resourceType' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "string",
  "name": "string",
  "description": "string",
  "quantity": 0,
  "outOfService": 0,
  "capacity": 0,
  "calendarIds": [
    "string"
  ]
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
resourceType — path
REQUIRED
---
equipments
rooms
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "locationId": "string",
  "name": "string",
  "description": "string",
  "quantity": 0,
  "outOfService": 0,
  "capacity": 0,
  "calendarIds": [
    "string"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!