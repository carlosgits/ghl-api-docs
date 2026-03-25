# Generate Invoice Number

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/generate-invoice-number

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_invoices_generate-invoice-number_screenshot.png

---

InvoiceInvoiceGenerate Invoice Number
Generate Invoice Number
GET
 https://services.leadconnectorhq.com/invoices/generate-invoice-number
Get the next invoice number for the given location
Requirements
Scope(s)
invoices.readonly
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
QUERY PARAMETERS
altId
string
REQUIRED
Location Id
altType
string
REQUIRED
Possible values: [location]
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
invoiceNumber
number
Invoice Number
Example:19



















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
curl -L 'https://services.leadconnectorhq.com/invoices/generate-invoice-number' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
altId — query
REQUIRED
altType — query
REQUIRED
---
location
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!