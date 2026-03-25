# GET all or email/sms templates

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/get-all-or-email-sms-templates

Screenshot: images/ghl_locations_get-all-or-email-sms-templates_screenshot.png

---

Sub-Account (Formerly location)TemplateGET all or email/sms templates
GET all or email/sms templates
GET
 https://services.leadconnectorhq.com/locations/:locationId/templates
GET all or email/sms templates
Requirements
Scope(s)
locations/templates.readonly
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
PATH PARAMETERS
locationId
string
REQUIRED
Location Id
Example: ve9EPM428h8vShlRW1KT
QUERY PARAMETERS
deleted
boolean
Default value:false
skip
string
Default value:0
Example: 1
limit
string
Default value:25
Example: 25
type
string
Possible values: [sms, email, whatsapp]
originId
string
REQUIRED
Origin Id
Example: ve9EPM428h8vShlRW1KT
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
templates
object[]
totalCount
number
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
curl -L 'https://services.leadconnectorhq.com/locations/:locationId/templates' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — path
REQUIRED
originId — query
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