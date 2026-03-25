# Get locations by stripeId with companyId

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/locations-deprecated

Screenshot: images/ghl_saas_locations-deprecated_screenshot.png

---

SaasSaasGet locations by stripeId with companyId
Get locations by stripeId with companyId
GET
 https://services.leadconnectorhq.com/saas-api/public-api/locations
DEPRECATED
This endpoint has been deprecated and may be replaced or removed in future versions of the API.
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
Stripe customer ID to find locations for
Example: cus_OD2oBjRfKEF6FV
subscriptionId
string
Stripe subscription ID to find locations for
Example: sub_1NVqlLByVlfITvRXgirIdpyc
companyId
string
REQUIRED
Company ID to filter locations
Example: 5DP4iH6HLkQsiKESj6rh
Responses
200
400
401
404
500
Locations retrieved successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
Array [
string
]

























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
curl -L 'https://services.leadconnectorhq.com/saas-api/public-api/locations' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
companyId — query
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