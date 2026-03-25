# Create Price for a Product

Source: https://marketplace.gohighlevel.com/docs/ghl/products/create-price-for-product

Screenshot: images/ghl_products_create-price-for-product_screenshot.png

---

ProductsPricesCreate Price for a Product
Create Price for a Product
POST
 https://services.leadconnectorhq.com/products/:productId/price
The "Create Price for a Product" API allows adding a new price associated with a specific product to the system. Use this endpoint to create a price with the specified details for a particular product. Ensure that the required information is provided in the request payload.
Requirements
Scope(s)
products/prices.write
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
ID of the product that needs to be used
Example: 6578278e879ad2646715ba9c
APPLICATION/JSON
BODY
REQUIRED
name
string
REQUIRED
The name of the price.
Example:Price Name
type
string
REQUIRED
The type of the price.
Possible values: [one_time, recurring]
Example:one_time
currency
string
REQUIRED
The currency of the price.
Example:USD
amount
number
REQUIRED
The amount of the price. ( min: 0 )
Example:99.99
recurring
object
description
string
A brief description of the price.
membershipOffers
object[]
trialPeriod
number
The trial period duration in days (if applicable).
Example:7
totalCycles
number
The total number of billing cycles for the price. ( min: 1 )
Example:12
setupFee
number
The setup fee for the price.
Example:10.99
variantOptionIds
string[]
An array of variant option IDs associated with the price.
Example:["option_id_1","option_id_2"]
compareAtPrice
number
The compare at price for the price.
Example:19.99
locationId
string
REQUIRED
The unique identifier of the location associated with the price.
Example:6578278e879ad2646715ba9c
userId
string
The unique identifier of the user who created the price.
Example:6578278e879ad2646715ba9c
meta
object
trackInventory
boolean
Need to track inventory stock quantity
Example:true
availableQuantity
number
Available inventory stock quantity
Example:5
allowOutOfStockPurchases
boolean
Continue selling when out of stock
Example:true
sku
string
The unique identifier of the SKU associated with the price
Example:sku_123
shippingOptions
object
isDigitalProduct
boolean
Is the product a digital product
Example:true
digitalDelivery
string[]
Digital delivery options
Responses
201
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
The unique identifier for the price.
Example:655b33aa2209e60b6adb87a7
membershipOffers
object[]
variantOptionIds
string[]
An array of variant option IDs associated with the price.
Example:["h4z7u0im2q8","h3nst2ltsnn"]
locationId
string
The unique identifier for the location.
Example:3SwdhCsvxI8Au3KsPJt6
product
string
The unique identifier for the associated product.
Example:655b33a82209e60b6adb87a5
userId
string
The unique identifier for the user.
Example:6YAtzfzpmHAdj0e8GkKp
name
string
REQUIRED
The name of the price.
Example:Red / S
type
string
REQUIRED
The type of the price (e.g., one_time).
Possible values: [one_time, recurring]
Example:one_time
currency
string
REQUIRED
The currency code for the price.
Example:INR
amount
number
REQUIRED
The amount of the price.
Example:199999
recurring
object
createdAt
date-time
The creation timestamp of the price.
Example:2023-11-20T10:23:38.645Z
updatedAt
date-time
The last update timestamp of the price.
Example:2024-01-23T09:57:04.852Z
compareAtPrice
number
The compare-at price for comparison purposes.
Example:2000000
trackInventory
boolean
Indicates whether inventory tracking is enabled.
Example:null
availableQuantity
number
Available inventory stock quantity
Example:5
allowOutOfStockPurchases
boolean
Continue selling when out of stock
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
curl -L 'https://services.leadconnectorhq.com/products/:productId/price' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "name": "Price Name",
  "type": "one_time",
  "currency": "USD",
  "amount": 99.99,
  "recurring": {
    "interval": "day",
    "intervalCount": 1
  },
  "description": "string",
  "membershipOffers": [
    {
      "label": "top_50",
      "value": "50",
      "_id": "655b33aa2209e60b6adb87a7"
    }
  ],
  "trialPeriod": 7,
  "totalCycles": 12,
  "setupFee": 10.99,
  "variantOptionIds": [
    "option_id_1",
    "option_id_2"
  ],
  "compareAtPrice": 19.99,
  "locationId": "6578278e879ad2646715ba9c",
  "userId": "6578278e879ad2646715ba9c",
  "meta": {
    "source": "stripe",
    "sourceId": "123",
    "stripePriceId": "price_123",
    "internalSource": "agency_plan"
  },
  "trackInventory": true,
  "availableQuantity": 5,
  "allowOutOfStockPurchases": true,
  "sku": "sku_123",
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
  "isDigitalProduct": true,
  "digitalDelivery": [
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
  "name": "Price Name",
  "type": "one_time",
  "currency": "USD",
  "amount": 99.99,
  "recurring": {
    "interval": "day",
    "intervalCount": 1
  },
  "description": "string",
  "membershipOffers": [
    {
      "label": "top_50",
      "value": "50",
      "_id": "655b33aa2209e60b6adb87a7"
    }
  ],
  "trialPeriod": 7,
  "totalCycles": 12,
  "setupFee": 10.99,
  "variantOptionIds": [
    "option_id_1",
    "option_id_2"
  ],
  "compareAtPrice": 19.99,
  "locationId": "6578278e879ad2646715ba9c",
  "userId": "6578278e879ad2646715ba9c",
  "meta": {
    "source": "stripe",
    "sourceId": "123",
    "stripePriceId": "price_123",
    "internalSource": "agency_plan"
  },
  "trackInventory": true,
  "availableQuantity": 5,
  "allowOutOfStockPurchases": true,
  "sku": "sku_123",
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
  "isDigitalProduct": true,
  "digitalDelivery": [
    "string"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!