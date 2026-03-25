# Bulk Update Products

Source: https://marketplace.gohighlevel.com/docs/ghl/products/bulk-update

Screenshot: images/ghl_products_bulk-update_screenshot.png

---

ProductsProductsBulk Update Products
Bulk Update Products
POST
 https://services.leadconnectorhq.com/products/bulk-update
API to bulk update products (price, availability, collections, delete)
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
type
string
REQUIRED
Type of bulk update operation
Possible values: [bulk-update-price, bulk-update-availability, bulk-update-product-collection, bulk-delete-products, bulk-update-currency]
Example:bulk-update-price
productIds
string[]
REQUIRED
Array of product IDs
Example:["5f8d0d55b54764421b7156c1"]
filters
object
price
object
compareAtPrice
object
availability
boolean
New availability status
collectionIds
string[]
Array of collection IDs
currency
string
Currency code
Example:USD
Responses
201
400
401
422
Products updated successfully
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
curl -L 'https://services.leadconnectorhq.com/products/bulk-update' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "type": "bulk-update-price",
  "productIds": [
    "5f8d0d55b54764421b7156c1"
  ],
  "filters": {
    "collectionIds": [
      "5f8d0d55b54764421b7156c1",
      "5f8d0d55b54764421b7156c2"
    ],
    "productType": "one-time",
    "availableInStore": true,
    "search": "blue t-shirt"
  },
  "price": {
    "type": "INCREASE_BY_AMOUNT",
    "value": 100,
    "roundToWhole": true
  },
  "compareAtPrice": {
    "type": "INCREASE_BY_AMOUNT",
    "value": 100,
    "roundToWhole": true
  },
  "availability": true,
  "collectionIds": [
    "string"
  ],
  "currency": "USD"
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
  "type": "bulk-update-price",
  "productIds": [
    "5f8d0d55b54764421b7156c1"
  ],
  "filters": {
    "collectionIds": [
      "5f8d0d55b54764421b7156c1",
      "5f8d0d55b54764421b7156c2"
    ],
    "productType": "one-time",
    "availableInStore": true,
    "search": "blue t-shirt"
  },
  "price": {
    "type": "INCREASE_BY_AMOUNT",
    "value": 100,
    "roundToWhole": true
  },
  "compareAtPrice": {
    "type": "INCREASE_BY_AMOUNT",
    "value": 100,
    "roundToWhole": true
  },
  "availability": true,
  "collectionIds": [
    "string"
  ],
  "currency": "USD"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!