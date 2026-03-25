# Get all knowledge bases for a location by location Id (paginated)

Source: https://marketplace.gohighlevel.com/docs/ghl/knowledge-base/list-all-knowledge-bases-paginated

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_knowledge-base_list-all-knowledge-bases-paginated_screenshot.png

---

Knowledge BaseKnowledge BaseGet all knowledge bases for a location by location Id (paginated)
Get all knowledge bases for a location by location Id (paginated)
GET
 https://services.leadconnectorhq.com/knowledge-bases/
Get all knowledge bases for a location by location Id (paginated)
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
query
string
search query for knowledge base name
limit
number
Maximum number of knowledge bases to return
Default value:20
Example: 20
lastKnowledgeBaseId
string
ID of the last knowledge base from the previous page (for pagination)
Example: ZwTB8S0yo0FIBY6OPZTD
Responses
200
400
401
Paginated knowledge bases retrieved successfully
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