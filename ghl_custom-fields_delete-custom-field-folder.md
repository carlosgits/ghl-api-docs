# Delete Custom Field Folder

Source: https://marketplace.gohighlevel.com/docs/ghl/custom-fields/delete-custom-field-folder

Screenshot: images/ghl_custom-fields_delete-custom-field-folder_screenshot.png

---

Custom Fields V2Custom Fields V2Delete Custom Field Folder
Delete Custom Field Folder
DELETE
 https://services.leadconnectorhq.com/custom-fields/folder/:id
Create Custom Field Folder
INFO
Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
Requirements
Scope(s)
locations/customFields.write
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
id
string
REQUIRED
QUERY PARAMETERS
locationId
string
REQUIRED
Location Id
Example: ve9EPM428h8vShlRW1KT
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
succeded
boolean
REQUIRED
Example:true
id
string
REQUIRED
Example:3v34PM428h8vShlRW1KT
key
string
REQUIRED
Example:custom_object.pet.name














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
curl -L -X DELETE 'https://services.leadconnectorhq.com/custom-fields/folder/:id' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
id — path
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