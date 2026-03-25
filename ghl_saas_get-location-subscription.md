# Get Location Subscription Details

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/get-location-subscription

Screenshot: images/ghl_saas_get-location-subscription_screenshot.png

---

SaasSaasGet Location Subscription Details
Get Location Subscription Details
GET
 https://services.leadconnectorhq.com/saas/get-saas-subscription/:locationId
Fetch subscription details for a specific location from location metadata
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
locationId
string
REQUIRED
QUERY PARAMETERS
companyId
string
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
curl -L 'https://services.leadconnectorhq.com/saas/get-saas-subscription/:locationId' \
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
companyId — query
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!