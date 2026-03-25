# Fetch Coupon

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/get-coupon

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_payments_get-coupon_screenshot.png

---

PaymentsCouponsFetch Coupon
Fetch Coupon
GET
 https://services.leadconnectorhq.com/payments/coupon
The "Get Coupon Details" API enables you to retrieve comprehensive information about a specific coupon using either its unique identifier or promotional code. Use this endpoint to view coupon parameters, usage statistics, validity periods, and other promotional details.
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
id
string
REQUIRED
Coupon id
Example: 6241712be68f7a98102ba272
code
string
REQUIRED
Coupon code
Example: DEAL50
Responses
200
422
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
_id
string
REQUIRED
Unique MongoDB identifier for the coupon
Example:67f6c132d9485f9dacd5f123
usageCount
number
REQUIRED
Number of times the coupon has been used
Example:12
limitPerCustomer
number
REQUIRED
Maximum number of times a customer can use this coupon (0 for unlimited)
Example:5
altId
string
REQUIRED
Location Id
Example:79t07PzK8Tvf73d12312
altType
string
REQUIRED
Type of entity
Example:location
name
string
REQUIRED
Display name of the coupon
Example:NEWT6
code
string
REQUIRED
Redemption code for the coupon
Example:NEWT6
discountType
string
REQUIRED
Type of discount (percentage or amount)
Possible values: [percentage, amount]
Example:percentage
discountValue
number
REQUIRED
Value of the discount (percentage or fixed amount)
Example:25
status
string
REQUIRED
Current status of the coupon
Possible values: [scheduled, active, expired]
Example:scheduled
startDate
string
REQUIRED
Date when the coupon becomes active
Example:2025-04-30T18:30:00.000Z
endDate
string
End date when the coupon expires
Example:2025-05-30T18:30:00.000Z
applyToFuturePayments
boolean
REQUIRED
Indicates if the coupon applies to future recurring payments
Example:true
applyToFuturePaymentsConfig
object
userId
string
User ID associated with the coupon (if applicable)
Example:q0m15dTLGeiGOXG123123
createdAt
string
REQUIRED
Creation timestamp
Example:2025-04-09T18:49:22.026Z
updatedAt
string
REQUIRED
Last update timestamp
Example:2025-04-09T18:49:22.026Z
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
curl -L 'https://services.leadconnectorhq.com/payments/coupon' \
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
id — query
REQUIRED
code — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!