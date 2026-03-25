# Delete shipping rate

Source: https://marketplace.gohighlevel.com/docs/ghl/store/delete-shipping-rate

Screenshot: images/ghl_store_delete-shipping-rate_screenshot.png

---

StoreShipping Zone RatesDelete shipping rate
Delete shipping rate
DELETE
 https://services.leadconnectorhq.com/store/shipping-zone/:shippingZoneId/shipping-rate/:shippingRateId
Delete specific shipping rate with Id :shippingRateId
Requirements
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
PATH PARAMETERS
shippingZoneId
string
REQUIRED
ID of the shipping zone
Example: 6578278e879ad2646715ba9c
shippingRateId
string
REQUIRED
ID of the shipping rate that needs to be returned
Example: 6578278e879ad2646715ba9c
QUERY PARAMETERS
altId
string
REQUIRED
Location Id or Agency Id
Example: 6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
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
status
boolean
REQUIRED
Status of api action
Example:true
message
string
Success message
Example:Successfully created




















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
curl -L -X DELETE 'https://services.leadconnectorhq.com/store/shipping-zone/:shippingZoneId/shipping-rate/:shippingRateId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
shippingZoneId — path
REQUIRED
shippingRateId — path
REQUIRED
altId — query
REQUIRED
altType — query
REQUIRED
---
location
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!