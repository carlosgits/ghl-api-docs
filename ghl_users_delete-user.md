# Delete User

Source: https://marketplace.gohighlevel.com/docs/ghl/users/delete-user

Screenshot: images/ghl_users_delete-user_screenshot.png

---

UsersUsersDelete User
Delete User
DELETE
 https://services.leadconnectorhq.com/users/:userId
Delete User
Requirements
Scope(s)
users.write
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Agency Token
Sub-Account Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
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
succeded
boolean
Example:true
message
string
Example:Queued deleting user with e-mail john@deo.com and name John Deo. Will take effect in a few minutes.




















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
curl -L -X DELETE 'https://services.leadconnectorhq.com/users/:userId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Security Scheme
Agency-Access
Location-Access
Bearer Token
Parameters
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!