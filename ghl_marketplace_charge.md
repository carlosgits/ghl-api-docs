# Create a new wallet charge

Source: https://marketplace.gohighlevel.com/docs/ghl/marketplace/charge

Screenshot: images/ghl_marketplace_charge_screenshot.png

---

Developer marketplaceWallet ChargesCreate a new wallet charge
Create a new wallet charge
POST
 https://services.leadconnectorhq.com/marketplace/billing/charges
Create a new wallet charge
Requirements
Scope(s)
charges.write
Auth Method(s)
OAuth Access Token
Token Type(s)
Sub-Account Token
Request
APPLICATION/JSON
BODY
REQUIRED
appId
string
REQUIRED
App ID of the App
meterId
string
REQUIRED
Billing Meter ID (you can find this on your app's pricing page)
eventId
string
REQUIRED
Event ID / Transaction ID on your server's side. This will help you maintain the reference of the event/transaction on your end that you charged the customer for.
userId
string
User ID
locationId
string
REQUIRED
ID of the Sub-Account to be charged
companyId
string
REQUIRED
ID of the Agency the Sub-account belongs to
description
string
REQUIRED
Description of the charge
price
number
Price per unit to charge
units
number
REQUIRED
Number of units to charge
eventTime
string
The timestamp when the event/transaction was performed. If blank, the billing timestamp will be set as the event time. ISO8601 Format.
Example:2025-03-26T00:00:000Z
Responses
201
400
422
Charge created successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
Example:true
chargeId
string
Example:charge_123















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
curl -L 'https://services.leadconnectorhq.com/marketplace/billing/charges' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "appId": "string",
  "meterId": "string",
  "eventId": "string",
  "userId": "string",
  "locationId": "string",
  "companyId": "string",
  "description": "string",
  "price": 0,
  "units": 0,
  "eventTime": "2025-03-26T00:00:000Z"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Body
 REQUIRED
{
  "appId": "string",
  "meterId": "string",
  "eventId": "string",
  "userId": "string",
  "locationId": "string",
  "companyId": "string",
  "description": "string",
  "price": 0,
  "units": 0,
  "eventTime": "2025-03-26T00:00:000Z"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!