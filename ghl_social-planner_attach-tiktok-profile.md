# Attach Tiktok profile

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/attach-tiktok-profile

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_attach-tiktok-profile_screenshot.png

---

Social PlannerOauth | TiktokAttach Tiktok profile
Attach Tiktok profile
POST
 https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/tiktok/accounts/:accountId
Attach Tiktok profile
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
type
string
REQUIRED
Type of TikTok account
Possible values: [page, group, profile, location, business]
Example:profile
originId
string
REQUIRED
Original platform-specific account identifier
Example:244405****11687
name
string
REQUIRED
Display name of the account
Example:JOHN_DEO
avatar
string
REQUIRED
Avatar or profile picture URL
Example:https://example.com/avatar.jpg
verified
boolean
Indicates if the TikTok account is verified
Example:true
username
string
Username or handle of the TikTok account
Example:JOHN_DEO
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
Example:Added Tiktok Account
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/tiktok/accounts/:accountId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "type": "profile",
  "originId": "244405****11687",
  "name": "JOHN_DEO",
  "avatar": "https://example.com/avatar.jpg",
  "verified": true,
  "username": "JOHN_DEO"
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
  "type": "profile",
  "originId": "244405****11687",
  "name": "JOHN_DEO",
  "avatar": "https://example.com/avatar.jpg",
  "verified": true,
  "username": "JOHN_DEO"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!