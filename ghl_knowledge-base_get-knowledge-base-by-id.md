# Get knowledge base by ID

Source: https://marketplace.gohighlevel.com/docs/ghl/knowledge-base/get-knowledge-base-by-id

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_knowledge-base_get-knowledge-base-by-id_screenshot.png

---

Knowledge BaseKnowledge BaseGet knowledge base by ID
Get knowledge base by ID
GET
 https://services.leadconnectorhq.com/knowledge-bases/:knowledgeBaseId
Get knowledge base by ID
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
Knowledge base by ID retrieved successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Success status of the operation
Example:true
data
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
curl -L 'https://services.leadconnectorhq.com/knowledge-bases/:knowledgeBaseId' \
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