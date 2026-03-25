# Filter Users by Email

Source: https://marketplace.gohighlevel.com/docs/ghl/users/filter-users-by-email

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_users_filter-users-by-email_screenshot.png

---

UsersSearchFilter Users by Email
Filter Users by Email
POST
 https://services.leadconnectorhq.com/users/search/filter-by-email
Filter users by company ID, deleted status, and email array
Requirements
Scope(s)
users.readonly
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Agency Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
APPLICATION/JSON
BODY
REQUIRED
companyId
string
REQUIRED
Company ID to filter users
Example:5DP41231LkQsiKESj6rh
emails
string
REQUIRED
Comma-separated list of email addresses to filter users
Example:user1@example.com,user2@example.com
deleted
boolean
Filter deleted users
Default value: false
Example:false
skip
string
No of results to be skipped before returning the result
Default value: 0
Example:1
limit
string
No of results to be limited before returning the result
Default value: 25
Example:10
projection
string
Projection fields to return. Use "all" for all fields, or specify comma-separated field names. Default returns only id and email
Example:all
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
users
object[]
count
number
Example:1231




















































































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
curl -L 'https://services.leadconnectorhq.com/users/search/filter-by-email' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "companyId": "5DP41231LkQsiKESj6rh",
  "emails": "user1@example.com,user2@example.com",
  "deleted": false,
  "skip": "1",
  "limit": "10",
  "projection": "all"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "companyId": "5DP41231LkQsiKESj6rh",
  "emails": "user1@example.com,user2@example.com",
  "deleted": false,
  "skip": "1",
  "limit": "10",
  "projection": "all"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!