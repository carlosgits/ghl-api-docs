# Update Custom Value

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/update-custom-value

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_locations_update-custom-value_screenshot.png

---

Sub-Account (Formerly location)Custom ValueUpdate Custom Value
Update Custom Value
PUT
 https://services.leadconnectorhq.com/locations/:locationId/customValues/:id
Update Custom Value
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
APPLICATION/JSON
BODY
REQUIRED
name
string
REQUIRED
Example:Custom Field Name
value
string
REQUIRED
Example:Value
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
curl -L -X PUT 'https://services.leadconnectorhq.com/locations/:locationId/customValues/:id' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "name": "Custom Field Name",
  "value": "Value"
}'
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
Body
 REQUIRED
{
  "name": "Custom Field Name",
  "value": "Value"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!