# Attach Twitter profile

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/attach-twitter-profile

Screenshot: images/ghl_social-planner_attach-twitter-profile_screenshot.png

---

Social PlannerOauth | TwitterAttach Twitter profile
Attach Twitter profile
POST
 https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/twitter/accounts/:accountId
DEPRECATED
This endpoint has been deprecated and may be replaced or removed in future versions of the API.
As of December 4, 2024, X (formerly Twitter) is no longer supported. We apologise for any inconvenience.
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
Original Twitter platform identifier
Example:244405****11687
name
string
Name of the Twitter account
Example:JOHN_DEO
username
string
Username or handle of the Twitter account
Example:user_name
avatar
string
Avatar or profile picture URL
Example:https://storage.googleapis.com/2ad21ebc23/test
protected
boolean
Indicates if the Twitter account is protected (private)
Example:true
verified
boolean
Indicates if the Twitter account is verified
Example:true
companyId
string
Company ID
Example:sdfdsfdsfEWEsdfsdsW32dd
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
Example:Added Twitter Account
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/twitter/accounts/:accountId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-d '{
  "originId": "244405****11687",
  "name": "JOHN_DEO",
  "username": "user_name",
  "avatar": "https://storage.googleapis.com/2ad21ebc23/test",
  "protected": true,
  "verified": true,
  "companyId": "sdfdsfdsfEWEsdfsdsW32dd"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
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
  "username": "user_name",
  "avatar": "https://storage.googleapis.com/2ad21ebc23/test",
  "protected": true,
  "verified": true,
  "companyId": "sdfdsfdsfEWEsdfsdsW32dd"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!