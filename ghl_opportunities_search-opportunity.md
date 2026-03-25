# Search Opportunity

Source: https://marketplace.gohighlevel.com/docs/ghl/opportunities/search-opportunity

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_opportunities_search-opportunity_screenshot.png

---

OpportunitiesSearchSearch Opportunity
Search Opportunity
GET
 https://services.leadconnectorhq.com/opportunities/search
Search Opportunity
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
QUERY PARAMETERS
q
string
Example: john@deo.com
location_id
string
REQUIRED
Location Id
Example: i2SpAtBVHSVea1sL6oah
pipeline_id
string
Pipeline Id
Example: bCkKGpDsyPP4peuKowkG
pipeline_stage_id
string
stage Id
Example: 7915dedc-8f18-44d5-8bc3-77c04e994a10
contact_id
string
Contact Id
Example: WFwVrSSjZ2CNHbZThQX2
status
string
Possible values: [open, won, lost, abandoned, all]
assigned_to
string
Example: 082goXVW3lIExEQPOnd3
campaignId
string
Campaign Id
Example: Y2I9XM7aO1hncuSOlc9L
id
string
Opportunity Id
Example: 123akv4LFn6C9frZoy3e
order
string
Example: added_asc
endDate
string
End date
Example: mm-dd-yyyy
startAfter
string
Start After
Example: 1628008053263
startAfterId
string
Start After Id
Example: UIaE1WjAwWKdlyD7osQI
date
string
Start date
Example: mm-dd-yyyy
country
string
Example: US
page
number
Default value:1
limit
number
Limit Per Page records count. will allow maximum up to 100 and default will be 20
Default value:20
getTasks
boolean
get Tasks in contact
getNotes
boolean
get Notes in contact
getCalendarEvents
boolean
get Calender event in contact
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
meta
object
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
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
location_id — query
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