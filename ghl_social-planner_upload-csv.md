# Upload CSV

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/upload-csv

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_upload-csv_screenshot.png

---

Social PlannerCSVUpload CSV
Upload CSV
POST
 https://services.leadconnectorhq.com/social-media-posting/:locationId/csv
Upload a CSV file containing social media posts for bulk scheduling
Requirements
Scope(s)
socialplanner/csv.write
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
MULTIPART/FORM-DATA
BODY
REQUIRED
file
binary
REQUIRED
CSV file to upload containing social media posts
Example:sample.csv
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
Example:Uploaded CSV
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
curl -L -X POST 'https://services.leadconnectorhq.com/social-media-posting/:locationId/csv' \
-H 'Content-Type: multipart/form-data' \
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
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
file
REQUIRED
CSV file to upload containing social media posts
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!