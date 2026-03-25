# Create a new category queue

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/create-queue

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_create-queue_screenshot.png

---

Social PlannerCategory QueueCreate a new category queue
Create a new category queue
POST
 https://services.leadconnectorhq.com/social-media-posting/category/queues
Creates a queue in draft status for a category. Published posts are auto-added. Use update endpoint to activate.
Requirements
Scope(s)
socialplanner/category.write
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
Possible values: [2021-07-28]
API Version
Example: 2021-07-28
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
Location ID
Example:609e126a1c4ae1001291e1b5
categoryId
string
REQUIRED
Category ID
Example:60af88475f1b2c001f5d5f4b
timeSlots
object[]
REQUIRED
enableFuturePosts
boolean
Enable Future Posts. Defaults to false.
Example:true
prioritizeNewContent
boolean
Prioritize New Content. Defaults to false.
Example:false
userId
string
REQUIRED
User id
Example:w37swmmLbA02zgqKPpxITe
Responses
201
400
401
422
Queue created successfully.
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Example:true
statusCode
number
REQUIRED
Example:201
results
object
REQUIRED
traceId
string














































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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/category/queues' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "609e126a1c4ae1001291e1b5",
  "categoryId": "60af88475f1b2c001f5d5f4b",
  "timeSlots": [
    {
      "dayOfWeek": 0,
      "time": "09:00"
    }
  ],
  "enableFuturePosts": true,
  "prioritizeNewContent": false,
  "userId": "w37swmmLbA02zgqKPpxITe"
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
2021-07-28
Body
 REQUIRED
{
  "locationId": "609e126a1c4ae1001291e1b5",
  "categoryId": "60af88475f1b2c001f5d5f4b",
  "timeSlots": [
    {
      "dayOfWeek": 0,
      "time": "09:00"
    }
  ],
  "enableFuturePosts": true,
  "prioritizeNewContent": false,
  "userId": "w37swmmLbA02zgqKPpxITe"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!