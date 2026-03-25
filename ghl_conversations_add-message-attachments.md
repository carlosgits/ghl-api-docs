# Add message attachments

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/add-message-attachments

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_conversations_add-message-attachments_screenshot.png

---

ConversationsMessagesAdd message attachments
Add message attachments
PUT
 https://services.leadconnectorhq.com/conversations/messages/:messageId/attachments
Set attachments on an existing message (replaces existing). Maximum 5 URLs. Supported for Custom Call message type.
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
attachments
string[]
REQUIRED
Array of attachment URLs to set on the message (replaces existing). Maximum 5 URLs.
Example:["https://provider.com/recordings/call-123.mp3"]
Responses
200
400
401
403
Successfully set message attachments
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Indicates whether the operation was successful.
Example:true
messageId
string
REQUIRED
The ID of the message that was updated.
Example:ve9EPM428h8vShlRW1KT
attachments
string[]
REQUIRED
The updated list of attachment URLs on the message.
Example:["https://provider.com/recordings/call-123.mp3"]





















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
curl -L -X PUT 'https://services.leadconnectorhq.com/conversations/messages/:messageId/attachments' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "attachments": [
    "https://provider.com/recordings/call-123.mp3"
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
  "attachments": [
    "https://provider.com/recordings/call-123.mp3"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!