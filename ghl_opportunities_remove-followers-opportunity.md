# Remove Followers

Source: https://marketplace.gohighlevel.com/docs/ghl/opportunities/remove-followers-opportunity

Screenshot: images/ghl_opportunities_remove-followers-opportunity_screenshot.png

---

OpportunitiesFollowersRemove Followers
Remove Followers
DELETE
 https://services.leadconnectorhq.com/opportunities/:id/followers
Allows removal of one or all followers from an opportunity.
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
QUERY PARAMETERS
isRemoveAllFollowers
boolean
APPLICATION/JSON
BODY
REQUIRED
followers
string[]
REQUIRED
Example:["sx6wyHhbFdRXh302Lunr","sx6wyHhbFdRXh302Lunr"]
Responses
200
400
401
422
Followers successfully removed.
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
followers
string[]
Example:["sx6wyHhbFdRXh302Lunr","sx6wyHhbFdRXh302LLss"]
followersRemoved
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/opportunities/:id/followers' \
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
Show optional parameters
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