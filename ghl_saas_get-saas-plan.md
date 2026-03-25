# Get SaaS Plan

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/get-saas-plan

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_saas_get-saas-plan_screenshot.png

---

SaasSaasGet SaaS Plan
Get SaaS Plan
GET
 https://services.leadconnectorhq.com/saas/saas-plan/:planId
Fetch a specific SaaS plan by plan ID
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
planId
string
REQUIRED
QUERY PARAMETERS
companyId
string
REQUIRED
Responses
200
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
curl -L 'https://services.leadconnectorhq.com/saas/saas-plan/:planId' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
planId — path
REQUIRED
companyId — query
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!