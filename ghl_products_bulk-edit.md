# Bulk Edit Products and Prices

Source: https://marketplace.gohighlevel.com/docs/ghl/products/bulk-edit

Screenshot: images/ghl_products_bulk-edit_screenshot.png

---

ProductsProductsBulk Edit Products and Prices
Bulk Edit Products and Prices
POST
 https://services.leadconnectorhq.com/products/bulk-update/edit
API to bulk edit products and their associated prices (max 30 entities)
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
products
object[]
REQUIRED
Responses
201
400
401
422
Products and prices updated successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
message
string
REQUIRED
Success message
Example:Products updated successfully
status
boolean
REQUIRED
Operation status
Example:true
updatedCount
number
REQUIRED
Number of products updated
Example:5





















Share your feedback
★
★
★
★
★
CURL
NODEJS
PYTHON
PHP
JAVA
GO
RUBY
POWERSHELL
CURL
curl -L 'https://services.leadconnectorhq.com/products/bulk-update/edit' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "products": [
    {
      "_id": "64a1b2c3d4e5f67890123456",
      "name": "Premium Product",
      "description": "A high-quality premium product with excellent features and durability",
      "image": "https://example.com/product-image.jpg",
      "availableInStore": true,
      "prices": [
        {
          "_id": "64a1b2c3d4e5f67890123456",
          "name": "Standard Plan",
          "amount": 99.99,
          "currency": "USD",
          "compareAtPrice": 129.99,
          "availableQuantity": 100,
          "trackInventory": true,
          "allowOutOfStockPurchases": false,
          "sku": "SKU-001",
          "trialPeriod": 7,
          "totalCycles": 12,
          "setupFee": 25,
          "shippingOptions": {
            "weight": {
              "value": 10,
              "unit": "kg"
            },
            "dimensions": {
              "height": 10,
              "width": 10,
              "length": 10,
              "unit": "cm"
            }
          },
          "recurring": {
            "interval": "day",
            "intervalCount": 1
          }
        }
      ],
      "collectionIds": [
        "64a1b2c3d4e5f67890123458",
        "64a1b2c3d4e5f67890123459"
      ],
      "isLabelEnabled": true,
      "isTaxesEnabled": true,
      "seo": {
        "title": "Best Product - Buy Now",
        "description": "This is the best product you can buy online with amazing features and great value"
      },
      "slug": "premium-product",
      "automaticTaxCategoryId": "64a1b2c3d4e5f67890123460",
      "taxInclusive": false,
      "taxes": [
        {}
      ],
      "medias": [
        {}
      ],
      "label": {}
    }
  ]
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
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
  "products": [
    {
      "_id": "64a1b2c3d4e5f67890123456",
      "name": "Premium Product",
      "description": "A high-quality premium product with excellent features and durability",
      "image": "https://example.com/product-image.jpg",
      "availableInStore": true,
      "prices": [
        {
          "_id": "64a1b2c3d4e5f67890123456",
          "name": "Standard Plan",
          "amount": 99.99,
          "currency": "USD",
          "compareAtPrice": 129.99,
          "availableQuantity": 100,
          "trackInventory": true,
          "allowOutOfStockPurchases": false,
          "sku": "SKU-001",
          "trialPeriod": 7,
          "totalCycles": 12,
          "setupFee": 25,
          "shippingOptions": {
            "weight": {
              "value": 10,
              "unit": "kg"
            },
            "dimensions": {
              "height": 10,
              "width": 10,
              "length": 10,
              "unit": "cm"
            }
          },
          "recurring": {
            "interval": "day",
            "intervalCount": 1
          }
        }
      ],
      "collectionIds": [
        "64a1b2c3d4e5f67890123458",
        "64a1b2c3d4e5f67890123459"
      ],
      "isLabelEnabled": true,
      "isTaxesEnabled": true,
      "seo": {
        "title": "Best Product - Buy Now",
        "description": "This is the best product you can buy online with amazing features and great value"
      },
      "slug": "premium-product",
      "automaticTaxCategoryId": "64a1b2c3d4e5f67890123460",
      "taxInclusive": false,
      "taxes": [
        {}
      ],
      "medias": [
        {}
      ],
      "label": {}
    }
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!