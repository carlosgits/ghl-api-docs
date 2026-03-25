# Get Custom Fields By Object Key

Source: https://marketplace.gohighlevel.com/docs/ghl/custom-fields/get-custom-fields-by-object-key

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_custom-fields_get-custom-fields-by-object-key_screenshot.png

---

Custom Fields V2Custom Fields V2Get Custom Fields By Object Key
Get Custom Fields By Object Key
GET
 https://services.leadconnectorhq.com/custom-fields/object-key/:objectKey
Get Custom Fields By Object Key
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
objectKey
string
REQUIRED
key of the Object. Must include "custom_objects." prefix for custom objects. Available on the Custom Objects details Page under settings
Example: custom_objects.pet
QUERY PARAMETERS
locationId
string
REQUIRED
Example: Location Id
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
fields
object[]
folders
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
curl -L 'https://services.leadconnectorhq.com/custom-fields/object-key/:objectKey' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
objectKey — path
REQUIRED
locationId — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!