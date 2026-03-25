# Fetch Product Store Stats

Source: https://marketplace.gohighlevel.com/docs/ghl/products/get-product-store-stats

Screenshot: images/ghl_products_get-product-store-stats_screenshot.png

---

ProductsStoreFetch Product Store Stats
Fetch Product Store Stats
GET
 https://services.leadconnectorhq.com/products/store/:storeId/stats
API to fetch the total number of products, included in the store, and excluded from the store and other stats
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
PATH PARAMETERS
storeId
string
REQUIRED
Products related to the store
Example: 3SwdhCu3svxI8AKsPJt6
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
search
string
The name of the product for searching.
Example: Awesome product
collectionIds
string
Filter by product collection Ids. Supports comma separated values
Example: 65c2789a812e52f9bd6ec577,65c2789a812e52de9a6ec576
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
totalProducts
number
REQUIRED
Total number of products
Example:100
includedInStore
number
REQUIRED
Number of products included in the store
Example:80
excludedFromStore
number
REQUIRED
Number of products excluded from the store
Example:20





















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
curl -L 'https://services.leadconnectorhq.com/products/store/:storeId/stats' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
storeId — path
REQUIRED
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