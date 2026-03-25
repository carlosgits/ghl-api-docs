# Attach Instagram Professional Accounts

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/attach-instagram-page-group

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_attach-instagram-page-group_screenshot.png

---

Social PlannerOauth | InstagramAttach Instagram Professional Accounts
Attach Instagram Professional Accounts
POST
 https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/instagram/accounts/:accountId
Attach Instagram Professional Accounts
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
Account Location Id
Example: w37swmmLbA02zgqKPpxITe2
accountId
string
REQUIRED
Account Id
Example: w37swmmLbA02zgqKPpxITe
APPLICATION/JSON
BODY
REQUIRED
originId
string
Original platform-specific account identifier
Example:244405****11687
name
string
Display name of the account
Example:JOHN_DEO
avatar
string
Avatar or profile picture URL
Example:https://storage.googleapis.com/2ad21ebc23/test
pageId
string
REQUIRED
Facebook page ID associated with the Instagram account
Example:234234234242sd
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
success
boolean
REQUIRED
Success or Failure
Example:true
statusCode
number
REQUIRED
Status Code
Example:201
message
string
REQUIRED
Message
Example:Added Instagram Account
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/instagram/accounts/:accountId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "originId": "244405****11687",
  "name": "JOHN_DEO",
  "avatar": "https://storage.googleapis.com/2ad21ebc23/test",
  "pageId": "234234234242sd"
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
accountId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "originId": "244405****11687",
  "name": "JOHN_DEO",
  "avatar": "https://storage.googleapis.com/2ad21ebc23/test",
  "pageId": "234234234242sd"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!