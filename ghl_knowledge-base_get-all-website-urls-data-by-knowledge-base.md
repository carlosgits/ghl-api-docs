# Get all trained page links by knowledge base

Source: https://marketplace.gohighlevel.com/docs/ghl/knowledge-base/get-all-website-urls-data-by-knowledge-base

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_knowledge-base_get-all-website-urls-data-by-knowledge-base_screenshot.png

---

Knowledge BaseWeb CrawlerGet all trained page links by knowledge base
Get all trained page links by knowledge base
GET
 https://services.leadconnectorhq.com/knowledge-bases/crawler
Get all trained page links by knowledge base
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
Example: tDtDnQdgm2LXpyiqYvZ6
locationId
string
REQUIRED
location ID as string
Example: tDtDnQdgm2LXpyiqYvZ6
page
number
Page number
Example: 1
pageLength
number
Records per page
Example: 1
query
string
query to filter on url links
Example: www.example.com/
Responses
200
400
401
422
500
Trained page links retrieved successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
count
number
REQUIRED
Total count of URLs in the knowledge base
Example:64
urls
object[]
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
curl -L 'https://services.leadconnectorhq.com/knowledge-bases/crawler' \
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