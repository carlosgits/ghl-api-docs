# Get Invoice Settings

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/get-invoice-settings

Screenshot: images/ghl_invoices_get-invoice-settings_screenshot.png

---

InvoiceInvoiceGet Invoice Settings
Get Invoice Settings
GET
 https://services.leadconnectorhq.com/invoices/settings
Get the invoice settings for the given location
Requirements
Scope(s)
invoices.readonly
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
Sub-Account Id
Example:6578278e879ad2646715ba9c
altType
string
Alt Type
Possible values: [location]
Example:location
termsNote
string
Terms and conditions for invoices
Example:Payment is due within 30 days.
estimatesTermsNote
string
Terms and conditions for estimates
Example:This estimate is valid for 30 days.
title
string
Title for invoices
Possible values: <= 40 characters
Example:INVOICE
estimatesTitle
string
Title for estimates
Possible values: <= 40 characters
Example:ESTIMATE
invoiceNumberPrefix
string
Prefix for invoice numbers
Possible values: <= 10 characters
Example:INV-
estimateNumberPrefix
string
Prefix for estimate numbers
Possible values: <= 10 characters
Example:EST-
dueAfterXDays
number
Number of days after which invoice is due
Example:30
estimatesExpireAfterXDays
number
Number of days after which estimate expires
Example:30
minimumPercentagePartialPayment
number
Minimum percentage for partial payment
Example:25
customFields
string[]
Custom fields array
Possible values: <= 3
Example:["6578278e879ad2646715baxc","6901e9fb77ac4d701ba0b996"]
customNotification
object
businessDetails
object
senderConfiguration
object
productSettings
object
reminderSettings
object
lateFeesConfiguration
object
tipsConfiguration
object
paymentMethods
object































































































































































































































































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
curl -L 'https://services.leadconnectorhq.com/invoices/settings' \
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
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!