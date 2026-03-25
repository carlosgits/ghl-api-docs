# List Actions for an Agent

Source: https://marketplace.gohighlevel.com/docs/ghl/conversation-ai/list-actions

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_conversation-ai_list-actions_screenshot.png

---

Conversation AIActionsList Actions for an Agent
List Actions for an Agent
GET
 https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/list
List for actions for an agent
Requirements
Scope(s)
conversation-ai.readonly
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
Possible values: [2021-04-15]
API Version
PATH PARAMETERS
agentId
string
REQUIRED
Responses
200
400
401
422
Success
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
data
object[]
REQUIRED
success
boolean
REQUIRED
Success status of the request
Example:true



































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
curl -L 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/list' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
agentId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!