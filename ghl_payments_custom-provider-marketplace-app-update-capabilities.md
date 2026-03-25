# Custom-provider marketplace app update capabilities

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/custom-provider-marketplace-app-update-capabilities

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_payments_custom-provider-marketplace-app-update-capabilities_screenshot.png

---

PaymentsCustom ProviderCustom-provider marketplace app update capabilities
Custom-provider marketplace app update capabilities
PUT
 https://services.leadconnectorhq.com/payments/custom-provider/capabilities
Toggle capabilities for the marketplace app tied to the OAuth client
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
APPLICATION/JSON
BODY
REQUIRED
supportsSubscriptionSchedules
boolean
REQUIRED
Whether the marketplace app supports subscription schedules or not
Example:true
companyId
string
Company id. Mandatory if locationId is not provided
Example:Yjnwuduw83e8x30sm0
locationId
string
Location / Sub-account id. Mandatory if companyId is not provided
Example:Yjnwuduw83e8x30sm0
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
success
boolean
REQUIRED
Whether the custom provider capabilities are updated or not. true represents capabilities are updated
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
curl -L -X PUT 'https://services.leadconnectorhq.com/payments/custom-provider/capabilities' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "supportsSubscriptionSchedules": true,
  "companyId": "Yjnwuduw83e8x30sm0",
  "locationId": "Yjnwuduw83e8x30sm0"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "supportsSubscriptionSchedules": true,
  "companyId": "Yjnwuduw83e8x30sm0",
  "locationId": "Yjnwuduw83e8x30sm0"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!