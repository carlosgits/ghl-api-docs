# Get Services

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/get-services-catalog

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_calendars_get-services-catalog_screenshot.png

---

CalendarsServicesGet Services
Get Services
GET
 https://services.leadconnectorhq.com/calendars/services/catalog
Get all services in a location.
Requirements
Scope(s)
calendars.readonly
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
QUERY PARAMETERS
locationId
string
REQUIRED
Location ID
Example: 0007BWpSzSwfiuSl0tR2
serviceCategoryId
string
Filter by service category ID
Example: 65e5f6dfacf123513228d384
isPrivate
boolean
Filter services: true = private only, false = public only, unset = all services
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
services
object[]
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
curl -L 'https://services.leadconnectorhq.com/calendars/services/catalog' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — query
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