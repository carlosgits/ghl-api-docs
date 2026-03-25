# Get Store Settings

Source: https://marketplace.gohighlevel.com/docs/ghl/store/get-store-settings

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_store_get-store-settings_screenshot.png

---

StoreStore SettingGet Store Settings
Get Store Settings
GET
 https://services.leadconnectorhq.com/store/store-setting
Get store settings by altId and altType.
Requirements
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
QUERY PARAMETERS
altId
string
REQUIRED
Location Id or Agency Id
Example: 6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
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
status
boolean
REQUIRED
Status of api action
Example:true
message
string
Success message
Example:Successfully created
data
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
curl -L 'https://services.leadconnectorhq.com/store/store-setting' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
altId — query
REQUIRED
altType — query
REQUIRED
---
location
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!