# Create Product Collection

Source: https://marketplace.gohighlevel.com/docs/ghl/products/create-product-collection

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_products_create-product-collection_screenshot.png

---

ProductsCollectionsCreate Product Collection
Create Product Collection
POST
 https://services.leadconnectorhq.com/products/collections
Create a new Product Collection for a specific location
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
collectionId
string
Unique Identifier of the Product Collection, Mongo Id
Example:66057f9d28536eae584ec047
name
string
REQUIRED
Name of the Product Collection
Example:Best Sellers
slug
string
REQUIRED
Slug of the Product Collection which helps in navigation
Example:best-sellers
image
string
The URL of the image that is going to be displayed as the collection Thumbnail
Example:http://example.com/watermark.png
seo
object
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
data
object






























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
curl -L 'https://services.leadconnectorhq.com/products/collections' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "LOCATION",
  "collectionId": "66057f9d28536eae584ec047",
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
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "LOCATION",
  "collectionId": "66057f9d28536eae584ec047",
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