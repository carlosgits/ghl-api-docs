# Set Accounts

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/set-accounts

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_set-accounts_screenshot.png

---

Social PlannerCSVSet Accounts
Set Accounts
POST
 https://services.leadconnectorhq.com/social-media-posting/:locationId/set-accounts
Set social media accounts for a CSV import to publish posts to
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
APPLICATION/JSON
BODY
REQUIRED
accountIds
string[]
REQUIRED
Account Ids
Example:["aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"]
filePath
string
REQUIRED
File path
Example:omaDY3RbWtTP511e/social-import/d23d68c2-82c0-1db6e2.csv
rowsCount
number
REQUIRED
Entries Count. rowsCount must be between 1 and number of posts in CSV
Example:1
fileName
string
REQUIRED
Name of file
Example:test.csv
approver
string
Approver User Id
Example:o6241QsiRwUIJHyjuhos
userId
string
REQUIRED
User ID
Example:ve9EPM428h8vShlRW1KT
csvFileType
string
CSV file type - determines the format of the CSV file being imported
Possible values: [basic, advance]
Example:basic
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
Example:Accounts Set Successfully
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/:locationId/set-accounts' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "accountIds": [
    "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"
  ],
  "filePath": "omaDY3RbWtTP511e/social-import/d23d68c2-82c0-1db6e2.csv",
  "rowsCount": 1,
  "fileName": "test.csv",
  "approver": "o6241QsiRwUIJHyjuhos",
  "userId": "ve9EPM428h8vShlRW1KT",
  "csvFileType": "basic"
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
  "accountIds": [
    "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"
  ],
  "filePath": "omaDY3RbWtTP511e/social-import/d23d68c2-82c0-1db6e2.csv",
  "rowsCount": 1,
  "fileName": "test.csv",
  "approver": "o6241QsiRwUIJHyjuhos",
  "userId": "ve9EPM428h8vShlRW1KT",
  "csvFileType": "basic"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!