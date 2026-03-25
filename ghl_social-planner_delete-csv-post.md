# Delete CSV Post

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/delete-csv-post

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_delete-csv-post_screenshot.png

---

Social PlannerCSVDelete CSV Post
Delete CSV Post
DELETE
 https://services.leadconnectorhq.com/social-media-posting/:locationId/csv/:csvId/post/:postId
Delete a specific post from a CSV import
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
postId
string
REQUIRED
CSV Post Id
Example: 65f92e55cc884f0d0845e447
csvId
string
REQUIRED
CSV Id
Example: 65f92e55cc884f0d0845e447
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
Example:Deleted CSV Post
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/social-media-posting/:locationId/csv/:csvId/post/:postId' \
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
postId — path
REQUIRED
csvId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!