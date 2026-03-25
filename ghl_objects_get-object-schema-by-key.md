# Get Object Schema by key / id

Source: https://marketplace.gohighlevel.com/docs/ghl/objects/get-object-schema-by-key

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_objects_get-object-schema-by-key_screenshot.png

---

ObjectsObject SchemaGet Object Schema by key / id
Get Object Schema by key / id
GET
 https://services.leadconnectorhq.com/objects/:key
Retrieve Object Schema by key or ID. This will return the schema of the custom object, including all its fields and properties. Supported objects include contact, opportunity, business and custom objects.To understand objects and records, please have a look the documentation here : https://doc.clickup.com/8631005/d/h/87cpx-277156/93bf0c2e23177b0
Requirements
Scope(s)
objects/schema.readonly
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
key
string
REQUIRED
key of the custom or standard object. For custom objects, the key must include the prefix “custom_objects.”. This key can be found on the Object Details page under Settings in the UI.
Example: custom_objects.pet
QUERY PARAMETERS
locationId
string
REQUIRED
location id of the sub account
Example: 632c34b4c9b7da3358ac9891
fetchProperties
string
Fetch Properties , Fetches all the standard / custom fields of the object when set to true
Example:
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
object
object
cache
boolean
REQUIRED
Is the response served from cache
Example:true
fields
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
curl -L 'https://services.leadconnectorhq.com/objects/:key' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
key — path
REQUIRED
locationId — query
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