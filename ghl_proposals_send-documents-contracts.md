# Send document

Source: https://marketplace.gohighlevel.com/docs/ghl/proposals/send-documents-contracts

Screenshot: images/ghl_proposals_send-documents-contracts_screenshot.png

---

ProposalsDocumentsSend document
Send document
POST
 https://services.leadconnectorhq.com/proposals/document/send
Send document to a client
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
locationId
string
REQUIRED
Location Id
Example:hTlkh7t8gujsahgg93
documentId
string
REQUIRED
Document Id
Example:hTlkh7t8gujsahgg93
documentName
string
Document Name
Example:new Document
medium
string
Medium to be used for sending the document
Possible values: [link, email]
Example:email
ccRecipients
object[]
notificationSettings
object
sentBy
string
REQUIRED
Sent ByUser Id
Example:1234567890
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
curl -L 'https://services.leadconnectorhq.com/proposals/document/send' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "locationId": "hTlkh7t8gujsahgg93",
  "documentId": "hTlkh7t8gujsahgg93",
  "documentName": "new Document",
  "medium": "email",
  "ccRecipients": [
    {
      "id": "u240JcS0E5qE0ziHnwMm",
      "email": "jim@gmail.com",
      "imageUrl": "",
      "contactName": "Jim Anton",
      "firstName": "Jim",
      "lastName": "Anton"
    }
  ],
  "notificationSettings": {
    "sender": {
      "fromName": "",
      "fromEmail": ""
    },
    "receive": {
      "subject": "",
      "templateId": ""
    }
  },
  "sentBy": "1234567890"
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
  "locationId": "hTlkh7t8gujsahgg93",
  "documentId": "hTlkh7t8gujsahgg93",
  "documentName": "new Document",
  "medium": "email",
  "ccRecipients": [
    {
      "id": "u240JcS0E5qE0ziHnwMm",
      "email": "jim@gmail.com",
      "imageUrl": "",
      "contactName": "Jim Anton",
      "firstName": "Jim",
      "lastName": "Anton"
    }
  ],
  "notificationSettings": {
    "sender": {
      "fromName": "",
      "fromEmail": ""
    },
    "receive": {
      "subject": "",
      "templateId": ""
    }
  },
  "sentBy": "1234567890"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!