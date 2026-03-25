# Get Call Log

Source: https://marketplace.gohighlevel.com/docs/ghl/voice-ai/get-call-log

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_voice-ai_get-call-log_screenshot.png

---

Voice AIDashboardGet Call Log
Get Call Log
GET
 https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs/:callId
Returns a call log by callId.
Requirements
Scope(s)
voice-ai-dashboard.readonly
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
callId
string
REQUIRED
Call ID
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
Successfully retrieved call log
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
id
string
REQUIRED
Unique identifier for the call
Example:507f1f77bcf86cd799439011
contactId
string
Associated contact ID
Example:507f1f77bcf86cd799439012
agentId
string
REQUIRED
Agent ID associated with the call
Example:507f1f77bcf86cd799439013
isAgentDeleted
boolean
REQUIRED
Whether the agent is deleted
Example:false
fromNumber
string
Caller phone number
Example:+1234567890
createdAt
date-time
REQUIRED
Timestamp when the call was created
Example:2024-01-15T10:30:00.000Z
duration
number
REQUIRED
Call duration in seconds
Example:180
trialCall
boolean
REQUIRED
Whether this call was a trial call
Example:false
executedCallActions
object[]
REQUIRED
summary
string
REQUIRED
Call summary
Example:Customer called to inquire about product pricing and was transferred to sales team.
transcript
string
REQUIRED
Call transcript
Example:bot: Hello, how can I help you today? human: I would like to know about your pricing...
translation
object
extractedData
object
messageId
string
Message identifier associated with the call
Example:507f1f77bcf86cd799439014












































































































































































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
curl -L 'https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs/:callId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
callId — path
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