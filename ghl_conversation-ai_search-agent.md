# Search Agents

Source: https://marketplace.gohighlevel.com/docs/ghl/conversation-ai/search-agent

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_conversation-ai_search-agent_screenshot.png

---

Conversation AIAgentsSearch Agents
Search Agents
GET
 https://services.leadconnectorhq.com/conversation-ai/agents/search
Searches for AI agents based on various criteria including name, status, and configuration. Supports advanced filtering and full-text search capabilities.
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
QUERY PARAMETERS
startAfter
string
Start after is the agent id to start after, Serving as skip, send empty when first page
Example: Exampleee123
limit
number
Records per page
Example: 1
query
string
query to search on agent name, must be provided in lowercase
Example: booking
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
agents
object[]
REQUIRED
totalCount
number
REQUIRED
Total number of agents in the location (unfiltered count).
Example:100
count
number
REQUIRED
Number of agents in the current response (filtered/paginated count).
Example:25
























































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
curl -L 'https://services.leadconnectorhq.com/conversation-ai/agents/search' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!