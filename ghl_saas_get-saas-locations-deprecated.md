# Get SaaS Locations

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/get-saas-locations-deprecated

Screenshot: images/ghl_saas_get-saas-locations-deprecated_screenshot.png

---

SaasSaasGet SaaS Locations
Get SaaS Locations
GET
 https://services.leadconnectorhq.com/saas-api/public-api/saas-locations/:companyId
DEPRECATED
This endpoint has been deprecated and may be replaced or removed in future versions of the API.
Fetch all SaaS-activated locations for a company with pagination
Requirements
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
Possible values: [2021-04-15]
API Version
PATH PARAMETERS
companyId
string
REQUIRED
Company ID to get SaaS locations for
Example: 5DP4iH6HLkQsiKESj6rh
QUERY PARAMETERS
page
number
Page number for pagination
Example: 1
Responses
200
400
401
404
500
SaaS locations retrieved successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
locations
object[]
REQUIRED
pagination
object
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
curl -L 'https://services.leadconnectorhq.com/saas-api/public-api/saas-locations/:companyId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
companyId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!