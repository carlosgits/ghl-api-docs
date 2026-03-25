# Get Agent Action

Source: https://marketplace.gohighlevel.com/docs/ghl/voice-ai/get-action

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_voice-ai_get-action_screenshot.png

---

Voice AIActionsGet Agent Action
Get Agent Action
GET
 https://services.leadconnectorhq.com/voice-ai/actions/:actionId
Retrieve details of a specific action by its ID. Returns the action configuration including actionParameters.
Requirements
Scope(s)
voice-ai-agent-goals.readonly
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
Responses
200
400
401
422
Action details retrieved successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
id
string
REQUIRED
Unique identifier for the action
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
curl -L 'https://services.leadconnectorhq.com/voice-ai/actions/:actionId' \
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