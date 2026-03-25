# Record Order Payment

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/record-order-payment

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_payments_record-order-payment_screenshot.png

---

PaymentsOrdersRecord Order Payment
Record Order Payment
POST
 https://services.leadconnectorhq.com/payments/orders/:orderId/record-payment
The "Record Order Payment" API allows to record a payment for an order. Use this endpoint to record payment for an order and update the order status to "Paid".
Requirements
Scope(s)
payments/orders.collectPayment
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
Order ID
Example: 5e2d4c8e0e8b4e001c1c4f5d
APPLICATION/JSON
BODY
REQUIRED
altId
string
REQUIRED
location Id / company Id based on altType
Example:6578278e879ad2646715ba9c
altType
string
REQUIRED
Alt Type
Possible values: [location]
Example:location
mode
string
REQUIRED
manual payment method
Possible values: [cash, card, cheque, bank_transfer, other]
Example:card
card
object
cheque
object
notes
string
Any note to be recorded with the transaction
Example:This was a direct payment
amount
number
Amount to be paid against the invoice.
Example:100
meta
object
Meta data to be recorded with the transaction
isPartialPayment
boolean
Indicates if the order is intended to be a partial payment.
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
Success status of the request
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
curl -L 'https://services.leadconnectorhq.com/payments/orders/:orderId/record-payment' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "mode": "card",
  "card": {
    "type": "mastercard",
    "last4": "1234"
  },
  "cheque": {
    "number": "129-129-129-912"
  },
  "notes": "This was a direct payment",
  "amount": 100,
  "meta": {},
  "isPartialPayment": true
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
  "mode": "card",
  "card": {
    "type": "mastercard",
    "last4": "1234"
  },
  "cheque": {
    "number": "129-129-129-912"
  },
  "notes": "This was a direct payment",
  "amount": 100,
  "meta": {},
  "isPartialPayment": true
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!