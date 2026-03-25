# Fetch Timezones

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/get-timezones

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_locations_get-timezones_screenshot.png

---

Sub-Account (Formerly location)TimezoneFetch Timezones
Fetch Timezones
GET
 https://services.leadconnectorhq.com/locations/:locationId/timezones
Fetch the available timezones
Requirements
Scope(s)
locations.readonly
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
Responses
200
400
401
422
Successful response
















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
curl -L 'https://services.leadconnectorhq.com/locations/:locationId/timezones' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Security Scheme
bearer
Location-Access
Bearer Token
Parameters
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!