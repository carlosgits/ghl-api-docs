# Pause location

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/pause-location-deprecated

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_saas_pause-location-deprecated_screenshot.png

---

SaasSaasPause location
Pause location
POST
 https://services.leadconnectorhq.com/saas-api/public-api/pause/:locationId
DEPRECATED
This endpoint has been deprecated and may be replaced or removed in future versions of the API.
Pause Sub account for given locationId
Requirements
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
Possible values: [2021-04-15]
API Version
PATH PARAMETERS
locationId
string
REQUIRED
Location ID to pause/unpause
Example: AUKAtFVo0lWezBsBQ3FE
APPLICATION/JSON
BODY
REQUIRED
paused
boolean
REQUIRED
Paused
Example:true
companyId
string
REQUIRED
Company ID
Example:companyId1
Responses
200
400
401
404
500
Location paused/unpaused successfully
APPLICATION/JSON
Schema
SCHEMA
boolean
boolean






















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
curl -L 'https://services.leadconnectorhq.com/saas-api/public-api/pause/:locationId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "paused": true,
  "companyId": "companyId1"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "paused": true,
  "companyId": "companyId1"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!