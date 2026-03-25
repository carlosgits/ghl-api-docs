# Record a manual payment for an invoice

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/record-invoice

Screenshot: images/ghl_invoices_record-invoice_screenshot.png

---

InvoiceInvoiceRecord a manual payment for an invoice
Record a manual payment for an invoice
POST
 https://services.leadconnectorhq.com/invoices/:invoiceId/record-payment
API to record manual payment for an invoice by invoice id
Requirements
Scope(s)
invoices.write
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
invoiceId
string
REQUIRED
Invoice Id
Example: 6578278e879ad2646715ba9c
APPLICATION/JSON
BODY
REQUIRED
altId
string
REQUIRED
location Id / company Id based on altType
Example:6578278e879ad2646715ba9c
altType
string
REQUIRED
Alt Type
Possible values: [location]
Example:location
mode
string
REQUIRED
manual payment method
Possible values: [cash, card, cheque, bank_transfer, other]
Example:card
card
object
REQUIRED
cheque
object
REQUIRED
notes
string
REQUIRED
Any note to be recorded with the transaction
Example:This was a direct payment
amount
number
Amount to be paid against the invoice.
Example:999
meta
object
paymentScheduleIds
string[]
Payment Schedule Ids to be recorded against the invoice.
Example:["6578278e879ad2646715ba9c"]
fulfilledAt
string
Updated At to be recorded against the invoice.
Example:2025-03-19T05:03:00.000Z
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
success
boolean
REQUIRED
status
Example:true
invoice
object
REQUIRED














































































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
curl -L 'https://services.leadconnectorhq.com/invoices/:invoiceId/record-payment' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "mode": "card",
  "card": {
    "brand": "string",
    "last4": "string"
  },
  "cheque": {
    "number": "129-129-129-912"
  },
  "notes": "This was a direct payment",
  "amount": 999,
  "meta": {},
  "paymentScheduleIds": [
    "6578278e879ad2646715ba9c"
  ],
  "fulfilledAt": "2025-03-19T05:03:00.000Z"
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
invoiceId — path
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
  "mode": "card",
  "card": {
    "brand": "string",
    "last4": "string"
  },
  "cheque": {
    "number": "129-129-129-912"
  },
  "notes": "This was a direct payment",
  "amount": 999,
  "meta": {},
  "paymentScheduleIds": [
    "6578278e879ad2646715ba9c"
  ],
  "fulfilledAt": "2025-03-19T05:03:00.000Z"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!