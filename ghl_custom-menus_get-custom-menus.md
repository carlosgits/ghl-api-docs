# Get Custom Menu Links

Source: https://marketplace.gohighlevel.com/docs/ghl/custom-menus/get-custom-menus

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_custom-menus_get-custom-menus_screenshot.png

---

Custom menusCustom Menu LinksGet Custom Menu Links
Get Custom Menu Links
GET
 https://services.leadconnectorhq.com/custom-menus/
Fetches a collection of custom menus based on specified criteria. This endpoint allows clients to retrieve custom menu configurations, which may include menu items, categories, and associated metadata. The response can be tailored using query parameters for filtering, sorting, and pagination.
Requirements
Scope(s)
custom-menu-link.readonly
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Agency Token
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
Unique identifier of the location
Example: 5DP4iH6HLkQsiKESj6rh
skip
number
Number of items to skip for pagination
Default value:0
Example: 0
limit
number
Possible values: >= 1
Maximum number of items to return
Default value:20
Example: 10
query
string
Search query to filter custom menus by name, supports partial || full names
Example: custom-menu-link-name
showOnCompany
boolean
Filter to show only agency-level menu links. When omitted, fetches both agency and sub-account menu links. Ignored if locationId is provided
Example:
Responses
200
400
401
403
422
Successfully retrieved custom menus. Returns an array of custom menu objects, potentially including their structure, items, and relevant metadata.
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
customMenus
object[]
totalLinks
number
Total number of custom menu records
Example:100






































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
curl -L 'https://services.leadconnectorhq.com/custom-menus/' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
Version — header
REQUIRED
---
2021-07-28
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!