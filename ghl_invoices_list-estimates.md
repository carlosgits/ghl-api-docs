# List Estimates

Source: https://marketplace.gohighlevel.com/docs/ghl/invoices/list-estimates

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_invoices_list-estimates_screenshot.png

---

InvoiceEstimateList Estimates
List Estimates
GET
 https://services.leadconnectorhq.com/invoices/estimate/list
Get a paginated list of estimates
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
search text for estimates name
Example: Home services estimate
status
string
Possible values: [all, draft, sent, accepted, declined, invoiced, viewed]
estimate status
Example: sent
contactId
string
Contact ID for the estimate
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
estimates
string[]
REQUIRED
List of estimates
total
number
REQUIRED
Total number of estimates
traceId
string
REQUIRED
Unique identifier for tracing the request























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
curl -L 'https://services.leadconnectorhq.com/invoices/estimate/list' \
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