# Add Contact to Campaign

Source: https://marketplace.gohighlevel.com/docs/ghl/contacts/add-contact-to-campaign

Screenshot: images/ghl_contacts_add-contact-to-campaign_screenshot.png

---

ContactsCampaignsAdd Contact to Campaign
Add Contact to Campaign
POST
 https://services.leadconnectorhq.com/contacts/:contactId/campaigns/:campaignId
Add contact to Campaign
Requirements
Scope(s)
contacts.write
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
contactId
string
REQUIRED
Contact Id
Example: 3bZD1nQzbul0MCancbQD
campaignId
string
REQUIRED
Campaigns Id
Example: Y2I9XM7aO1hncuSOlc9L
APPLICATION/JSON
BODY
REQUIRED
object
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
succeded
boolean
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
curl -L 'https://services.leadconnectorhq.com/contacts/:contactId/campaigns/:campaignId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
contactId — path
REQUIRED
campaignId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!