# Create a new template

Source: https://marketplace.gohighlevel.com/docs/ghl/emails/create-template

Screenshot: images/ghl_emails_create-template_screenshot.png

---

EmailTemplatesCreate a new template
Create a new template
POST
 https://services.leadconnectorhq.com/emails/builder
Create a new template
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
title
string
Example:template title
type
string
REQUIRED
Possible values: [html, folder, import, builder, blank, ai_template]
updatedBy
string
Example:zYy3YOUuHxgomU1uYJty
builderVersion
string
Possible values: [1, 2]
Default value: 2
name
string
Example:Template1
parentId
string
Example:zYy3YOUuHxgomU1uYJty
templateDataUrl
string
Example:
importProvider
string
REQUIRED
Possible values: [mailchimp, active_campaign, kajabi, other]
importURL
string
Example:https://tplshare.com/fhYJ3Mi
templateSource
string
Example:template_library
isPlainText
boolean
Example:false
subjectLine
string
Example:Email Subject
fromName
string
Example:Name of sender
fromEmail
string
Example:test@abc.com
previewText
string
Example:preview text
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
redirect
string
REQUIRED
template id
Example:66e811229245fc098765590
traceId
string
REQUIRED
trace id
Example:0c52e980-41f6-4be7-8c4b-e2c5a13dc3c2




















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
curl -L 'https://services.leadconnectorhq.com/emails/builder' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "title": "template title",
  "type": "html",
  "updatedBy": "zYy3YOUuHxgomU1uYJty",
  "builderVersion": "2",
  "name": "Template1",
  "parentId": "zYy3YOUuHxgomU1uYJty",
  "templateDataUrl": "",
  "importProvider": "mailchimp",
  "importURL": "https://tplshare.com/fhYJ3Mi",
  "templateSource": "template_library",
  "isPlainText": false,
  "subjectLine": "Email Subject",
  "fromName": "Name of sender",
  "fromEmail": "test@abc.com",
  "previewText": "preview text"
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
  "title": "template title",
  "type": "html",
  "updatedBy": "zYy3YOUuHxgomU1uYJty",
  "builderVersion": "2",
  "name": "Template1",
  "parentId": "zYy3YOUuHxgomU1uYJty",
  "templateDataUrl": "",
  "importProvider": "mailchimp",
  "importURL": "https://tplshare.com/fhYJ3Mi",
  "templateSource": "template_library",
  "isPlainText": false,
  "subjectLine": "Email Subject",
  "fromName": "Name of sender",
  "fromEmail": "test@abc.com",
  "previewText": "preview text"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!