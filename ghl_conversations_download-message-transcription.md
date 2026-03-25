# Download transcription by Message ID

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/download-message-transcription

Screenshot: images/ghl_conversations_download-message-transcription_screenshot.png

---

ConversationsMessagesDownload transcription by Message ID
Download transcription by Message ID
GET
 https://services.leadconnectorhq.com/conversations/locations/:locationId/messages/:messageId/transcription/download
Download the recording transcription for a message by passing the message id
Requirements
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
Possible values: [2021-04-15]
API Version
PATH PARAMETERS
locationId
string
REQUIRED
Location ID as string
Example: tDtDnQdgm2LXpyiqYvZ6
messageId
string
REQUIRED
Message ID as string
Example: tDtDnQdgm2LXpyiqYvZ6
Responses
200
400
401
Downloads the attached transcription of the message
Response Headers









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
curl -L 'https://services.leadconnectorhq.com/conversations/locations/:locationId/messages/:messageId/transcription/download' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Security Scheme
bearer
Location-Access
Bearer Token
Parameters
locationId — path
REQUIRED
messageId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!