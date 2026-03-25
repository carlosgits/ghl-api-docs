# Get Blogs by Location ID

Source: https://marketplace.gohighlevel.com/docs/ghl/blogs/get-blogs

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_blogs_get-blogs_screenshot.png

---

BlogsBlogsGet Blogs by Location ID
Get Blogs by Location ID
GET
 https://services.leadconnectorhq.com/blogs/site/all
The "Get Blogs by Location ID" API allows you get blogs using Location ID.Please use blogs/list.readonly
Requirements
Scope(s)
blogs/list.readonly
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
skip
number
REQUIRED
Example: 0
limit
number
REQUIRED
Example: 4
searchTerm
string
search for any post by name
Example: ai news
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
data
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
curl -L 'https://services.leadconnectorhq.com/blogs/site/all' \
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
skip — query
REQUIRED
limit — query
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