# Create Conversation

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/create-conversation

Screenshot: images/ghl_conversations_create-conversation_screenshot.png

---

ConversationsConversationsCreate Conversation
Create Conversation
POST
 https://services.leadconnectorhq.com/conversations/
Creates a new conversation with the data provided
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
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
Location ID as string
Example:tDtDnQdgm2LXpyiqYvZ6
contactId
string
REQUIRED
Contact ID as string
Example:tDtDnQdgm2LXpyiqYvZ6
Responses
201
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
Indicates whether the API request was successful.
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
curl -L 'https://services.leadconnectorhq.com/conversations/' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "tDtDnQdgm2LXpyiqYvZ6",
  "contactId": "tDtDnQdgm2LXpyiqYvZ6"
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
  "locationId": "tDtDnQdgm2LXpyiqYvZ6",
  "contactId": "tDtDnQdgm2LXpyiqYvZ6"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!