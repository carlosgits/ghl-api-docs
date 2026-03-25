# Attach oauth accounts

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/attach-oauth-accounts

Screenshot: images/ghl_social-planner_attach-oauth-accounts_screenshot.png

---

Social PlannerOAuth | GenericAttach oauth accounts
Attach oauth accounts
POST
 https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/:platform/accounts/:accountId
Attach oauth accounts
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
Example: 2021-07-28
PATH PARAMETERS
locationId
string
REQUIRED
Account Location Id
Example: w37swmmLbA02zgqKPpxITe2
platform
string
REQUIRED
Possible values: [google, facebook, instagram, linkedin, tiktok, youtube, pinterest]
Platform
Example: facebook
accountId
string
REQUIRED
Account Id
Example: w37swmmLbA02zgqKPpxITe
APPLICATION/JSON
BODY
REQUIRED
oneOf
Facebook
Instagram
Google Business Account
Pinterest
Tiktok
YouTube
Linkedin
type
string
REQUIRED
Type of Facebook account (must be page)
Possible values: [page]
Example:page
originId
string
REQUIRED
Original Facebook platform identifier
Example:244405****11687
name
string
REQUIRED
Name of the Facebook page or account
Example:JOHN_DEO
avatar
string
REQUIRED
Avatar or profile picture URL
Example:https://storage.googleapis.com/2ad21ebc23/test
Responses
201
400
401
422
Successful response - Account attached. Response structure varies by platform.
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
oneOf
Facebook
Instagram
Google Business Account
Linkedin
Tiktok
YouTube
Pinterest
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
Example:Added Facebook Account
results
object
































































Share your feedback
★
★
★
★
★
CURL
NODEJS
PYTHON
PHP
JAVA
GO
RUBY
POWERSHELL
CURL
curl -L 'https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/:platform/accounts/:accountId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-d '{
  "type": "page",
  "originId": "244405****11687",
  "name": "JOHN_DEO",
  "avatar": "https://storage.googleapis.com/2ad21ebc23/test"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Parameters
locationId — path
REQUIRED
platform — path
REQUIRED
---
google
facebook
instagram
linkedin
tiktok
youtube
pinterest
accountId — path
REQUIRED
Authorization — header
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "type": "page",
  "originId": "244405****11687",
  "name": "JOHN_DEO",
  "avatar": "https://storage.googleapis.com/2ad21ebc23/test"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!