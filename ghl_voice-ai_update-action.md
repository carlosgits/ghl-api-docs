# Update Agent Action

Source: https://marketplace.gohighlevel.com/docs/ghl/voice-ai/update-action

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_voice-ai_update-action_screenshot.png

---

Voice AIActionsUpdate Agent Action
Update Agent Action
PUT
 https://services.leadconnectorhq.com/voice-ai/actions/:actionId
Update an existing action for a voice AI agent. Modifies the behavior and configuration of an agent action.
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
200
400
401
422
Action updated successfully
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
curl -L -X PUT 'https://services.leadconnectorhq.com/voice-ai/actions/:actionId' \
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
actionId — path
REQUIRED
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