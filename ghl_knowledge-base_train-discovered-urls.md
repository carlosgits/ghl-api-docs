# Train discovered website pages and ingest into the knowledge base

Source: https://marketplace.gohighlevel.com/docs/ghl/knowledge-base/train-discovered-urls

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_knowledge-base_train-discovered-urls_screenshot.png

---

Knowledge BaseWeb CrawlerTrain discovered website pages and ingest into the knowledge base
Train discovered website pages and ingest into the knowledge base
POST
 https://services.leadconnectorhq.com/knowledge-bases/crawler/train
Train discovered website pages and ingest into the knowledge base
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
urlIds
string[]
REQUIRED
List of Object ids of the discovered urls
Example:["688b640bcb02d498102a13ec","688b640bcb02d498102a13ea"]
knowledgeBaseId
string
REQUIRED
knowledge base id
Example:jjkkxftgvbhjmn,
operationId
string
REQUIRED
operation id as string
Example:688b640bcb02d498102a13f0,
Responses
201
400
401
422
500
Pages trained successfully
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
curl -L 'https://services.leadconnectorhq.com/knowledge-bases/crawler/train' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "tDtDnQdgm2LXpyiqYvZ6",
  "urlIds": [
    "688b640bcb02d498102a13ec",
    "688b640bcb02d498102a13ea"
  ],
  "knowledgeBaseId": "jjkkxftgvbhjmn,",
  "operationId": "688b640bcb02d498102a13f0,"
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
  "urlIds": [
    "688b640bcb02d498102a13ec",
    "688b640bcb02d498102a13ea"
  ],
  "knowledgeBaseId": "jjkkxftgvbhjmn,",
  "operationId": "688b640bcb02d498102a13f0,"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!