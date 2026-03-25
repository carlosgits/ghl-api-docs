# Get rebilling config for an app subscription and usage plans

Source: https://marketplace.gohighlevel.com/docs/ghl/marketplace/get-rebilling-config-for-app

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_marketplace_get-rebilling-config-for-app_screenshot.png

---

Developer marketplaceApp Billing ManagementGet rebilling config for an app subscription and usage plans
Get rebilling config for an app subscription and usage plans
GET
 https://services.leadconnectorhq.com/marketplace/app/:appId/rebilling-config/location/:locationId
Get rebilling config for an app subscription and usage plans for the authenticated sub-account. This endpoint returns the subscription and usage plans for an app.
Requirements
Scope(s)
oauth.readonly
Auth Method(s)
OAuth Access Token
Token Type(s)
Sub-Account Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
PATH PARAMETERS
appId
string
REQUIRED
ID of the app to get rebilling config
locationId
string
REQUIRED
Responses
200
400
403
Successfully retrieved rebilling config for the app
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
plans
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
curl -L 'https://services.leadconnectorhq.com/marketplace/app/:appId/rebilling-config/location/:locationId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
appId — path
REQUIRED
locationId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!