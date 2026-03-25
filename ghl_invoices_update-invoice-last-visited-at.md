# Update invoice last visited at

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/update-invoice-last-visited-at

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_invoices_update-invoice-last-visited-at_screenshot.png

---

InvoiceInvoiceUpdate invoice last visited at
Update invoice last visited at
PATCH
 https://services.leadconnectorhq.com/invoices/stats/last-visited-at
API to update invoice last visited at by invoice id
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
invoiceId
string
REQUIRED
Invoice Id
Example:6578278e879ad2646715ba9c
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
curl -L -X PATCH 'https://services.leadconnectorhq.com/invoices/stats/last-visited-at' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "invoiceId": "6578278e879ad2646715ba9c"
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
  "invoiceId": "6578278e879ad2646715ba9c"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!