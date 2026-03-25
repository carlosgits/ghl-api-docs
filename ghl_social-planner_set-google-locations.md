# Set google business locations

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/set-google-locations

Screenshot: images/ghl_social-planner_set-google-locations_screenshot.png

---

Social PlannerOauth | GoogleSet google business locations
Set google business locations
POST
 https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/google/locations/:accountId
Set google business locations
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
location
object
account
object
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
Example:Added Google Business Account
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/google/locations/:accountId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "location": {
    "name": "string",
    "storeCode": "string",
    "title": "string",
    "storefrontAddress": {},
    "metadata": {},
    "maxLocation": true,
    "isVerified": true,
    "isConnected": true
  },
  "account": {
    "name": "string",
    "accountName": "string",
    "type": "string",
    "verificationState": "string",
    "vettedState": "string"
  }
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
  "location": {
    "name": "string",
    "storeCode": "string",
    "title": "string",
    "storefrontAddress": {},
    "metadata": {},
    "maxLocation": true,
    "isVerified": true,
    "isConnected": true
  },
  "account": {
    "name": "string",
    "accountName": "string",
    "type": "string",
    "verificationState": "string",
    "vettedState": "string"
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!