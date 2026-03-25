# List Prices for a Product

Source: https://marketplace.gohighlevel.com/docs/ghl/products/list-prices-for-product

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_products_list-prices-for-product_screenshot.png

---

ProductsPricesList Prices for a Product
List Prices for a Product
GET
 https://services.leadconnectorhq.com/products/:productId/price
The "List Prices for a Product" API allows retrieving a paginated list of prices associated with a specific product. Customize your results by filtering prices or paginate through the list using the provided query parameters.
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
The unique identifier for the location.
Example: 3SwdhCsvxI8Au3KsPJt6
ids
string
To filter the response only with the given price ids, Please provide with comma separated
Example: 6241712be68f7a98102ba272,632027d51f7876cd3020213d
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
prices
object[]
REQUIRED
total
number
REQUIRED
Default value: Total number of prices available
Example:10




















































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
curl -L 'https://services.leadconnectorhq.com/products/:productId/price' \
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