# Delete Agent Action

Source: https://marketplace.gohighlevel.com/docs/ghl/voice-ai/delete-action

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_voice-ai_delete-action_screenshot.png

---

Voice AIActionsDelete Agent Action
Delete Agent Action
DELETE
 https://services.leadconnectorhq.com/voice-ai/actions/:actionId
Delete an existing action from a voice AI agent. This permanently removes the action and its configuration.
Requirements
Scope(s)
voice-ai-agent-goals.write
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
Unique identifier for the action
QUERY PARAMETERS
locationId
string
REQUIRED
Location ID
Example: LOC123456789ABCDEF
agentId
string
REQUIRED
Agent ID the action is attached to
Responses
204
400
401
422
Action deleted successfully
















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
curl -L -X DELETE 'https://services.leadconnectorhq.com/voice-ai/actions/:actionId' \
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
locationId — query
REQUIRED
agentId — query
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!