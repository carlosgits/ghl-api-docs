# Create a new FAQ inside knowledge base

Source: https://marketplace.gohighlevel.com/docs/ghl/knowledge-base/create

Screenshot: images/ghl_knowledge-base_create_screenshot.png

---

Knowledge BaseFaqsCreate a new FAQ inside knowledge base
Create a new FAQ inside knowledge base
POST
 https://services.leadconnectorhq.com/knowledge-bases/faqs
Create a new FAQ inside knowledge base
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
locationId
string
REQUIRED
location ID as string
Example:HqDZpF8GH3qvgJTmKCoL
question
string
REQUIRED
faq question as a string
Example:What is the capital of France?
answer
string
REQUIRED
faq answer as a string
Example:The capital of France is Paris.
knowledgeBaseId
string
REQUIRED
knowledge base ID as string
Example:710KoEzy793Fxubft0bc
Responses
201
400
401
422
500
FAQ created successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Success status of the operation
Example:true
faq
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
curl -L 'https://services.leadconnectorhq.com/knowledge-bases/faqs' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "HqDZpF8GH3qvgJTmKCoL",
  "question": "What is the capital of France?",
  "answer": "The capital of France is Paris.",
  "knowledgeBaseId": "710KoEzy793Fxubft0bc"
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
  "locationId": "HqDZpF8GH3qvgJTmKCoL",
  "question": "What is the capital of France?",
  "answer": "The capital of France is Paris.",
  "knowledgeBaseId": "710KoEzy793Fxubft0bc"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!