# Update invoice late fees configuration

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/update-invoice-late-fees-configuration

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_invoices_update-invoice-late-fees-configuration_screenshot.png

---

InvoiceInvoiceUpdate invoice late fees configuration
Update invoice late fees configuration
PATCH
 https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration
API to update invoice late fees configuration by invoice id
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
lateFeesConfiguration
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
_id
string
REQUIRED
Invoice Id
Example:6578278e879ad2646715ba9c
status
string
REQUIRED
Invoice Status
Possible values: [draft, sent, payment_processing, paid, void, partially_paid]
Example:draft
liveMode
boolean
REQUIRED
Live Mode
Example:false
amountPaid
number
REQUIRED
Amount Paid
Example:0
altId
string
REQUIRED
Location Id or Agency Id
Example:6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
name
string
REQUIRED
Name of the invoice
Example:New Invoice
businessDetails
object
REQUIRED
Business Details
Example:{"name":"Alex","address":{"addressLine1":"9931 Beechwood","city":"St. Houston","state":"TX","countryCode":"USA","postalCode":"559-6993"},"phoneNo":"+1-214-559-6993","website":"www.example.com"}
invoiceNumber
number
REQUIRED
Invoice Number
Example:19
currency
string
REQUIRED
Currency
Example:USD
contactDetails
object
REQUIRED
Contact Details
Example:{"id":"c6tZZU0rJBf30ZXx9Gli","phoneNo":"+1-214-559-6993","email":"alex@example.com","customFields":[],"name":"Alex","address":{"countryCode":"US"}}
issueDate
string
REQUIRED
Issue date in YYYY-MM-DD format
Example:2023-01-01
dueDate
string
REQUIRED
Due date in YYYY-MM-DD format
Example:2023-01-01
discount
object
Discount
Example:{"type":"percentage","value":0}
invoiceItems
string[]
REQUIRED
Invoice Items
Example:[{"taxes":[],"_id":"c6tZZU0rJBf30ZXx9Gli","productId":"c6tZZU0rJBf30ZXx9Gli","priceId":"c6tZZU0rJBf30ZXx9Gli","currency":"USD","name":"Macbook Pro","qty":1,"amount":999}]
total
number
REQUIRED
Total Amount
Example:999
title
string
REQUIRED
Title
Example:INVOICE
amountDue
number
REQUIRED
Total Amount Due
Example:999
createdAt
string
REQUIRED
created at
Example:2023-12-12T09:27:42.355Z
updatedAt
string
REQUIRED
updated at
Example:2023-12-12T09:27:42.355Z
automaticTaxesEnabled
boolean
Automatic taxes enabled for the Invoice
Example:true
automaticTaxesCalculated
boolean
Is Automatic taxes calculated for the Invoice items
Example:true
paymentSchedule
object
split invoice into payment schedule summing up to full invoice amount











































































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
curl -L -X PATCH 'https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "lateFeesConfiguration": {
    "enable": true,
    "value": 10,
    "type": "fixed",
    "frequency": {
      "intervalCount": 10,
      "interval": "day"
    },
    "grace": {
      "intervalCount": 10,
      "interval": "day"
    },
    "maxLateFees": {
      "type": "fixed",
      "value": "10"
    }
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
  "lateFeesConfiguration": {
    "enable": true,
    "value": 10,
    "type": "fixed",
    "frequency": {
      "intervalCount": 10,
      "interval": "day"
    },
    "grace": {
      "intervalCount": 10,
      "interval": "day"
    },
    "maxLateFees": {
      "type": "fixed",
      "value": "10"
    }
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!