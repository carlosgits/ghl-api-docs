# Delete a template

Source: https://marketplace.gohighlevel.com/docs/ghl/emails/delete-template

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_emails_delete-template_screenshot.png

---

EmailTemplatesDelete a template
Delete a template
DELETE
 https://services.leadconnectorhq.com/emails/builder/:locationId/:templateId
Delete a template
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
PATH PARAMETERS
locationId
string
REQUIRED
Example: ve9EPM428h8vShlRW1KT
templateId
string
REQUIRED
Example: zYy3YOUuHxgomU1uYJty
Responses
200
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/emails/builder/:locationId/:templateId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — path
REQUIRED
templateId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!