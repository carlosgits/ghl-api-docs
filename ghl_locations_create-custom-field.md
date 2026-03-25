# Create Custom Field

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/create-custom-field

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_locations_create-custom-field_screenshot.png

---

Sub-Account (Formerly location)Custom FieldCreate Custom Field
Create Custom Field
POST
 https://services.leadconnectorhq.com/locations/:locationId/customFields
Create Custom Field
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
locationId
string
REQUIRED
Location Id
Example: ve9EPM428h8vShlRW1KT
APPLICATION/JSON
BODY
REQUIRED
name
string
REQUIRED
Example:Custom Field
dataType
string
REQUIRED
Example:TEXT
placeholder
string
Example:Placeholder Text
acceptedFormat
string[]
Example:[".pdf",".docx",".jpeg"]
isMultipleFile
boolean
Example:false
maxNumberOfFiles
number
Example:2
textBoxListOptions
object[]
position
number
Default value: 0
Example:0
model
string
Model of the custom field you want to create
Possible values: [contact, opportunity]
Example:opportunity
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
customField
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
curl -L 'https://services.leadconnectorhq.com/locations/:locationId/customFields' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "name": "Custom Field",
  "dataType": "TEXT",
  "placeholder": "Placeholder Text",
  "acceptedFormat": [
    ".pdf",
    ".docx",
    ".jpeg"
  ],
  "isMultipleFile": false,
  "maxNumberOfFiles": 2,
  "textBoxListOptions": [
    {
      "label": "First",
      "prefillValue": ""
    },
    {
      "label": "First",
      "prefillValue": ""
    }
  ],
  "position": 0,
  "model": "opportunity"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "name": "Custom Field",
  "dataType": "TEXT",
  "placeholder": "Placeholder Text",
  "acceptedFormat": [
    ".pdf",
    ".docx",
    ".jpeg"
  ],
  "isMultipleFile": false,
  "maxNumberOfFiles": 2,
  "textBoxListOptions": [
    {
      "label": "First",
      "prefillValue": ""
    },
    {
      "label": "First",
      "prefillValue": ""
    }
  ],
  "position": 0,
  "model": "opportunity"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!