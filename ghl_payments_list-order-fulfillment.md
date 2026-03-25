# List fulfillment

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/list-order-fulfillment

Screenshot: images/ghl_payments_list-order-fulfillment_screenshot.png

---

PaymentsOrder fulfillmentsList fulfillment
List fulfillment
GET
 https://services.leadconnectorhq.com/payments/orders/:orderId/fulfillments
List all fulfillment history of an order
Requirements
Scope(s)
payments/orders.readonly
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
data
object[]
REQUIRED
















































































































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
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
orderId — path
REQUIRED
altId — query
REQUIRED
altType — query
REQUIRED
---
location
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!