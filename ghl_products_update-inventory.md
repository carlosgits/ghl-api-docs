# Update Inventory

Source: https://marketplace.gohighlevel.com/docs/ghl/products/update-inventory

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_products_update-inventory_screenshot.png

---

ProductsPricesUpdate Inventory
Update Inventory
POST
 https://services.leadconnectorhq.com/products/inventory
The Update Inventory API allows the user to bulk update the inventory for multiple items. Use this endpoint to update the available quantity and out-of-stock purchase settings for multiple items in the inventory.
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
items
object[]
REQUIRED
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
curl -L 'https://services.leadconnectorhq.com/products/inventory' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "items": [
    {
      "priceId": "5e9f8f8f8f8f8f8f8f8f8f8",
      "availableQuantity": 10,
      "allowOutOfStockPurchases": false
    }
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
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "items": [
    {
      "priceId": "5e9f8f8f8f8f8f8f8f8f8f8",
      "availableQuantity": 10,
      "allowOutOfStockPurchases": false
    }
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!