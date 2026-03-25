# Search

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/search-locations

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_locations_search-locations_screenshot.png

---

Sub-Account (Formerly location)SearchSearch
Search
GET
 https://services.leadconnectorhq.com/locations/search
Search Sub-Account (Formerly Location)
Requirements
Scope(s)
locations.readonly
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Agency Token
Sub-Account Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
QUERY PARAMETERS
companyId
string
The company/agency id on which you want to perform the search
Example: 5DP4iH6HLkQsiKESj6rh
skip
string
The value by which the results should be skipped. Default will be 0
Default value:0
Example: 1
limit
string
The value by which the results should be limited. Default will be 10
Default value:10
Example: 10
order
string
The order in which the results should be returned - Allowed values asc, desc. Default will be asc
Default value:asc
Example: asc
email
string
Example: johndoe@mail.com
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
locations
object[]




















































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
curl -L 'https://services.leadconnectorhq.com/locations/search' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Security Scheme
Agency-Access
Location-Access
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