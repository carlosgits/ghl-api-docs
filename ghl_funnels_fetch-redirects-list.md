# Fetch List of Redirects

Source: https://marketplace.gohighlevel.com/docs/ghl/funnels/fetch-redirects-list

Screenshot: images/ghl_funnels_fetch-redirects-list_screenshot.png

---

FunnelsRedirectFetch List of Redirects
Fetch List of Redirects
GET
 https://services.leadconnectorhq.com/funnels/lookup/redirect/list
Retrieves a list of all URL redirects based on the given query parameters.
Requirements
Scope(s)
funnels/redirect.readonly
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
Example: 6p2RxpgtMKQwO3E6IUaT
limit
number
REQUIRED
Example: 20
offset
number
REQUIRED
Example: 10
search
string
Example: example.com/test
Responses
200
422
Successful response - List of URL redirects returned
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
data
object
REQUIRED
Object containing the count of redirects and an array of redirect data
Example:{"count":42,"data":[]}






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
curl -L 'https://services.leadconnectorhq.com/funnels/lookup/redirect/list' \
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
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!