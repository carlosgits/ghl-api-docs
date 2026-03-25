# Get Tiktok Business profile

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/get-tiktok-business-profile

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_get-tiktok-business-profile_screenshot.png

---

Social PlannerOauth | TiktokGet Tiktok Business profile
Get Tiktok Business profile
GET
 https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/tiktok-business/accounts/:accountId
Get Tiktok Business profile
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
Example:201
message
string
REQUIRED
Message
Example:Fetched Tiktok Business Account
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/tiktok-business/accounts/:accountId' \
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
accountId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!