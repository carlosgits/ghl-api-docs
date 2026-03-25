# Get Forms Submissions

Source: https://marketplace.gohighlevel.com/docs/ghl/forms/get-forms-submissions

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_forms_get-forms-submissions_screenshot.png

---

FormsFormsGet Forms Submissions
Get Forms Submissions
GET
 https://services.leadconnectorhq.com/forms/submissions
Get Forms Submissions
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
page
number
Page No. By default it will be 1
Default value:1
Example: 1
limit
number
Limit Per Page records count. will allow maximum up to 100 and default will be 20
Default value:20
Example: 20
formId
string
Filter submission by form id
Example: jjusM6EOngDExnbo2DbU
q
string
Filter by contactId, name, email or phone no.
Example: john@deo.com
startAt
string
Get submission by starting of this date. By default it will be same date of last month(YYYY-MM-DD).
Example: 2020-11-14
endAt
string
Get submission by ending of this date. By default it will be current date(YYYY-MM-DD).
Example: 2020-12-14
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
submissions
object[]
meta
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
curl -L 'https://services.leadconnectorhq.com/forms/submissions' \
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