# Get Campaign Statistics

Source: https://marketplace.gohighlevel.com/docs/ghl/emails/get-campaign-stats

Screenshot: images/ghl_emails_get-campaign-stats_screenshot.png

---

EmailStatisticsGet Campaign Statistics
Get Campaign Statistics
GET
 https://services.leadconnectorhq.com/emails/stats/location/:locationId/:source/:sourceId
Get statistics for email campaigns, workflows, or bulk actions
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
PATH PARAMETERS
locationId
string
REQUIRED
Location ID
Example: ve9EPM428h8vShlRW1KT
source
string
REQUIRED
Possible values: [email-campaigns, workflow-campaigns, bulk-actions]
Source type: email-campaigns, workflow-campaigns, or bulk-actions
Example: email-campaigns
sourceId
string
REQUIRED
ID of the email campaign, workflow campaign, or bulk action
Example: abc123
QUERY PARAMETERS
subSourceId
string
Workflow action ID. Only valid when source is workflow-campaigns
Example: step001
Responses
200
400
401
422
Success
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
locationId
string
REQUIRED
Location ID
Example:abc123
source
string
REQUIRED
Source type
Possible values: [email-campaigns, workflow-campaigns, bulk-actions]
Example:email-campaigns
sourceId
string
REQUIRED
Source ID
Example:campaign123
subSourceId
string
Workflow action ID
Example:step001
stats
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
curl -L 'https://services.leadconnectorhq.com/emails/stats/location/:locationId/:source/:sourceId' \
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
source — path
REQUIRED
---
email-campaigns
workflow-campaigns
bulk-actions
sourceId — path
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