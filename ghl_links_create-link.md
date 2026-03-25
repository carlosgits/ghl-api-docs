# Create Link

Source: https://marketplace.gohighlevel.com/docs/ghl/links/create-link

Screenshot: images/ghl_links_create-link_screenshot.png

---

Trigger LinksTrigger LinksCreate Link
Create Link
POST
 https://services.leadconnectorhq.com/links/
Create Link
Requirements
Scope(s)
links.write
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
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
Example:ve9EPM428h8vShlRW1KT
name
string
REQUIRED
Example:first tag
redirectTo
string
REQUIRED
Example:https://www.google.com/
Responses
201
400
401
422
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
curl -L 'https://services.leadconnectorhq.com/links/' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "name": "first tag",
  "redirectTo": "https://www.google.com/"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "name": "first tag",
  "redirectTo": "https://www.google.com/"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!