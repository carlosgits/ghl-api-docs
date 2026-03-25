# List Subscriptions

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/list-subscriptions

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_payments_list-subscriptions_screenshot.png

---

PaymentsSubscriptionsList Subscriptions
List Subscriptions
GET
 https://services.leadconnectorhq.com/payments/subscriptions
The "List Subscriptions" API allows to retrieve a paginated list of subscriptions. Customize your results by filtering subscriptions based on name, alt type, subscription status, payment mode, date range, type of source, contact, subscription id, entity id, contact or paginate through the list using the provided query parameters. This endpoint provides a straightforward way to explore and retrieve subscription information.
Requirements
Scope(s)
payments/subscriptions.readonly
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
altId
string
REQUIRED
AltId is the unique identifier e.g: location id.
Example: 3SwdhCu3svxI8AKsPJt6
altType
string
REQUIRED
Possible values: [location]
AltType is the type of identifier.
Example: location
entityId
string
Entity id for filtering of subscriptions.
Example: 61dd0fe9c077f73e67f78803
paymentMode
string
Mode of payment.
Example: live
startAt
string
Starting interval of subscriptions.
Example: 2024-02-01
endAt
string
Closing interval of subscriptions.
Example: 2024-02-13
entitySourceType
string
Source of the subscriptions.
Example: funnel
search
string
The name of the subscription for searching.
Example: Awesome subscription
contactId
string
Contact ID for the subscription
Example: AmuzcoPBpgKeccNsFlib
id
string
Subscription id for filtering of subscriptions.
Example: 64bf78af39118e4011926cba
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
getPaymentsCollectedCount
boolean
Get the total payments collected for the subscription.
Example: true
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
total subscriptions count















































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
curl -L 'https://services.leadconnectorhq.com/payments/subscriptions' \
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
---
location
Version — header
REQUIRED
---
2021-07-28
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!