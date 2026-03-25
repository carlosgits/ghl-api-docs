# Create Invoice from Estimate

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/create-invoice-from-estimate

Screenshot: images/ghl_invoices_create-invoice-from-estimate_screenshot.png

---

InvoiceEstimateCreate Invoice from Estimate
Create Invoice from Estimate
POST
 https://services.leadconnectorhq.com/invoices/estimate/:estimateId/invoice
Create a new invoice from an existing estimate
Requirements
Scope(s)
invoices/estimate.write
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
PATH PARAMETERS
estimateId
string
REQUIRED
Estimate Id
Example: 5f9d6d8b1b2d2c001f2d9e4b
APPLICATION/JSON
BODY
REQUIRED
altId
string
REQUIRED
Location Id or Agency Id
Example:6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
markAsInvoiced
boolean
REQUIRED
Mark Estimate as Invoiced
Example:true
version
string
Version of the update request
Possible values: [v1, v2]
Example:v2
Responses
200
400
401
422
Successfully Created
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
estimate
object
invoice
object
































































































































































































































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
curl -L 'https://services.leadconnectorhq.com/invoices/estimate/:estimateId/invoice' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "markAsInvoiced": true,
  "version": "v2"
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
estimateId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "markAsInvoiced": true,
  "version": "v2"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!