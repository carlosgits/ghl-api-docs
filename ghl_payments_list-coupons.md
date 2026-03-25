# List Coupons

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/list-coupons

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_payments_list-coupons_screenshot.png

---

PaymentsCouponsList Coupons
List Coupons
GET
 https://services.leadconnectorhq.com/payments/coupon/list
The "List Coupons" API allows you to retrieve a list of all coupons available in your location. Use this endpoint to view all promotional offers and special discounts for your customers.
Requirements
Scope(s)
payments/coupons.readonly
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
Location Id
Example: BQdAwxa0ky1iK2sstLGJ
altType
string
REQUIRED
Possible values: [location]
Alt Type
Example: location
limit
number
Maximum number of coupons to return
Default value:100
Example: 10
offset
number
Number of coupons to skip for pagination
Default value:0
Example: 0
status
string
Possible values: [scheduled, active, expired]
Filter coupons by status
Example: active
search
string
Search term to filter coupons by name or code
Example: DEAL50
Responses
200
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
Total number of coupons matching the query criteria
Example:20
traceId
string
REQUIRED
Unique identifier for tracing this API request
Example:c667b18d-8f5e-44cf-a914




































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
curl -L 'https://services.leadconnectorhq.com/payments/coupon/list' \
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