# Get Workflow Campaigns

Source: https://marketplace.gohighlevel.com/docs/ghl/emails/fetch-workflow-campaigns

Screenshot: images/ghl_emails_fetch-workflow-campaigns_screenshot.png

---

EmailCampaignsGet Workflow Campaigns
Get Workflow Campaigns
GET
 https://services.leadconnectorhq.com/emails/campaigns/workflows
Get list of workflow campaigns for a location
Requirements
Scope(s)
emails/schedule.readonly
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
Example: 2021-07-28
QUERY PARAMETERS
locationId
string
REQUIRED
Example: k23k23jl23l32l
limit
number
Possible values: >= 1 and <= 20
Number of campaigns to return. Defaults to 10, minimum is 1, maximum is 20
Default value:10
Example: 10
offset
number
Number of items to skip for pagination. Defaults to 0, minimum is 0
Default value:0
Example: 0
search
string
Default value:
Example: workflow
status
string
Possible values: [published, draft]
Filter by campaign status
Example: published
Responses
200
400
401
403
404
422
Success
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
campaigns
object[]
REQUIRED
total
number
REQUIRED
Total count of campaigns
Example:50







































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
curl -L 'https://services.leadconnectorhq.com/emails/campaigns/workflows' \
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