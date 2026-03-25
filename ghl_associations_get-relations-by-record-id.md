# Get all relations By record Id

Source: https://marketplace.gohighlevel.com/docs/ghl/associations/get-relations-by-record-id

Screenshot: images/ghl_associations_get-relations-by-record-id_screenshot.png

---

AssociationsRelationsGet all relations By record Id
Get all relations By record Id
GET
 https://services.leadconnectorhq.com/associations/relations/:recordId
Get all relations by record Id
Requirements
Scope(s)
associations/relation.readonly
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
recordId
string
REQUIRED
QUERY PARAMETERS
locationId
string
REQUIRED
Your Sub Account's ID
Example: clF1LD04GTUKN3b3XuOj
skip
number
REQUIRED
Example: 10
limit
number
REQUIRED
Example: 100
associationIds
string[]
Association Ids
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
curl -L 'https://services.leadconnectorhq.com/associations/relations/:recordId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
recordId — path
REQUIRED
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
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!