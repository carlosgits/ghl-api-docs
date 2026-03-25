# Export messages by location ID

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/export-messages-by-location

Screenshot: images/ghl_conversations_export-messages-by-location_screenshot.png

---

ConversationsMessagesExport messages by location ID
Export messages by location ID
GET
 https://services.leadconnectorhq.com/conversations/messages/export
Export messages for a specific location with cursor-based pagination support.
Channel Filtering Behavior:
When channel is omitted: Returns all non-email message types, including messages that don't belong to any specific channel.
When channel=Email: Returns email messages only.
When channel is specified (SMS, Call, WhatsApp, etc.): Returns messages for that specific channel.
Limitations:
Group Chat and SMS Review Request message types are not supported.
Cursor validity is 2 minutes from the last request made.
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
QUERY PARAMETERS
locationId
string
REQUIRED
Location ID to filter messages by
channel
string
Possible values: [Call, SMS, Email, WhatsApp, Instagram, Facebook]
Filter by message channel. Optional - when not provided, all non-email message types will be returned including activity messages (opportunity updates, appointments, etc.). To fetch email messages, you must explicitly set channel=Email.
limit
number
Possible values: >= 10 and <= 500
Number of messages to return per page
Default value:100
cursor
string
Cursor for pagination. Pass the nextCursor from previous response to get next page.
Example: a748514c-f49e-4fa8-9954-b53afc78d81d
sortBy
string
Possible values: [createdAt, updatedAt]
Field to sort by
Default value:createdAt
sortOrder
string
Possible values: [asc, desc]
Sort order
Default value:desc
conversationId
string
Filter messages by conversation ID
contactId
string
Filter messages by contact ID
startDate
string
Start date to filter messages by
endDate
string
End date to filter messages by
Responses
200
400
401
List of messages for the location with pagination details.
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
messages
object[]
REQUIRED
nextCursor
string
Cursor for fetching next page. Null if no more results.
Example:a748514c-f49e-4fa8-9954-b53afc78d81d
total
number
REQUIRED
Total number of messages matching the query
Example:1234































































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
curl -L 'https://services.leadconnectorhq.com/conversations/messages/export' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — query
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!