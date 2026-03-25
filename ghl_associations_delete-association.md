# Delete Association

Source: https://marketplace.gohighlevel.com/docs/ghl/associations/delete-association

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_associations_delete-association_screenshot.png

---

AssociationsAssociationsDelete Association
Delete Association
DELETE
 https://services.leadconnectorhq.com/associations/:associationId
Delete USER_DEFINED Association By Id, deleting an association will also all the relations for that association
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
deleted
boolean
REQUIRED
Deletion status
Example:true
id
string
REQUIRED
Association Id
Example:6d6f6e676f5f6576656e7473
message
string
REQUIRED
Example:Association deleted successfully





















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
curl -L -X DELETE 'https://services.leadconnectorhq.com/associations/:associationId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!