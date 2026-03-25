# Fetch list of funnel pages

Source: https://marketplace.gohighlevel.com/docs/ghl/funnels/get-pages-by-funnel-id

Screenshot: images/ghl_funnels_get-pages-by-funnel-id_screenshot.png

---

FunnelsFunnelFetch list of funnel pages
Fetch list of funnel pages
GET
 https://services.leadconnectorhq.com/funnels/page
Retrieves a list of all funnel pages based on the given query parameters.
Requirements
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
QUERY PARAMETERS
locationId
string
REQUIRED
funnelId
string
REQUIRED
name
string
limit
number
REQUIRED
offset
number
REQUIRED
Responses
200
Successful response - List of funnel pages returned
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
_id
string
REQUIRED
Example:0yJbP3q7t7pLmeTWRAE2
locationId
string
REQUIRED
Example:ojQjykmwNIU88vfsfzvH
funnelId
string
REQUIRED
Example:iucJ6TdFZiddhq9f6znh
name
string
REQUIRED
Example:Home
stepId
string
REQUIRED
Example:343bf634-3aa6-4ade-b963-2d3cd0bf2ede
deleted
string
REQUIRED
Example:false
updatedAt
string
REQUIRED
Example:2024-04-18T12:25:23.029Z









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
curl -L 'https://services.leadconnectorhq.com/funnels/page' \
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
funnelId — query
REQUIRED
limit — query
REQUIRED
offset — query
REQUIRED
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!