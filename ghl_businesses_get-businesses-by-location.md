# Get Businesses by Location

Source: https://marketplace.gohighlevel.com/docs/ghl/businesses/get-businesses-by-location

Screenshot: images/ghl_businesses_get-businesses-by-location_screenshot.png

---

BusinessBusinessesGet Businesses by Location
Get Businesses by Location
GET
 https://services.leadconnectorhq.com/businesses/
Get Businesses by Location
Requirements
Scope(s)
businesses.readonly
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
Example: 5DP4iH6HLkQsiKESj6rh
limit
string
Default value:100
Example: 100
skip
string
Default value:0
Example: 10
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
businesses
object[]
REQUIRED































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
curl -L 'https://services.leadconnectorhq.com/businesses/' \
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