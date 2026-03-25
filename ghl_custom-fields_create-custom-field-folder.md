# Create Custom Field Folder

Source: https://marketplace.gohighlevel.com/docs/ghl/custom-fields/create-custom-field-folder

Screenshot: images/ghl_custom-fields_create-custom-field-folder_screenshot.png

---

Custom Fields V2Custom Fields V2Create Custom Field Folder
Create Custom Field Folder
POST
 https://services.leadconnectorhq.com/custom-fields/folder
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
APPLICATION/JSON
BODY
REQUIRED
objectKey
string
REQUIRED
The key for your custom object. This key uniquely identifies the custom object. Example: "custom_object.pet" for a custom object related to pets.
Example:custom_object.pet
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
201
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
curl -L 'https://services.leadconnectorhq.com/custom-fields/folder' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "objectKey": "custom_object.pet",
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
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "objectKey": "custom_object.pet",
  "name": "Name",
  "locationId": "ve9EPM428h8vShlRW1KT"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!