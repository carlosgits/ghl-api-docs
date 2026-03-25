# Delete Coupon

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/delete-coupon

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_payments_delete-coupon_screenshot.png

---

PaymentsCouponsDelete Coupon
Delete Coupon
DELETE
 https://services.leadconnectorhq.com/payments/coupon
The "Delete Coupon" API allows you to permanently remove a coupon from your system using its unique identifier. Use this endpoint to discontinue promotional offers or clean up unused coupons. Note that this action cannot be undone.
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
success
boolean
REQUIRED
Indicates whether the delete was successful
Example:true
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/payments/coupon' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "BQdAwxa0ky1iK2sstLGJ",
  "altType": "location",
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
  "id": "6241712be68f7a98102ba272"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!