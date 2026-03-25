# Delete Price by ID for a Product

Source: https://marketplace.gohighlevel.com/docs/ghl/products/delete-price-by-id-for-product

Screenshot: images/ghl_products_delete-price-by-id-for-product_screenshot.png

---

ProductsPricesDelete Price by ID for a Product
Delete Price by ID for a Product
DELETE
 https://services.leadconnectorhq.com/products/:productId/price/:priceId
The "Delete Price by ID for a Product" API allows deleting a specific price associated with a particular product using its unique identifier. Use this endpoint to remove a price from the system.
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
status
boolean
REQUIRED
returns true if the price is successfully deleted
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/products/:productId/price/:priceId' \
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