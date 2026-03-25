# Disconnect existing provider config

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/disconnect-config

Screenshot: images/ghl_payments_disconnect-config_screenshot.png

---

PaymentsCustom ProviderDisconnect existing provider config
Disconnect existing provider config
POST
 https://services.leadconnectorhq.com/payments/custom-provider/disconnect
API to disconnect an existing payment config for given location
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
liveMode
boolean
REQUIRED
Whether the config is for test mode or live mode. true represents config is for live payments
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
success
boolean
REQUIRED
Whether the custom provider config is disconnect or not. true represents config is disconnect
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
curl -L 'https://services.leadconnectorhq.com/payments/custom-provider/disconnect' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "liveMode": "true"
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
  "liveMode": "true"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!