# Get Details about individual product collection

Source: https://marketplace.gohighlevel.com/docs/ghl/products/get-product-collection-id

Screenshot: images/ghl_products_get-product-collection-id_screenshot.png

---

ProductsCollectionsGet Details about individual product collection
Get Details about individual product collection
GET
 https://services.leadconnectorhq.com/products/collections/:collectionId
Get Details about individual product collection
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
PATH PARAMETERS
collectionId
string
REQUIRED
Collection Id
Example: 65d71377c326ea78e1c47df5
QUERY PARAMETERS
altId
string
REQUIRED
Location Id
Example: 3SwdhCsvxI8Au3KsPJt6
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
object
REQUIRED
Collection Data
status
boolean
REQUIRED
Status of the operation
Example:true




















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
curl -L 'https://services.leadconnectorhq.com/products/collections/:collectionId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
collectionId — path
REQUIRED
altId — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!