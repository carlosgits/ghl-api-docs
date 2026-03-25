# Get email by Id

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/get-email-by-id

Screenshot: images/ghl_conversations_get-email-by-id_screenshot.png

---

ConversationsEmailGet email by Id
Get email by Id
GET
 https://services.leadconnectorhq.com/conversations/messages/email/:id
Get email by Id
Request
Responses
200
Email object for the id given.
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
External Id
Example:ve9EPM428h8vShlRW1KT
threadId
string
REQUIRED
Message Id or thread Id
Example:ve9EPM428h8vShlRW1KT
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
subject
string
Example:Order confirm
body
string
REQUIRED
Example:Hi there
direction
string
REQUIRED
Possible values: [inbound, outbound]
status
string
Possible values: [pending, scheduled, sent, delivered, read, undelivered, connected, failed, opened]
contentType
string
REQUIRED
Example:text/plain
attachments
string[]
An array of attachment URLs.
provider
string
from
string
REQUIRED
Name and Email Id of the sender
to
string[]
REQUIRED
List of email Ids of the receivers
cc
string[]
List of email Ids of the people in the cc field
bcc
string[]
List of email Ids of the people in the bcc field
replyToMessageId
string
In case of reply, email message Id of the reply to email
source
string
Email source
Possible values: [workflow, bulk_actions, campaign, api, app]
conversationProviderId
string
Conversation provider ID
Example:cI08i1Bls3iTB9bKgF01
error
string
Error message for bounced/failed emails
































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
curl -L 'https://services.leadconnectorhq.com/conversations/messages/email/:id' \
-H 'Accept: application/json'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!