# Update estimate last visited at

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/update-estimate-last-visited-at

Screenshot: images/ghl_invoices_update-estimate-last-visited-at_screenshot.png

---

InvoiceEstimateUpdate estimate last visited at
Update estimate last visited at
PATCH
 https://services.leadconnectorhq.com/invoices/estimate/stats/last-visited-at
API to update estimate last visited at by estimate id
Requirements
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Agency Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
APPLICATION/JSON
BODY
REQUIRED
estimateId
string
REQUIRED
Estimate Id
Example:5f9d6d8b1b2d2c001f2d9e4b
Responses
200
400
401









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
curl -L -X PATCH 'https://services.leadconnectorhq.com/invoices/estimate/stats/last-visited-at' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "estimateId": "5f9d6d8b1b2d2c001f2d9e4b"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Security Scheme
Location-Access
Agency-Access
Bearer Token
Parameters
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "estimateId": "5f9d6d8b1b2d2c001f2d9e4b"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!