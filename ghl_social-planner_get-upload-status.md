# Get Upload Status

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/get-upload-status

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_get-upload-status_screenshot.png

---

Social PlannerCSVGet Upload Status
Get Upload Status
GET
 https://services.leadconnectorhq.com/social-media-posting/:locationId/csv
Get the status of all CSV imports for a location
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
QUERY PARAMETERS
skip
string
Number of records to skip
Default value:0
Example: 1
limit
string
Maximum number of records to return
Default value:10
Example: 10
includeUsers
string
Include user data in response
Example: true
isFromTemplate
string
Filter CSVs imported from template library
Example: true
userId
string
REQUIRED
User ID
Example: sdfdsfdsfEWEsdfsdsW32dd
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
Example:Fetched CSV Upload Status
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/:locationId/csv' \
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
userId — query
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