# Get all FAQs by knowledge base with pagination support

Source: https://marketplace.gohighlevel.com/docs/ghl/knowledge-base/list

Screenshot: images/ghl_knowledge-base_list_screenshot.png

---

Knowledge BaseFaqsGet all FAQs by knowledge base with pagination support
Get all FAQs by knowledge base with pagination support
GET
 https://services.leadconnectorhq.com/knowledge-bases/faqs
Retrieves FAQs for a knowledge base. Supports pagination using limit and lastFaqId parameters.
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
QUERY PARAMETERS
knowledgeBaseId
string
REQUIRED
knowledge base ID as string
Example: 710KoEzy793Fxubft0bc
locationId
string
REQUIRED
location ID as string
Example: qDZpF8GH3qvgJTmKCoL
limit
number
Limit the number of FAQs returned
Default value:10
Example: 10
lastFaqId
string
Last FAQ ID for pagination (cursor-based)
Example: 3rzeElC1FOVY91veVBkp
Responses
200
400
401
422
500
FAQs retrieved successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
count
number
REQUIRED
Total count of all FAQs in the knowledge base
Example:150
faqs
object[]
REQUIRED
lastFaqId
string
Last FAQ ID for pagination (use as lastFaqId in next request)
Example:3rzeElC1FOVY91veVBkp
hasMore
boolean
Whether there are more FAQs available
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
curl -L 'https://services.leadconnectorhq.com/knowledge-bases/faqs' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
knowledgeBaseId — query
REQUIRED
locationId — query
REQUIRED
Authorization — header
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