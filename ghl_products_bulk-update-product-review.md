# Update Product Reviews

Source: https://marketplace.gohighlevel.com/docs/ghl/products/bulk-update-product-review

Screenshot: images/ghl_products_bulk-update-product-review_screenshot.png

---

ProductsReviewsUpdate Product Reviews
Update Product Reviews
POST
 https://services.leadconnectorhq.com/products/reviews/bulk-update
Update one or multiple product reviews: status, reply, etc.
Requirements
Scope(s)
products.write
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
Location Id or Agency Id
Example:6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
reviews
object[]
REQUIRED
status
object
REQUIRED
Status of the review
Example:approved
Responses
201
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
message
string
Success message
Example:Successfully created




















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
curl -L 'https://services.leadconnectorhq.com/products/reviews/bulk-update' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "reviews": [
    {
      "reviewId": "6578278e879ad2646715ba9c",
      "productId": "6578278e879ad2646715ba9d",
      "storeId": "a1b2c3d4e5f6g7h8i9j0k1l2"
    }
  ],
  "status": "approved"
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
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "reviews": [
    {
      "reviewId": "6578278e879ad2646715ba9c",
      "productId": "6578278e879ad2646715ba9d",
      "storeId": "a1b2c3d4e5f6g7h8i9j0k1l2"
    }
  ],
  "status": "approved"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!