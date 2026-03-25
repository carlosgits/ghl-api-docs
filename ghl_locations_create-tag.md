# Create Tag

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/create-tag

Screenshot: images/ghl_locations_create-tag_screenshot.png

---

Sub-Account (Formerly location)TagsCreate Tag
Create Tag
POST
 https://services.leadconnectorhq.com/locations/:locationId/tags
Create tag
Requirements
Scope(s)
locations/tags.write
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
PATH PARAMETERS
locationId
string
REQUIRED
Location Id
Example: ve9EPM428h8vShlRW1KT
APPLICATION/JSON
BODY
REQUIRED
name
string
REQUIRED
Tag name
Example:Tag
Responses
200
400
401
422
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
tag
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
curl -L 'https://services.leadconnectorhq.com/locations/:locationId/tags' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "name": "Tag"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "name": "Tag"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!