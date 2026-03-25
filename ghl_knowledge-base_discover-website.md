# Start crawling and discover pages for training

Source: https://marketplace.gohighlevel.com/docs/ghl/knowledge-base/discover-website

Screenshot: images/ghl_knowledge-base_discover-website_screenshot.png

---

Knowledge BaseWeb CrawlerStart crawling and discover pages for training
Start crawling and discover pages for training
POST
 https://services.leadconnectorhq.com/knowledge-bases/crawler
Start crawling and discover pages for training
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
Location ID as string
Example:tDtDnQdgm2LXpyiqYvZ6
url
string
REQUIRED
Website URL as string
Example:https://kubernetes.io/tDtDnQdgm2LXpyiqYvZ6
option
string
REQUIRED
Mode as string
Possible values: [Exact, Path, Domain]
Example:Exact
knowledgeBaseId
string
REQUIRED
knowledge base ID as string
Example:tDtDnQdgm2LXpyiqYvZ6
Responses
201
400
401
422
500
Crawling and discovery started successfully
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
curl -L 'https://services.leadconnectorhq.com/knowledge-bases/crawler' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "tDtDnQdgm2LXpyiqYvZ6",
  "url": "https://kubernetes.io/tDtDnQdgm2LXpyiqYvZ6",
  "option": "Exact",
  "knowledgeBaseId": "tDtDnQdgm2LXpyiqYvZ6"
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
  "locationId": "tDtDnQdgm2LXpyiqYvZ6",
  "url": "https://kubernetes.io/tDtDnQdgm2LXpyiqYvZ6",
  "option": "Exact",
  "knowledgeBaseId": "tDtDnQdgm2LXpyiqYvZ6"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!