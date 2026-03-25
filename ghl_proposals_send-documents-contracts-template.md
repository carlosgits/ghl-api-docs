# Send template

Source: https://marketplace.gohighlevel.com/docs/ghl/proposals/send-documents-contracts-template

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_proposals_send-documents-contracts-template_screenshot.png

---

ProposalsTemplatesSend template
Send template
POST
 https://services.leadconnectorhq.com/proposals/templates/send
Send template to a client
Requirements
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Agency Token
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
templateId
string
REQUIRED
Template Id
Example:hTlkh7t8gujsahgg93
userId
string
REQUIRED
User Id
Example:hTlkh7t8gujsahgg93
sendDocument
boolean
Send Document
Example:true
locationId
string
REQUIRED
Location Id
Example:hTlkh7t8gujsahgg93
contactId
string
REQUIRED
Contact Id
Example:hTlkh7t8gujsahgg93
opportunityId
string
Opportunity Id
Example:hTlkh7t8gujsahgg93
Responses
200
400
Document sent successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Success status
Example:true
links
object[]
REQUIRED



















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
curl -L 'https://services.leadconnectorhq.com/proposals/templates/send' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "templateId": "hTlkh7t8gujsahgg93",
  "userId": "hTlkh7t8gujsahgg93",
  "sendDocument": true,
  "locationId": "hTlkh7t8gujsahgg93",
  "contactId": "hTlkh7t8gujsahgg93",
  "opportunityId": "hTlkh7t8gujsahgg93"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Security Scheme
Location-Access
Agency-Access
Bearer Token
Parameters
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "templateId": "hTlkh7t8gujsahgg93",
  "userId": "hTlkh7t8gujsahgg93",
  "sendDocument": true,
  "locationId": "hTlkh7t8gujsahgg93",
  "contactId": "hTlkh7t8gujsahgg93",
  "opportunityId": "hTlkh7t8gujsahgg93"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!