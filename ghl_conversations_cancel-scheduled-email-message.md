# Cancel a scheduled email message.

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/cancel-scheduled-email-message

Screenshot: images/ghl_conversations_cancel-scheduled-email-message_screenshot.png

---

ConversationsEmailCancel a scheduled email message.
Cancel a scheduled email message.
DELETE
 https://services.leadconnectorhq.com/conversations/messages/email/:emailMessageId/schedule
Post the messageId for the API to delete a scheduled email message.
Request
PATH PARAMETERS
emailMessageId
string
REQUIRED
Email Message Id
Example: ve9EPM428h8vShlRW1KT
Responses
200
The scheduled email message was cancelled successfully
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
CURL
NODEJS
PYTHON
PHP
JAVA
GO
RUBY
POWERSHELL
CURL
curl -L -X DELETE 'https://services.leadconnectorhq.com/conversations/messages/email/:emailMessageId/schedule' \
-H 'Accept: application/json'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Parameters
emailMessageId — path
REQUIRED
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!