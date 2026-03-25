# Get Agency Plans

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/get-agency-plans

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_saas_get-agency-plans_screenshot.png

---

SaasSaasGet Agency Plans
Get Agency Plans
GET
 https://services.leadconnectorhq.com/saas/agency-plans/:companyId
Fetch all agency subscription plans for a given company ID
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
curl -L 'https://services.leadconnectorhq.com/saas/agency-plans/:companyId' \
-H 'Authorization: Bearer <TOKEN>'
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
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!