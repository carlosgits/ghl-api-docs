# Get Record By Id

Source: https://marketplace.gohighlevel.com/docs/ghl/objects/get-record-by-id

Screenshot: images/ghl_objects_get-record-by-id_screenshot.png

---

ObjectsRecordsGet Record By Id
Get Record By Id
GET
 https://services.leadconnectorhq.com/objects/:schemaKey/records/:id
Allows you to get a Standard Object like business and custom object record by Id
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
curl -L 'https://services.leadconnectorhq.com/objects/:schemaKey/records/:id' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!