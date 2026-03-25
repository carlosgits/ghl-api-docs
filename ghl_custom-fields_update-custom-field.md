# Update Custom Field By Id

Source: https://marketplace.gohighlevel.com/docs/ghl/custom-fields/update-custom-field

Screenshot: images/ghl_custom-fields_update-custom-field_screenshot.png

---

Custom Fields V2Custom Fields V2Update Custom Field By Id
Update Custom Field By Id
PUT
 https://services.leadconnectorhq.com/custom-fields/:id
Update Custom Field By Id
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
maxFileLimit
number
Maximum file limit for uploads. Applicable only for fields with a data type of FILE_UPLOAD.
Example:2
Responses
200
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
curl -L -X PUT 'https://services.leadconnectorhq.com/custom-fields/:id' \
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
  "maxFileLimit": 2
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
  "maxFileLimit": 2
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!