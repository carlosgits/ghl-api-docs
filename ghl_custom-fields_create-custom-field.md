# Create Custom Field

Source: https://marketplace.gohighlevel.com/docs/ghl/custom-fields/create-custom-field

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_custom-fields_create-custom-field_screenshot.png

---

Custom Fields V2Custom Fields V2Create Custom Field
Create Custom Field
POST
 https://services.leadconnectorhq.com/custom-fields/
Create Custom Field
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
locationId
string
REQUIRED
Location Id
Example:ve9EPM428h8vShlRW1KT
name
string
Field name
Example:Name
description
string
Description of the field
placeholder
string
Placeholder text for the field
showInForms
boolean
REQUIRED
Whether the field should be shown in forms
options
object[]
acceptedFormats
string
Allowed file formats for uploads. Options include: .pdf, .docx, .doc, .jpg, .jpeg, .png, .gif, .csv, .xlsx, .xls, all
Possible values: [.pdf, .docx, .doc, .jpg, .jpeg, .png, .gif, .csv, .xlsx, .xls, all]
dataType
string
REQUIRED
Type of field that you are trying to create
Possible values: [TEXT, LARGE_TEXT, NUMERICAL, PHONE, MONETORY, CHECKBOX, SINGLE_OPTIONS, MULTIPLE_OPTIONS, DATE, TEXTBOX_LIST, FILE_UPLOAD, RADIO, EMAIL]
fieldKey
string
REQUIRED
Field key. For Custom Object it's formatted as "custom_object.{objectKey}.{fieldKey}". "custom_object" is a fixed prefix, "{objectKey}" is your custom object's identifier, and "{fieldKey}" is the unique field name within that object. Example: "custom_object.pet.name" for a "name" field in a "pet" custom object.
Example:custom_object.pet.name
objectKey
string
REQUIRED
The key for your custom object. This key uniquely identifies the custom object. Example: "custom_object.pet" for a custom object related to pets.
Example:custom_object.pet
maxFileLimit
number
Maximum file limit for uploads. Applicable only for fields with a data type of FILE_UPLOAD.
Example:2
allowCustomOption
boolean
Determines if users can add a custom option value different from the predefined options in records for RADIO type fields. A custom value added in one record does not automatically become an option and will not appear as an option for other records.
Example:true
parentId
string
REQUIRED
ID of the parent folder
Responses
201
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
field
object



































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
curl -L 'https://services.leadconnectorhq.com/custom-fields/' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "name": "Name",
  "description": "string",
  "placeholder": "string",
  "showInForms": true,
  "options": [
    {
      "key": "string",
      "label": "string",
      "url": "string"
    }
  ],
  "acceptedFormats": ".pdf",
  "dataType": "TEXT",
  "fieldKey": "custom_object.pet.name",
  "objectKey": "custom_object.pet",
  "maxFileLimit": 2,
  "allowCustomOption": true,
  "parentId": "string"
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
  "locationId": "ve9EPM428h8vShlRW1KT",
  "name": "Name",
  "description": "string",
  "placeholder": "string",
  "showInForms": true,
  "options": [
    {
      "key": "string",
      "label": "string",
      "url": "string"
    }
  ],
  "acceptedFormats": ".pdf",
  "dataType": "TEXT",
  "fieldKey": "custom_object.pet.name",
  "objectKey": "custom_object.pet",
  "maxFileLimit": 2,
  "allowCustomOption": true,
  "parentId": "string"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!