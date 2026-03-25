# Update a template

Source: https://marketplace.gohighlevel.com/docs/ghl/emails/update-template

Screenshot: images/ghl_emails_update-template_screenshot.png

---

EmailTemplatesUpdate a template
Update a template
POST
 https://services.leadconnectorhq.com/emails/builder/data
Update a template
Requirements
Scope(s)
emails/builder.write
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
Example: 2021-07-28
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
Example:ve9EPM428h8vShlRW1KT
templateId
string
REQUIRED
Example:zYy3YOUuHxgomU1uYJty
updatedBy
string
REQUIRED
Example:zYy3YOUuHxgomU1uYJty
dnd
object
html
string
REQUIRED
Example:
editorType
string
REQUIRED
Possible values: [html, builder]
previewText
string
Example:zYy3YOUuHxgomU1uYJty
isPlainText
boolean
Example:false
usedEmailAI
boolean
Whether Email AI was used
Example:false
Responses
201
400
401
404
422
Success
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
ok
string
ok
Example:true
traceId
string
trace id
Example:0c52e980-41f6-4be7-8c4b-32332ss
previewUrl
string
preview url
Example:https://example.com
templateDownloadUrl
string
template data download url
Example:https://example.com
versionId
string
version id of the saved template
Example:507f1f77bcf86cd799439011























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
curl -L 'https://services.leadconnectorhq.com/emails/builder/data' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "templateId": "zYy3YOUuHxgomU1uYJty",
  "updatedBy": "zYy3YOUuHxgomU1uYJty",
  "dnd": "{elements:[], attrs:{}, templateSettings:{}}",
  "html": "",
  "editorType": "html",
  "previewText": "zYy3YOUuHxgomU1uYJty",
  "isPlainText": "false",
  "usedEmailAI": false
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
  "templateId": "zYy3YOUuHxgomU1uYJty",
  "updatedBy": "zYy3YOUuHxgomU1uYJty",
  "dnd": "{elements:[], attrs:{}, templateSettings:{}}",
  "html": "",
  "editorType": "html",
  "previewText": "zYy3YOUuHxgomU1uYJty",
  "isPlainText": "false",
  "usedEmailAI": false
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!