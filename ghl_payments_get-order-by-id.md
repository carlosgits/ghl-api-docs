# Get Order by ID

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/get-order-by-id

Screenshot: images/ghl_payments_get-order-by-id_screenshot.png

---

PaymentsOrdersGet Order by ID
Get Order by ID
GET
 https://services.leadconnectorhq.com/payments/orders/:orderId
The "Get Order by ID" API allows to retrieve information for a specific order using its unique identifier. Use this endpoint to fetch details for a single order based on the provided order ID.
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
locationId
string
LocationId is the id of the sub-account.
Example: 3SwdhCu3svxI8AKsPJt6
altId
string
REQUIRED
AltId is the unique identifier e.g: location id.
Example: 3SwdhCu3svxI8AKsPJt6
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
_id
string
REQUIRED
The unique identifier for the order.
Example:653f5e0cde5a1314e62a837c
altId
string
REQUIRED
AltId is the unique identifier eg: location id.
Example:3SwdhCu3svxI8AKsPJt6
altType
string
REQUIRED
AltType is the type of identifier.
Example:location
contactId
string
Contact id corresponding to the order.
Example:XPLSw2SVagl12LMDeTmQ
currency
string
Currency in which order was created.
Example:USD
amount
number
Order value.
Example:100
status
string
REQUIRED
The status of the order (e.g., completed).
Example:completed
liveMode
boolean
Order is in live / test mode.
Example:false
createdAt
date-time
REQUIRED
The creation timestamp of the order.
Example:2023-11-20T10:23:36.515Z
updatedAt
date-time
REQUIRED
The last update timestamp of the order.
Example:2024-01-23T09:57:04.846Z
fulfillmentStatus
string
Fulfillment status of the order.
Example:unfulfilled
contactSnapshot
object
Contact details of the order.
Example:{ last_name: "Mcclain", type: "lead", first_name_lower_case: "rogan", email: "anish+11@gohighlevel.com", last_name_lower_case: "mcclain", location_id: "o6241QsiRwUIJHyjuhos", company_name: "Jordan and Cox Trading"}
amountSummary
object
source
object
items
string[]
Item details of the order.
Example:{ _id: 61dd33e88058b9f967ca79dc, authorizeAmount: 0, locationId: "SBAWb4yu7A4LSc0skQ6g", name: "Sample Product": price: {}, product: { name: "Testing product", productType: "SERVICE" }}
coupon
object
Coupon details of the order.
Example:{ code: "FEST10", _id: "63455e48901b43d4ef364a20" }
trackingId
string
Tracking id of the order.
Example:63319ef9-de0a-4c84-aebd-3585fb4a0cdf
fingerprint
string
Fingerprint id of the order.
Example:5d51db5a-42b0-4b04-ba88-2c046c982a3a
meta
object
Meta details of the order.
Example:{ couponSessionExpired: true }
markAsTest
boolean
Is test order.
Example:false
traceId
string
Trace id of the order.
Example:d3b16a92-a8ed-4e6b-8467-844750f78ed5
automaticTaxesCalculated
boolean
Automatic taxes applied for the Order
Example:true
taxCalculationProvider
object
Provider name for automatic tax calculation
Example:taxjar
createdBy
string
User ID who created the order.
Example:user123










































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
curl -L 'https://services.leadconnectorhq.com/payments/orders/:orderId' \
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
Version — header
REQUIRED
---
2021-07-28
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!