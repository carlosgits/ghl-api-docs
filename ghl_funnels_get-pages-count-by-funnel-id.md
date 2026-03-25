# Fetch count of funnel pages

Source: https://marketplace.gohighlevel.com/docs/ghl/funnels/get-pages-count-by-funnel-id

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_funnels_get-pages-count-by-funnel-id_screenshot.png

---

FunnelsFunnelFetch count of funnel pages
Fetch count of funnel pages
GET
 https://services.leadconnectorhq.com/funnels/page/count
Retrieves count of all funnel pages based on the given query parameters.
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
Responses
200
Successful response - Count of funnel pages returned
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
count
number
REQUIRED
Example:20



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
curl -L 'https://services.leadconnectorhq.com/funnels/page/count' \
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
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!