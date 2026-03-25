# Execute Agent

Source: https://marketplace.gohighlevel.com/docs/ghl/agent-studio/execute-agent

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_agent-studio_execute-agent_screenshot.png

---

AI Agent StudioAgentsExecute Agent
Execute Agent
POST
 https://services.leadconnectorhq.com/agent-studio/public-api/agents/:agentId/execute
Executes the specified agent and returns a non-streaming JSON response with the complete agent output. The agent must be in active status and belong to the specified location. locationId is required in the request body.
Session Management:
For the first message in a new session, do not include the executionId in the request payload.
The API will return an executionId along with the agent response, which uniquely identifies this conversation session.
To continue the conversation within the same session, include the executionId from the previous response in subsequent requests. This allows the agent to maintain conversation context and history across multiple interactions.
Requirements
Scope(s)
agent-studio.write
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
source
string
Example: api
APPLICATION/JSON
BODY
REQUIRED
message
string
REQUIRED
Message to send to the agent
Example:How can you help me with my marketing?
executionId
string
Execution ID for continuing an existing conversation
Example:a1b2c3d4e5f6g7h8i9j0k1l2
inputVariables
object
Input variables to pass to the agent
versionId
string
Published version ID to execute
Example:b2b1c1d2-3e4f-5a6b-7c8d-9e0f1a2b3c4d
attachments
object[]
locationId
string
REQUIRED
Location ID
Example:C2QujeCh8ZnC7al2InWR
Responses
200
400
401
403
404
422
500
Agent executed successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Success status
Example:true
executionId
string
REQUIRED
Unique session identifier that maintains conversational context across multiple interactions within the same agent session
Example:a1b2c3d4e5f6g7h8i9j0k1l2
interactionId
string
REQUIRED
Unique identifier for a single interaction cycle, consisting of one user input and the corresponding agent response
Example:m9n8o7p6q5r4s3t2u1v0w9x8
response
string
REQUIRED
Agent response text
Example:I can help you with various tasks...
type
string
REQUIRED
Response type
Example:text
nextExpectedInput
string
REQUIRED
Expected input type for next interaction
Example:text
goalCompletion
boolean
REQUIRED
When end node is added in the graph, this will be true if the agent reached the end node in the graph
Example:false
executionStatus
string
REQUIRED
Execution status
Example:completed
attachments
array
REQUIRED
Response attachments
Example:[]
generativeOutputs
array
REQUIRED
Generated outputs
Example:[]




























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
curl -L 'https://services.leadconnectorhq.com/agent-studio/public-api/agents/:agentId/execute' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "message": "How can you help me with my marketing?",
  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",
  "inputVariables": {},
  "versionId": "b2b1c1d2-3e4f-5a6b-7c8d-9e0f1a2b3c4d",
  "attachments": [
    {
      "type": "image",
      "imageUrl": "https://example.com/image.png"
    }
  ],
  "locationId": "C2QujeCh8ZnC7al2InWR"
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
Show optional parameters
Body
 REQUIRED
{
  "message": "How can you help me with my marketing?",
  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",
  "inputVariables": {},
  "versionId": "b2b1c1d2-3e4f-5a6b-7c8d-9e0f1a2b3c4d",
  "attachments": [
    {
      "type": "image",
      "imageUrl": "https://example.com/image.png"
    }
  ],
  "locationId": "C2QujeCh8ZnC7al2InWR"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!