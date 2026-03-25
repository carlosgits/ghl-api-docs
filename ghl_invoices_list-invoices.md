# List invoices

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/list-invoices

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_invoices_list-invoices_screenshot.png

---

InvoiceInvoiceList invoices
List invoices
GET
 https://services.leadconnectorhq.com/invoices/
API to get list of invoices
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
contactId
string
Contact ID for the invoice
Example: AmuzcoPBpgKeccNsFlib
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
sortField
string
Possible values: [issueDate]
The field on which sorting should be applied
Example: issueDate
sortOrder
string
Possible values: [ascend, descend]
The order of sort which should be applied for the sortField
Example: descend
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
invoices
object[]
REQUIRED
total
number
REQUIRED
Total number of invoices
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
curl -L 'https://services.leadconnectorhq.com/invoices/' \
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