# Bulk Delete Social Planner Posts

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/bulk-delete-social-planner-posts

Screenshot: images/ghl_social-planner_bulk-delete-social-planner-posts_screenshot.png

---

Social PlannerPostBulk Delete Social Planner Posts
Bulk Delete Social Planner Posts
POST
 https://services.leadconnectorhq.com/social-media-posting/:locationId/posts/bulk-delete
Deletes multiple posts based on the provided list of post IDs. This operation is useful for clearing up large numbers of posts efficiently.
Note:
1.The maximum number of posts that can be deleted in a single request is '50'.
2.However, It will only get deleted in Highlevel database but still it is recommended to be cautious of this operation.
Requirements
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
postIds
string[]
Requested Results
Example:["662791ee3f216822d7da0c8c"]
Responses
201
400
401
404
422
500
Posts deleted successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Success or Failure
Example:true
statusCode
number
REQUIRED
Status Code
Example:201
message
string
REQUIRED
Message
Example:Posts Deleted Successfully
results
REQUIRED
Message and deleted count
Example:{ message: "Posts deleted successfully", deletedCount: 10 }






















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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/:locationId/posts/bulk-delete' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "postIds": [
    "662791ee3f216822d7da0c8c"
  ]
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
  "postIds": [
    "662791ee3f216822d7da0c8c"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!