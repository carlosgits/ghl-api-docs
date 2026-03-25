# Upsert Opportunity

Source: https://marketplace.gohighlevel.com/docs/ghl/opportunities/upsert-opportunity

Screenshot: images/ghl_opportunities_upsert-opportunity_screenshot.png

---

OpportunitiesOpportunitiesUpsert Opportunity
Upsert Opportunity
POST
 https://services.leadconnectorhq.com/opportunities/upsert
Upsert Opportunity
Requirements
Scope(s)
opportunities.write
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
id
string
opportunityId
Example:yWQobCRIhRguQtD2llvk
pipelineId
string
REQUIRED
pipeline Id
Example:bCkKGpDsyPP4peuKowkG
locationId
string
REQUIRED
locationId
Example:CLu7BaljjqrEjBGKTNNe
followers
string[]
REQUIRED
contactId
Example:LiKJ2vnRg5ETM8Z19K7
isRemoveAllFollowers
boolean
REQUIRED
isRemoveAllFollowers
Example:true
followersActionType
string
REQUIRED
followers action type
Possible values: [add, remove]
Example:add
name
string
name
Example:opportunity name
status
string
Possible values: [open, won, lost, abandoned, all]
pipelineStageId
string
Example:7915dedc-8f18-44d5-8bc3-77c04e994a10
monetaryValue
number
Example:220
assignedTo
string
Example:082goXVW3lIExEQPOnd3
lostReasonId
string
lost reason Id
Example:CLu7BaljjqrEjBGKTNNe
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
opportunity
object
REQUIRED
Updated / New Opportunity
new
boolean
REQUIRED
Example:true




















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
curl -L 'https://services.leadconnectorhq.com/opportunities/upsert' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "id": "yWQobCRIhRguQtD2llvk",
  "pipelineId": "bCkKGpDsyPP4peuKowkG",
  "locationId": "CLu7BaljjqrEjBGKTNNe",
  "followers": "LiKJ2vnRg5ETM8Z19K7",
  "isRemoveAllFollowers": true,
  "followersActionType": "add",
  "name": "opportunity name",
  "status": "open",
  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",
  "monetaryValue": 220,
  "assignedTo": "082goXVW3lIExEQPOnd3",
  "lostReasonId": "CLu7BaljjqrEjBGKTNNe"
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
  "id": "yWQobCRIhRguQtD2llvk",
  "pipelineId": "bCkKGpDsyPP4peuKowkG",
  "locationId": "CLu7BaljjqrEjBGKTNNe",
  "followers": "LiKJ2vnRg5ETM8Z19K7",
  "isRemoveAllFollowers": true,
  "followersActionType": "add",
  "name": "opportunity name",
  "status": "open",
  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",
  "monetaryValue": 220,
  "assignedTo": "082goXVW3lIExEQPOnd3",
  "lostReasonId": "CLu7BaljjqrEjBGKTNNe"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!