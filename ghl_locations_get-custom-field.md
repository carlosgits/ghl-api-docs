# Get Custom Field

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/get-custom-field

Screenshot: images/ghl_locations_get-custom-field_screenshot.png

---

Sub-Account (Formerly location)Custom FieldGet Custom Field
Get Custom Field
GET
 https://services.leadconnectorhq.com/locations/:locationId/customFields/:id
Get Custom Field
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
Custom Field Id or Field Key (e.g. "contact.first_name" or "opportunity.pipeline_id")
Examples:
id
field_key
Custom Field ID
Example:00NhGCcN1tlO8ZHcu7Wb
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
customField
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
curl -L 'https://services.leadconnectorhq.com/locations/:locationId/customFields/:id' \
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