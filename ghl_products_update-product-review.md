# Update Product Reviews

Source: https://marketplace.gohighlevel.com/docs/ghl/products/update-product-review

Screenshot: images/ghl_products_update-product-review_screenshot.png

---

ProductsReviewsUpdate Product Reviews
Update Product Reviews
PUT
 https://services.leadconnectorhq.com/products/reviews/:reviewId
Update status, reply, etc of a particular review
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
PATH PARAMETERS
reviewId
string
REQUIRED
Review Id
Example: 6578278e879ad2646715ba9c
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
productId
string
REQUIRED
Product Id
Example:6578278e879ad2646715ba9c
status
string
REQUIRED
Status of the review
Example:approved
reply
object[]
rating
number
Rating of the product
Example:4.5
headline
string
Headline of the Review
Example:Amazing product with great quality
detail
string
Detailed Review of the product
Example:The product is for sure a must and recommended buy
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
curl -L -X PUT 'https://services.leadconnectorhq.com/products/reviews/:reviewId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "productId": "6578278e879ad2646715ba9c",
  "status": "approved",
  "reply": [
    {
      "headline": "Amazing product with great quality",
      "comment": "This product exceeded my expectations in terms of quality and performance. Highly recommended!",
      "user": {
        "name": "John Doe",
        "email": "example@example.com",
        "phone": "+1-555-555-5555",
        "isCustomer": true
      }
    }
  ],
  "rating": "4.5",
  "headline": "Amazing product with great quality",
  "detail": "The product is for sure a must and recommended buy"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
reviewId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "productId": "6578278e879ad2646715ba9c",
  "status": "approved",
  "reply": [
    {
      "headline": "Amazing product with great quality",
      "comment": "This product exceeded my expectations in terms of quality and performance. Highly recommended!",
      "user": {
        "name": "John Doe",
        "email": "example@example.com",
        "phone": "+1-555-555-5555",
        "isCustomer": true
      }
    }
  ],
  "rating": "4.5",
  "headline": "Amazing product with great quality",
  "detail": "The product is for sure a must and recommended buy"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!