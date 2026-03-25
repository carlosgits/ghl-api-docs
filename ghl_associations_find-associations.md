# Get all associations for a sub-account / location

Source: https://marketplace.gohighlevel.com/docs/ghl/associations/find-associations

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_associations_find-associations_screenshot.png

---

AssociationsAssociationsGet all associations for a sub-account / location
Get all associations for a sub-account / location
GET
 https://services.leadconnectorhq.com/associations/
Get all Associations
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
QUERY PARAMETERS
locationId
string
REQUIRED
Example: string
skip
number
REQUIRED
Example: 10
limit
number
REQUIRED
Example: 100
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
curl -L 'https://services.leadconnectorhq.com/associations/' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — query
REQUIRED
skip — query
REQUIRED
limit — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!