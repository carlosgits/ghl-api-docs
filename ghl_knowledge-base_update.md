# Update an existing knowledge base FAQ

Source: https://marketplace.gohighlevel.com/docs/ghl/knowledge-base/update

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_knowledge-base_update_screenshot.png

---

Knowledge BaseFaqsUpdate an existing knowledge base FAQ
Update an existing knowledge base FAQ
PUT
 https://services.leadconnectorhq.com/knowledge-bases/faqs/:id
Update an existing knowledge base FAQ
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
PATH PARAMETERS
id
string
REQUIRED
faq ID as string
Example: 710KoEzy793Fxubft0bc
APPLICATION/JSON
BODY
REQUIRED
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
Responses
200
400
401
422
500
FAQ updated successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Success status of the update operation
Example:true























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
curl -L -X PUT 'https://services.leadconnectorhq.com/knowledge-bases/faqs/:id' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "question": "What is the capital of France?",
  "answer": "The capital of France is Paris."
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
id — path
REQUIRED
Authorization — header
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "question": "What is the capital of France?",
  "answer": "The capital of France is Paris."
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!