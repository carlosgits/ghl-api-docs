# Get lost reason

Source: https://marketplace.gohighlevel.com/docs/ghl/opportunities/get-lost-reason

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_opportunities_get-lost-reason_screenshot.png

---

OpportunitiesLost reasonGet lost reason
Get lost reason
GET
 https://services.leadconnectorhq.com/opportunities/lost-reason
Get lost reason
Requirements
Scope(s)
opportunities.readonly
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
QUERY PARAMETERS
locationId
string
REQUIRED
Example: ve9EPM428h8vShlRW1KT
name
string
lost reason name
Example: lost reason
deleted
boolean
deleted
Default value:false
query
string
search query
Example: dentist
skip
number
skip
Default value:0
Example: 1
limit
number
limit
Default value:100
Example: 10
getCount
boolean
get count
Example: field
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
lostReasons
object[]
total
number
Example:100




























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
curl -L 'https://services.leadconnectorhq.com/opportunities/lost-reason' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — query
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