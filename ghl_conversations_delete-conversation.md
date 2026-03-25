# Delete Conversation

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/delete-conversation

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_conversations_delete-conversation_screenshot.png

---

ConversationsConversationsDelete Conversation
Delete Conversation
DELETE
 https://services.leadconnectorhq.com/conversations/:conversationId
Delete the conversation details based on the conversation ID
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/conversations/:conversationId' \
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