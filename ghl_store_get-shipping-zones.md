# Get Shipping Zone

Source: https://marketplace.gohighlevel.com/docs/ghl/store/get-shipping-zones

Screenshot: images/ghl_store_get-shipping-zones_screenshot.png

---

StoreShipping ZoneGet Shipping Zone
Get Shipping Zone
GET
 https://services.leadconnectorhq.com/store/shipping-zone/:shippingZoneId
The "List Shipping Zone" API allows to retrieve a paginated list of shipping zone.
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
ID of the item that needs to be returned
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
withShippingRate
boolean
Include shipping rates array
Example:
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
curl -L 'https://services.leadconnectorhq.com/store/shipping-zone/:shippingZoneId' \
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
altId — query
REQUIRED
altType — query
REQUIRED
---
location
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!