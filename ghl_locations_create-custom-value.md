# Create Custom Value

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/create-custom-value

Screenshot: images/ghl_locations_create-custom-value_screenshot.png

---

Sub-Account (Formerly location)Custom ValueCreate Custom Value
Create Custom Value
POST
 https://services.leadconnectorhq.com/locations/:locationId/customValues
Create Custom Value
Requirements
Scope(s)
locations/customValues.write
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
201
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
curl -L 'https://services.leadconnectorhq.com/locations/:locationId/customValues' \
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