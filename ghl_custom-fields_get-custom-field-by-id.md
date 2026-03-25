# Get Custom Field / Folder By Id

Source: https://marketplace.gohighlevel.com/docs/ghl/custom-fields/get-custom-field-by-id

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_custom-fields_get-custom-field-by-id_screenshot.png

---

Custom Fields V2Custom Fields V2Get Custom Field / Folder By Id
Get Custom Field / Folder By Id
GET
 https://services.leadconnectorhq.com/custom-fields/:id
Get Custom Field / Folder By Id.
INFO
Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
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
id
string
REQUIRED
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
field
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
curl -L 'https://services.leadconnectorhq.com/custom-fields/:id' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
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