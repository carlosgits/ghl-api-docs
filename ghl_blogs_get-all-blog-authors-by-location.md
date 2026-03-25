# Get all authors

Source: https://marketplace.gohighlevel.com/docs/ghl/blogs/get-all-blog-authors-by-location

Screenshot: images/ghl_blogs_get-all-blog-authors-by-location_screenshot.png

---

BlogsBlogsGet all authors
Get all authors
GET
 https://services.leadconnectorhq.com/blogs/authors
The "Get all authors" Api return the blog authors for a given location ID. Please use "blogs/author.readonly"
Requirements
Scope(s)
blogs/author.readonly
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
Location Id
Example: ve9EPM428h8vShlRW1KT
limit
number
REQUIRED
Number of authors to show in the listing
Example: 5
offset
number
REQUIRED
Number of authors to skip in listing
Example: 0
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
authors
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
curl -L 'https://services.leadconnectorhq.com/blogs/authors' \
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