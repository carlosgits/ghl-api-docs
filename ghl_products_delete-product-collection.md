# Delete Product Collection

Source: https://marketplace.gohighlevel.com/docs/ghl/products/delete-product-collection

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_products_delete-product-collection_screenshot.png

---

ProductsCollectionsDelete Product Collection
Delete Product Collection
DELETE
 https://services.leadconnectorhq.com/products/collections/:collectionId
Delete specific product collection with Id :collectionId
Requirements
Scope(s)
products/collection.write
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
collectionId
string
REQUIRED
MongoId of the collection
Example: 65d71377c326ea78e1c47df5
QUERY PARAMETERS
altId
string
REQUIRED
Location Id
Example: 6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
The type of alt. For now it is only LOCATION
Example: LOCATION
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/products/collections/:collectionId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
collectionId — path
REQUIRED
altId — query
REQUIRED
altType — query
REQUIRED
---
location
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!