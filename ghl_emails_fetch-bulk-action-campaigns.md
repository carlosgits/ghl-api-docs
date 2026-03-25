# Get Bulk Action Campaigns

Source: https://marketplace.gohighlevel.com/docs/ghl/emails/fetch-bulk-action-campaigns

Screenshot: images/ghl_emails_fetch-bulk-action-campaigns_screenshot.png

---

EmailCampaignsGet Bulk Action Campaigns
Get Bulk Action Campaigns
GET
 https://services.leadconnectorhq.com/emails/campaigns/bulk-actions
Get list of bulk action campaigns for a location
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
Location ID
Example: ve9EPM428h8vShlRW1KT
limit
number
Possible values: >= 1 and <= 20
Number of campaigns to return. Defaults to 10, minimum is 1, maximum is 20
Default value:10
Example: 10
offset
number
Number of campaigns to skip for pagination. Defaults to 0, minimum is 0
Default value:0
Example: 0
dateFrom
string
Filter by start date (ISO 8601 format)
Example: 2024-01-01T00:00:00.000Z
dateTo
string
Filter by end date (ISO 8601 format)
Example: 2024-12-31T23:59:59.999Z
status
string
Possible values: [processing, scheduled, paused, complete, cancelled]
Filter by status
Example: complete
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
Total count of bulk action campaigns
Example:25















































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
curl -L 'https://services.leadconnectorhq.com/emails/campaigns/bulk-actions' \
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