# Create Shipping Rate

Source: https://marketplace.gohighlevel.com/docs/ghl/store/create-shipping-rate

Screenshot: images/ghl_store_create-shipping-rate_screenshot.png

---

StoreShipping Zone RatesCreate Shipping Rate
Create Shipping Rate
POST
 https://services.leadconnectorhq.com/store/shipping-zone/:shippingZoneId/shipping-rate
The "Create Shipping Rate" API allows adding a new shipping rate.
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
APPLICATION/JSON
BODY
REQUIRED
altId
string
REQUIRED
Location Id or Agency Id
Example:6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
name
string
REQUIRED
Name of the shipping zone
Example:North zone
description
string
Delivery description
Example:Ships next day
currency
string
REQUIRED
The currency of the amount of the rate / handling fee
Example:USD
amount
number
REQUIRED
The amount of the shipping rate if it is normal rate (0 means free ). Fixed Handling fee if it is a carrier rate (it will add to the carrier rate).
Example:99.99
conditionType
string
REQUIRED
Type of condition to provide the conditional pricing
Possible values: [none, price, weight]
Example:price
minCondition
number
REQUIRED
Minimum condition for applying this price. set 0 or null if there is no minimum
Example:99.99
maxCondition
number
REQUIRED
Maximum condition for applying this price. set 0 or null if there is no maximum
Example:99.99
isCarrierRate
boolean
is this a carrier rate
Example:true
shippingCarrierId
string
REQUIRED
Shipping carrier id
Example:655b33a82209e60b6adb87a5
percentageOfRateFee
number
Percentage of rate fee if it is a carrier rate.
Example:10.99
shippingCarrierServices
object[]
Responses
201
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
curl -L 'https://services.leadconnectorhq.com/store/shipping-zone/:shippingZoneId/shipping-rate' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "name": "North zone",
  "description": "Ships next day",
  "currency": "USD",
  "amount": 99.99,
  "conditionType": "price",
  "minCondition": 99.99,
  "maxCondition": 99.99,
  "isCarrierRate": true,
  "shippingCarrierId": "655b33a82209e60b6adb87a5",
  "percentageOfRateFee": 10.99,
  "shippingCarrierServices": [
    {
      "name": "Priority Mail Express International",
      "value": "PriorityMailExpressInternational"
    }
  ]
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
shippingZoneId — path
REQUIRED
Body
 REQUIRED
{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "name": "North zone",
  "description": "Ships next day",
  "currency": "USD",
  "amount": 99.99,
  "conditionType": "price",
  "minCondition": 99.99,
  "maxCondition": 99.99,
  "isCarrierRate": true,
  "shippingCarrierId": "655b33a82209e60b6adb87a5",
  "percentageOfRateFee": 10.99,
  "shippingCarrierServices": [
    {
      "name": "Priority Mail Express International",
      "value": "PriorityMailExpressInternational"
    }
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!