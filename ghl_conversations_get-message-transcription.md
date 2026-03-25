# Get transcription by Message ID

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/get-message-transcription

Screenshot: images/ghl_conversations_get-message-transcription_screenshot.png

---

ConversationsMessagesGet transcription by Message ID
Get transcription by Message ID
GET
 https://services.leadconnectorhq.com/conversations/locations/:locationId/messages/:messageId/transcription
Get the recording transcription for a message by passing the message id
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
Gives the attached recording transcription to the message
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
mediaChannel
number
REQUIRED
Media channel describes the user interaction channel
Example:1
sentenceIndex
number
REQUIRED
Index of the sentence in the transcription
Example:1
startTime
number
REQUIRED
Start time of the sentence in milliseconds
Example:34
endTime
number
REQUIRED
End time of the sentence in milliseconds
Example:45
transcript
string
REQUIRED
Transcript of the sentence
Example:This call may be recorded for quality assurance purposes.
confidence
number
REQUIRED
Confidence of the transcription
Example:0.5

















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
curl -L 'https://services.leadconnectorhq.com/conversations/locations/:locationId/messages/:messageId/transcription' \
-H 'Accept: application/json' \
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