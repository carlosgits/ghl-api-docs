# Delete Product by ID

Source: https://marketplace.gohighlevel.com/docs/ghl/products/delete-product-by-id

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_products_delete-product-by-id_screenshot.png

---

ProductsProductsDelete Product by ID
Delete Product by ID
DELETE
 https://services.leadconnectorhq.com/products/:productId
The "Delete Product by ID" API allows deleting a specific product using its unique identifier. Use this endpoint to remove a product from the system.
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
status
boolean
REQUIRED
returns true if the product is successfully deleted
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/products/:productId' \
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