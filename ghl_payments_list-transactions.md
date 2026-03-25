# List Transactions

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/list-transactions

Screenshot: images/ghl_payments_list-transactions_screenshot.png

---

PaymentsTransactionsList Transactions
List Transactions
GET
 https://services.leadconnectorhq.com/payments/transactions
The "List Transactions" API allows to retrieve a paginated list of transactions. Customize your results by filtering transactions based on name, alt type, transaction status, payment mode, date range, type of source, contact, subscription id, entity id or paginate through the list using the provided query parameters. This endpoint provides a straightforward way to explore and retrieve transaction information.
Requirements
Scope(s)
payments/transactions.readonly
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
altType
string
REQUIRED
AltType is the type of identifier.
Example: location
paymentMode
string
Mode of payment.
Example: live
startAt
string
Starting interval of transactions.
Example: 2024-02-01
endAt
string
Closing interval of transactions.
Example: 2024-02-13
entitySourceType
string
Source of the transactions.
Example: funnel
entitySourceSubType
string
Source sub-type of the transactions.
Example: two_step_order_form
search
string
The name of the transaction for searching.
Example: Awesome transaction
subscriptionId
string
Subscription id for filtering of transactions.
Example: sub_1KGcXDCScnf89tZoVkoEMCEL
entityId
string
Entity id for filtering of transactions.
Example: 61dd0fe9c077f73e67f78803
contactId
string
Contact id for filtering of transactions.
Example: XPLSw2SVagl12LMDeTmQ
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
total transactions count





















































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
curl -L 'https://services.leadconnectorhq.com/payments/transactions' \
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
altType — query
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