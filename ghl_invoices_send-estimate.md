# Send Estimate

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/send-estimate

Screenshot: images/ghl_invoices_send-estimate_screenshot.png

---

InvoiceEstimateSend Estimate
Send Estimate
POST
 https://services.leadconnectorhq.com/invoices/estimate/:estimateId/send
API to send estimate by estimate id
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
action
string
REQUIRED
Possible values: [sms_and_email, send_manually, email, sms]
liveMode
boolean
REQUIRED
livemode for estimate
Example:true
userId
string
REQUIRED
Please ensure that the UserId corresponds to an authorized personnel, either by an employee ID or agency ID, to access this location. This account will serve as the primary channel for all future communications and updates.
Example:6578278e879ad2646715ba9c
sentFrom
object
estimateName
string
estimate name
Example:Estimate
Responses
201
400
401
422
Created
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
curl -L 'https://services.leadconnectorhq.com/invoices/estimate/:estimateId/send' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
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
  "action": "sms_and_email",
  "liveMode": true,
  "userId": "6578278e879ad2646715ba9c",
  "sentFrom": {
    "fromName": "Alex",
    "fromEmail": "alex@example.com"
  },
  "estimateName": "Estimate"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!