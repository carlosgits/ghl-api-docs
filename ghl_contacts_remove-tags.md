# Remove Tags

Source: https://marketplace.gohighlevel.com/docs/ghl/contacts/remove-tags

Screenshot: images/ghl_contacts_remove-tags_screenshot.png

---

ContactsTagsRemove Tags
Remove Tags
DELETE
 https://services.leadconnectorhq.com/contacts/:contactId/tags
Remove Tags
Requirements
Scope(s)
contacts.write
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
contactId
string
REQUIRED
Contact Id
Example: sx6wyHhbFdRXh302LLNR
APPLICATION/JSON
BODY
REQUIRED
tags
string[]
REQUIRED
Example:["minim","velit magna"]
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
tags
string[]
Example:["minim","velit magna"]






















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
curl -L -X DELETE 'https://services.leadconnectorhq.com/contacts/:contactId/tags' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "tags": [
    "minim",
    "velit magna"
  ]
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
contactId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "tags": [
    "minim",
    "velit magna"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!