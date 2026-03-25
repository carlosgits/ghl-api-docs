# Get Custom Fields

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/get-custom-fields

Screenshot: images/ghl_locations_get-custom-fields_screenshot.png

---

Sub-Account (Formerly location)Custom FieldGet Custom Fields
Get Custom Fields
GET
 https://services.leadconnectorhq.com/locations/:locationId/customFields
Get Custom Fields
Requirements
Scope(s)
locations/customFields.readonly
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
QUERY PARAMETERS
model
string
Possible values: [contact, opportunity, all]
Model of the custom field you want to retrieve
Example: opportunity
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
customFields
object[]





































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
curl -L 'https://services.leadconnectorhq.com/locations/:locationId/customFields' \
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
Version — header
REQUIRED
---
2021-07-28
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!