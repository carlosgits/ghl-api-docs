# Update Agent

Source: https://marketplace.gohighlevel.com/docs/ghl/conversation-ai/update-agent

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_conversation-ai_update-agent_screenshot.png

---

Conversation AIAgentsUpdate Agent
Update Agent
PUT
 https://services.leadconnectorhq.com/conversation-ai/agents/:agentId
Updates an existing AI agent's configuration. All fields in the agent configuration can be updated including name, status, actions, and behavior settings.
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
APPLICATION/JSON
BODY
REQUIRED
name
string
Name of the agent.
Example:John Doe
businessName
string
Name of the business the agent represents.
Example:Tech Corp
mode
string
Mode of operation for the agent, required if primary is enabled.
Possible values: [off, suggestive, auto-pilot]
channels
string[]
Channels the agent can use.
Possible values: [IG, FB, SMS, WebChat, WhatsApp, Live_Chat]
isPrimary
boolean
Indicates if this agent is a primary agent.
Example:true
waitTime
number
Wait time before agent responds (max 5 for minutes, 300 for seconds).
Example:30
waitTimeUnit
string
Unit for wait time - SECONDS or MINUTES
Possible values: [minutes, seconds]
Example:seconds
sleepEnabled
boolean
Indicates if sleep functionality is enabled.
Example:false
sleepTime
number
Duration of sleep period (required if sleepEnabled is true). Set to null for indefinite sleep. (max 2880 for minutes, 172800 for seconds, 48 for hours)
Example:10
sleepTimeUnit
string
Unit of sleep time - HOURS, MINUTES, or SECONDS (required if sleepEnabled is true). Set to null for indefinite sleep.
Possible values: [hours, minutes, seconds]
personality
string
Personality traits of the agent.
Example:You re an AI assistant and you are friendly and helpful
goal
string
The goal of the agent.
Example:You are an AI assistant and you are helping customers with inquiries.
instructions
string
Instructions for the agent.
Example:Provide excellent customer service.
autoPilotMaxMessages
number
REQUIRED
Maximum number of messages in auto-pilot mode before requiring human intervention. (max: 100, min: 1)
Default value: 75
knowledgeBaseIds
string[]
Array of knowledge base IDs associated with this agent.
respondToImages
boolean
Allow agent to respond to images
Default value: false
Example:true
respondToAudio
boolean
Allow agent to respond to audio
Default value: false
Example:true
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
curl -L -X PUT 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "name": "John Doe",
  "businessName": "Tech Corp",
  "mode": "off",
  "channels": [
    "IG"
  ],
  "isPrimary": true,
  "waitTime": 30,
  "waitTimeUnit": "seconds",
  "sleepEnabled": false,
  "sleepTime": 10,
  "sleepTimeUnit": "hours",
  "personality": "You re an AI assistant and you are friendly and helpful",
  "goal": "You are an AI assistant and you are helping customers with inquiries.",
  "instructions": "Provide excellent customer service.",
  "autoPilotMaxMessages": 75,
  "knowledgeBaseIds": [
    "string"
  ],
  "respondToImages": true,
  "respondToAudio": true
}'
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
Body
 REQUIRED
{
  "name": "John Doe",
  "businessName": "Tech Corp",
  "mode": "off",
  "channels": [
    "IG"
  ],
  "isPrimary": true,
  "waitTime": 30,
  "waitTimeUnit": "seconds",
  "sleepEnabled": false,
  "sleepTime": 10,
  "sleepTimeUnit": "hours",
  "personality": "You re an AI assistant and you are friendly and helpful",
  "goal": "You are an AI assistant and you are helping customers with inquiries.",
  "instructions": "Provide excellent customer service.",
  "autoPilotMaxMessages": 75,
  "knowledgeBaseIds": [
    "string"
  ],
  "respondToImages": true,
  "respondToAudio": true
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!