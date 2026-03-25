# Create & Send

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/text-2-pay-invoice

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_invoices_text-2-pay-invoice_screenshot.png

---

InvoiceText2PayCreate & Send
Create & Send
POST
 https://services.leadconnectorhq.com/invoices/text2pay
API to create or update a text2pay invoice
Requirements
Scope(s)
invoices.write
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
Invoice Name
Example:New Invoice
currency
string
REQUIRED
Currency code
Example:USD
items
object[]
REQUIRED
termsNotes
string
Terms notes, Also supports HTML markups
Example:<p>This is a default terms.</p>
title
string
Title for the invoice
Example:INVOICE
contactDetails
object
invoiceNumber
string
Invoice Number
Example:1001
issueDate
string
REQUIRED
Issue date in YYYY-MM-DD format
Example:2023-01-01
dueDate
string
Due date in YYYY-MM-DD format
Example:2023-01-14
sentTo
object
REQUIRED
liveMode
boolean
REQUIRED
automaticTaxesEnabled
boolean
Automatic taxes enabled for the Invoice
Example:true
paymentSchedule
object
lateFeesConfiguration
object
tipsConfiguration
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
id
string
id of invoice to update. If skipped, a new invoice will be created
includeTermsNote
boolean
include terms & notes with receipts
Example:true
action
string
REQUIRED
create invoice in draft mode or send mode
Possible values: [draft, send]
Example:draft
userId
string
REQUIRED
id of user generating invoice
discount
object
businessDetails
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
invoiceUrl
string
REQUIRED
preview url of generated invoice














































































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
curl -L 'https://services.leadconnectorhq.com/invoices/text2pay' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "name": "New Invoice",
  "currency": "USD",
  "items": [
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
  "termsNotes": "<p>This is a default terms.</p>",
  "title": "INVOICE",
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
  "invoiceNumber": "1001",
  "issueDate": "2023-01-01",
  "dueDate": "2023-01-14",
  "sentTo": {
    "email": [
      "alex@example.com"
    ],
    "emailCc": [
      "alex@example.com"
    ],
    "emailBcc": [
      "alex@example.com"
    ],
    "phoneNo": [
      "+1-214-559-6993"
    ]
  },
  "liveMode": true,
  "automaticTaxesEnabled": true,
  "paymentSchedule": {
    "type": "percentage",
    "schedules": [
      "string"
    ]
  },
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
  },
  "tipsConfiguration": {
    "tipsPercentage": [
      5,
      10,
      15
    ],
    "tipsEnabled": true
  },
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
  },
  "id": "string",
  "includeTermsNote": true,
  "action": "draft",
  "userId": "string",
  "discount": {
    "value": 10,
    "type": "percentage",
    "validOnProductIds": "[ '\''6579751d56f60276e5bd4154'\'' ]"
  },
  "businessDetails": {
    "logoUrl": "https://example.com/logo.png",
    "name": "ABC Corp.",
    "phoneNo": "+1-214-559-6993",
    "address": "9931 Beechwood, TX",
    "website": "wwww.example.com",
    "customValues": [
      "string"
    ]
  }
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
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
  "currency": "USD",
  "items": [
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
  "termsNotes": "<p>This is a default terms.</p>",
  "title": "INVOICE",
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
  "invoiceNumber": "1001",
  "issueDate": "2023-01-01",
  "dueDate": "2023-01-14",
  "sentTo": {
    "email": [
      "alex@example.com"
    ],
    "emailCc": [
      "alex@example.com"
    ],
    "emailBcc": [
      "alex@example.com"
    ],
    "phoneNo": [
      "+1-214-559-6993"
    ]
  },
  "liveMode": true,
  "automaticTaxesEnabled": true,
  "paymentSchedule": {
    "type": "percentage",
    "schedules": [
      "string"
    ]
  },
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
  },
  "tipsConfiguration": {
    "tipsPercentage": [
      5,
      10,
      15
    ],
    "tipsEnabled": true
  },
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
  },
  "id": "string",
  "includeTermsNote": true,
  "action": "draft",
  "userId": "string",
  "discount": {
    "value": 10,
    "type": "percentage",
    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"
  },
  "businessDetails": {
    "logoUrl": "https://example.com/logo.png",
    "name": "ABC Corp.",
    "phoneNo": "+1-214-559-6993",
    "address": "9931 Beechwood, TX",
    "website": "wwww.example.com",
    "customValues": [
      "string"
    ]
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!