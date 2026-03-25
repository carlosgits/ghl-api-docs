# Delete Opportunity

Source: https://marketplace.gohighlevel.com/docs/ghl/opportunities/delete-opportunity

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_opportunities_delete-opportunity_screenshot.png

---

OpportunitiesOpportunitiesDelete Opportunity
Delete Opportunity
DELETE
 https://services.leadconnectorhq.com/opportunities/:id
Delete Opportunity
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/opportunities/:id' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!