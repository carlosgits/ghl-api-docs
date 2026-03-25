# Delete trained pages

Source: https://marketplace.gohighlevel.com/docs/ghl/knowledge-base/delete-trained-urls-for-knowledge-base

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_knowledge-base_delete-trained-urls-for-knowledge-base_screenshot.png

---

Knowledge BaseWeb CrawlerDelete trained pages
Delete trained pages
DELETE
 https://services.leadconnectorhq.com/knowledge-bases/crawler
Delete trained pages
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
knowledgeBaseId
string
REQUIRED
knowledge base ID as string
Example:tDtDnQdgm2LXpyiqYvZ6
locationId
string
REQUIRED
location ID as string
Example:tDtDnQdgm2LXpyiqYvZ6
urlIds
string[]
REQUIRED
List of trained urls ids ( fetched from the Get all trained page links by knowledge base endpoint)
Example:[tDtDnQdgm2LXpyiqYvZ6]
Responses
200
400
401
422
500
Selected pages deleted successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Indicates if the operation was successful
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/knowledge-bases/crawler' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "knowledgeBaseId": "tDtDnQdgm2LXpyiqYvZ6",
  "locationId": "tDtDnQdgm2LXpyiqYvZ6",
  "urlIds": "[tDtDnQdgm2LXpyiqYvZ6]"
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
  "knowledgeBaseId": "tDtDnQdgm2LXpyiqYvZ6",
  "locationId": "tDtDnQdgm2LXpyiqYvZ6",
  "urlIds": "[tDtDnQdgm2LXpyiqYvZ6]"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!