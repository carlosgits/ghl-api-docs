# Update Location Wallet Balance

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/update-location-wallet-balance

Screenshot: images/ghl_saas_update-location-wallet-balance_screenshot.png

---

SaasSaasUpdate Location Wallet Balance
Update Location Wallet Balance
POST
 https://services.leadconnectorhq.com/saas-api/public-api/companies/:companyId/locations/:locationId/wallet-balance/complimentary-credits
Update the wallet balance or complimentary credit settings for a specific location. Supports partial updates via updateMask field (AIP-134 compliant).
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
Company ID that owns the location
Example: 5DP4iH6HLkQsiKESj6rh
locationId
string
REQUIRED
Location ID to update wallet balance for
Example: AUKAtFVo0lWezBsBQ3FE
APPLICATION/JSON
BODY
REQUIRED
complimentaryCreditsAmount
number
Credit amount to be added
Example:100
Responses
200
400
401
404
500
Location wallet balance updated successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
walletId
string
REQUIRED
Wallet Id
Example:xyz789
balance
number
REQUIRED
Current wallet balance
Example:1500.5
complimentaryCredits
number
REQUIRED
Complimentary credits amount
Example:100



























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
curl -L 'https://services.leadconnectorhq.com/saas-api/public-api/companies/:companyId/locations/:locationId/wallet-balance/complimentary-credits' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "complimentaryCreditsAmount": 100
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
locationId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "complimentaryCreditsAmount": 100
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!