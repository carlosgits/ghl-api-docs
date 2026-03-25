# Get locations by stripeId with companyId

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/locations

Screenshot: images/ghl_saas_locations_screenshot.png

---

SaasSaasGet locations by stripeId with companyId
Get locations by stripeId with companyId
GET
 https://services.leadconnectorhq.com/saas/locations
Get locations by stripeCustomerId or stripeSubscriptionId with companyId
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
QUERY PARAMETERS
customerId
string
REQUIRED
subscriptionId
string
REQUIRED
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
curl -L 'https://services.leadconnectorhq.com/saas/locations' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
customerId — query
REQUIRED
subscriptionId — query
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