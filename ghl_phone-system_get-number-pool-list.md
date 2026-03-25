# List Number Pools

Source: https://marketplace.gohighlevel.com/docs/ghl/phone-system/get-number-pool-list

Screenshot: images/ghl_phone-system_get-number-pool-list_screenshot.png

---

Phone SystemNumber PoolsList Number Pools
List Number Pools
GET
 https://services.leadconnectorhq.com/phone-system/number-pools
Get list of number pools
Requirements
Scope(s)
numberpools.read
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
Location ID to filter pools
Example: ve9EPM428h8vShlRW1KT
Responses
200
400
401
403
Successfully retrieved number pools list
APPLICATION/JSON
Schema
Example (auto)
successful-response
SCHEMA
success
boolean
Indicates if the request was successful
Example:true
data
object[]
total
number
Total number of pools returned
Example:5

























































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
curl -L 'https://services.leadconnectorhq.com/phone-system/number-pools' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!