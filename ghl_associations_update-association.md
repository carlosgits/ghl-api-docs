# Update Association By Id

Source: https://marketplace.gohighlevel.com/docs/ghl/associations/update-association

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_associations_update-association_screenshot.png

---

AssociationsAssociationsUpdate Association By Id
Update Association By Id
PUT
 https://services.leadconnectorhq.com/associations/:associationId
Update Association , Allows you to update labels of an associations. Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3
Requirements
Scope(s)
associations.write
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
associationId
string
REQUIRED
APPLICATION/JSON
BODY
REQUIRED
firstObjectLabel
object
REQUIRED
Example:student
secondObjectLabel
object
REQUIRED
Example:tutor
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
curl -L -X PUT 'https://services.leadconnectorhq.com/associations/:associationId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "firstObjectLabel": "student",
  "secondObjectLabel": "tutor"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
associationId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "firstObjectLabel": "student",
  "secondObjectLabel": "tutor"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!