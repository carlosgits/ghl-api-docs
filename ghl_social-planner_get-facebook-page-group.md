# Get facebook pages

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/get-facebook-page-group

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_get-facebook-page-group_screenshot.png

---

Social PlannerOauth | FacebookGet facebook pages
Get facebook pages
GET
 https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/facebook/accounts/:accountId
Get facebook pages
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
QUERY PARAMETERS
search
string
Search term for filtering accounts/pages
Example: page name
Responses
200
400
401
422
Successful response, runs Facebook OAuth and redirects to application
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
Example:Fetched Facebook Account
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/facebook/accounts/:accountId' \
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
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!