# Get Agent

Source: https://marketplace.gohighlevel.com/docs/ghl/voice-ai/get-agent

Screenshot: images/ghl_voice-ai_get-agent_screenshot.png

---

Voice AIAgentsGet Agent
Get Agent
GET
 https://services.leadconnectorhq.com/voice-ai/agents/:agentId
Retrieve detailed configuration and settings for a specific voice AI agent
Requirements
Scope(s)
voice-ai-agents.readonly
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
Unique agent identifier
Example: 507f1f77bcf86cd799439011
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
Agent details retrieved successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
id
string
REQUIRED
Unique identifier for the created agent
Example:507f1f77bcf86cd799439011
locationId
string
REQUIRED
Unique identifier for the location where this agent operates
Example:LOC123456789ABCDEF
agentName
string
REQUIRED
Display name of the voice AI agent
Example:Customer Support Agent
businessName
string
REQUIRED
Name of the business this agent represents
Example:Acme Corporation
welcomeMessage
string
REQUIRED
Greeting message spoken when the agent answers calls
Example:Hello! Thank you for calling. How can I assist you today?
agentPrompt
string
REQUIRED
Custom instructions defining the agent's behavior
Example:You are a helpful customer service representative.
voiceId
string
REQUIRED
Identifier for the speech synthesis voice being used
Example:507f1f77bcf86cd799439011
language
string
REQUIRED
Language code for the agent's speech and understanding
Example:en-US
patienceLevel
string
REQUIRED
Current tolerance level for caller response delays
Example:medium
maxCallDuration
number
REQUIRED
Maximum call duration in seconds, between 180-900
Possible values: >= 180 and <= 900
Example:600
sendUserIdleReminders
boolean
REQUIRED
Indicates whether automatic idle reminders are enabled
Example:true
reminderAfterIdleTimeSeconds
number
REQUIRED
Seconds to wait before sending idle reminders, between 1-20
Possible values: >= 1 and <= 20
Example:5
inboundNumber
string
Phone number for receiving inbound calls
Example:+1234567890
numberPoolId
string
Identifier for the number pool managing this agent's phone allocation
Example:pool_507f1f77bcf86cd799439011
callEndWorkflowIds
string[]
Array of workflow IDs triggered automatically when calls end
Example:[]
sendPostCallNotificationTo
object
agentWorkingHours
object[]
timezone
string
REQUIRED
IANA timezone identifier for working hours and scheduling
Example:America/New_York
isAgentAsBackupDisabled
boolean
REQUIRED
Indicates whether this agent is excluded from backup scenarios
Example:false
translation
object
actions
object[]
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
curl -L 'https://services.leadconnectorhq.com/voice-ai/agents/:agentId' \
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