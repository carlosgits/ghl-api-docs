# Create an Agent

Source: https://marketplace.gohighlevel.com/docs/ghl/conversation-ai/create-agent

Screenshot: images/ghl_conversation-ai_create-agent_screenshot.png

---

Conversation AIAgentsCreate an Agent
Create an Agent
POST
 https://services.leadconnectorhq.com/conversation-ai/agents
Creates a new AI agent for the location. The agent will be created with the specified configuration including name, role, actions, and behavior settings.
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
APPLICATION/JSON
BODY
REQUIRED
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
Mode of operation - OFF, SUGGESTIVE, or AUTO_PILOT
Possible values: [off, suggestive, auto-pilot]
Default value: off
Example:auto-pilot
channels
string[]
Communication channels the agent can operate on
Possible values: [IG, FB, SMS, WebChat, WhatsApp, Live_Chat]
Example:["SMS","Live_Chat","WhatsApp"]
isPrimary
boolean
Indicates if this agent is a primary agent.
Default value: false
Example:true
waitTime
number
Wait time before agent responds (max 5 for minutes, 300 for seconds)
Default value: 2
Example:2
waitTimeUnit
string
Unit for wait time - SECONDS or MINUTES
Possible values: [minutes, seconds]
Default value: seconds
Example:seconds
sleepEnabled
boolean
Indicates if sleep functionality is enabled.
Default value: false
Example:false
sleepTime
number
Duration of sleep period (required if sleepEnabled is true). Set to null for indefinite sleep. (max 2880 for minutes, 172800 for seconds, 48 for hours)
Example:2
sleepTimeUnit
string
Unit of sleep time - HOURS, MINUTES, or SECONDS (required if sleepEnabled is true). Set to null for indefinite sleep.
Possible values: [hours, minutes, seconds]
Example:hours
personality
string
REQUIRED
Personality traits of the agent.
Example:Friendly and helpful
goal
string
REQUIRED
The goal of the agent.
Example:Assist customers with inquiries.
instructions
string
REQUIRED
Instructions for the agent.
Example:Provide customer service.
autoPilotMaxMessages
number
Maximum number of messages in auto-pilot mode before requiring human intervention. (max: 100, min: 1)
Default value: 75
Example:75
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
201
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
curl -L 'https://services.leadconnectorhq.com/conversation-ai/agents' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "name": "John Doe",
  "businessName": "Tech Corp",
  "mode": "auto-pilot",
  "channels": [
    "SMS",
    "Live_Chat",
    "WhatsApp"
  ],
  "isPrimary": true,
  "waitTime": 2,
  "waitTimeUnit": "seconds",
  "sleepEnabled": false,
  "sleepTime": 2,
  "sleepTimeUnit": "hours",
  "personality": "Friendly and helpful",
  "goal": "Assist customers with inquiries.",
  "instructions": "Provide  customer service.",
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
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "name": "John Doe",
  "businessName": "Tech Corp",
  "mode": "auto-pilot",
  "channels": [
    "SMS",
    "Live_Chat",
    "WhatsApp"
  ],
  "isPrimary": true,
  "waitTime": 2,
  "waitTimeUnit": "seconds",
  "sleepEnabled": false,
  "sleepTime": 2,
  "sleepTimeUnit": "hours",
  "personality": "Friendly and helpful",
  "goal": "Assist customers with inquiries.",
  "instructions": "Provide  customer service.",
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