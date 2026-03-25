# Get Campaigns

Source: https://marketplace.gohighlevel.com/docs/ghl/emails/fetch-campaigns

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_emails_fetch-campaigns_screenshot.png

---

EmailCampaignsGet Campaigns
Get Campaigns
GET
 https://services.leadconnectorhq.com/emails/schedule
Get Campaigns
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
Location ID to fetch campaigns from
Example: ohjiah0wdg3bzmzacvd6
limit
number
Maximum number of campaigns to return. Defaults to 10, maximum is 100
Example: 7
offset
number
Number of campaigns to skip for pagination
Example: 0
status
string
Possible values: [active, pause, complete, cancelled, retry, draft, resend-scheduled, processing]
Filter by schedule status
Default value:active
emailStatus
string
Possible values: [all, not-started, paused, cancelled, processing, resumed, next-drip, complete, success, error, waiting, queued, queueing, reading, scheduled]
Filter by email delivery status
Default value:complete
name
string
Filter campaigns by name
Example: Black Friday Campaign
parentId
string
Filter campaigns by parent folder ID
Example: folder123
limitedFields
boolean
When true, returns only essential campaign fields like id, templateDataDownloadUrl, updatedAt, type, templateType, templateId, downloadUrl and isPlainText. When false, returns complete campaign data including meta information, bulkRequestStatusInfo, ABTestInfo, resendScheduleInfo and all other campaign properties
Default value:false
Example: false
archived
boolean
Filter archived campaigns
Example: false
campaignsOnly
boolean
Return only campaigns, excluding folders
Default value:false
Example: false
showStats
boolean
When true, returns campaign statistics including delivered count, opened count, clicked count and revenue if available for the campaign. When false, returns campaign data without statistics.
Default value:true
Example: true
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
schedules
object[]
REQUIRED
total
string[]
REQUIRED
The total number of campaigns
traceId
string
REQUIRED
Trace Id


































































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
curl -L 'https://services.leadconnectorhq.com/emails/schedule' \
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