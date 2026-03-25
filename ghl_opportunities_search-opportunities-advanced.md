# Search Opportunities

Source: https://marketplace.gohighlevel.com/docs/ghl/opportunities/search-opportunities-advanced

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_opportunities_search-opportunities-advanced_screenshot.png

---

OpportunitiesSearchSearch Opportunities
Search Opportunities
POST
 https://services.leadconnectorhq.com/opportunities/search
Search Opportunities based on combinations of advanced filters. Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-424216/7bf11bc9b94f80f
Requirements
Scope(s)
opportunities.readonly
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
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
Location Id
Example:i2SpAtBVHSVea1sL6oah
query
string
REQUIRED
limit
number
REQUIRED
page
number
REQUIRED
searchAfter
string[]
REQUIRED
additionalDetails
object
REQUIRED
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
opportunities
object[]
total
number
REQUIRED
Example:100
aggregations
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
curl -L 'https://services.leadconnectorhq.com/opportunities/search' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "i2SpAtBVHSVea1sL6oah",
  "query": "string",
  "limit": 0,
  "page": 0,
  "searchAfter": [
    "string"
  ],
  "additionalDetails": {
    "notes": true,
    "tasks": true,
    "calendarEvents": true,
    "unReadConversations": true
  }
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "locationId": "i2SpAtBVHSVea1sL6oah",
  "query": "string",
  "limit": 0,
  "page": 0,
  "searchAfter": [
    "string"
  ],
  "additionalDetails": {
    "notes": true,
    "tasks": true,
    "calendarEvents": true,
    "unReadConversations": true
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!