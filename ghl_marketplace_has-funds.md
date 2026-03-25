# Check if account has sufficient funds

Source: https://marketplace.gohighlevel.com/docs/ghl/marketplace/has-funds

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_marketplace_has-funds_screenshot.png

---

Developer marketplaceWallet ChargesCheck if account has sufficient funds
Check if account has sufficient funds
GET
 https://services.leadconnectorhq.com/marketplace/billing/charges/has-funds
Check if account has sufficient funds
Requirements
Scope(s)
charges.readonly
Auth Method(s)
OAuth Access Token
Token Type(s)
Sub-Account Token
Request
Responses
200
422
Returns fund availability status
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
hasFunds
boolean
Example:true










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
curl -L 'https://services.leadconnectorhq.com/marketplace/billing/charges/has-funds' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!