# Update schedule

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/update-invoice-schedule

Screenshot: images/ghl_invoices_update-invoice-schedule_screenshot.png

---

InvoiceScheduleUpdate schedule
Update schedule
PUT
 https://services.leadconnectorhq.com/invoices/schedule/:scheduleId
API to update an schedule by schedule id
Requirements
Scope(s)
invoices/schedule.write
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
scheduleId
string
REQUIRED
Schedule Id
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
contactDetails
object
REQUIRED
schedule
object
REQUIRED
liveMode
boolean
REQUIRED
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
REQUIRED
termsNotes
string
title
string
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
Schedule Id
Example:6578278e879ad2646715ba9c
status
object
REQUIRED
Schedule Status
Example:draft
liveMode
boolean
REQUIRED
Live Mode
Example:false
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
schedule
object
invoices
object[]
REQUIRED
businessDetails
object
currency
string
REQUIRED
Currency
Example:USD
contactDetails
object
discount
object
items
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
termsNotes
string
REQUIRED
Terms notes
Example:Confidential
compiledTermsNotes
string
REQUIRED
Compiled terms notes
Example:Confidential
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
curl -L -X PUT 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "name": "string",
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
  "schedule": {
    "executeAt": "string",
    "rrule": {
      "intervalType": "monthly",
      "interval": 2,
      "startDate": "2023-01-01",
      "startTime": "20:45:00",
      "endDate": "2029-11-01",
      "endTime": "18:45:00",
      "dayOfMonth": 15,
      "dayOfWeek": "mo",
      "numOfWeek": -1,
      "monthOfYear": "jan",
      "count": 10,
      "daysBefore": 5,
      "useStartAsPrimaryUserAccepted": true,
      "endType": "by"
    }
  },
  "liveMode": true,
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
  "title": "string",
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
scheduleId — path
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
  "name": "string",
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
  "schedule": {
    "executeAt": "string",
    "rrule": {
      "intervalType": "monthly",
      "interval": 2,
      "startDate": "2023-01-01",
      "startTime": "20:45:00",
      "endDate": "2029-11-01",
      "endTime": "18:45:00",
      "dayOfMonth": 15,
      "dayOfWeek": "mo",
      "numOfWeek": -1,
      "monthOfYear": "jan",
      "count": 10,
      "daysBefore": 5,
      "useStartAsPrimaryUserAccepted": true,
      "endType": "by"
    }
  },
  "liveMode": true,
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
  "title": "string",
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