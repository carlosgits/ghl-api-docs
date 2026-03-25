# Agent/Ai-Bot is typing a message indicator for live chat

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/live-chat-agent-typing

Screenshot: images/ghl_conversations_live-chat-agent-typing_screenshot.png

---

ConversationsProvidersAgent/Ai-Bot is typing a message indicator for live chat
Agent/Ai-Bot is typing a message indicator for live chat
POST
 https://services.leadconnectorhq.com/conversations/providers/live-chat/typing
Agent/AI-Bot will call this when they are typing a message in live chat message
Requirements
Scope(s)
conversations/livechat.write
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
locationId
string
REQUIRED
Location Id
Example:ve9EPM428h8vShlRW1KT
isTyping
string
REQUIRED
Typing status
Example:true
visitorId
string
REQUIRED
visitorId is the Unique ID assigned to each Live chat visitor. visitorId will be added soon in GET Contact API
Example:ve9EPM428h8vShlRW1KT
conversationId
string
REQUIRED
Conversation Id
Example:ve9EPM428h8vShlRW1KT
Responses
201
400
401
422
Show typing indicator for live chat
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
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
curl -L 'https://services.leadconnectorhq.com/conversations/providers/live-chat/typing' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "isTyping": true,
  "visitorId": "ve9EPM428h8vShlRW1KT",
  "conversationId": "ve9EPM428h8vShlRW1KT"
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
  "locationId": "ve9EPM428h8vShlRW1KT",
  "isTyping": true,
  "visitorId": "ve9EPM428h8vShlRW1KT",
  "conversationId": "ve9EPM428h8vShlRW1KT"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!