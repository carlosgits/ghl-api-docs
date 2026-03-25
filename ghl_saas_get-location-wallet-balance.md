# Get Location Wallet Balance

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/get-location-wallet-balance

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_saas_get-location-wallet-balance_screenshot.png

---

SaasSaasGet Location Wallet Balance
Get Location Wallet Balance
GET
 https://services.leadconnectorhq.com/saas-api/public-api/companies/:companyId/locations/:locationId/wallet-balance
Fetch the wallet balance for a specific location. Returns a resource object with balance details.
Requirements
Scope(s)
saas/location.complimentaryCredit.read
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
Location ID to get wallet balance for
Example: AUKAtFVo0lWezBsBQ3FE
Responses
200
400
401
404
500
Location wallet balance retrieved successfully
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
curl -L 'https://services.leadconnectorhq.com/saas-api/public-api/companies/:companyId/locations/:locationId/wallet-balance' \
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
locationId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!