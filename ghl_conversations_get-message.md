# Get message by message id

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/get-message

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_conversations_get-message_screenshot.png

---

ConversationsMessagesGet message by message id
Get message by message id
GET
 https://services.leadconnectorhq.com/conversations/messages/:id
Get message by message id.
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
Responses
200
400
401
Message object for the id given.
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
id
string
REQUIRED
Example:ve9EPM428h8vShlRW1KT
altId
string
Alternative identifier for the message
Example:msg_123456789
type
number
REQUIRED
Example:1
messageType
string
REQUIRED
Type of the message as a string
Possible values: [TYPE_CALL, TYPE_SMS, TYPE_EMAIL, TYPE_SMS_REVIEW_REQUEST, TYPE_WEBCHAT, TYPE_SMS_NO_SHOW_REQUEST, TYPE_CAMPAIGN_SMS, TYPE_CAMPAIGN_CALL, TYPE_CAMPAIGN_EMAIL, TYPE_CAMPAIGN_VOICEMAIL, TYPE_FACEBOOK, TYPE_CAMPAIGN_FACEBOOK, TYPE_CAMPAIGN_MANUAL_CALL, TYPE_CAMPAIGN_MANUAL_SMS, TYPE_GMB, TYPE_CAMPAIGN_GMB, TYPE_REVIEW, TYPE_INSTAGRAM, TYPE_WHATSAPP, TYPE_CUSTOM_SMS, TYPE_CUSTOM_EMAIL, TYPE_CUSTOM_PROVIDER_SMS, TYPE_CUSTOM_PROVIDER_EMAIL, TYPE_IVR_CALL, TYPE_ACTIVITY_CONTACT, TYPE_ACTIVITY_INVOICE, TYPE_ACTIVITY_PAYMENT, TYPE_ACTIVITY_OPPORTUNITY, TYPE_LIVE_CHAT, TYPE_LIVE_CHAT_INFO_MESSAGE, TYPE_ACTIVITY_APPOINTMENT, TYPE_FACEBOOK_COMMENT, TYPE_INSTAGRAM_COMMENT, TYPE_CUSTOM_CALL, TYPE_INTERNAL_COMMENT, TYPE_ACTIVITY_EMPLOYEE_ACTION_LOG]
Example:SMS
locationId
string
REQUIRED
Example:ve9EPM428h8vShlRW1KT
contactId
string
REQUIRED
Example:ve9EPM428h8vShlRW1KT
conversationId
string
REQUIRED
Example:ve9EPM428h8vShlRW1KT
dateAdded
string
REQUIRED
Example:2024-03-27T18:13:49.000Z
body
string
Example:Hi there
direction
string
REQUIRED
Possible values: [inbound, outbound]
status
string
Possible values: [connected, delivered, failed, opened, pending, read, scheduled, sent, undelivered, clicked, opt_out]
contentType
string
REQUIRED
Example:text/plain
attachments
string[]
An array of attachment URLs. Attachments will be empty for Call and Voicemails, type 1 and 10. Please use get call recording API to fetch call recording and voicemails.
meta
object
source
string
Message source
Possible values: [workflow, bulk_actions, campaign, api, app]
userId
string
User Id
Example:ve9EPM428kjkvShlRW1KT
conversationProviderId
string
Conversation Provider Id
Example:ve9EPM428kjkvShlRW1KT
chatWidgetId
string
Chat Widget Id
Example:67b0cc8cf14b19d85ace7s35
from
string
Sender identifier (phone/name). Not returned for email types.
Example:+14155551234
to
string
Recipient identifier (phone/name). Not returned for email types.
Example:+14155555678
error
string
Error message if message delivery failed

























































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
curl -L 'https://services.leadconnectorhq.com/conversations/messages/:id' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!