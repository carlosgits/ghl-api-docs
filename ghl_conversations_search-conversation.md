# Search Conversations

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/search-conversation

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_conversations_search-conversation_screenshot.png

---

ConversationsSearchSearch Conversations
Search Conversations
GET
 https://services.leadconnectorhq.com/conversations/search
Returns a list of all conversations matching the search criteria along with the sort and filter options selected.
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
QUERY PARAMETERS
locationId
string
REQUIRED
Location Id
Example: ABCHkzuJQ8ZMd4Te84GK
contactId
string
Contact Id
Example: 9VEmS0si86GW6gXWU89b
assignedTo
string
User IDs that conversations are assigned to. Multiple IDs can be provided as comma-separated values. Use "unassigned" to fetch conversations not assigned to any user.
Example: ABCHkzuJQ8ZMd4Te84GK,fGiae4CHkzoskh8thsik
followers
string
User IDs of followers to filter conversations by. Multiple IDs can be provided as comma-separated values.
Example: ABCHkzuJQ8ZMd4Te84GK,fGiae4CHkzoskh8thsik
mentions
string
User Id of the mention. Multiple values are comma separated.
Example: ABCHkzuJQ8ZMd4Te84GK,fGiae4CHkzoskh8thsik
query
string
Search paramater as a string
Example: Search string
sort
string
Possible values: [asc, desc]
Sort paramater - asc or desc
Example: asc
startAfterDate
any
Search to begin after the specified date - should contain the sort value of the last document
Example: 1600854
id
string
Id of the conversation
Example: ABCHkzuJQ8ZMd4Te84GK
limit
number
Limit of conversations - Default is 20
Example: 20
lastMessageType
string
Possible values: [TYPE_CALL, TYPE_SMS, TYPE_EMAIL, TYPE_SMS_REVIEW_REQUEST, TYPE_WEBCHAT, TYPE_SMS_NO_SHOW_REQUEST, TYPE_CAMPAIGN_SMS, TYPE_CAMPAIGN_CALL, TYPE_CAMPAIGN_EMAIL, TYPE_CAMPAIGN_VOICEMAIL, TYPE_FACEBOOK, TYPE_CAMPAIGN_FACEBOOK, TYPE_CAMPAIGN_MANUAL_CALL, TYPE_CAMPAIGN_MANUAL_SMS, TYPE_GMB, TYPE_CAMPAIGN_GMB, TYPE_REVIEW, TYPE_INSTAGRAM, TYPE_WHATSAPP, TYPE_CUSTOM_SMS, TYPE_CUSTOM_EMAIL, TYPE_CUSTOM_PROVIDER_SMS, TYPE_CUSTOM_PROVIDER_EMAIL, TYPE_IVR_CALL, TYPE_ACTIVITY_CONTACT, TYPE_ACTIVITY_INVOICE, TYPE_ACTIVITY_PAYMENT, TYPE_ACTIVITY_OPPORTUNITY, TYPE_LIVE_CHAT, TYPE_LIVE_CHAT_INFO_MESSAGE, TYPE_ACTIVITY_APPOINTMENT, TYPE_FACEBOOK_COMMENT, TYPE_INSTAGRAM_COMMENT, TYPE_CUSTOM_CALL, TYPE_INTERNAL_COMMENT, TYPE_ACTIVITY_EMPLOYEE_ACTION_LOG]
Type of the last message in the conversation as a string
Example: TYPE_SMS
lastMessageAction
string
Possible values: [automated, manual]
Action of the last outbound message in the conversation as string.
Example: manual
lastMessageDirection
string
Possible values: [inbound, outbound]
Direction of the last message in the conversation as string.
Example: inbound
status
string
Possible values: [all, read, unread, starred, recents]
The status of the conversation to be filtered - all, read, unread, starred
Example: all
sortBy
string
Possible values: [last_manual_message_date, last_message_date, score_profile]
The sorting of the conversation to be filtered as - manual messages or all messages
Example: last_message_date
sortScoreProfile
string
Id of score profile on which sortBy.ScoreProfile should sort on
Example: ABCHkzuJQ8ZMd4Te84GK
scoreProfile
string
Id of score profile on which conversations should get filtered out, works with scoreProfileMin & scoreProfileMax
Example: ABCHkzuJQ8ZMd4Te84GK
scoreProfileMin
number
Minimum value for score
Example: ABCHkzuJQ8ZMd4Te84GK
scoreProfileMax
number
Maximum value for score
Example: ABCHkzuJQ8ZMd4Te84GK
Responses
200
400
401
Successfully fetched the conversations
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
conversations
object[]
REQUIRED
total
number
REQUIRED
Total Number of results found for the given query
Example:100



























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
curl -L 'https://services.leadconnectorhq.com/conversations/search' \
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