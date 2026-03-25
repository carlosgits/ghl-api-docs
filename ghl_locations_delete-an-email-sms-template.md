# DELETE an email/sms template

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/delete-an-email-sms-template

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_locations_delete-an-email-sms-template_screenshot.png

---

Sub-Account (Formerly location)TemplateDELETE an email/sms template
DELETE an email/sms template
DELETE
 https://services.leadconnectorhq.com/locations/:locationId/templates/:id
DELETE an email/sms template
Requirements
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
locationId
string
REQUIRED
Location Id
Example: ve9EPM428h8vShlRW1KT
id
string
REQUIRED
Template Id
Example: ve9EPM428h8vShlRW1KT
Responses
200
400
401
422
















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
curl -L -X DELETE 'https://services.leadconnectorhq.com/locations/:locationId/templates/:id' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — path
REQUIRED
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