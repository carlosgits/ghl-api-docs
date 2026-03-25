# List templates

Source: https://marketplace.gohighlevel.com/docs/ghl/proposals/list-documents-contracts-templates

Screenshot: images/ghl_proposals_list-documents-contracts-templates_screenshot.png

---

ProposalsTemplatesList templates
List templates
GET
 https://services.leadconnectorhq.com/proposals/templates
List document contract templates for a location
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
Example: jhg64gjhb436fv
dateFrom
string
Date start from (ISO 8601)
Example: 2025-02-03T18:30:00.000Z
dateTo
string
Date to (ISO 8601)
Example: 2025-02-14T18:29:59.999Z
type
string
Comma-separated template types. Valid values: proposal, estimate, contentLibrary
Example: proposal,estimate
name
string
Template Name
Example: Template Name
isPublicDocument
boolean
If the docForm is a DocForm
userId
string
User Id, required when isPublicDocument is true
Example: 1234567890
limit
string
Limit
Example: 10
skip
string
Skip
Example: 0
Responses
200
400
Templates fetched successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
data
object[]
REQUIRED
total
number
REQUIRED
Total number of templates
Example:2
traceId
string
Trace ID for request tracking
Example:d5656876-86a5-46fb-84df-788f1da7937a

























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
curl -L 'https://services.leadconnectorhq.com/proposals/templates' \
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