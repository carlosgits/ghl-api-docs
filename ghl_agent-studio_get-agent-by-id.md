# Get Agent

Source: https://marketplace.gohighlevel.com/docs/ghl/agent-studio/get-agent-by-id

Screenshot: images/ghl_agent-studio_get-agent-by-id_screenshot.png

---

AI Agent StudioAgentsGet Agent
Get Agent
GET
 https://services.leadconnectorhq.com/agent-studio/public-api/agents/:agentId
Gets a specific agent by its ID for the specified location. locationId is required parameter. The agent must have active status.
Requirements
Scope(s)
agent-studio.readonly
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
Example: p1q2r3s4t5u6v7w8x9y0z1a2
QUERY PARAMETERS
locationId
string
REQUIRED
Example: C2QujeCh8ZnC7al2InWR
source
string
Example: api
Responses
200
400
401
404
422
500
Agent retrieved successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Success status
Example:true
message
string
REQUIRED
Response message
Example:Agent retrieved successfully
agent
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
curl -L 'https://services.leadconnectorhq.com/agent-studio/public-api/agents/:agentId' \
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
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!