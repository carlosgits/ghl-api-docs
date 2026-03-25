# Remove Action from Agent

Source: https://marketplace.gohighlevel.com/docs/ghl/conversation-ai/delete-action

Screenshot: images/ghl_conversation-ai_delete-action_screenshot.png

---

Conversation AIActionsRemove Action from Agent
Remove Action from Agent
DELETE
 https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId
Permanently deletes an action. This will remove the action from all associated agents and cannot be undone.
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
Successful response
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId' \
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