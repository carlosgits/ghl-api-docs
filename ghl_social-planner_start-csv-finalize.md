# Start CSV Finalize

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/start-csv-finalize

Screenshot: images/ghl_social-planner_start-csv-finalize_screenshot.png

---

Social PlannerCSVStart CSV Finalize
Start CSV Finalize
PATCH
 https://services.leadconnectorhq.com/social-media-posting/:locationId/csv/:id
Finalize a CSV import and schedule all posts for publishing
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
id
string
REQUIRED
CSV Id
Example: 65f92e55cc884f0d0845e447
APPLICATION/JSON
BODY
REQUIRED
userId
string
REQUIRED
User ID
Example:sdfdsfdsfEWEsdfsdsW32dd
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
Example:Updated Successfully





















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
curl -L -X PATCH 'https://services.leadconnectorhq.com/social-media-posting/:locationId/csv/:id' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "userId": "sdfdsfdsfEWEsdfsdsW32dd"
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
id — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "userId": "sdfdsfdsfEWEsdfsdsW32dd"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!