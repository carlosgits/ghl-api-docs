# Get Price by ID for a Product

Source: https://marketplace.gohighlevel.com/docs/ghl/products/get-price-by-id-for-product

Screenshot: images/ghl_products_get-price-by-id-for-product_screenshot.png

---

ProductsPricesGet Price by ID for a Product
Get Price by ID for a Product
GET
 https://services.leadconnectorhq.com/products/:productId/price/:priceId
The "Get Price by ID for a Product" API allows retrieving information for a specific price associated with a particular product using its unique identifier. Use this endpoint to fetch details for a single price based on the provided price ID and product ID.
Requirements
Scope(s)
products/prices.readonly
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
priceId
string
REQUIRED
ID of the price that needs to be returned
Example: 6578278e879ad2646715ba9c
QUERY PARAMETERS
locationId
string
REQUIRED
location Id
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
curl -L 'https://services.leadconnectorhq.com/products/:productId/price/:priceId' \
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
priceId — path
REQUIRED
locationId — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!