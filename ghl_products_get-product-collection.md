# Fetch Product Collections

Source: https://marketplace.gohighlevel.com/docs/ghl/products/get-product-collection

Screenshot: images/ghl_products_get-product-collection_screenshot.png

---

ProductsCollectionsFetch Product Collections
Fetch Product Collections
GET
 https://services.leadconnectorhq.com/products/collections
Internal API to fetch the Product Collections
Requirements
Scope(s)
products/collection.readonly
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
altId
string
REQUIRED
Location Id
Example: 6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
The type of alt. For now it is only LOCATION
Example: LOCATION
collectionIds
string
Ids of the collections separated by comma(,) for search purposes
Example: 65d71377c326ea78e1c47df5,65d71377c326ea78e1c47d34
name
string
Query to search collection based on names
Example: Best Sellers
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
curl -L 'https://services.leadconnectorhq.com/products/collections' \
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