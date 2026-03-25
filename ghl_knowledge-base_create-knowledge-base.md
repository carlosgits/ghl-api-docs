# Create a new knowledge base (max 15 knowledge bases per location)

Source: https://marketplace.gohighlevel.com/docs/ghl/knowledge-base/create-knowledge-base

Screenshot: images/ghl_knowledge-base_create-knowledge-base_screenshot.png

---

Knowledge BaseKnowledge BaseCreate a new knowledge base (max 15 knowledge bases per location)
Create a new knowledge base (max 15 knowledge bases per location)
POST
 https://services.leadconnectorhq.com/knowledge-bases/
Create a new knowledge base (max 15 knowledge bases per location)
Requirements
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
HEADER PARAMETERS
Authorization
string
REQUIRED
Access Token
Example: Bearer 9c48df2694a849b6089f9d0d3513efe
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
description
string
locationId
string
REQUIRED
Responses
201
400
401
Knowledge base created successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Success status of the operation
Example:true
data
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
curl -L 'https://services.leadconnectorhq.com/knowledge-bases/' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "name": "string",
  "description": "string",
  "locationId": "string"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
Authorization — header
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "name": "string",
  "description": "string",
  "locationId": "string"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!