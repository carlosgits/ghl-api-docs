# Update Opportunity Status

Source: https://marketplace.gohighlevel.com/docs/ghl/opportunities/update-opportunity-status

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_opportunities_update-opportunity-status_screenshot.png

---

OpportunitiesOpportunitiesUpdate Opportunity Status
Update Opportunity Status
PUT
 https://services.leadconnectorhq.com/opportunities/:id/status
Update Opportunity Status
Requirements
Scope(s)
opportunities.write
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
PATH PARAMETERS
id
string
REQUIRED
Opportunity Id
Example: yWQobCRIhRguQtD2llvk
APPLICATION/JSON
BODY
REQUIRED
status
string
REQUIRED
Possible values: [open, won, lost, abandoned, all]
lostReasonId
string
lost reason Id
Example:CLu7BaljjqrEjBGKTNNe
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
succeded
boolean
Example:true



















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
curl -L -X PUT 'https://services.leadconnectorhq.com/opportunities/:id/status' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "status": "open",
  "lostReasonId": "CLu7BaljjqrEjBGKTNNe"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
id — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "status": "open",
  "lostReasonId": "CLu7BaljjqrEjBGKTNNe"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!