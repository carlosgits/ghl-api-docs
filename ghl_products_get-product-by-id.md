# Get Product by ID

Source: https://marketplace.gohighlevel.com/docs/ghl/products/get-product-by-id

Screenshot: images/ghl_products_get-product-by-id_screenshot.png

---

ProductsProductsGet Product by ID
Get Product by ID
GET
 https://services.leadconnectorhq.com/products/:productId
The "Get Product by ID" API allows to retrieve information for a specific product using its unique identifier. Use this endpoint to fetch details for a single product based on the provided product ID.
Requirements
Scope(s)
products.readonly
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Agency Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
PATH PARAMETERS
productId
string
REQUIRED
ID or the slug of the product that needs to be returned
Example: 6578278e879ad2646715ba9c
QUERY PARAMETERS
locationId
string
REQUIRED
location Id
Example: 6578278e879ad2646715ba9c
sendWishlistStatus
boolean
Parameter which will decide whether to show the wishlisting status of products
Example:
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
_id
string
REQUIRED
The unique identifier for the product.
Example:655b33a82209e60b6adb87a5
description
string
product description
Example:This is a really awesome product
variants
object[]
locationId
string
REQUIRED
The unique identifier for the location.
Example:3SwdhCsvxI8Au3KsPJt6
name
string
REQUIRED
The name of the product.
Example:Awesome Product
productType
string
REQUIRED
The type of the product (e.g., PHYSICAL).
Example:PHYSICAL
availableInStore
boolean
Indicates whether the product is available in-store.
Example:true
createdAt
date-time
REQUIRED
The creation timestamp of the product.
Example:2023-11-20T10:23:36.515Z
updatedAt
date-time
REQUIRED
The last update timestamp of the product.
Example:2024-01-23T09:57:04.846Z
statementDescriptor
string
The statement descriptor for the product.
Example:abcde
image
string
The URL for the product image.
Example:https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png
collectionIds
string[]
An array of category Ids for the product
Example:["65d71377c326ea78e1c47df5","65d71377c326ea78e1c47d34"]
isTaxesEnabled
boolean
The field indicates whether taxes are enabled for the product or not.
Default value: false
Example:true
taxes
string[]
An array of ids of Taxes attached to the Product. If the expand query includes tax, the taxes will be of type ProductTaxDto. Please refer to the ProductTaxDto for additional details.
Example:["654492a4e6bef380114de15a"]
automaticTaxCategoryId
string
Tax category ID for Automatic taxes calculation.
Example:65d71377c326ea78e1c47df5
label
object
slug
string
The slug of the product by which the product will be navigated
Example:washing-machine























































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
curl -L 'https://services.leadconnectorhq.com/products/:productId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Security Scheme
Location-Access
Agency-Access
Bearer Token
Parameters
productId — path
REQUIRED
locationId — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!