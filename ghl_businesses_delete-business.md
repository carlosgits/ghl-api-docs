# Delete Business

Source: https://marketplace.gohighlevel.com/docs/ghl/businesses/delete-business

Screenshot: images/ghl_businesses_delete-business_screenshot.png

---

BusinessBusinessesDelete Business
Delete Business
DELETE
 https://services.leadconnectorhq.com/businesses/:businessId
Delete Business
Requirements
Scope(s)
businesses.write
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
businessId
string
REQUIRED
Example: 5DP4iH6HLkQsiKESj6rh
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
success
boolean
REQUIRED
Success value
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/businesses/:businessId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
businessId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!