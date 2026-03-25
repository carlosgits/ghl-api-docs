# Get association key by key name

Source: https://marketplace.gohighlevel.com/docs/ghl/associations/get-association-key-by-key-name

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_associations_get-association-key-by-key-name_screenshot.png

---

AssociationsAssociationsGet association key by key name
Get association key by key name
GET
 https://services.leadconnectorhq.com/associations/key/:key_name
Using this api you can get standard / user defined association by key
Requirements
Scope(s)
associations.readonly
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
key_name
string
REQUIRED
QUERY PARAMETERS
locationId
string
REQUIRED
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
locationId
string
REQUIRED
Example:string
id
string
REQUIRED
Example:ve9EPM428h8vShlRW1KT
key
string
REQUIRED
First Objects Association Label (custom_objects.children)
Example:student
firstObjectLabel
object
REQUIRED
First Objects Association Label (custom_objects.children)
Example:student
firstObjectKey
object
REQUIRED
First Objects Key
Example:custom_objects.children
secondObjectLabel
object
REQUIRED
Second Object Association Label (contact)
Example:Teacher
secondObjectKey
object
REQUIRED
Second Objects Key
Example:contact
associationType
object
REQUIRED
Association Type can be USER_DEFINED or SYSTEM_DEFINED
Example:USER_DEFINED


























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
curl -L 'https://services.leadconnectorhq.com/associations/key/:key_name' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
key_name — path
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