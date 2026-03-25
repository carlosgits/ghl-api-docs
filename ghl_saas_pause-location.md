# Pause location

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/pause-location

Screenshot: images/ghl_saas_pause-location_screenshot.png

---

SaasSaasPause location
Pause location
POST
 https://services.leadconnectorhq.com/saas/pause/:locationId
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
201
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
curl -L 'https://services.leadconnectorhq.com/saas/pause/:locationId' \
-H 'Content-Type: application/json' \
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