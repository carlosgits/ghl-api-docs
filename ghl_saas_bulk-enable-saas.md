# Bulk Enable SaaS

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/bulk-enable-saas

Screenshot: images/ghl_saas_bulk-enable-saas_screenshot.png

---

SaasSaasBulk Enable SaaS
Bulk Enable SaaS
POST
 https://services.leadconnectorhq.com/saas/bulk-enable-saas/:companyId
Enable SaaS mode for multiple locations with support for both SaaS v1 and v2
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
APPLICATION/JSON
BODY
REQUIRED
locationIds
string[]
REQUIRED
Array of location IDs to enable SaaS for
Example:["locationId1","locationId2"]
isSaaSV2
boolean
REQUIRED
Indicates if the SaaS is V2
Example:true
actionPayload
object
Responses
201
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
curl -L 'https://services.leadconnectorhq.com/saas/bulk-enable-saas/:companyId' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationIds": [
    "locationId1",
    "locationId2"
  ],
  "isSaaSV2": true,
  "actionPayload": {
    "priceId": "price_1QDPY5FpU9DlKp7RQ8BXfywx",
    "stripeAccountId": "acct_1QDPY5FpU9DlKp7RQ8BXfywx",
    "saasPlanId": "66c4d36534f21f900dc2a265",
    "providerLocationId": "r06mdj4OrrERzYDvsOdh"
  }
}'
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
Body
 REQUIRED
{
  "locationIds": [
    "locationId1",
    "locationId2"
  ],
  "isSaaSV2": true,
  "actionPayload": {
    "priceId": "price_1QDPY5FpU9DlKp7RQ8BXfywx",
    "stripeAccountId": "acct_1QDPY5FpU9DlKp7RQ8BXfywx",
    "saasPlanId": "66c4d36534f21f900dc2a265",
    "providerLocationId": "r06mdj4OrrERzYDvsOdh"
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!