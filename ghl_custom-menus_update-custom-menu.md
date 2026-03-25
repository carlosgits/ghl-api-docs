# Update Custom Menu Link

Source: https://marketplace.gohighlevel.com/docs/ghl/custom-menus/update-custom-menu

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_custom-menus_update-custom-menu_screenshot.png

---

Custom menusCustom Menu LinksUpdate Custom Menu Link
Update Custom Menu Link
PUT
 https://services.leadconnectorhq.com/custom-menus/:customMenuId
Updates an existing custom menu for a given company. Requires authentication and proper permissions.
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
ID of the custom menu to update
Example: 62e589c1-c456-47e1-a9a7-cb8900014311
APPLICATION/JSON
BODY
REQUIRED
title
string
Title of the custom menu
Example:Custom Menu
url
string
URL of the custom menu
Example:https://custom-menus.com/
icon
object
showOnCompany
boolean
Whether the menu must be displayed on the agency's level
Default value: true
Example:true
showOnLocation
boolean
Whether the menu must be displayed for sub-accounts level
Default value: true
Example:true
showToAllLocations
boolean
Whether the menu must be displayed to all sub-accounts
Default value: true
Example:true
openMode
string
Mode for opening the menu link
Possible values: [iframe, new_tab, current_tab]
locations
string[]
List of sub-account IDs where the menu should be shown. This list is applicable only when showOnLocation is true and showToAllLocations is false
Example:["gfWreTIHL8pDbggBb7af","67WreTIHL8pDbggBb7ty"]
userRole
string
Which user-roles should the menu be accessible to?
Possible values: [all, admin, user]
allowCamera
boolean
Whether to allow camera access (only for iframe mode)
Example:false
allowMicrophone
boolean
Whether to allow microphone access (only for iframe mode)
Example:false
Responses
200
400
401
403
404
422
Custom menu successfully updated
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
Status of update
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
curl -L -X PUT 'https://services.leadconnectorhq.com/custom-menus/:customMenuId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "title": "Custom Menu",
  "url": "https://custom-menus.com/",
  "icon": {
    "name": "yin-yang",
    "fontFamily": "fab"
  },
  "showOnCompany": true,
  "showOnLocation": true,
  "showToAllLocations": true,
  "openMode": "iframe",
  "locations": [
    "gfWreTIHL8pDbggBb7af",
    "67WreTIHL8pDbggBb7ty"
  ],
  "userRole": "all",
  "allowCamera": false,
  "allowMicrophone": false
}'
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
Body
 REQUIRED
{
  "title": "Custom Menu",
  "url": "https://custom-menus.com/",
  "icon": {
    "name": "yin-yang",
    "fontFamily": "fab"
  },
  "showOnCompany": true,
  "showOnLocation": true,
  "showToAllLocations": true,
  "openMode": "iframe",
  "locations": [
    "gfWreTIHL8pDbggBb7af",
    "67WreTIHL8pDbggBb7ty"
  ],
  "userRole": "all",
  "allowCamera": false,
  "allowMicrophone": false
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!