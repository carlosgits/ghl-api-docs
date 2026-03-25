# Update Opportunity

Source: https://marketplace.gohighlevel.com/docs/ghl/opportunities/update-opportunity

Screenshot: images/ghl_opportunities_update-opportunity_screenshot.png

---

OpportunitiesOpportunitiesUpdate Opportunity
Update Opportunity
PUT
 https://services.leadconnectorhq.com/opportunities/:id
Update Opportunity
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
PATH PARAMETERS
id
string
REQUIRED
Opportunity Id
Example: yWQobCRIhRguQtD2llvk
APPLICATION/JSON
BODY
REQUIRED
pipelineId
string
pipeline Id
Example:bCkKGpDsyPP4peuKowkG
name
string
Example:First Opps
pipelineStageId
string
Example:7915dedc-8f18-44d5-8bc3-77c04e994a10
status
string
Possible values: [open, won, lost, abandoned, all]
monetaryValue
number
Example:220
assignedTo
string
Example:082goXVW3lIExEQPOnd3
customFields
object[]
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
curl -L -X PUT 'https://services.leadconnectorhq.com/opportunities/:id' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "pipelineId": "bCkKGpDsyPP4peuKowkG",
  "name": "First Opps",
  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",
  "status": "open",
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
id — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "pipelineId": "bCkKGpDsyPP4peuKowkG",
  "name": "First Opps",
  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",
  "status": "open",
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