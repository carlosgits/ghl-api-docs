# Get Blog posts by Blog ID

Source: https://marketplace.gohighlevel.com/docs/ghl/blogs/get-blog-post

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_blogs_get-blog-post_screenshot.png

---

BlogsBlogsGet Blog posts by Blog ID
Get Blog posts by Blog ID
GET
 https://services.leadconnectorhq.com/blogs/posts/all
The "Get Blog posts by Blog ID" API allows you get blog posts for any given blog site using blog ID.Please use blogs/posts.readonly
Requirements
Scope(s)
blogs/posts.readonly
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
blogId
string
REQUIRED
Example: 66f429b8afdce84227a4610d
limit
number
REQUIRED
Example: 4
offset
number
REQUIRED
Example: 0
searchTerm
string
search for any post by name
Example: ai news
status
string
Possible values: [ALL, PUBLISHED, SCHEDULED, ARCHIVED, DRAFT]
Example: PUBLISHED
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
blogs
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
curl -L 'https://services.leadconnectorhq.com/blogs/posts/all' \
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
blogId — query
REQUIRED
limit — query
REQUIRED
offset — query
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