# Delete Account

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/delete-account

Screenshot: images/ghl_social-planner_delete-account_screenshot.png

---

Social PlannerAccountDelete Account
Delete Account
DELETE
 https://services.leadconnectorhq.com/social-media-posting/:locationId/accounts/:id
Delete account and account from group
Requirements
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
Example: 2021-07-28
PATH PARAMETERS
locationId
string
REQUIRED
Location Id
Example: ve9EPM428h8vShlRW1KT
id
string
REQUIRED
Id
Example: 65fac446d599990d1313c1dd
QUERY PARAMETERS
companyId
string
Company ID
Example: sdfdsfdsfEWEsdfsdsW32dd
userId
string
User ID
Example: sdfdsfdsfEWEsdfsdsW32dd
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
Success or Failure
Example:true
statusCode
number
REQUIRED
Status Code
Example:200
message
string
REQUIRED
Message
Example:Deleted Account
results
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/social-media-posting/:locationId/accounts/:id' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — path
REQUIRED
id — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!