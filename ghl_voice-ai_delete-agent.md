# Delete Agent

Source: https://marketplace.gohighlevel.com/docs/ghl/voice-ai/delete-agent

Screenshot: images/ghl_voice-ai_delete-agent_screenshot.png

---

Voice AIAgentsDelete Agent
Delete Agent
DELETE
 https://services.leadconnectorhq.com/voice-ai/agents/:agentId
Delete a voice AI agent and all its configurations
Requirements
Scope(s)
voice-ai-agents.write
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
Unique agent identifier
Example: 507f1f77bcf86cd799439011
QUERY PARAMETERS
locationId
string
REQUIRED
Location ID
Example: LOC123456789ABCDEF
Responses
204
400
401
422
Agent deleted successfully
















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
curl -L -X DELETE 'https://services.leadconnectorhq.com/voice-ai/agents/:agentId' \
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
locationId — query
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!