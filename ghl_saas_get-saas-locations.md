# Get SaaS Locations

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/get-saas-locations

Screenshot: images/ghl_saas_get-saas-locations_screenshot.png

---

SaasSaasGet SaaS Locations
Get SaaS Locations
GET
 https://services.leadconnectorhq.com/saas/saas-locations/:companyId
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
QUERY PARAMETERS
page
number
REQUIRED
Responses
200
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
curl -L 'https://services.leadconnectorhq.com/saas/saas-locations/:companyId' \
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
page — query
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!