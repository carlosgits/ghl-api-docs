# Update Product by ID

Source: https://marketplace.gohighlevel.com/docs/ghl/products/update-product-by-id

Screenshot: images/ghl_products_update-product-by-id_screenshot.png

---

ProductsProductsUpdate Product by ID
Update Product by ID
PUT
 https://services.leadconnectorhq.com/products/:productId
The "Update Product by ID" API allows modifying information for a specific product using its unique identifier. Use this endpoint to update details for a single product based on the provided product ID.
Requirements
Scope(s)
products.write
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
APPLICATION/JSON
BODY
REQUIRED
name
string
REQUIRED
The name of the product.
Example:Awesome Product
locationId
string
REQUIRED
The unique identifier for the location.
Example:3SwdhCsvxI8Au3KsPJt6
description
string
A brief description of the product.
Example:Product description goes here.
productType
string
REQUIRED
Possible values: [DIGITAL, PHYSICAL, SERVICE, PHYSICAL/DIGITAL]
image
string
The URL for the product image.
Example:https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png
statementDescriptor
string
The statement descriptor for the product.
Example:abcde
availableInStore
boolean
Indicates whether the product is available in-store.
Example:true
medias
object[]
variants
object[]
collectionIds
string[]
An array of category Ids for the product
Example:["65d71377c326ea78e1c47df5","65d71377c326ea78e1c47d34"]
isTaxesEnabled
boolean
Are there any taxes attached to the product. If this is true, taxes array cannot be empty.
Default value: false
Example:true
taxes
string[]
List of ids of Taxes attached to the Product. If taxes are passed, isTaxesEnabled should be true.
Example:["654492a4e6bef380114de15a"]
automaticTaxCategoryId
string
Tax category ID for Automatic taxes calculation.
Example:65d71377c326ea78e1c47df5
isLabelEnabled
boolean
Is the product label enabled. If this is true, label object cannot be empty.
Default value: false
Example:true
label
object
slug
string
The slug using which the product navigation will be handled
Example:awesome-product
seo
object
taxInclusive
boolean
Whether the taxes should be included in the purchase price
Default value: false
Example:true
prices
string[]
The prices of the product
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
curl -L -X PUT 'https://services.leadconnectorhq.com/products/:productId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "name": "Awesome Product",
  "locationId": "3SwdhCsvxI8Au3KsPJt6",
  "description": "Product description goes here.",
  "productType": "DIGITAL",
  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",
  "statementDescriptor": "abcde",
  "availableInStore": true,
  "medias": [
    {
      "id": "fzrgusiuu0m",
      "title": "1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png",
      "url": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png",
      "type": "image",
      "isFeatured": true,
      "priceIds": "6578278e879ad2646715ba9c"
    }
  ],
  "variants": [
    {
      "id": "38s63qmxfr4",
      "name": "Size",
      "options": [
        {
          "id": "h4z7u0im2q8",
          "name": "XL"
        }
      ]
    }
  ],
  "collectionIds": [
    "65d71377c326ea78e1c47df5",
    "65d71377c326ea78e1c47d34"
  ],
  "isTaxesEnabled": true,
  "taxes": [
    "654492a4e6bef380114de15a"
  ],
  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",
  "isLabelEnabled": true,
  "label": {
    "title": "Featured",
    "startDate": "2024-06-26T05:43:35.000Z",
    "endDate": "2024-06-30T05:43:39.000Z"
  },
  "slug": "awesome-product",
  "seo": {
    "title": "Best Product - Buy Now",
    "description": "This is the best product you can buy online with amazing features and great value"
  },
  "taxInclusive": true,
  "prices": [
    "string"
  ]
}'
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
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "name": "Awesome Product",
  "locationId": "3SwdhCsvxI8Au3KsPJt6",
  "description": "Product description goes here.",
  "productType": "DIGITAL",
  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",
  "statementDescriptor": "abcde",
  "availableInStore": true,
  "medias": [
    {
      "id": "fzrgusiuu0m",
      "title": "1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png",
      "url": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png",
      "type": "image",
      "isFeatured": true,
      "priceIds": "6578278e879ad2646715ba9c"
    }
  ],
  "variants": [
    {
      "id": "38s63qmxfr4",
      "name": "Size",
      "options": [
        {
          "id": "h4z7u0im2q8",
          "name": "XL"
        }
      ]
    }
  ],
  "collectionIds": [
    "65d71377c326ea78e1c47df5",
    "65d71377c326ea78e1c47d34"
  ],
  "isTaxesEnabled": true,
  "taxes": [
    "654492a4e6bef380114de15a"
  ],
  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",
  "isLabelEnabled": true,
  "label": {
    "title": "Featured",
    "startDate": "2024-06-26T05:43:35.000Z",
    "endDate": "2024-06-30T05:43:39.000Z"
  },
  "slug": "awesome-product",
  "seo": {
    "title": "Best Product - Buy Now",
    "description": "This is the best product you can buy online with amazing features and great value"
  },
  "taxInclusive": true,
  "prices": [
    "string"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!