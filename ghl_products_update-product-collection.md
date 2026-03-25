# Update Product Collection

Source: https://marketplace.gohighlevel.com/docs/ghl/products/update-product-collection

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_products_update-product-collection_screenshot.png

---

ProductsCollectionsUpdate Product Collection
Update Product Collection
PUT
 https://services.leadconnectorhq.com/products/collections/:collectionId
Update a specific product collection with Id :collectionId
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
APPLICATION/JSON
BODY
REQUIRED
altId
string
REQUIRED
Location Id
Example:6578278e879ad2646715ba9c
altType
string
REQUIRED
The type of alt. For now it is only LOCATION
Possible values: [location]
Example:LOCATION
name
string
Name of the Product Collection
Example:Best Sellers
slug
string
Slug of the Product Collection which helps in navigation
Example:best-sellers
image
string
The URL of the image that is going to be displayed as the collection Thumbnail
Example:http://example.com/watermark.png
seo
object
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
curl -L -X PUT 'https://services.leadconnectorhq.com/products/collections/:collectionId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "LOCATION",
  "name": "Best Sellers",
  "slug": "best-sellers",
  "image": "http://example.com/watermark.png",
  "seo": {
    "title": "Best Sellers",
    "description": "Collections where all the best products are available"
  }
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
collectionId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "LOCATION",
  "name": "Best Sellers",
  "slug": "best-sellers",
  "image": "http://example.com/watermark.png",
  "seo": {
    "title": "Best Sellers",
    "description": "Collections where all the best products are available"
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!