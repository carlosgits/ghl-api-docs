# Starts OAuth For Facebook Account

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/start-facebook-oauth

Screenshot: images/ghl_social-planner_start-facebook-oauth_screenshot.png

---

Social PlannerOauth | FacebookStarts OAuth For Facebook Account
Starts OAuth For Facebook Account
GET
 https://services.leadconnectorhq.com/social-media-posting/oauth/facebook/start
Open the API in a window with appropriate params and headers instead of using the Curl. User is navigated to Facebook login OAuth screen. On successful login, listen on window object for message where event listener returns data in its callback function.
Sample code to listen to event data:
window.addEventListener('message', function(e) { if (e.data && e.data.page === 'social_media_posting') { const { actionType, page, platform, placement, accountId, reconnectAccounts } = e.data } }, false)
Event Data Response:
{ actionType: string, Ex: "close" page: string, Ex: "social-media-posting" platform: string, Ex: "facebook" placement: string, Ex: "placement" accountId: string, Ex: "658a9b6833b91e0ecb8f3958" reconnectAccounts: string[]] Ex: ["658a9b6833b91e0ecb834acd", "efd2daa9b6833b91e0ecb8f3511"] }
The accountId retrieved from above data can be used to fetch Facebook account details using below API -
API: '/social-media-posting/oauth/facebook/accounts/:accountId'
Method: GET
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
QUERY PARAMETERS
locationId
string
REQUIRED
Account Location Id
Example: w37swmmLbA02zgqKPpxITe2
userId
string
REQUIRED
User ID
Example: u37swmmLbA02zgqKPpxITe2
page
string
Facebook Page
Example: integration
reconnect
string
Reconnect boolean as string
Example: true
Responses
200
400
401
422
Successful Response
















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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/oauth/facebook/start' \
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
userId — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!