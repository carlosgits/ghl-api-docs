# Get Sub-Account (Formerly Location)

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/get-location

Screenshot: images/ghl_locations_get-location_screenshot.png

---

Sub-Account (Formerly location)Sub-Account (Formerly Location)Get Sub-Account (Formerly Location)
Get Sub-Account (Formerly Location)
GET
 https://services.leadconnectorhq.com/locations/:locationId
Get details of a Sub-Account (Formerly Location) by passing the sub-account id
Requirements
Scope(s)
locations.readonly
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Agency Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
PATH PARAMETERS
locationId
string
REQUIRED
Location Id
Example: ve9EPM428h8vShlRW1KT
Responses
200
400
401
422
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
location
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
curl -L 'https://services.leadconnectorhq.com/locations/:locationId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Security Scheme
Location-Access
Agency-Access
Bearer Token
Parameters
locationId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!