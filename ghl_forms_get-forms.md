# Get Forms

Source: https://marketplace.gohighlevel.com/docs/ghl/forms/get-forms

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_forms_get-forms_screenshot.png

---

FormsFormsGet Forms
Get Forms
GET
 https://services.leadconnectorhq.com/forms/
Get Forms
Requirements
Scope(s)
forms.readonly
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
QUERY PARAMETERS
locationId
string
REQUIRED
Example: ve9EPM428h8vShlRW1KT
skip
number
Example: 0
limit
number
Limit Per Page records count. will allow maximum up to 50 and default will be 10
Default value:10
Example: 20
type
string
Example: folder
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
forms
object[]
total
number
Total number of forms
Example:20



















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
curl -L 'https://services.leadconnectorhq.com/forms/' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
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