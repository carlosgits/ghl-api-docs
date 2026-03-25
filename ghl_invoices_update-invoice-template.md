# Update template

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/update-invoice-template

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_invoices_update-invoice-template_screenshot.png

---

InvoiceTemplateUpdate template
Update template
PUT
 https://services.leadconnectorhq.com/invoices/template/:templateId
API to update an template by template id
Requirements
Scope(s)
invoices/template.write
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
templateId
string
REQUIRED
Template Id
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
internal
boolean
name
string
REQUIRED
Name of the template
Example:New Template
businessDetails
object
REQUIRED
currency
string
REQUIRED
items
object[]
REQUIRED
discount
object
termsNotes
string
title
string
Template title
Example:New Template
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
Template Id
Example:6578278e879ad2646715ba9c
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
Name of the Template
Example:New Template
businessDetails
object
currency
string
REQUIRED
Currency
Example:USD
discount
object
items
string[]
REQUIRED
Invoice Items
Example:[{"taxes":[],"_id":"c6tZZU0rJBf30ZXx9Gli","productId":"c6tZZU0rJBf30ZXx9Gli","priceId":"c6tZZU0rJBf30ZXx9Gli","currency":"USD","name":"Macbook Pro","qty":1,"amount":999}]
invoiceNumberPrefix
string
prefix for invoice number
Example:INV-
total
number
REQUIRED
Total Amount
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
curl -L -X PUT 'https://services.leadconnectorhq.com/invoices/template/:templateId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "internal": true,
  "name": "New Template",
  "businessDetails": {
    "logoUrl": "https://example.com/logo.png",
    "name": "ABC Corp.",
    "phoneNo": "+1-214-559-6993",
    "address": "9931 Beechwood, TX",
    "website": "wwww.example.com",
    "customValues": [
      "string"
    ]
  },
  "currency": "string",
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
  "discount": {
    "value": 10,
    "type": "percentage",
    "validOnProductIds": "[ '\''6579751d56f60276e5bd4154'\'' ]"
  },
  "termsNotes": "string",
  "title": "New Template",
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
templateId — path
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
  "internal": true,
  "name": "New Template",
  "businessDetails": {
    "logoUrl": "https://example.com/logo.png",
    "name": "ABC Corp.",
    "phoneNo": "+1-214-559-6993",
    "address": "9931 Beechwood, TX",
    "website": "wwww.example.com",
    "customValues": [
      "string"
    ]
  },
  "currency": "string",
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
  "discount": {
    "value": 10,
    "type": "percentage",
    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"
  },
  "termsNotes": "string",
  "title": "New Template",
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