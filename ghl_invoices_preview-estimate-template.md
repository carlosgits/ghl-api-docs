# Preview Estimate Template

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/preview-estimate-template

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_invoices_preview-estimate-template_screenshot.png

---

InvoiceEstimatePreview Estimate Template
Preview Estimate Template
GET
 https://services.leadconnectorhq.com/invoices/estimate/template/preview
Get a preview of an estimate template
Requirements
Scope(s)
invoices/estimate.readonly
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
QUERY PARAMETERS
altId
string
REQUIRED
Location Id or Agency Id
Example: 6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
templateId
string
REQUIRED
Template Id
Example: 5f9d6d8b1b2d2c001f2d9e4b
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
curl -L 'https://services.leadconnectorhq.com/invoices/estimate/template/preview' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
altId — query
REQUIRED
altType — query
REQUIRED
---
location
templateId — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!