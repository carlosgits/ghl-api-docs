# Update a knowledge base

Source: https://marketplace.gohighlevel.com/docs/ghl/knowledge-base/update-knowledge-base

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_knowledge-base_update-knowledge-base_screenshot.png

---

Knowledge BaseKnowledge BaseUpdate a knowledge base
Update a knowledge base
PUT
 https://services.leadconnectorhq.com/knowledge-bases/:id
Update a knowledge base
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
id
string
REQUIRED
APPLICATION/JSON
BODY
REQUIRED
name
string
field to update the name of the knowledge base
description
string
field to update the description of the knowledge base
Responses
200
400
401
Knowledge base updated successfully
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
curl -L -X PUT 'https://services.leadconnectorhq.com/knowledge-bases/:id' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "name": "string",
  "description": "string"
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
Authorization — header
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "name": "string",
  "description": "string"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!