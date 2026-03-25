# Get Link by ID

Source: https://marketplace.gohighlevel.com/docs/ghl/links/get-link-by-id

Screenshot: images/ghl_links_get-link-by-id_screenshot.png

---

Trigger LinksTrigger LinksGet Link by ID
Get Link by ID
GET
 https://services.leadconnectorhq.com/links/id/:linkId
Get a single link by its ID
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
Possible values: [2021-07-28]
API Version
PATH PARAMETERS
linkId
string
REQUIRED
Link Id
QUERY PARAMETERS
locationId
string
REQUIRED
Location Id
Example: ABCHkzuJQ8ZMd4Te84GK
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
link
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
curl -L 'https://services.leadconnectorhq.com/links/id/:linkId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
linkId — path
REQUIRED
locationId — query
REQUIRED
Authorization — header
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!