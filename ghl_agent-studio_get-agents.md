# List Agents

Source: https://marketplace.gohighlevel.com/docs/ghl/agent-studio/get-agents

Screenshot: images/ghl_agent-studio_get-agents_screenshot.png

---

AI Agent StudioAgentsList Agents
List Agents
GET
 https://services.leadconnectorhq.com/agent-studio/public-api/agents
Lists all active agents for the specified location. locationId is required parameter to ensure optimal performance. Supports pagination using limit and offset.
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
QUERY PARAMETERS
locationId
string
REQUIRED
Example: C2QujeCh8ZnC7al2InWR
limit
string
REQUIRED
Example: 20
offset
string
REQUIRED
Example: 0
source
string
Example: api
Responses
200
400
401
422
500
Agents retrieved successfully
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
Example:Agents retrieved successfully
agents
object[]
REQUIRED
pagination
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
curl -L 'https://services.leadconnectorhq.com/agent-studio/public-api/agents' \
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
limit — query
REQUIRED
offset — query
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