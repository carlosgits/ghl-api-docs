# Search Trigger Links

Source: https://marketplace.gohighlevel.com/docs/ghl/links/search-trigger-links

Screenshot: images/ghl_links_search-trigger-links_screenshot.png

---

Trigger LinksTrigger Links SearchSearch Trigger Links
Search Trigger Links
GET
 https://services.leadconnectorhq.com/links/search
Get list of links by searching
Requirements
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
HEADER PARAMETERS
Authorization
string
REQUIRED
Access Token
Example: Bearer 9c48df2694a849b6089f9d0d3513efe
Version
string
REQUIRED
Possible values: [2021-04-15]
API Version
QUERY PARAMETERS
locationId
string
REQUIRED
Location Id
Example: ABCHkzuJQ8ZMd4Te84GK
query
string
Search query as a string
Example: Search string
skip
number
Numbers of query results to skip
Default value:0
Example: 1
limit
number
Limit on number of search results
Default value:20
Example: 10
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
links
object[]




















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
curl -L 'https://services.leadconnectorhq.com/links/search' \
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
Authorization — header
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!