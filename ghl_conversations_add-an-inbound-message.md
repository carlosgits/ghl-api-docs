# Add an inbound message

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/add-an-inbound-message

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_conversations_add-an-inbound-message_screenshot.png

---

ConversationsMessagesAdd an inbound message
Add an inbound message
POST
 https://services.leadconnectorhq.com/conversations/messages/inbound
Post the necessary fields for the API to add a new inbound message.

Note: Either conversationId or contactId is required
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
Possible values: [SMS, Email, WhatsApp, GMB, IG, FB, Custom, WebChat, Live_Chat, Call]
Example:SMS
attachments
string[]
Array of attachments
message
string
Message Body
conversationId
string
Conversation Id
Example:ve9EPM428h8vShlRW1KT
contactId
string
Contact Id
Example:ve9EPM428h8vShlRW1KT
conversationProviderId
string
REQUIRED
Conversation Provider Id
Example:61d6d1f9cdac7612faf80753
html
string
HTML Body of Email
subject
string
Subject of the Email
emailFrom
string
Email address to send from. This field is associated with the contact record and cannot be dynamically changed.
Example:sender@company.com
emailTo
string
Recipient email address. This field is associated with the contact record and cannot be dynamically changed.
emailCc
string[]
List of email address to CC
Example:["john1@doe.com","john2@doe.com"]
emailBcc
string[]
List of email address to BCC
Example:["john1@doe.com","john2@doe.com"]
emailMessageId
string
Send the email message id for which this email should be threaded. This is for replying to a specific email
altId
string
external mail provider's message id
Example:61d6d1f9cdac7612faf80753
direction
object
Message direction, if required can be set manually, default is outbound
Default value: outbound
Example:["outbound","inbound"]
date
date-time
Date of the inbound message
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
curl -L 'https://services.leadconnectorhq.com/conversations/messages/inbound' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "type": "SMS",
  "attachments": [
    "string"
  ],
  "message": "string",
  "conversationId": "ve9EPM428h8vShlRW1KT",
  "contactId": "ve9EPM428h8vShlRW1KT",
  "conversationProviderId": "61d6d1f9cdac7612faf80753",
  "html": "string",
  "subject": "string",
  "emailFrom": "sender@company.com",
  "emailTo": "string",
  "emailCc": [
    "john1@doe.com",
    "john2@doe.com"
  ],
  "emailBcc": [
    "john1@doe.com",
    "john2@doe.com"
  ],
  "emailMessageId": "string",
  "altId": "61d6d1f9cdac7612faf80753",
  "direction": [
    "outbound",
    "inbound"
  ],
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
  "type": "SMS",
  "attachments": [
    "string"
  ],
  "message": "string",
  "conversationId": "ve9EPM428h8vShlRW1KT",
  "contactId": "ve9EPM428h8vShlRW1KT",
  "conversationProviderId": "61d6d1f9cdac7612faf80753",
  "html": "string",
  "subject": "string",
  "emailFrom": "sender@company.com",
  "emailTo": "string",
  "emailCc": [
    "john1@doe.com",
    "john2@doe.com"
  ],
  "emailBcc": [
    "john1@doe.com",
    "john2@doe.com"
  ],
  "emailMessageId": "string",
  "altId": "61d6d1f9cdac7612faf80753",
  "direction": [
    "outbound",
    "inbound"
  ],
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