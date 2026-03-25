# Enable SaaS for Sub-Account (Formerly Location)

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/enable-saas-location-deprecated

Screenshot: images/ghl_saas_enable-saas-location-deprecated_screenshot.png

---

SaasSaasEnable SaaS for Sub-Account (Formerly Location)
Enable SaaS for Sub-Account (Formerly Location)
POST
 https://services.leadconnectorhq.com/saas-api/public-api/enable-saas/:locationId
DEPRECATED
This endpoint has been deprecated and may be replaced or removed in future versions of the API.
Enable SaaS for Sub-Account (Formerly Location) based on the data provided
INFO
This feature is only available on Agency Pro ($497) plan.
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
Location ID to enable SaaS for
Example: AUKAtFVo0lWezBsBQ3FE
APPLICATION/JSON
BODY
REQUIRED
stripeAccountId
string
Stripe account id(Required only for SaaS V1)
Example:acct_1QDPY5FpU9DlKp7RQ8BXfywx
name
string
Name of the stripe customer(Required only for SaaS V1)
Example:John Doe
email
string
Email of the stripe customer(Required only for SaaS V1)
Example:john.doe@example.com
stripeCustomerId
string
Stripe customer id if exists(Required only for SaaS V1)
Example:cus_1QDPY5FpU9DlKp7RQ8BXfywx
companyId
string
REQUIRED
isSaaSV2
boolean
REQUIRED
Denotes if it is a saas v2 or v1 sub-account
Example:true
contactId
string
Agency subaccount used for payment provider integration(Required Only for SaaS V2)
Example:1QDPY5FpU9DlKp7RQ8BXfywx
providerLocationId
string
Agency Subaccount ID
Example:r06mdj4OrrERzYDvsOdh
description
string
Description
Example:Description
saasPlanId
string
Required only while pre-configuring saas subscription
Example:1QDPY5FpU9DlKp7RQ8BXfywx
priceId
string
Required only while pre-configuring saas subscription
Example:price_1QDPY5FpU9DlKp7RQ8BXfywx
Responses
200
400
401
404
500
SaaS enabled successfully for location
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
data
object
REQUIRED
Response data from the enable SaaS operation
Example:{"customer_id":"cus_1QDPY5FpU9DlKp7RQ8BXfywx","ok":true,"paymentMethodAdded":true}





























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
curl -L 'https://services.leadconnectorhq.com/saas-api/public-api/enable-saas/:locationId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "stripeAccountId": "acct_1QDPY5FpU9DlKp7RQ8BXfywx",
  "name": "John Doe",
  "email": "john.doe@example.com",
  "stripeCustomerId": "cus_1QDPY5FpU9DlKp7RQ8BXfywx",
  "companyId": "string",
  "isSaaSV2": true,
  "contactId": "1QDPY5FpU9DlKp7RQ8BXfywx",
  "providerLocationId": "r06mdj4OrrERzYDvsOdh",
  "description": "Description",
  "saasPlanId": "1QDPY5FpU9DlKp7RQ8BXfywx",
  "priceId": "price_1QDPY5FpU9DlKp7RQ8BXfywx"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "stripeAccountId": "acct_1QDPY5FpU9DlKp7RQ8BXfywx",
  "name": "John Doe",
  "email": "john.doe@example.com",
  "stripeCustomerId": "cus_1QDPY5FpU9DlKp7RQ8BXfywx",
  "companyId": "string",
  "isSaaSV2": true,
  "contactId": "1QDPY5FpU9DlKp7RQ8BXfywx",
  "providerLocationId": "r06mdj4OrrERzYDvsOdh",
  "description": "Description",
  "saasPlanId": "1QDPY5FpU9DlKp7RQ8BXfywx",
  "priceId": "price_1QDPY5FpU9DlKp7RQ8BXfywx"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!