# Get Surveys Submissions

Source: https://marketplace.gohighlevel.com/docs/ghl/surveys/get-surveys-submissions

Screenshot: images/ghl_surveys_get-surveys-submissions_screenshot.png

---

SurveysSurveysGet Surveys Submissions
Get Surveys Submissions
GET
 https://services.leadconnectorhq.com/surveys/submissions
Get Surveys Submissions
Requirements
Scope(s)
surveys.readonly
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
surveyId
string
Filter submission by survey id
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
curl -L 'https://services.leadconnectorhq.com/surveys/submissions' \
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