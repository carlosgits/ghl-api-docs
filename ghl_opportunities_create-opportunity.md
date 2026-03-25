# Create Opportunity

Source: https://marketplace.gohighlevel.com/docs/ghl/opportunities/create-opportunity

Screenshot: images/ghl_opportunities_create-opportunity_screenshot.png

---

OpportunitiesOpportunitiesCreate Opportunity
Create Opportunity
POST
 https://services.leadconnectorhq.com/opportunities/
Create Opportunity
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
pipelineId
string
REQUIRED
pipeline Id
Example:VDm7RPYC2GLUvdpKmBfC
locationId
string
REQUIRED
Example:ve9EPM428h8vShlRW1KT
name
string
REQUIRED
Example:First Opps
pipelineStageId
string
Example:7915dedc-8f18-44d5-8bc3-77c04e994a10
status
string
REQUIRED
Possible values: [open, won, lost, abandoned, all]
contactId
string
REQUIRED
Example:mTkSCb1UBjb5tk4OvB69
monetaryValue
number
Example:220
assignedTo
string
Example:082goXVW3lIExEQPOnd3
customFields
object[]
Responses
201
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
curl -L 'https://services.leadconnectorhq.com/opportunities/' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "pipelineId": "VDm7RPYC2GLUvdpKmBfC",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "name": "First Opps",
  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",
  "status": "open",
  "contactId": "mTkSCb1UBjb5tk4OvB69",
  "monetaryValue": 220,
  "assignedTo": "082goXVW3lIExEQPOnd3",
  "customFields": [
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": "9039160788"
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": [
        "test",
        "test2"
      ]
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": {}
    }
  ]
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
  "pipelineId": "VDm7RPYC2GLUvdpKmBfC",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "name": "First Opps",
  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",
  "status": "open",
  "contactId": "mTkSCb1UBjb5tk4OvB69",
  "monetaryValue": 220,
  "assignedTo": "082goXVW3lIExEQPOnd3",
  "customFields": [
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": "9039160788"
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": [
        "test",
        "test2"
      ]
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": {}
    }
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!