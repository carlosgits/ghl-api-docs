# List Call Logs

Source: https://marketplace.gohighlevel.com/docs/ghl/voice-ai/get-call-logs

Screenshot: images/ghl_voice-ai_get-call-logs_screenshot.png

---

Voice AIDashboardList Call Logs
List Call Logs
GET
 https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs
Returns call logs for Voice AI agents scoped to a location. Supports filtering by agent, contact, call type, action types, and date range (interpreted in the provided IANA timezone). Also supports sorting and 1-based pagination.
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
QUERY PARAMETERS
locationId
string
REQUIRED
Location identifier. Filters results to this location.
agentId
string
Agent identifier. When provided, returns logs for this agent only.
Example: 507f1f77bcf86cd799439011
contactId
string
Contact IDs (comma-separated) to filter by.
Example: contact123,contact456
callType
string
Possible values: [LIVE, TRIAL]
Call type filter.
startDate
number
Start date filter (Unix timestamp). Must be less than endDate. Both startDate and endDate must be provided together.
Example: 1679308800000
endDate
number
End date filter (Unix timestamp). Must be greater than startDate. Both startDate and endDate must be provided together.
Example: 1679395199000
actionType
string
Possible values: [CALL_TRANSFER, DATA_EXTRACTION, IN_CALL_DATA_EXTRACTION, WORKFLOW_TRIGGER, SMS, APPOINTMENT_BOOKING, CUSTOM_ACTION, KNOWLEDGE_BASE]
Action type filter for call logs (comma-separated ACTION_TYPE values)
Example: SMS,CALL_TRANSFER,WORKFLOW_TRIGGER
sortBy
string
Possible values: [duration, createdAt]
Field to sort by. Defaults to newest if omitted.
sort
string
Possible values: [ascend, descend]
Sort direction. Applies only when sortBy is provided.
page
number
Page number (1-based).
Default value:1
pageSize
number
Page size (max 50).
Default value:10
Responses
200
400
401
Successfully retrieved call logs
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
total
number
REQUIRED
Total number of items
Example:150
page
number
REQUIRED
Page number starting from 1
Example:2
pageSize
number
REQUIRED
Number of items per page
Example:10
callLogs
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
curl -L 'https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — query
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!