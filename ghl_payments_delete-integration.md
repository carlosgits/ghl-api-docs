# Deleting an existing integration

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/delete-integration

Screenshot: images/ghl_payments_delete-integration_screenshot.png

---

PaymentsCustom ProviderDeleting an existing integration
Deleting an existing integration
DELETE
 https://services.leadconnectorhq.com/payments/custom-provider/provider
API to delete an association for an app and location
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/payments/custom-provider/provider' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!