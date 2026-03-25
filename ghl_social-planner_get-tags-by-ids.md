# Get tags by ids

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/get-tags-by-ids

Screenshot: images/ghl_social-planner_get-tags-by-ids_screenshot.png

---

Social PlannerTagGet tags by ids
Get tags by ids
POST
 https://services.leadconnectorhq.com/social-media-posting/:locationId/tags/details
Retrieve specific tags by their IDs
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
Location Id
Example: ve9EPM428h8vShlRW1KT
APPLICATION/JSON
BODY
REQUIRED
tagIds
string[]
REQUIRED
Array of Tag Ids
Example:["65fbdcfecc884f07e645ea8b"]
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
Example:Fetched Tags by Tag IDs
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/:locationId/tags/details' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "tagIds": [
    "65fbdcfecc884f07e645ea8b"
  ]
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
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "tagIds": [
    "65fbdcfecc884f07e645ea8b"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!