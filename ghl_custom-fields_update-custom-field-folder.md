# Update Custom Field Folder Name

Source: https://marketplace.gohighlevel.com/docs/ghl/custom-fields/update-custom-field-folder

Screenshot: images/ghl_custom-fields_update-custom-field-folder_screenshot.png

---

Custom Fields V2Custom Fields V2Update Custom Field Folder Name
Update Custom Field Folder Name
PUT
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
APPLICATION/JSON
BODY
REQUIRED
name
string
REQUIRED
Field name
Example:Name
locationId
string
REQUIRED
Location Id
Example:ve9EPM428h8vShlRW1KT
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
id
string
REQUIRED
Unique identifier of the object
objectKey
string
REQUIRED
The key for your custom object. This key uniquely identifies the custom object. Example: "custom_object.pet" for a custom object related to pets.
Example:custom_object.pet
locationId
string
REQUIRED
Location Id
Example:ve9EPM428h8vShlRW1KT
name
string
REQUIRED
Field name
Example:Name















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
curl -L -X PUT 'https://services.leadconnectorhq.com/custom-fields/folder/:id' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "name": "Name",
  "locationId": "ve9EPM428h8vShlRW1KT"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
id — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "name": "Name",
  "locationId": "ve9EPM428h8vShlRW1KT"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!