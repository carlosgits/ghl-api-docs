# Update invoice

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/update-invoice

Screenshot: images/ghl_invoices_update-invoice_screenshot.png

---

InvoiceInvoiceUpdate invoice
Update invoice
PUT
 https://services.leadconnectorhq.com/invoices/:invoiceId
API to update invoice by invoice id
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
name
string
REQUIRED
Name to be updated
Example:New Invoice
title
string
Title for the invoice
Example:INVOICE
currency
string
REQUIRED
Currency
Example:USD
description
string
Description
Example:ABC Corp payments
businessDetails
object
invoiceNumber
string
Invoice Number
Example:1001
contactId
string
Id of the contact which you need to send the invoice
Example:6578278e879ad2646715ba9c
contactDetails
object
termsNotes
string
Terms notes, Also supports HTML markups
Example:<p>This is a default terms.</p>
discount
object
invoiceItems
object[]
REQUIRED
automaticTaxesEnabled
boolean
Automatic taxes enabled for the Invoice
Example:true
liveMode
boolean
Payment mode
issueDate
string
REQUIRED
Issue date in YYYY-MM-DD format
Example:2023-01-01
dueDate
string
REQUIRED
Due date in YYYY-MM-DD format
Example:2023-01-14
paymentSchedule
object
tipsConfiguration
object
xeroDetails
object
invoiceNumberPrefix
string
prefix for invoice number
Example:INV-
paymentMethods
object
attachments
object[]
miscellaneousCharges
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
curl -L -X PUT 'https://services.leadconnectorhq.com/invoices/:invoiceId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "name": "New Invoice",
  "title": "INVOICE",
  "currency": "USD",
  "description": "ABC Corp payments",
  "businessDetails": {
    "name": "Alex",
    "address": {
      "addressLine1": "9931 Beechwood",
      "city": "St. Houston",
      "state": "TX",
      "countryCode": "USA",
      "postalCode": "559-6993"
    },
    "phoneNo": "+1-214-559-6993",
    "website": "www.example.com"
  },
  "invoiceNumber": "1001",
  "contactId": "6578278e879ad2646715ba9c",
  "contactDetails": {
    "id": "6578278e879ad2646715ba9c",
    "name": "Alex",
    "phoneNo": "+1234567890",
    "email": "alex@example.com",
    "additionalEmails": [
      {
        "email": "alex@example.com"
      }
    ],
    "companyName": "ABC Corp.",
    "address": {
      "addressLine1": "9931 Beechwood",
      "addressLine2": "Beechwood",
      "city": "St. Houston",
      "state": "TX",
      "countryCode": "US",
      "postalCode": "559-6993"
    },
    "customFields": [
      "string"
    ]
  },
  "termsNotes": "<p>This is a default terms.</p>",
  "discount": {
    "value": 10,
    "type": "percentage",
    "validOnProductIds": "[ '\''6579751d56f60276e5bd4154'\'' ]"
  },
  "invoiceItems": [
    {
      "name": "ABC Product",
      "description": "ABC Corp.",
      "productId": "6578278e879ad2646715ba9c",
      "priceId": "6578278e879ad2646715ba9c",
      "currency": "USD",
      "amount": 999,
      "qty": 1,
      "taxes": [
        {
          "_id": "string",
          "name": "string",
          "rate": 0,
          "calculation": "exclusive",
          "description": "string",
          "taxId": "string"
        }
      ],
      "automaticTaxCategoryId": "6578278e879ad2646715ba9c",
      "isSetupFeeItem": true,
      "type": "one_time",
      "taxInclusive": true
    }
  ],
  "automaticTaxesEnabled": true,
  "liveMode": true,
  "issueDate": "2023-01-01",
  "dueDate": "2023-01-14",
  "paymentSchedule": {
    "type": "percentage",
    "schedules": [
      "string"
    ]
  },
  "tipsConfiguration": {
    "tipsPercentage": [
      5,
      10,
      15
    ],
    "tipsEnabled": true
  },
  "xeroDetails": {},
  "invoiceNumberPrefix": "INV-",
  "paymentMethods": {
    "stripe": {
      "enableBankDebitOnly": false
    }
  },
  "attachments": [
    {
      "id": "6241712be68f7a98102ba272",
      "name": "Electronics.pdf",
      "url": "https://example.com/digital-delivery",
      "type": "string",
      "size": 10000
    }
  ],
  "miscellaneousCharges": {
    "charges": [
      [
        null
      ]
    ],
    "collectedMiscellaneousCharges": 10,
    "paidCharges": [
      {
        "name": "Processing Fee",
        "charge": 10,
        "amount": 10,
        "_id": "673d01d7d547648a8dab6211"
      }
    ]
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
  "name": "New Invoice",
  "title": "INVOICE",
  "currency": "USD",
  "description": "ABC Corp payments",
  "businessDetails": {
    "name": "Alex",
    "address": {
      "addressLine1": "9931 Beechwood",
      "city": "St. Houston",
      "state": "TX",
      "countryCode": "USA",
      "postalCode": "559-6993"
    },
    "phoneNo": "+1-214-559-6993",
    "website": "www.example.com"
  },
  "invoiceNumber": "1001",
  "contactId": "6578278e879ad2646715ba9c",
  "contactDetails": {
    "id": "6578278e879ad2646715ba9c",
    "name": "Alex",
    "phoneNo": "+1234567890",
    "email": "alex@example.com",
    "additionalEmails": [
      {
        "email": "alex@example.com"
      }
    ],
    "companyName": "ABC Corp.",
    "address": {
      "addressLine1": "9931 Beechwood",
      "addressLine2": "Beechwood",
      "city": "St. Houston",
      "state": "TX",
      "countryCode": "US",
      "postalCode": "559-6993"
    },
    "customFields": [
      "string"
    ]
  },
  "termsNotes": "<p>This is a default terms.</p>",
  "discount": {
    "value": 10,
    "type": "percentage",
    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"
  },
  "invoiceItems": [
    {
      "name": "ABC Product",
      "description": "ABC Corp.",
      "productId": "6578278e879ad2646715ba9c",
      "priceId": "6578278e879ad2646715ba9c",
      "currency": "USD",
      "amount": 999,
      "qty": 1,
      "taxes": [
        {
          "_id": "string",
          "name": "string",
          "rate": 0,
          "calculation": "exclusive",
          "description": "string",
          "taxId": "string"
        }
      ],
      "automaticTaxCategoryId": "6578278e879ad2646715ba9c",
      "isSetupFeeItem": true,
      "type": "one_time",
      "taxInclusive": true
    }
  ],
  "automaticTaxesEnabled": true,
  "liveMode": true,
  "issueDate": "2023-01-01",
  "dueDate": "2023-01-14",
  "paymentSchedule": {
    "type": "percentage",
    "schedules": [
      "string"
    ]
  },
  "tipsConfiguration": {
    "tipsPercentage": [
      5,
      10,
      15
    ],
    "tipsEnabled": true
  },
  "xeroDetails": {},
  "invoiceNumberPrefix": "INV-",
  "paymentMethods": {
    "stripe": {
      "enableBankDebitOnly": false
    }
  },
  "attachments": [
    {
      "id": "6241712be68f7a98102ba272",
      "name": "Electronics.pdf",
      "url": "https://example.com/digital-delivery",
      "type": "string",
      "size": 10000
    }
  ],
  "miscellaneousCharges": {
    "charges": [
      [
        null
      ]
    ],
    "collectedMiscellaneousCharges": 10,
    "paidCharges": [
      {
        "name": "Processing Fee",
        "charge": 10,
        "amount": 10,
        "_id": "673d01d7d547648a8dab6211"
      }
    ]
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!