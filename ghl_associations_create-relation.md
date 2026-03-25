# Create Relation for you associated entities.

Source: https://marketplace.gohighlevel.com/docs/ghl/associations/create-relation

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_associations_create-relation_screenshot.png

---

AssociationsRelationsCreate Relation for you associated entities.
Create Relation for you associated entities.
POST
 https://services.leadconnectorhq.com/associations/relations
Create Relation.Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3
Requirements
Scope(s)
associations/relation.write
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
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
Your Sub Account's ID
Example:clF1LD04GTUKN3b3XuOj
associationId
string
REQUIRED
Association's Id
Example:ve9EPM428h8vShlRW1KT
firstRecordId
string
REQUIRED
First Record's Id. For instance, if you have an association between a contact and a custom object, and you specify the contact as the first object while creating the association, then your firstRecordId would be the contactId
Example:ve9EPM428h8vShlRW1KT
secondRecordId
string
REQUIRED
Second Record's Id.For instance, if you have an association between a contact and a custom object, and you specify the custom object as the second entity while creating the association, then your secondRecordId would be the customObject record Id
Example:ve9EPM428h8vShlRW1KT
Responses
201
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
curl -L 'https://services.leadconnectorhq.com/associations/relations' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "clF1LD04GTUKN3b3XuOj",
  "associationId": "ve9EPM428h8vShlRW1KT",
  "firstRecordId": "ve9EPM428h8vShlRW1KT",
  "secondRecordId": "ve9EPM428h8vShlRW1KT"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "locationId": "clF1LD04GTUKN3b3XuOj",
  "associationId": "ve9EPM428h8vShlRW1KT",
  "firstRecordId": "ve9EPM428h8vShlRW1KT",
  "secondRecordId": "ve9EPM428h8vShlRW1KT"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!