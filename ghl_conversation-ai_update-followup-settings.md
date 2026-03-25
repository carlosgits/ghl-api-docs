# Update Followup Settings

Source: https://marketplace.gohighlevel.com/docs/ghl/conversation-ai/update-followup-settings

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_conversation-ai_update-followup-settings_screenshot.png

---

Conversation AIActionsUpdate Followup Settings
Update Followup Settings
PATCH
 https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings
Update the followup settings for an action
Requirements
Scope(s)
conversation-ai.write
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
agentId
string
REQUIRED
APPLICATION/JSON
BODY
REQUIRED
actionIds
string[]
REQUIRED
Example:["edxcfghbnjkimd"]
followupSettings
object
REQUIRED
Responses
200
400
401
422
Success
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
data
object
success
boolean
REQUIRED
Success status of the request
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
curl -L -X PATCH 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "actionIds": [
    "edxcfghbnjkimd"
  ],
  "followupSettings": {
    "dynamicChannelSwitching": true,
    "followUpHours": true,
    "workingHours": [
      {
        "dayOfTheWeek": 1,
        "intervals": [
          {
            "startHour": 9,
            "startMinute": 0,
            "endHour": 17,
            "endMinute": 30
          }
        ]
      }
    ],
    "timezoneToUse": "contact"
  }
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
agentId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "actionIds": [
    "edxcfghbnjkimd"
  ],
  "followupSettings": {
    "dynamicChannelSwitching": true,
    "followUpHours": true,
    "workingHours": [
      {
        "dayOfTheWeek": 1,
        "intervals": [
          {
            "startHour": 9,
            "startMinute": 0,
            "endHour": 17,
            "endMinute": 30
          }
        ]
      }
    ],
    "timezoneToUse": "contact"
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!