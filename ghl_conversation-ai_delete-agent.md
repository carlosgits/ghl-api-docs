# Delete Agent

Source: https://marketplace.gohighlevel.com/docs/ghl/conversation-ai/delete-agent

Screenshot: images/ghl_conversation-ai_delete-agent_screenshot.png

---

Conversation AIAgentsDelete Agent
Delete Agent
DELETE
 https://services.leadconnectorhq.com/conversation-ai/agents/:agentId
Deletes an AI agent permanently. This action cannot be undone. All associated configurations and conversation history will be removed.
Requirements
Scope(s)
conversation-ai.write
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
Conversations AI agent id
Example: EmployeeId123
Responses
200
400
401
422
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Indicates if the agent was deleted successfully.
Example:true
id
string
REQUIRED
Unique identifier of the deleted agent.
Example:emp_123




















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
curl -L -X DELETE 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId' \
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