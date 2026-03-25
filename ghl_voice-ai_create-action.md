# Create Agent Action

Source: https://marketplace.gohighlevel.com/docs/ghl/voice-ai/create-action

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_voice-ai_create-action_screenshot.png

---

Voice AIActionsCreate Agent Action
Create Agent Action
POST
 https://services.leadconnectorhq.com/voice-ai/actions
Create a new action for a voice AI agent. Actions define specific behaviors and capabilities for the agent during calls.
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
APPLICATION/JSON
BODY
REQUIRED
agentId
string
REQUIRED
Agent ID to attach the action to
Example:507f1f77bcf86cd799439011
locationId
string
REQUIRED
Location ID
Example:507f1f77bcf86cd799439012
actionType
string
REQUIRED
Type of action
Possible values: [CALL_TRANSFER, DATA_EXTRACTION, IN_CALL_DATA_EXTRACTION, WORKFLOW_TRIGGER, SMS, APPOINTMENT_BOOKING, CUSTOM_ACTION, KNOWLEDGE_BASE]
Example:CALL_TRANSFER
name
string
REQUIRED
Human-readable name for this action
Example:Transfer to Manager
actionParameters
object
REQUIRED
Responses
201
400
401
422
Action created successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
id
string
REQUIRED
Unique identifier for the created action
Example:507f1f77bcf86cd799439011
actionType
string
REQUIRED
Type of action
Possible values: [CALL_TRANSFER, DATA_EXTRACTION, IN_CALL_DATA_EXTRACTION, WORKFLOW_TRIGGER, SMS, APPOINTMENT_BOOKING, CUSTOM_ACTION, KNOWLEDGE_BASE]
Example:CALL_TRANSFER
name
string
REQUIRED
Human-readable name for this action
Example:Transfer to Manager
actionParameters
object
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
curl -L 'https://services.leadconnectorhq.com/voice-ai/actions' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "agentId": "507f1f77bcf86cd799439011",
  "locationId": "507f1f77bcf86cd799439012",
  "actionType": "CALL_TRANSFER",
  "name": "Transfer to Manager",
  "actionParameters": {
    "triggerPrompt": "When the caller asks to speak to a manager",
    "transferToType": "number",
    "transferToValue": "+12345678901",
    "triggerMessage": "Let me transfer you to a manager right away",
    "hearWhisperMessage": true
  }
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "agentId": "507f1f77bcf86cd799439011",
  "locationId": "507f1f77bcf86cd799439012",
  "actionType": "CALL_TRANSFER",
  "name": "Transfer to Manager",
  "actionParameters": {
    "triggerPrompt": "When the caller asks to speak to a manager",
    "transferToType": "number",
    "transferToValue": "+12345678901",
    "triggerMessage": "Let me transfer you to a manager right away",
    "hearWhisperMessage": true
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!