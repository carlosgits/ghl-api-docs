# Attach linkedin pages and profile

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/attach-linkedin-page-profile

Screenshot: images/ghl_social-planner_attach-linkedin-page-profile_screenshot.png

---

Social PlannerOauth | LinkedInAttach linkedin pages and profile
Attach linkedin pages and profile
POST
 https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/linkedin/accounts/:accountId
Attach linkedin pages and profile
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
Type of LinkedIn account (must be one of: page, profile)
Possible values: [page, group, profile, location, business]
Example:page
originId
string
REQUIRED
Original LinkedIn platform identifier
Example:244405****11687
name
string
REQUIRED
Name of the LinkedIn page or profile
Example:JOHN_DEO
avatar
string
REQUIRED
Avatar or profile picture URL
Example:https://storage.googleapis.com/2ad21ebc23/test
urn
string
REQUIRED
LinkedIn URN (Uniform Resource Name) identifier
Example:urn:li:organization:80847980
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
Example:200
message
string
REQUIRED
Message
Example:Added LinkedIn Account
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/linkedin/accounts/:accountId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "type": "page",
  "originId": "244405****11687",
  "name": "JOHN_DEO",
  "avatar": "https://storage.googleapis.com/2ad21ebc23/test",
  "urn": "urn:li:organization:80847980"
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
  "type": "page",
  "originId": "244405****11687",
  "name": "JOHN_DEO",
  "avatar": "https://storage.googleapis.com/2ad21ebc23/test",
  "urn": "urn:li:organization:80847980"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!