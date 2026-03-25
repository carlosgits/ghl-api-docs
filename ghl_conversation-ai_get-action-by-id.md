# Get Action by ID

Source: https://marketplace.gohighlevel.com/docs/ghl/conversation-ai/get-action-by-id

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_conversation-ai_get-action-by-id_screenshot.png

---

Conversation AIActionsGet Action by ID
Get Action by ID
GET
 https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId
Retrieves detailed information about a specific action using its unique identifier. Returns the action configuration, associated agents, and performance metrics.
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
actionId
string
REQUIRED
The unique identifier of the action ID Attached to the agent
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
object
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
curl -L 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
actionId — path
REQUIRED
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