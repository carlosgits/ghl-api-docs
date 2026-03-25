# Create Agent

Source: https://marketplace.gohighlevel.com/docs/ghl/voice-ai/create-agent

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_voice-ai_create-agent_screenshot.png

---

Voice AIAgentsCreate Agent
Create Agent
POST
 https://services.leadconnectorhq.com/voice-ai/agents
Create a new voice AI agent configuration and settings
Requirements
Scope(s)
voice-ai-agents.write
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
locationId
string
REQUIRED
Unique identifier for the location where this agent will operate
Example:LOC123456789ABCDEF
agentName
string
Display name for the voice AI agent, between 1-40 characters. Default: "My Agent {random 3 digit number}"
Possible values: non-empty and <= 40 characters
Example:Customer Support Agent
businessName
string
Name of the business this agent represents. Default: Uses location name
Possible values: non-empty
Example:Acme Corporation
welcomeMessage
string
Initial greeting spoken when the agent answers calls. Default: Auto generated
Possible values: non-empty and <= 190 characters
Example:Hello! Thank you for calling Acme Corporation. How can I assist you today?
agentPrompt
string
Custom instructions defining the agent's behavior and personality. Default: Basic prompt generated automatically
Example:You are a helpful customer service representative. Always be polite and professional.
voiceId
string
Identifier for the speech synthesis voice from available voice options. Default: Auto generated
Example:507f1f77bcf86cd799439011
language
VoiceAILanguage (string)
Language code for the agent's speech and understanding. Default: "en-US"
Possible values: [en-US, pt-BR, es, fr, de, it, nl-NL, multi]
Example:en-US
patienceLevel
PatienceLevel (string)
Tolerance level for caller response delays. Default: "high"
Possible values: [low, medium, high]
Example:low
maxCallDuration
number
Maximum call duration in seconds, between 180-900 (3-15 minutes). Default: 300 seconds (5 minutes)
Possible values: >= 180 and <= 900
Example:600
sendUserIdleReminders
boolean
Enables automatic reminders when callers are silent. Default: true
Example:true
reminderAfterIdleTimeSeconds
number
Seconds to wait before sending idle reminders, between 1-20. Default: 8 seconds
Possible values: >= 1 and <= 20
Example:5
inboundNumber
string
Phone number for receiving inbound calls to this agent. Default: null
Example:+1234567890
numberPoolId
string
Identifier for the number pool managing phone number allocation. Default: null
Example:pool_507f1f77bcf86cd799439011
callEndWorkflowIds
string[]
Array of workflow IDs to trigger automatically when calls end. Default: []
Possible values: <= 10
Example:["wf_507f1f77bcf86cd799439011","wf_507f1f77bcf86cd799439012"]
sendPostCallNotificationTo
object
agentWorkingHours
object[]
timezone
string
IANA timezone identifier affecting working hours and scheduling. Default: Location timezone
Possible values: Value must match regular expression ^[A-Za-z_]+/[A-Za-z_]+$
Example:America/New_York
isAgentAsBackupDisabled
boolean
Prevents this agent from being used as a fallback option. Default: false (Available as backup agent)
Example:false
translation
object
Responses
201
400
401
422
Agent created successfully
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
curl -L 'https://services.leadconnectorhq.com/voice-ai/agents' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "locationId": "LOC123456789ABCDEF",
  "agentName": "Customer Support Agent",
  "businessName": "Acme Corporation",
  "welcomeMessage": "Hello! Thank you for calling Acme Corporation. How can I assist you today?",
  "agentPrompt": "You are a helpful customer service representative. Always be polite and professional.",
  "voiceId": "507f1f77bcf86cd799439011",
  "language": "en-US",
  "patienceLevel": "low",
  "maxCallDuration": 600,
  "sendUserIdleReminders": true,
  "reminderAfterIdleTimeSeconds": 5,
  "inboundNumber": "+1234567890",
  "numberPoolId": "pool_507f1f77bcf86cd799439011",
  "callEndWorkflowIds": [
    "wf_507f1f77bcf86cd799439011",
    "wf_507f1f77bcf86cd799439012"
  ],
  "sendPostCallNotificationTo": {
    "admins": true,
    "allUsers": false,
    "contactAssignedUser": false,
    "specificUsers": [
      "user_507f1f77bcf86cd799439011"
    ],
    "customEmails": [
      "manager@company.com"
    ]
  },
  "agentWorkingHours": [
    {
      "dayOfTheWeek": 1,
      "intervals": [
        {
          "startHour": 9,
          "startMinute": 0,
          "endHour": 17,
          "endMinute": 30
        }
      ]
    }
  ],
  "timezone": "America/New_York",
  "isAgentAsBackupDisabled": false,
  "translation": {
    "enabled": false,
    "language": "es"
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
  "locationId": "LOC123456789ABCDEF",
  "agentName": "Customer Support Agent",
  "businessName": "Acme Corporation",
  "welcomeMessage": "Hello! Thank you for calling Acme Corporation. How can I assist you today?",
  "agentPrompt": "You are a helpful customer service representative. Always be polite and professional.",
  "voiceId": "507f1f77bcf86cd799439011",
  "language": "en-US",
  "patienceLevel": "low",
  "maxCallDuration": 600,
  "sendUserIdleReminders": true,
  "reminderAfterIdleTimeSeconds": 5,
  "inboundNumber": "+1234567890",
  "numberPoolId": "pool_507f1f77bcf86cd799439011",
  "callEndWorkflowIds": [
    "wf_507f1f77bcf86cd799439011",
    "wf_507f1f77bcf86cd799439012"
  ],
  "sendPostCallNotificationTo": {
    "admins": true,
    "allUsers": false,
    "contactAssignedUser": false,
    "specificUsers": [
      "user_507f1f77bcf86cd799439011"
    ],
    "customEmails": [
      "manager@company.com"
    ]
  },
  "agentWorkingHours": [
    {
      "dayOfTheWeek": 1,
      "intervals": [
        {
          "startHour": 9,
          "startMinute": 0,
          "endHour": 17,
          "endMinute": 30
        }
      ]
    }
  ],
  "timezone": "America/New_York",
  "isAgentAsBackupDisabled": false,
  "translation": {
    "enabled": false,
    "language": "es"
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!