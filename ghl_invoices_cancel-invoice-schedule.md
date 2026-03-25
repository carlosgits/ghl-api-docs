# Cancel an scheduled invoice

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/cancel-invoice-schedule

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_invoices_cancel-invoice-schedule_screenshot.png

---

InvoiceScheduleCancel an scheduled invoice
Cancel an scheduled invoice
POST
 https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/cancel
API to cancel a scheduled invoice by schedule id
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
curl -L 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/cancel' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location"
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
  "altType": "location"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!