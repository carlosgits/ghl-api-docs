# List Calendar Resources

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/fetch-calendar-resources

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_fetch-calendar-resources_screenshot.png

---

CalendarsCalendar Resources: Rooms & EquipmentsList Calendar Resources
List Calendar Resources
GET
 https://services.leadconnectorhq.com/calendars/resources/:resourceType
DEPRECATED
This endpoint has been deprecated and may be replaced or removed in future versions of the API.
List calendar resources by resource type and location ID (Services V1)
Requirements
Scope(s)
calendars/resources.readonly
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
QUERY PARAMETERS
locationId
string
REQUIRED
limit
number
REQUIRED
skip
number
REQUIRED
Responses
200
400
401
Calendar resources listed
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
Array [
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
curl -L 'https://services.leadconnectorhq.com/calendars/resources/:resourceType' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
locationId — query
REQUIRED
limit — query
REQUIRED
skip — query
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!