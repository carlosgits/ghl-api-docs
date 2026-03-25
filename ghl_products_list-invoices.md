# List Products

Source: https://marketplace.gohighlevel.com/docs/ghl/products/list-invoices

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_products_list-invoices_screenshot.png

---

ProductsProductsList Products
List Products
GET
 https://services.leadconnectorhq.com/products/
The "List Products" API allows to retrieve a paginated list of products. Customize your results by filtering products based on name or paginate through the list using the provided query parameters. This endpoint provides a straightforward way to explore and retrieve product information.
Requirements
Scope(s)
products.readonly
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
QUERY PARAMETERS
limit
number
The maximum number of items to be included in a single page of results
Default value:0
Example: 20
offset
number
The starting index of the page, indicating the position from which the results should be retrieved.
Default value:0
Example: 0
locationId
string
REQUIRED
LocationId is the id of the sub-account
Example: 3SwdhCu3svxI8AKsPJt6
search
string
The name of the product for searching.
Example: Awesome product
collectionIds
string
Filter by product category Ids. Supports comma separated values
collectionSlug
string
The slug value of the collection by which the collection would be searched
expand
string[]
Name of an entity whose data has to be fetched along with product. Possible entities are tax, stripe and paypal. If not mentioned, only ID will be returned in case of taxes
productIds
string[]
List of product ids to be fetched.
storeId
string
fetch and project products based on the storeId
Example: 3SwdhCu3svxI8AKsPJt6
includedInStore
boolean
Separate products by which are included in the store and which are not
Example:
availableInStore
boolean
If the product is included in the online store
Example:
sortOrder
string
Possible values: [asc, desc]
The order of sort which should be applied for the date
Example: desc
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
products
object[]
REQUIRED
total
object[]
REQUIRED
































































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
curl -L 'https://services.leadconnectorhq.com/products/' \
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