# Get Agent

Source: https://marketplace.gohighlevel.com/docs/ghl/conversation-ai/get-agent

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_conversation-ai_get-agent_screenshot.png

---

Conversation AIAgentsGet Agent
Get Agent
GET
 https://services.leadconnectorhq.com/conversation-ai/agents/:agentId
Retrieves a specific AI agent by its ID. Returns the complete agent configuration including name, status, actions, and settings.
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
id
string
REQUIRED
Unique identifier for the agent.
Example:emp_123
name
string
REQUIRED
Name of the agent.
Example:John Doe
businessName
string
Name of the business the agent represents.
Example:Tech Corp
mode
string
REQUIRED
Current operating mode of the agent.
Possible values: [off, suggestive, auto-pilot]
Example:auto-pilot
channels
string[]
REQUIRED
Communication channels the agent operates on.
Possible values: [IG, FB, SMS, WebChat, WhatsApp, Live_Chat]
Example:["SMS","Live_Chat"]
waitTime
number
REQUIRED
Wait time before agent responds.
Example:30
waitTimeUnit
string
REQUIRED
Unit for wait time.
Possible values: [minutes, seconds]
Example:seconds
sleepEnabled
boolean
REQUIRED
Indicates if sleep functionality is enabled.
Example:false
sleepTime
number
Duration of sleep period.
Example:2
sleepTimeUnit
string
Unit of sleep time.
Possible values: [hours, minutes, seconds]
Example:hours
actions
object[]
REQUIRED
isPrimary
boolean
REQUIRED
Indicates if this agent is a primary agent.
Example:false
autoPilotMaxMessages
number
REQUIRED
Maximum number of messages in auto-pilot mode before requiring human intervention.
Example:25
goal
string
The goal of the agent.
Example:Assist customers with inquiries
personality
string
Personality traits of the agent.
Example:Friendly and helpful
instructions
string
Instructions for the agent.
Example:Provide excellent customer service
knowledgeBaseIds
string[]
Array of knowledge base IDs associated with this agent.
Example:["kb_123","kb_456"]














































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
curl -L 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId' \
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