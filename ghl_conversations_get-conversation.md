# Get Conversation

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/get-conversation

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_conversations_get-conversation_screenshot.png

---

ConversationsConversationsGet Conversation
Get Conversation
GET
 https://services.leadconnectorhq.com/conversations/:conversationId
Get the conversation details based on the conversation ID
Requirements
Scope(s)
conversations.readonly
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
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
contactId
string
REQUIRED
Unique identifier of the contact associated with this conversation
Example:ve9EPM428kjkvShlRW1KT
locationId
string
REQUIRED
Unique identifier of the business location where this conversation takes place
Example:ve9EPM428kjkvShlRW1KT
deleted
boolean
REQUIRED
Flag indicating if this conversation has been moved to trash/deleted
Example:false
inbox
boolean
REQUIRED
Flag indicating if this conversation is currently in the main inbox view
Example:true
type
number
REQUIRED
Communication channel type for this conversation: 1 (Phone), 2 (Email), 3 (Facebook Messenger), 4 (Review), 5 (Group SMS), 6 (Internal Chat - coming soon)
unreadCount
number
REQUIRED
Number of messages in this conversation that have not been read by the user
Example:1
assignedTo
string
Unique identifier of the team member currently responsible for handling this conversation
Example:ve9EPM428kjkvShlRW1KT
id
string
REQUIRED
Unique identifier for this specific conversation thread
Example:ve9EPM428kjkvShlRW1KT
starred
boolean
Flag indicating if this conversation has been marked as important/starred by the user
Example:true




















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
curl -L 'https://services.leadconnectorhq.com/conversations/:conversationId' \
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
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!