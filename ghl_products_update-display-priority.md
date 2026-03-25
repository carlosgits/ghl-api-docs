# Update product display priorities in store

Source: https://marketplace.gohighlevel.com/docs/ghl/products/update-display-priority

Screenshot: images/ghl_products_update-display-priority_screenshot.png

---

ProductsStoreUpdate product display priorities in store
Update product display priorities in store
POST
 https://services.leadconnectorhq.com/products/store/:storeId/priority
API to set the display priority of products in a store
Requirements
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
products
array[]
REQUIRED
Array of products with their display priorities
Responses
200
400
401
Successfully updated display priorities









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
curl -L 'https://services.leadconnectorhq.com/products/store/:storeId/priority' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "products": [
    [
      null
    ]
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
  "products": [
    [
      null
    ]
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!