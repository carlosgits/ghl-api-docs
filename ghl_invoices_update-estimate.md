# Update Estimate

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/update-estimate

Screenshot: images/ghl_invoices_update-estimate_screenshot.png

---

InvoiceEstimateUpdate Estimate
Update Estimate
PUT
 https://services.leadconnectorhq.com/invoices/estimate/:estimateId
Update an existing estimate with new details
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
name
string
REQUIRED
Estimate Name
Example:Home Service Estimate
businessDetails
object
REQUIRED
currency
string
REQUIRED
Currency code
Example:USD
items
object[]
REQUIRED
liveMode
boolean
livemode for estimate
Default value: true
Example:true
discount
object
REQUIRED
termsNotes
string
Terms notes, Also supports HTML markups
Example:<p>This is a default terms.</p>
title
string
Title for the estimate
Example:ESTIMATE
contactDetails
object
estimateNumber
number
Estimate Number, if not specified will take in the next valid estimate number
Example:1001
issueDate
string
issue date estimate
Example:2024-08-07
expiryDate
string
expiry date estimate
Example:2024-08-10
sentTo
object
automaticTaxesEnabled
boolean
Automatic taxes enabled for the Estimate
Default value: false
Example:true
meta
object
Meta data for the estimate
Example:{"key":"value"}
sendEstimateDetails
object
frequencySettings
object
estimateNumberPrefix
string
Prefix for the estimate number
Default value: EST-
Example:EST-
userId
string
User Id
Example:6578278e879ad2646715ba9c
attachments
object[]
autoInvoice
object
miscellaneousCharges
object
paymentScheduleConfig
object
estimateStatus
string
Estimate Status
Possible values: [all, draft, sent, accepted, declined, invoiced, viewed]
Example:sent
Responses
200
400
401
422
Successfully updated
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
altId
string
REQUIRED
Location Id or Agency Id
Example:6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
_id
string
REQUIRED
Unique identifier
Example:67ac9a51106ee8311e911XXXX
liveMode
boolean
REQUIRED
Indicates if it is in live mode
Example:true
deleted
boolean
REQUIRED
Indicates if deleted
Example:false
name
string
REQUIRED
Name
Example:Estimate Name
currency
string
REQUIRED
Currency code
Example:USD
businessDetails
object
REQUIRED
Business details associated with the estimate
Example:{"logoUrl":"your_image-url","name":"Business name","address":{"addressLine1":"address line 1","city":"Test City","state":"State Name","countryCode":"US","postalCode":"12345"},"phoneNo":"+1 1234567890","website":"www.example.com","customValues":[{"name":"Test","fieldKey":"{{custom_values.test}}","id":"5DYTWoiQvWiIJZXX44XXX","value":"Test's Custom Value"}]}
items
array[]
REQUIRED
An array of items
Example:[{"taxes":[],"taxInclusive":false,"_id":"67ac9a51106ee8311e911XXXX","description":"<p>Futuristic anti-gravity racing</p>","currency":"USD","productId":"67ac9a51106ee8311e911XXXX","priceId":"67ac9a51106ee8311e911XXXX","amount":9.99,"qty":1,"name":"TEST","type":"one_time"},{"taxes":[{"_id":"67ac9a51106ee8311e911XXXX","name":"TaxTwo","rate":8.5,"calculation":"exclusive"}],"taxInclusive":true,"_id":"67ac9a51106ee8311e911XXXX","productId":"67ac9a51106ee8311e911XXXX","priceId":"67ac9a51106ee8311e911XXXX","currency":"USD","name":"TEST2","qty":1,"amount":500,"description":"","type":"recurring"}]
discount
object
title
string
Title
Example:ESTIMATE
estimateNumberPrefix
string
Estimate number prefix
Example:EST-
attachments
object[]
updatedBy
string
User Id of who last updated
Example:3HIpOF9NIc5ltriQXXXX
total
number
REQUIRED
Total amount
Example:1222.03
createdAt
date-time
REQUIRED
Timestamp when created
Example:2025-02-12T13:17:47.416Z
updatedAt
date-time
REQUIRED
Timestamp when last updated
Example:2025-02-12T13:17:47.416Z
__v
number
REQUIRED
Version number
Example:0
automaticTaxesEnabled
boolean
REQUIRED
Indicates if automatic taxes are enabled for this estimate
Example:false
termsNotes
string
Terms and conditions for the estimate, supports HTML markup
Example:<p>All services are subject to availability.</p>
companyId
string
REQUIRED
Company identifier associated with the estimate
Example:COMP12345
contactDetails
object
REQUIRED
Contact details for the estimate
Example:{"id":"jvzfKTNdE7OYXXXXXX","name":"Contact Name","phoneNo":"+911111111114","email":"email@test.com","address":{"countryCode":"US"}}
issueDate
date-time
REQUIRED
Date when the estimate was issued
Example:2023-06-15T00:00:00.000Z
expiryDate
date-time
REQUIRED
Date when the estimate expires
Example:2023-07-15T00:00:00.000Z
sentBy
string
User who sent the estimate
Example:user@example.com
automaticTaxesCalculated
boolean
REQUIRED
Indicates if automatic taxes were calculated
Example:true
meta
object
REQUIRED
Additional metadata associated with the estimate
Example:{"key":"value"}
estimateActionHistory
string[]
REQUIRED
History of actions taken on the estimate
Example:[{"action":"Created","timestamp":"2023-06-15T10:00:00.000Z"}]
sentTo
object
REQUIRED
Recipient details for the estimate
Example:{"email":["test@example.com"],"phoneNo":["+1 99444444444"]}
frequencySettings
object
lastVisitedAt
date-time
REQUIRED
Timestamp when the estimate was last visited
Example:2023-06-20T08:30:00.000Z
totalamountInUSD
number
REQUIRED
Total amount in USD
Example:1500.75
autoInvoice
object
Auto-invoice settings for the estimate
Example:{"enabled":true,"directPayments":false}
traceId
string
REQUIRED
Trace ID for logging and debugging
Example:010c7a01-857f-4619-970d-xyxyxyxy



































































































































































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
curl -L -X PUT 'https://services.leadconnectorhq.com/invoices/estimate/:estimateId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "name": "Home Service Estimate",
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
      "taxInclusive": true,
      "attachments": [
        "https://example.com/file1.jpg",
        "https://example.com/file2.png"
      ]
    }
  ],
  "liveMode": true,
  "discount": {
    "value": 10,
    "type": "percentage",
    "validOnProductIds": "[ '\''6579751d56f60276e5bd4154'\'' ]"
  },
  "termsNotes": "<p>This is a default terms.</p>",
  "title": "ESTIMATE",
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
  "estimateNumber": 1001,
  "issueDate": "2024-08-07",
  "expiryDate": "2024-08-10",
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
  "automaticTaxesEnabled": true,
  "meta": {
    "key": "value"
  },
  "sendEstimateDetails": {
    "altId": "6578278e879ad2646715ba9c",
    "altType": "location",
    "action": "sms_and_email",
    "liveMode": true,
    "userId": "6578278e879ad2646715ba9c",
    "sentFrom": {
      "fromName": "Alex",
      "fromEmail": "alex@example.com"
    },
    "estimateName": "Estimate"
  },
  "frequencySettings": {
    "enabled": true,
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
    }
  },
  "estimateNumberPrefix": "EST-",
  "userId": "6578278e879ad2646715ba9c",
  "attachments": [
    {
      "id": "6241712be68f7a98102ba272",
      "name": "Electronics.pdf",
      "url": "https://example.com/digital-delivery",
      "type": "string",
      "size": 10000
    }
  ],
  "autoInvoice": {
    "enabled": true,
    "directPayments": true
  },
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
  "paymentScheduleConfig": {
    "type": "fixed",
    "dateConfig": {
      "depositDateType": "estimate_accepted",
      "scheduleDateType": "regular_interval"
    },
    "schedules": [
      [
        null
      ]
    ]
  },
  "estimateStatus": "sent"
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
  "name": "Home Service Estimate",
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
      "taxInclusive": true,
      "attachments": [
        "https://example.com/file1.jpg",
        "https://example.com/file2.png"
      ]
    }
  ],
  "liveMode": true,
  "discount": {
    "value": 10,
    "type": "percentage",
    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"
  },
  "termsNotes": "<p>This is a default terms.</p>",
  "title": "ESTIMATE",
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
  "estimateNumber": 1001,
  "issueDate": "2024-08-07",
  "expiryDate": "2024-08-10",
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
  "automaticTaxesEnabled": true,
  "meta": {
    "key": "value"
  },
  "sendEstimateDetails": {
    "altId": "6578278e879ad2646715ba9c",
    "altType": "location",
    "action": "sms_and_email",
    "liveMode": true,
    "userId": "6578278e879ad2646715ba9c",
    "sentFrom": {
      "fromName": "Alex",
      "fromEmail": "alex@example.com"
    },
    "estimateName": "Estimate"
  },
  "frequencySettings": {
    "enabled": true,
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
    }
  },
  "estimateNumberPrefix": "EST-",
  "userId": "6578278e879ad2646715ba9c",
  "attachments": [
    {
      "id": "6241712be68f7a98102ba272",
      "name": "Electronics.pdf",
      "url": "https://example.com/digital-delivery",
      "type": "string",
      "size": 10000
    }
  ],
  "autoInvoice": {
    "enabled": true,
    "directPayments": true
  },
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
  "paymentScheduleConfig": {
    "type": "fixed",
    "dateConfig": {
      "depositDateType": "estimate_accepted",
      "scheduleDateType": "regular_interval"
    },
    "schedules": [
      [
        null
      ]
    ]
  },
  "estimateStatus": "sent"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!