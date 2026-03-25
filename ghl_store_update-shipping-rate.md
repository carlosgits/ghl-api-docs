# Update Shipping Rate

Source: https://marketplace.gohighlevel.com/docs/ghl/store/update-shipping-rate

Screenshot: images/ghl_store_update-shipping-rate_screenshot.png

---

StoreShipping Zone RatesUpdate Shipping Rate
Update Shipping Rate
PUT
 https://services.leadconnectorhq.com/store/shipping-zone/:shippingZoneId/shipping-rate/:shippingRateId
The "update Shipping Rate" API allows update a shipping rate to the system.
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
APPLICATION/JSON
BODY
REQUIRED
altId
string
Location Id or Agency Id
Example:6578278e879ad2646715ba9c
altType
string
Possible values: [location]
name
string
Name of the shipping zone
Example:North zone
description
string
Delivery description
Example:Ships next day
currency
string
The currency of the amount of the rate / handling fee
Example:USD
amount
number
The amount of the shipping rate if it is normal rate (0 means free ). Fixed Handling fee if it is a carrier rate (it will add to the carrier rate).
Example:99.99
conditionType
string
Type of condition to provide the conditional pricing
Possible values: [none, price, weight]
Example:price
minCondition
number
Minimum condition for applying this price. set 0 or null if there is no minimum
Example:99.99
maxCondition
number
Maximum condition for applying this price. set 0 or null if there is no maximum
Example:99.99
isCarrierRate
boolean
is this a carrier rate
Example:true
shippingCarrierId
string
Shipping carrier id
Example:655b33a82209e60b6adb87a5
percentageOfRateFee
number
Percentage of rate fee if it is a carrier rate.
Example:10.99
shippingCarrierServices
object[]
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
curl -L -X PUT 'https://services.leadconnectorhq.com/store/shipping-zone/:shippingZoneId/shipping-rate/:shippingRateId' \
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
shippingRateId — path
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