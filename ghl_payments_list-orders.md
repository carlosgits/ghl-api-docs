# List Orders

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/list-orders

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_payments_list-orders_screenshot.png

---

PaymentsOrdersList Orders
List Orders
GET
 https://services.leadconnectorhq.com/payments/orders
The "List Orders" API allows to retrieve a paginated list of orders. Customize your results by filtering orders based on name, alt type, order status, payment mode, date range, type of source, contact, funnel products or paginate through the list using the provided query parameters. This endpoint provides a straightforward way to explore and retrieve order information.
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
status
string
Order status.
Example: completed
paymentStatus
string
Possible values: [paid, unpaid, refunded, partially_paid]
Payment Status of the Order
Example: unpaid
paymentMode
string
Mode of payment.
Example: live
startAt
string
Starting interval of orders.
Example: 2024-02-01
endAt
string
Closing interval of orders.
Example: 2024-02-13
search
string
The name of the order for searching.
Example: Awesome order
contactId
string
Contact id for filtering of orders.
Example: XPLSw2SVagl12LMDeTmQ
funnelProductIds
string
Funnel product ids separated by comma.
Example: 61dd0c7dc077f712a5f787ff,61d6afc9d39ac5e35965c017
sourceId
string
Source id
Example: 61dd0c7dc077f712a5f787ff
limit
number
The maximum number of items to be included in a single page of results
Default value:10
Example: 20
offset
number
The starting index of the page, indicating the position from which the results should be retrieved.
Default value:0
Example: 0
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
data
object[]
REQUIRED
totalCount
number
REQUIRED
total orders count
















































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
curl -L 'https://services.leadconnectorhq.com/payments/orders' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
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