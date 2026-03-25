# Cancel a scheduled message.

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/cancel-scheduled-message

Screenshot: images/ghl_conversations_cancel-scheduled-message_screenshot.png

---

ConversationsMessagesCancel a scheduled message.
Cancel a scheduled message.
DELETE
 https://services.leadconnectorhq.com/conversations/messages/:messageId/schedule
Post the messageId for the API to delete a scheduled message.
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
Responses
200
400
401
The scheduled message was cancelled successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
status
number
REQUIRED
HTTP Status code of the request
Example:404
message
string
REQUIRED
Error message of the request
Example:Failed cancel the scheduled message













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
curl -L -X DELETE 'https://services.leadconnectorhq.com/conversations/messages/:messageId/schedule' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!