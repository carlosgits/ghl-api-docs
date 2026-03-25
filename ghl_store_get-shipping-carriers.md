# Get Shipping Carrier

Source: https://marketplace.gohighlevel.com/docs/ghl/store/get-shipping-carriers

Screenshot: images/ghl_store_get-shipping-carriers_screenshot.png

---

StoreShipping CarrierGet Shipping Carrier
Get Shipping Carrier
GET
 https://services.leadconnectorhq.com/store/shipping-carrier/:shippingCarrierId
The "List Shipping Carrier" API allows to retrieve a paginated list of shipping carrier.
Requirements
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
PATH PARAMETERS
shippingCarrierId
string
REQUIRED
ID of the shipping carrier that needs to be returned
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
data
object





































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
curl -L 'https://services.leadconnectorhq.com/store/shipping-carrier/:shippingCarrierId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
shippingCarrierId — path
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