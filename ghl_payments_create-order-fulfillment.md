# Create order fulfillment

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/create-order-fulfillment

Screenshot: images/ghl_payments_create-order-fulfillment_screenshot.png

---

PaymentsOrder fulfillmentsCreate order fulfillment
Create order fulfillment
POST
 https://services.leadconnectorhq.com/payments/orders/:orderId/fulfillments
The "Order Fulfillment" API facilitates the process of fulfilling an order.
Requirements
Scope(s)
payments/orders.write
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
PATH PARAMETERS
orderId
string
REQUIRED
ID of the order that needs to be returned
Example: 653f5e0cde5a1314e62a837c
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
trackings
object[]
REQUIRED
items
object[]
REQUIRED
notifyCustomer
boolean
REQUIRED
Need to send a notification to customer
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
status
boolean
REQUIRED
Status of api action
Example:true
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
curl -L 'https://services.leadconnectorhq.com/payments/orders/:orderId/fulfillments' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "trackings": [
    {
      "trackingNumber": "40012345678",
      "shippingCarrier": "FedEx",
      "trackingUrl": "https://www.fedex.com/wtrk/track/?trknbr=40012345678"
    }
  ],
  "items": [
    {
      "priceId": "6578278e879ad2646715ba9c",
      "qty": 1
    }
  ],
  "notifyCustomer": true
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
orderId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "trackings": [
    {
      "trackingNumber": "40012345678",
      "shippingCarrier": "FedEx",
      "trackingUrl": "https://www.fedex.com/wtrk/track/?trknbr=40012345678"
    }
  ],
  "items": [
    {
      "priceId": "6578278e879ad2646715ba9c",
      "qty": 1
    }
  ],
  "notifyCustomer": true
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!