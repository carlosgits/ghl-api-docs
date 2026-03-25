# Update message status

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/update-message-status

Screenshot: images/ghl_conversations_update-message-status_screenshot.png

---

ConversationsMessagesUpdate message status
Update message status
PUT
 https://services.leadconnectorhq.com/conversations/messages/:messageId/status
Post the necessary fields for the API to update message status.
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
PATH PARAMETERS
messageId
string
REQUIRED
Message Id
Example: ve9EPM428h8vShlRW1KT
APPLICATION/JSON
BODY
REQUIRED
status
string
REQUIRED
Message status
Possible values: [delivered, failed, pending, read]
Example:read
error
object
emailMessageId
string
Email message Id
Example:ve9EPM428h8vShlRW1KT
recipients
string[]
Email delivery status for additional email recipients.
Responses
200
400
401
403
Created the message
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
conversationId
string
REQUIRED
Conversation ID.
Example:ABC12h2F6uBrIkfXYazb
emailMessageId
string
This contains the email message id (only for Email type). Use this ID to send inbound replies to GHL to create a threaded email.
Example:rnGyqh2F6uBrIkfhFo9A
messageId
string
REQUIRED
This is the main Message ID
Example:t22c6DQcTDf3MjRhwf77
messageIds
string[]
When sending via the GMB channel, we will be returning list of messageIds instead of single messageId.
msg
string
Additional response message when sending a workflow message
Example:Message queued successfully.























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
curl -L -X PUT 'https://services.leadconnectorhq.com/conversations/messages/:messageId/status' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "status": "read",
  "error": {
    "code": "1",
    "type": "saas",
    "message": "There was an error from the provider"
  },
  "emailMessageId": "ve9EPM428h8vShlRW1KT",
  "recipients": [
    "string"
  ]
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
messageId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "status": "read",
  "error": {
    "code": "1",
    "type": "saas",
    "message": "There was an error from the provider"
  },
  "emailMessageId": "ve9EPM428h8vShlRW1KT",
  "recipients": [
    "string"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!