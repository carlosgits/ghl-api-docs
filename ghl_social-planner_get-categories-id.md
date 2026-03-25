# Get categories by id

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/get-categories-id

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_get-categories-id_screenshot.png

---

Social PlannerCategoryGet categories by id
Get categories by id
GET
 https://services.leadconnectorhq.com/social-media-posting/:locationId/categories/:id
Retrieve a specific category by its ID
Requirements
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
HEADER PARAMETERS
Authorization
string
REQUIRED
Access Token
Example: Bearer 9c48df2694a849b6089f9d0d3513efe
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
Example: 2021-07-28
PATH PARAMETERS
id
string
REQUIRED
Category Id
Example: 6284c43d519161e96cc09c13
locationId
string
REQUIRED
Location Id
Example: 6284c43d519161e96cc09c13
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
Example:Fetched Category
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/:locationId/categories/:id' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
id — path
REQUIRED
locationId — path
REQUIRED
Authorization — header
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!