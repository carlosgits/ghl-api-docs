# Create Estimate Template

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/create-estimate-template

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_invoices_create-estimate-template_screenshot.png

---

InvoiceEstimateCreate Estimate Template
Create Estimate Template
POST
 https://services.leadconnectorhq.com/invoices/estimate/template
Create a new estimate template
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
Example:Home Service Estimate Template
businessDetails
object
REQUIRED
currency
string
REQUIRED
Currency code
Example:USD
items
array[]
REQUIRED
An array of items for the estimate.
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
estimateNumberPrefix
string
Prefix for the estimate number
Default value: EST-
Example:EST-
attachments
object[]
miscellaneousCharges
object
Responses
201
400
401
422
Successfully created
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
curl -L 'https://services.leadconnectorhq.com/invoices/estimate/template' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "name": "Home Service Estimate Template",
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
    [
      null
    ]
  ],
  "liveMode": true,
  "discount": {
    "value": 10,
    "type": "percentage",
    "validOnProductIds": "[ '\''6579751d56f60276e5bd4154'\'' ]"
  },
  "termsNotes": "<p>This is a default terms.</p>",
  "title": "ESTIMATE",
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
  "estimateNumberPrefix": "EST-",
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
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "name": "Home Service Estimate Template",
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
    [
      null
    ]
  ],
  "liveMode": true,
  "discount": {
    "value": 10,
    "type": "percentage",
    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"
  },
  "termsNotes": "<p>This is a default terms.</p>",
  "title": "ESTIMATE",
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
  "estimateNumberPrefix": "EST-",
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