# Update Coupon

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/update-coupon

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_payments_update-coupon_screenshot.png

---

PaymentsCouponsUpdate Coupon
Update Coupon
PUT
 https://services.leadconnectorhq.com/payments/coupon
The "Update Coupon" API enables you to modify existing coupon details such as discount values, validity periods, usage limits, and other promotional parameters. Use this endpoint to adjust or extend promotional offers for your customers.
Requirements
Scope(s)
payments/coupons.write
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
APPLICATION/JSON
BODY
REQUIRED
altId
string
REQUIRED
Location Id
Example:BQdAwxa0ky1iK2sstLGJ
altType
string
REQUIRED
Alt Type
Possible values: [location]
Example:location
name
string
REQUIRED
Coupon Name
Example:New Year Sale
code
string
REQUIRED
Coupon Code
Example:LEVELUPDAY2022
discountType
string
REQUIRED
Discount Type
Possible values: [percentage, amount]
Example:amount
discountValue
number
REQUIRED
Discount Value
Example:10
startDate
string
REQUIRED
Start date in YYYY-MM-DDTHH:mm:ssZ format
Example:2023-01-01T22:45:00.000Z
endDate
string
End date in YYYY-MM-DDTHH:mm:ssZ format
Example:2023-01-31T22:45:00.000Z
usageLimit
number
Max number of times coupon can be used
Example:10
productIds
string[]
Product Ids
Example:["6241712be68f7a98102ba272"]
applyToFuturePayments
boolean
Is Coupon applicable on upcoming subscription transactions
Default value: true
Example:true
applyToFuturePaymentsConfig
object
limitPerCustomer
boolean
Limits whether a coupon can be redeemed only once per customer.
Default value: false
Example:true
id
string
REQUIRED
Coupon Id
Example:6241712be68f7a98102ba272
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
curl -L -X PUT 'https://services.leadconnectorhq.com/payments/coupon' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "BQdAwxa0ky1iK2sstLGJ",
  "altType": "location",
  "name": "New Year Sale",
  "code": "LEVELUPDAY2022",
  "discountType": "amount",
  "discountValue": 10,
  "startDate": "2023-01-01T22:45:00.000Z",
  "endDate": "2023-01-31T22:45:00.000Z",
  "usageLimit": 10,
  "productIds": [
    "6241712be68f7a98102ba272"
  ],
  "applyToFuturePayments": true,
  "applyToFuturePaymentsConfig": [
    {
      "type": "fixed",
      "duration": 5,
      "durationType": "months"
    },
    {
      "type": "forever"
    }
  ],
  "limitPerCustomer": true,
  "id": "6241712be68f7a98102ba272"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "altId": "BQdAwxa0ky1iK2sstLGJ",
  "altType": "location",
  "name": "New Year Sale",
  "code": "LEVELUPDAY2022",
  "discountType": "amount",
  "discountValue": 10,
  "startDate": "2023-01-01T22:45:00.000Z",
  "endDate": "2023-01-31T22:45:00.000Z",
  "usageLimit": 10,
  "productIds": [
    "6241712be68f7a98102ba272"
  ],
  "applyToFuturePayments": true,
  "applyToFuturePaymentsConfig": [
    {
      "type": "fixed",
      "duration": 5,
      "durationType": "months"
    },
    {
      "type": "forever"
    }
  ],
  "limitPerCustomer": true,
  "id": "6241712be68f7a98102ba272"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!