# Get Custom Value

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/get-custom-value

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_locations_get-custom-value_screenshot.png

---

Sub-Account (Formerly location)Custom ValueGet Custom Value
Get Custom Value
GET
 https://services.leadconnectorhq.com/locations/:locationId/customValues/:id
Get Custom Value
Requirements
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
Possible values: [2021-07-28]
API Version
PATH PARAMETERS
locationId
string
REQUIRED
Location Id
Example: ve9EPM428h8vShlRW1KT
id
string
REQUIRED
Custom Value Id
Example: kOBjMVAJhFuUeYIojVet
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
customValue
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
curl -L 'https://services.leadconnectorhq.com/locations/:locationId/customValues/:id' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — path
REQUIRED
id — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!