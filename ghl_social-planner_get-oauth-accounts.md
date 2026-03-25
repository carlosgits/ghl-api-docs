# Get oauth accounts

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/get-oauth-accounts

Screenshot: images/ghl_social-planner_get-oauth-accounts_screenshot.png

---

Social PlannerOAuth | GenericGet oauth accounts
Get oauth accounts
GET
 https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/:platform/accounts/:accountId
Get oauth accounts
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
Possible values: [google, facebook, instagram, linkedin, tiktok, tiktok-business, youtube, pinterest]
Platform
Example: facebook
accountId
string
REQUIRED
Account Id
Example: w37swmmLbA02zgqKPpxITe
Responses
200
400
401
422
Successful response, runs OAuth and returns accounts. Response structure varies by platform.
APPLICATION/JSON
Schema
Example (auto)
facebook
instagram
google
SCHEMA
oneOf
Facebook
Instagram
Google Business Account
Linkedin
Tiktok
Tiktok Business
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
Example:200
message
string
REQUIRED
Message
Example:Fetched Facebook Account
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
-H 'Accept: application/json'
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
tiktok-business
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
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!