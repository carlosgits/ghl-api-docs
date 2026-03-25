# Get crawling status for the latest operation

Source: https://marketplace.gohighlevel.com/docs/ghl/knowledge-base/get-crawling-status-for-latest-operation

Screenshot: images/ghl_knowledge-base_get-crawling-status-for-latest-operation_screenshot.png

---

Knowledge BaseWeb CrawlerGet crawling status for the latest operation
Get crawling status for the latest operation
GET
 https://services.leadconnectorhq.com/knowledge-bases/crawler/status
Get crawling status for the latest operation
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
locationId
string
REQUIRED
Location ID as string
Example: tDtDnQdgm2LXpyiqYvZ6
operationId
string
REQUIRED
operation id as string
Example: 1
knowledgeBaseId
string
REQUIRED
knowledge base id
Example: jjkkxftgvbhjmn,
Responses
200
400
401
422
500
Operation status fetched successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Indicates if the operation was successful
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
curl -L 'https://services.leadconnectorhq.com/knowledge-bases/crawler/status' \
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
operationId — query
REQUIRED
knowledgeBaseId — query
REQUIRED
Authorization — header
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!