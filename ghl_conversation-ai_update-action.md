# Update Action

Source: https://marketplace.gohighlevel.com/docs/ghl/conversation-ai/update-action

Screenshot: images/ghl_conversation-ai_update-action_screenshot.png

---

Conversation AIActionsUpdate Action
Update Action
PUT
 https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId
Updates an existing action's configuration. This includes modifying the action name, description, trigger conditions, and behavior settings.
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
APPLICATION/JSON
BODY
REQUIRED
type
string
REQUIRED
Possible values: [triggerWorkflow, updateContactField, appointmentBooking, stopBot, humanHandOver, advancedFollowup, transferBot]
Example:triggerWorkflow
name
string
REQUIRED
Example:Trigger a Workflow
details
object
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
curl -L -X PUT 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "type": "triggerWorkflow",
  "name": "Trigger a Workflow",
  "details": {
    "workflowIds": [
      "workflow123",
      "workflow456"
    ],
    "triggerCondition": "When user requests appointment",
    "triggerMessage": "Workflow triggered successfully"
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
agentId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "type": "triggerWorkflow",
  "name": "Trigger a Workflow",
  "details": {
    "workflowIds": [
      "workflow123",
      "workflow456"
    ],
    "triggerCondition": "When user requests appointment",
    "triggerMessage": "Workflow triggered successfully"
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!