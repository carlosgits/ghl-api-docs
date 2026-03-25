# Action to include/exclude the product in store

Source: https://marketplace.gohighlevel.com/docs/ghl/products/update-store-status

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_products_update-store-status_screenshot.png

---

ProductsStoreAction to include/exclude the product in store
Action to include/exclude the product in store
POST
 https://services.leadconnectorhq.com/products/store/:storeId
API to update the status of products in a particular store
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
PATH PARAMETERS
storeId
string
REQUIRED
Products related to the store
Example: 3SwdhCu3svxI8AKsPJt6
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
action
string
REQUIRED
Action to include or exclude the product from the store
Possible values: [include, exclude]
Example:include
productIds
string[]
REQUIRED
Array of product IDs
Example:["productId1","productId2"]
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
curl -L 'https://services.leadconnectorhq.com/products/store/:storeId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "action": "include",
  "productIds": [
    "productId1",
    "productId2"
  ]
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
storeId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "action": "include",
  "productIds": [
    "productId1",
    "productId2"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!