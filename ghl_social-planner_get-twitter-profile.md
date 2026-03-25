# Get Twitter profile

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/get-twitter-profile

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_get-twitter-profile_screenshot.png

---

Social PlannerOauth | TwitterGet Twitter profile
Get Twitter profile
GET
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
Example:Fetched Twitter Account
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
-H 'Accept: application/json'
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
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!