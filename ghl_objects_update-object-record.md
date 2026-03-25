# Update Record

Source: https://marketplace.gohighlevel.com/docs/ghl/objects/update-object-record

Screenshot: images/ghl_objects_update-object-record_screenshot.png

---

ObjectsRecordsUpdate Record
Update Record
PUT
 https://services.leadconnectorhq.com/objects/:schemaKey/records/:id
Update a Custom Object Record by Id. Supported Objects are business and custom objects. Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-277156/93bf0c2e23177b0/87cpx-376296
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
schemaKey
string
REQUIRED
The key of the Custom Object / Standard Object Schema. For custom objects, the key must include the “custom_objects.” prefix, while standard objects use their respective object keys. This information is available on the Custom Objects Details page under Settings.
Example: custom_objects.pet or business.email (for company's email)
id
string
REQUIRED
id of the record to be updated. Available on the Record details page under the 3 dots or in the url
Example: 632c34b4c9b7da3358ac9891
QUERY PARAMETERS
locationId
string
REQUIRED
APPLICATION/JSON
BODY
REQUIRED
object
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
record
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
curl -L -X PUT 'https://services.leadconnectorhq.com/objects/:schemaKey/records/:id' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
schemaKey — path
REQUIRED
id — path
REQUIRED
locationId — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!