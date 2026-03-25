# List documents

Source: https://marketplace.gohighlevel.com/docs/ghl/proposals/list-documents-contracts

Screenshot: images/ghl_proposals_list-documents-contracts_screenshot.png

---

ProposalsDocumentsList documents
List documents
GET
 https://services.leadconnectorhq.com/proposals/document
List documents for a location
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
QUERY PARAMETERS
locationId
string
REQUIRED
Location Id
Example: hTlkh7t8gujsahgg93
status
string
Possible values: [draft, sent, viewed, completed, accepted]
Document status, pass as comma separated values
Example: draft
paymentStatus
string
Possible values: [waiting_for_payment, paid, no_payment]
Payment status, pass as comma separated values
Example: paid
limit
number
Limit to fetch number of records
Example: 10
skip
number
Skip number of records
Example: 0
query
string
Search string
Example: document
dateFrom
string
Date start from (ISO 8601), dateFrom & DateTo must be provided together
Example: 2025-02-03T18:30:00.000Z
dateTo
string
Date to (ISO 8601), dateFrom & DateTo must be provided together
Example: 2025-02-14T18:29:59.999Z
Responses
200
400
Document fetched successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
documents
object[]
REQUIRED
total
number
REQUIRED
Total records available
Example:10
whiteLabelBaseUrl
number
WhiteLabel url for document
Example:https://example.com
whiteLabelBaseUrlForInvoice
number
WhiteLabel url for invoice
Example:https://example.com













































































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
curl -L 'https://services.leadconnectorhq.com/proposals/document' \
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
locationId — query
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