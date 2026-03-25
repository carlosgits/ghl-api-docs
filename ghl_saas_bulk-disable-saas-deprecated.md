# Disable SaaS for locations

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/bulk-disable-saas-deprecated

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_saas_bulk-disable-saas-deprecated_screenshot.png

---

SaasSaasDisable SaaS for locations
Disable SaaS for locations
POST
 https://services.leadconnectorhq.com/saas-api/public-api/bulk-disable-saas/:companyId
DEPRECATED
This endpoint has been deprecated and may be replaced or removed in future versions of the API.
Disable SaaS for locations for given locationIds
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
companyId
string
REQUIRED
Company ID to disable SaaS for
Example: 5DP4iH6HLkQsiKESj6rh
APPLICATION/JSON
BODY
REQUIRED
locationIds
string[]
REQUIRED
Location IDs
Example:["locationId1","locationId2"]
Responses
200
400
401
404
500
SaaS disabled successfully for locations
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
data
object
REQUIRED
Response data from the bulk disable SaaS operation
Example:{"msg":"success"}



























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
curl -L 'https://services.leadconnectorhq.com/saas-api/public-api/bulk-disable-saas/:companyId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationIds": [
    "locationId1",
    "locationId2"
  ]
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
companyId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "locationIds": [
    "locationId1",
    "locationId2"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!