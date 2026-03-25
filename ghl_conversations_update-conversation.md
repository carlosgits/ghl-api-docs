# Update Conversation

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/update-conversation

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_conversations_update-conversation_screenshot.png

---

ConversationsConversationsUpdate Conversation
Update Conversation
PUT
 https://services.leadconnectorhq.com/conversations/:conversationId
Update the conversation details based on the conversation ID
Requirements
Scope(s)
conversations.write
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
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
Location ID as string
Example:tDtDnQdgm2LXpyiqYvZ6
unreadCount
number
Count of unread messages in the conversation
Example:1
starred
boolean
Starred status of the conversation.
Example:true
feedback
object
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Boolean value as the API response.
Example:true
conversation
object


























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
curl -L -X PUT 'https://services.leadconnectorhq.com/conversations/:conversationId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "tDtDnQdgm2LXpyiqYvZ6",
  "unreadCount": 1,
  "starred": true,
  "feedback": {}
}'
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
Body
 REQUIRED
{
  "locationId": "tDtDnQdgm2LXpyiqYvZ6",
  "unreadCount": 1,
  "starred": true,
  "feedback": {}
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!