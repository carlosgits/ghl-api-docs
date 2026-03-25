# Delete a knowledge base

Source: https://marketplace.gohighlevel.com/docs/ghl/knowledge-base/delete-knowledge-base

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_knowledge-base_delete-knowledge-base_screenshot.png

---

Knowledge BaseKnowledge BaseDelete a knowledge base
Delete a knowledge base
DELETE
 https://services.leadconnectorhq.com/knowledge-bases/:knowledgeBaseId
Delete a knowledge base
Requirements
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
HEADER PARAMETERS
Authorization
string
REQUIRED
Access Token
Example: Bearer 9c48df2694a849b6089f9d0d3513efe
Version
string
REQUIRED
Possible values: [2021-04-15]
API Version
PATH PARAMETERS
knowledgeBaseId
string
REQUIRED
Responses
200
400
401
Knowledge base deleted successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED












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
curl -L -X DELETE 'https://services.leadconnectorhq.com/knowledge-bases/:knowledgeBaseId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
knowledgeBaseId — path
REQUIRED
Authorization — header
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!