# Send invoice

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/send-invoice

Screenshot: images/ghl_invoices_send-invoice_screenshot.png

---

InvoiceInvoiceSend invoice
Send invoice
POST
 https://services.leadconnectorhq.com/invoices/:invoiceId/send
API to send invoice by invoice id
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
userId
string
REQUIRED
Please ensure that the UserId corresponds to an authorized personnel, either by an employee ID or agency ID, to access this location. This account will serve as the primary channel for all future communications and updates.
Example:6578278e879ad2646715ba9c
action
string
REQUIRED
Possible values: [sms_and_email, send_manually, email, sms]
liveMode
boolean
REQUIRED
sentFrom
object
autoPayment
object
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
invoice
object
REQUIRED
smsData
object
REQUIRED
emailData
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
curl -L 'https://services.leadconnectorhq.com/invoices/:invoiceId/send' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "userId": "6578278e879ad2646715ba9c",
  "action": "sms_and_email",
  "liveMode": true,
  "sentFrom": {
    "fromName": "Alex",
    "fromEmail": "alex@example.com"
  },
  "autoPayment": {
    "enable": true,
    "type": "string",
    "paymentMethodId": "string",
    "customerId": "string",
    "card": {
      "brand": "string",
      "last4": "string"
    },
    "usBankAccount": {
      "bank_name": "string",
      "last4": "string"
    },
    "sepaDirectDebit": {
      "bank_code": "string",
      "last4": "string",
      "branch_code": "string"
    },
    "bacsDirectDebit": {
      "sort_code": "string",
      "last4": "string"
    },
    "becsDirectDebit": {
      "bsb_number": "string",
      "last4": "string"
    },
    "cardId": "string",
    "provider": {}
  }
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
  "userId": "6578278e879ad2646715ba9c",
  "action": "sms_and_email",
  "liveMode": true,
  "sentFrom": {
    "fromName": "Alex",
    "fromEmail": "alex@example.com"
  },
  "autoPayment": {
    "enable": true,
    "type": "string",
    "paymentMethodId": "string",
    "customerId": "string",
    "card": {
      "brand": "string",
      "last4": "string"
    },
    "usBankAccount": {
      "bank_name": "string",
      "last4": "string"
    },
    "sepaDirectDebit": {
      "bank_code": "string",
      "last4": "string",
      "branch_code": "string"
    },
    "bacsDirectDebit": {
      "sort_code": "string",
      "last4": "string"
    },
    "becsDirectDebit": {
      "bsb_number": "string",
      "last4": "string"
    },
    "cardId": "string",
    "provider": {}
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!