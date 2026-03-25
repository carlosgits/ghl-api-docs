# Fetch Product Reviews

Source: https://marketplace.gohighlevel.com/docs/ghl/products/get-product-reviews

Screenshot: images/ghl_products_get-product-reviews_screenshot.png

---

ProductsReviewsFetch Product Reviews
Fetch Product Reviews
GET
 https://services.leadconnectorhq.com/products/reviews
API to fetch the Product Reviews
Requirements
Scope(s)
products.readonly
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
Location Id or Agency Id
Example: 6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
limit
number
The maximum number of items to be included in a single page of results
Default value:0
Example: 20
offset
number
The starting index of the page, indicating the position from which the results should be retrieved.
Default value:0
Example: 0
sortField
string
Possible values: [createdAt, rating]
The field upon which the sort should be applied
Example: rating
sortOrder
string
Possible values: [asc, desc]
The order of sort which should be applied for the sortField
Example: desc
rating
number
Key to filter the ratings
Example: 4
startDate
string
The start date for filtering reviews
Example: 2023-01-01T00:00:00Z
endDate
string
The end date for filtering reviews
Example: 2023-12-31T23:59:59Z
productId
string
Comma-separated list of product IDs
Example: 60d21b4667d0d8992e610c88,60d21b4667d0d8992e610c89,60d21b4667d0d8992e610c8a
storeId
string
Comma-separated list of store IDs
Example: 60d21b4667d0d8992e610c85,60d21b4667d0d8992e610c86,60d21b4667d0d8992e610c87
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
array[]
REQUIRED
Array of Collections
total
number
REQUIRED
The total count of the collections present, which is useful to calculate the pagination
























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
curl -L 'https://services.leadconnectorhq.com/products/reviews' \
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