# Create new integration

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/create-integration

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_payments_create-integration_screenshot.png

---

PaymentsCustom ProviderCreate new integration
Create new integration
POST
 https://services.leadconnectorhq.com/payments/custom-provider/provider
API to create a new association for an app and location
Requirements
Scope(s)
payments/custom-provider.write
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
QUERY PARAMETERS
locationId
string
REQUIRED
Location id
Example: Lk3nlfk4lxlelVEwcW
APPLICATION/JSON
BODY
REQUIRED
name
string
REQUIRED
The name of the custom provider
Example:Company Paypal Integration
description
string
REQUIRED
Description of payment gateway. Shown on the payments integrations page as subtext
Example:This payment gateway supports payments in India via UPI, Net banking, cards and wallets.
paymentsUrl
string
REQUIRED
This url will be loaded in iFrame to start a payment session.
Example:https://testpayment.paypal.com
queryUrl
string
REQUIRED
The url used for querying payments related events. Ex. verify, refund, subscription etc.
Example:https://testsubscription.paypal.com
imageUrl
string
REQUIRED
Public image url for logo of the payment gateway displayed on the payments integrations page.
Example:https://testsubscription.paypal.com
supportsSubscriptionSchedule
boolean
REQUIRED
Whether the config supports subscription schedule or not. true represents config supports subscription schedule
Example:true
Responses
200
400
401
422
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
name
string
REQUIRED
The name of the custom provider
Example:Company Paypal Integration
description
string
REQUIRED
Description of payment gateway. Shown on the payments integrations page as subtext
Example:This payment gateway supports payments in India via UPI, Net banking, cards and wallets.
paymentsUrl
string
REQUIRED
This url will be loaded in iFrame to start a payment session.
Example:https://testpayment.paypal.com
queryUrl
string
REQUIRED
The url used for querying payments related events. Ex. verify, refund, subscription etc.
Example:https://testsubscription.paypal.com
imageUrl
string
REQUIRED
Public image url for logo of the payment gateway displayed on the payments integrations page.
Example:https://testsubscription.paypal.com
_id
string
REQUIRED
The unique identifier for the custom provider.
Example:662a44ad19a2a44d3cd9d749
locationId
string
REQUIRED
Location id
Example:Lk3nlfk4lxlelVEwcW
marketplaceAppId
string
REQUIRED
The application id of marketplace
Example:65f0b217a05c774da7f1efa5
paymentProvider
object
Payment provider details.
Example:{ live: { liveMode: true }, test: { liveMode: false, apiKey: "y5ZQxryRFXZHvUJZdLXXXXXX", publishableKey: "rzp_test_zPRoVMLOa0A9wo" }}
deleted
boolean
REQUIRED
Whether the config is deleted or not. true represents config is deleted
Example:true
createdAt
date-time
REQUIRED
The creation timestamp of the custom provider.
Example:2023-11-20T10:23:36.515Z
updatedAt
date-time
REQUIRED
The last update timestamp of the custom provider.
Example:2024-01-23T09:57:04.846Z
traceId
string
Trace id of the custom provider.
Example:302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a































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
curl -L 'https://services.leadconnectorhq.com/payments/custom-provider/provider' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "name": "Company Paypal Integration",
  "description": "This payment gateway supports payments in India via UPI, Net banking, cards and wallets.",
  "paymentsUrl": "https://testpayment.paypal.com",
  "queryUrl": "https://testsubscription.paypal.com",
  "imageUrl": "https://testsubscription.paypal.com",
  "supportsSubscriptionSchedule": true
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "name": "Company Paypal Integration",
  "description": "This payment gateway supports payments in India via UPI, Net banking, cards and wallets.",
  "paymentsUrl": "https://testpayment.paypal.com",
  "queryUrl": "https://testsubscription.paypal.com",
  "imageUrl": "https://testsubscription.paypal.com",
  "supportsSubscriptionSchedule": true
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!