# Add an external outbound call

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/add-an-outbound-message

Screenshot: images/ghl_conversations_add-an-outbound-message_screenshot.png

---

ConversationsMessagesAdd an external outbound call
Add an external outbound call
POST
 https://services.leadconnectorhq.com/conversations/messages/outbound
Post the necessary fields for the API to add a new outbound call.
Requirements
Scope(s)
conversations/message.write
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
APPLICATION/JSON
BODY
REQUIRED
type
string
REQUIRED
Message Type
Possible values: [Call]
Example:Call
attachments
string[]
Array of attachments
conversationId
string
REQUIRED
Conversation Id
Example:ve9EPM428h8vShlRW1KT
conversationProviderId
string
REQUIRED
Conversation Provider Id
Example:61d6d1f9cdac7612faf80753
altId
string
external mail provider's message id
Example:61d6d1f9cdac7612faf80753
date
date-time
Date of the outbound message
call
object
Responses
200
400
401
Created the message
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
conversationId
string
REQUIRED
Conversation ID.
Example:ABC12h2F6uBrIkfXYazb
messageId
string
REQUIRED
This is the main Message ID
Example:t22c6DQcTDf3MjRhwf77
message
string
REQUIRED
contactId
string
dateAdded
date-time
emailMessageId
string


















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
curl -L 'https://services.leadconnectorhq.com/conversations/messages/outbound' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "type": "Call",
  "attachments": [
    "string"
  ],
  "conversationId": "ve9EPM428h8vShlRW1KT",
  "conversationProviderId": "61d6d1f9cdac7612faf80753",
  "altId": "61d6d1f9cdac7612faf80753",
  "date": "2024-07-29T15:51:28.071Z",
  "call": {
    "to": "+15037081210",
    "from": "+15037081210",
    "status": "completed"
  }
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
2021-04-15
Body
 REQUIRED
{
  "type": "Call",
  "attachments": [
    "string"
  ],
  "conversationId": "ve9EPM428h8vShlRW1KT",
  "conversationProviderId": "61d6d1f9cdac7612faf80753",
  "altId": "61d6d1f9cdac7612faf80753",
  "date": "2024-07-29T15:51:28.071Z",
  "call": {
    "to": "+15037081210",
    "from": "+15037081210",
    "status": "completed"
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!