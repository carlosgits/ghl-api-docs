# Update template late fees configuration

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/update-invoice-payment-methods-configuration

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_invoices_update-invoice-payment-methods-configuration_screenshot.png

---

InvoiceTemplateUpdate template late fees configuration
Update template late fees configuration
PATCH
 https://services.leadconnectorhq.com/invoices/template/:templateId/payment-methods-configuration
API to update template late fees configuration by template id
Requirements
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
paymentMethods
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
curl -L -X PATCH 'https://services.leadconnectorhq.com/invoices/template/:templateId/payment-methods-configuration' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "paymentMethods": {
    "stripe": {
      "enableBankDebitOnly": false
    }
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
  "paymentMethods": {
    "stripe": {
      "enableBankDebitOnly": false
    }
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!