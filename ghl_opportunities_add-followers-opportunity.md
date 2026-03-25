# Add Followers

Source: https://marketplace.gohighlevel.com/docs/ghl/opportunities/add-followers-opportunity

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_opportunities_add-followers-opportunity_screenshot.png

---

OpportunitiesFollowersAdd Followers
Add Followers
POST
 https://services.leadconnectorhq.com/opportunities/:id/followers
Add Followers
Requirements
Scope(s)
opportunities.write
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
PATH PARAMETERS
id
string
REQUIRED
Opportunity Id
Example: sx6wyHhbFdRXh302Lunr
APPLICATION/JSON
BODY
REQUIRED
followers
string[]
REQUIRED
Example:["sx6wyHhbFdRXh302Lunr","sx6wyHhbFdRXh302Lunr"]
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
followers
string[]
Example:["sx6wyHhbFdRXh302Lunr","sx6wyHhbFdRXh302LLss"]
followersAdded
string[]
Example:["Mx6wyHhbFdRXh302Luer","Ka6wyHhbFdRXh302LLsAm"]


























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
curl -L 'https://services.leadconnectorhq.com/opportunities/:id/followers' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "followers": [
    "sx6wyHhbFdRXh302Lunr",
    "sx6wyHhbFdRXh302Lunr"
  ]
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
id — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "followers": [
    "sx6wyHhbFdRXh302Lunr",
    "sx6wyHhbFdRXh302Lunr"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!