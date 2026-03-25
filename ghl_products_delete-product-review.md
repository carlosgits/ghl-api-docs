# Delete Product Review

Source: https://marketplace.gohighlevel.com/docs/ghl/products/delete-product-review

Screenshot: images/ghl_products_delete-product-review_screenshot.png

---

ProductsReviewsDelete Product Review
Delete Product Review
DELETE
 https://services.leadconnectorhq.com/products/reviews/:reviewId
Delete specific product review
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
QUERY PARAMETERS
altId
string
REQUIRED
Location Id or Agency Id
Example: 6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
productId
string
REQUIRED
Product Id of the product
Example: 6578278e879ad2646715ba9c
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/products/reviews/:reviewId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
reviewId — path
REQUIRED
altId — query
REQUIRED
altType — query
REQUIRED
---
location
productId — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!