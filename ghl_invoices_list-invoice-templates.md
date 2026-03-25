# List templates

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/list-invoice-templates

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_invoices_list-invoice-templates_screenshot.png

---

InvoiceTemplateList templates
List templates
GET
 https://services.leadconnectorhq.com/invoices/template
API to get list of templates
Requirements
Scope(s)
invoices/template.readonly
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
location Id / company Id based on altType
Example: 6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
Alt Type
Example: location
status
string
status to be filtered
startAt
string
startAt in YYYY-MM-DD format
Example: 2023-01-01
endAt
string
endAt in YYYY-MM-DD format
Example: 2023-01-01
search
string
To search for an invoice by id / name / email / phoneNo
Example: Alex
paymentMode
string
Possible values: [default, live, test]
payment mode
Example: live
limit
string
REQUIRED
Limit the number of items to return
Example: 10
offset
string
REQUIRED
Number of items to skip
Example: 10
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
data
object[]
REQUIRED
totalCount
number
REQUIRED
Total number of Templates
Example:100




























































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
curl -L 'https://services.leadconnectorhq.com/invoices/template' \
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
limit — query
REQUIRED
offset — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!