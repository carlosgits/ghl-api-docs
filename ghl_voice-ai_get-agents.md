# List Agents

Source: https://marketplace.gohighlevel.com/docs/ghl/voice-ai/get-agents

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_voice-ai_get-agents_screenshot.png

---

Voice AIAgentsList Agents
List Agents
GET
 https://services.leadconnectorhq.com/voice-ai/agents
Retrieve a paginated list of agents for given location.
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
QUERY PARAMETERS
page
number
Possible values: >= 1 and <= 5000
Page number starting from 1
Default value:1
Example: 1
pageSize
number
Possible values: >= 1 and <= 50
Number of items per page
Default value:10
Example: 10
locationId
string
REQUIRED
Location ID
query
string
Query
Responses
200
400
401
422
Agent list retrieved successfully.
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
agents
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
curl -L 'https://services.leadconnectorhq.com/voice-ai/agents' \
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