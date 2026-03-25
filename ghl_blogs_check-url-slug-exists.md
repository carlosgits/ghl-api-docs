# Check url slug

Source: https://marketplace.gohighlevel.com/docs/ghl/blogs/check-url-slug-exists

Screenshot: images/ghl_blogs_check-url-slug-exists_screenshot.png

---

BlogsBlogsCheck url slug
Check url slug
GET
 https://services.leadconnectorhq.com/blogs/posts/url-slug-exists
The "Check url slug" API allows check the blog slug validation which is needed before publishing any blog post. Please use blogs/check-slug.readonly. you can find the POST ID from the post edit url.
Requirements
Scope(s)
blogs/check-slug.readonly
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
urlSlug
string
REQUIRED
locationId
string
REQUIRED
Example: ve9EPM428h8vShlRW1KT
postId
string
Example: 66f429b8afdce84227a4610d
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
exists
boolean
REQUIRED
Indicates whether the url slug exists or not



















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
curl -L 'https://services.leadconnectorhq.com/blogs/posts/url-slug-exists' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
urlSlug — query
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