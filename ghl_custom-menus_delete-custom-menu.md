# Delete Custom Menu Link

Source: https://marketplace.gohighlevel.com/docs/ghl/custom-menus/delete-custom-menu

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_custom-menus_delete-custom-menu_screenshot.png

---

Custom menusCustom Menu LinksDelete Custom Menu Link
Delete Custom Menu Link
DELETE
 https://services.leadconnectorhq.com/custom-menus/:customMenuId
Removes a specific custom menu from the system. This operation requires authentication and proper permissions. The custom menu is identified by its unique ID, and the operation is performed within the context of a specific company.
Requirements
Scope(s)
custom-menu-link.write
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
ID of the custom menu to delete
Example: 62e589c1-c456-47e1-a9a7-cb8900014311
Responses
200
400
401
403
404
422
Custom menu successfully deleted
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
Indicates whether the custom menu was successfully deleted
Example:true
message
string
A message providing additional information about the deletion operation
Example:Custom menu successfully deleted
deletedMenuId
string
The ID of the deleted custom menu
Example:12345abcde
deletedAt
date-time
Timestamp of when the deletion was performed
Example:2023-09-12T15:30:45.123Z


















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
curl -L -X DELETE 'https://services.leadconnectorhq.com/custom-menus/:customMenuId' \
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