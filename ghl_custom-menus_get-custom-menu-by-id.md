# Get Custom Menu Link

Source: https://marketplace.gohighlevel.com/docs/ghl/custom-menus/get-custom-menu-by-id

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_custom-menus_get-custom-menu-by-id_screenshot.png

---

Custom menusCustom Menu LinksGet Custom Menu Link
Get Custom Menu Link
GET
 https://services.leadconnectorhq.com/custom-menus/:customMenuId
Fetches a single custom menus based on id. This endpoint allows clients to retrieve custom menu configurations, which may include menu items, categories, and associated metadata
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
PATH PARAMETERS
customMenuId
string
REQUIRED
Unique identifier of the custom menu
Example: 62e589c1-c456-47e1-a9a7-cb8900014311
Responses
200
400
401
403
422
Successfully retrieved custom menu. Returns a single custom menu object, potentially including its structure, items, and relevant metadata.
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
customMenu
object



































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
curl -L 'https://services.leadconnectorhq.com/custom-menus/:customMenuId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
customMenuId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!