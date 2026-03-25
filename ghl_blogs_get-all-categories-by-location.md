# Get all categories

Source: https://marketplace.gohighlevel.com/docs/ghl/blogs/get-all-categories-by-location

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_blogs_get-all-categories-by-location_screenshot.png

---

BlogsBlogsGet all categories
Get all categories
GET
 https://services.leadconnectorhq.com/blogs/categories
The "Get all categories" Api return the blog categoies for a given location ID. Please use "blogs/category.readonly"
Requirements
Scope(s)
blogs/category.readonly
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
QUERY PARAMETERS
locationId
string
REQUIRED
Example: ve9EPM428h8vShlRW1KT
limit
number
REQUIRED
Number of categories to show in the listing
offset
number
REQUIRED
Number of categories to skip in listing
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
categories
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
curl -L 'https://services.leadconnectorhq.com/blogs/categories' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — query
REQUIRED
limit — query
REQUIRED
offset — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!