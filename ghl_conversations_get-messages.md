# Get messages by conversation id

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/get-messages

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_conversations_get-messages_screenshot.png

---

ConversationsMessagesGet messages by conversation id
Get messages by conversation id
GET
 https://services.leadconnectorhq.com/conversations/:conversationId/messages
Get messages by conversation id.
Requirements
Scope(s)
conversations/message.readonly
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
conversationId
string
REQUIRED
Conversation ID as string
Example: tDtDnQdgm2LXpyiqYvZ6
QUERY PARAMETERS
lastMessageId
string
Message ID of the last message in the list as a string
Example: tDtDnQdgm2LXpyiqYvZ6
limit
number
Number of messages to be fetched from the conversation. Default limit is 20
Example: 20
type
string
Possible values: [TYPE_CALL, TYPE_SMS, TYPE_EMAIL, TYPE_FACEBOOK, TYPE_GMB, TYPE_INSTAGRAM, TYPE_WHATSAPP, TYPE_ACTIVITY_APPOINTMENT, TYPE_ACTIVITY_CONTACT, TYPE_ACTIVITY_INVOICE, TYPE_ACTIVITY_PAYMENT, TYPE_ACTIVITY_OPPORTUNITY, TYPE_LIVE_CHAT, TYPE_INTERNAL_COMMENTS, TYPE_ACTIVITY_EMPLOYEE_ACTION_LOG]
Types of message to fetched separated with comma
Example: TYPE_SMS,TYPE_CALL
Responses
200
400
401
List of messages for the conversation id of the given type.
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
messages
object
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
curl -L 'https://services.leadconnectorhq.com/conversations/:conversationId/messages' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
conversationId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!