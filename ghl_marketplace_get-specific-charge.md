# Get specific wallet charge details

Source: https://marketplace.gohighlevel.com/docs/ghl/marketplace/get-specific-charge

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_marketplace_get-specific-charge_screenshot.png

---

Developer marketplaceWallet ChargesGet specific wallet charge details
Get specific wallet charge details
GET
 https://services.leadconnectorhq.com/marketplace/billing/charges/:chargeId
Get specific wallet charge details
Requirements
Scope(s)
charges.readonly
Auth Method(s)
OAuth Access Token
Token Type(s)
Sub-Account Token
Request
PATH PARAMETERS
chargeId
string
REQUIRED
ID of the charge to retrieve
Responses
200
404
422
Returns charge details
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
refunded
boolean
Value is 'true' if the charge has subsequently been refunded.
currency
string
Currency of the transaction. We currently support USD only.
appId
string
App ID
meterId
string
Billing Meter ID (you can find this on your app's pricing page)
chargeId
string
Charge ID
entityType
string
Indicates who was charged? Currently, we support charges for 'location' only
entityId
string
If the entityType is Location, entityld would be locationld.
amountCharged
number
Total amount charged
pricePerUnit
number
Price per unit for the charge
transactionType
string
This can be one of two values - 'charge' or 'refund'
units
number
Number of units that the sub-account was charged for
meta
object
meta object contains details that were sent while creating the charge via the API - eventID, description, eventTime, userld
createdAt
date-time
Timestamp when the charge was created in our system
updatedAt
date-time
Timestamp when the charge was last updated in our system



























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
curl -L 'https://services.leadconnectorhq.com/marketplace/billing/charges/:chargeId' \
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