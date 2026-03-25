# Get Location Subscription Details

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/get-location-subscription-deprecated

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_saas_get-location-subscription-deprecated_screenshot.png

---

SaasSaasGet Location Subscription Details
Get Location Subscription Details
GET
 https://services.leadconnectorhq.com/saas-api/public-api/get-saas-subscription/:locationId
DEPRECATED
This endpoint has been deprecated and may be replaced or removed in future versions of the API.
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
Location ID to get subscription details for
Example: AUKAtFVo0lWezBsBQ3FE
QUERY PARAMETERS
companyId
string
REQUIRED
Company ID to filter subscription details
Example: 5DP4iH6HLkQsiKESj6rh
Responses
200
400
401
404
500
Location subscription details retrieved successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
locationId
string
REQUIRED
Location ID
Example:locationId1
isSaaSV2
boolean
REQUIRED
Indicates if the SaaS is V2
Example:true
companyId
string
REQUIRED
Company ID
Example:companyId1
saasMode
string
SaaS mode
Example:saasV2
subscriptionId
string
Subscription ID
Example:subscriptionId1
customerId
string
Customer ID
Example:customerId1
productId
string
Product ID
Example:productId1
priceId
string
Price ID
Example:priceId1
saasPlanId
string
SaaS plan ID
Example:saasPlanId1
subscriptionStatus
string
Subscription status
Example:active


































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
curl -L 'https://services.leadconnectorhq.com/saas-api/public-api/get-saas-subscription/:locationId' \
-H 'Accept: application/json' \
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