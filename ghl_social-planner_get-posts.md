# Get posts

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/get-posts

Screenshot: images/ghl_social-planner_get-posts_screenshot.png

---

Social PlannerPostGet posts
Get posts
POST
 https://services.leadconnectorhq.com/social-media-posting/:locationId/posts/list
Get Posts
Requirements
Scope(s)
socialplanner/post.readonly
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
PATH PARAMETERS
locationId
string
REQUIRED
Location Id
Example: ve9EPM428h8vShlRW1KT
APPLICATION/JSON
BODY
REQUIRED
type
string
type must be one of the following values: recent, all, scheduled, draft, failed, in_review, published, in_progress, pending and deleted
Default value: all
Example:all
accounts
string
List of account Ids separated by comma as a string
Example:660a83fc29deacac50033e2b_omaDY3RbWtTP511e808O_17841465964543589, 38bF83fc29deacac50033e2b_omaDY3RbWtr3P11e808O_17841465964543998
skip
string
REQUIRED
Number of records to skip for pagination
Default value: 0
Example:0
limit
string
REQUIRED
Maximum number of records to return
Default value: 10
Example:10
fromDate
string
REQUIRED
From Date
Example:2024-01-22T05:32:49.463Z
toDate
string
REQUIRED
To Date
Example:2024-03-20T05:32:49.463Z
includeUsers
string
REQUIRED
Include User Data
Example:true
postType
object
Post Type must be one of the following values: - post, story, reel
Example:post
Responses
201
400
401
422
Successful response
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
Example:Fetched Posts
results
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/:locationId/posts/list' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "type": "all",
  "accounts": "660a83fc29deacac50033e2b_omaDY3RbWtTP511e808O_17841465964543589, 38bF83fc29deacac50033e2b_omaDY3RbWtr3P11e808O_17841465964543998",
  "skip": "0",
  "limit": "10",
  "fromDate": "2024-01-22T05:32:49.463Z",
  "toDate": "2024-03-20T05:32:49.463Z",
  "includeUsers": "true",
  "postType": "post"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "type": "all",
  "accounts": "660a83fc29deacac50033e2b_omaDY3RbWtTP511e808O_17841465964543589, 38bF83fc29deacac50033e2b_omaDY3RbWtr3P11e808O_17841465964543998",
  "skip": "0",
  "limit": "10",
  "fromDate": "2024-01-22T05:32:49.463Z",
  "toDate": "2024-03-20T05:32:49.463Z",
  "includeUsers": "true",
  "postType": "post"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!