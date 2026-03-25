# Delete a wallet charge

Source: https://marketplace.gohighlevel.com/docs/ghl/marketplace/delete-charge

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_marketplace_delete-charge_screenshot.png

---

Developer marketplaceWallet ChargesDelete a wallet charge
Delete a wallet charge
DELETE
 https://services.leadconnectorhq.com/marketplace/billing/charges/:chargeId
Delete a wallet charge
Requirements
Scope(s)
charges.write
Auth Method(s)
OAuth Access Token
Token Type(s)
Sub-Account Token
Request
PATH PARAMETERS
chargeId
string
REQUIRED
ID of the charge to delete
Responses
200
404
422
Charge deleted successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/marketplace/billing/charges/:chargeId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
chargeId — path
REQUIRED
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!