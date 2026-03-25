# Create Custom Menu Link

Source: https://marketplace.gohighlevel.com/docs/ghl/custom-menus/create-custom-menu

Screenshot: images/ghl_custom-menus_create-custom-menu_screenshot.png

---

Custom menusCustom Menu LinksCreate Custom Menu Link
Create Custom Menu Link
POST
 https://services.leadconnectorhq.com/custom-menus/
Creates a new custom menu for a company. Requires authentication and proper permissions. For Icon Usage Details please refer to https://doc.clickup.com/8631005/d/h/87cpx-243696/d60fa70db6b92b2
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
APPLICATION/JSON
BODY
REQUIRED
title
string
REQUIRED
Title of the custom menu
Example:Custom Menu
url
string
REQUIRED
URL of the custom menu
Example:https://custom-menus.com/
icon
object
showOnCompany
boolean
REQUIRED
Whether the menu must be displayed on the agency's level
Default value: true
Example:true
showOnLocation
boolean
REQUIRED
Whether the menu must be displayed for sub-accounts level
Default value: true
Example:true
showToAllLocations
boolean
REQUIRED
Whether the menu must be displayed to all sub-accounts
Default value: true
Example:true
openMode
string
REQUIRED
Mode for opening the menu link
Possible values: [iframe, new_tab, current_tab]
locations
string[]
REQUIRED
List of sub-account IDs where the menu should be shown. This list is applicable only when showOnLocation is true and showToAllLocations is false
Example:["gfWreTIHL8pDbggBb7af","67WreTIHL8pDbggBb7ty"]
userRole
string
REQUIRED
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
201
400
401
403
422
Custom menu successfully created
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
curl -L 'https://services.leadconnectorhq.com/custom-menus/' \
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