# Starts OAuth For Oauth Account

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/start-oauth

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_start-oauth_screenshot.png

---

Social PlannerOAuth | GenericStarts OAuth For Oauth Account
Starts OAuth For Oauth Account
GET
 https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start
Open the API in a window with appropriate params and headers instead of using the Curl. User is navigated to OAuth login screen. On successful login, listen on window object for message where event listener returns data in its callback function.
Sample code to listen to event data:
window.addEventListener('message', function(e) { if (e.data && e.data.page === 'social_media_posting') { const { actionType, page, platform, placement, accountId, reconnectAccounts } = e.data } }, false)
Event Data Response:
{ actionType: string, Ex: "close" page: string, Ex: "social-media-posting" platform: string, Ex: "facebook" placement: string, Ex: "placement" accountId: string, Ex: "658a9b6833b91e0ecb8f3958" reconnectAccounts: string[]] Ex: ["658a9b6833b91e0ecb834acd", "efd2daa9b6833b91e0ecb8f3511"] }
The accountId retrieved from above data can be used to fetch account details using below API -
API: '/social-media-posting/oauth/{locationId}/{platform}/accounts/{accountId}'
Method: GET
Request
HEADER PARAMETERS
Authorization
string
REQUIRED
Access Token
Example: Bearer 9c48df2694a849b6089f9d0d3513efe
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
Example: 2021-07-28
PATH PARAMETERS
platform
string
REQUIRED
Possible values: [google, facebook, instagram, linkedin, tiktok, tiktok-business, youtube, pinterest]
Platform
Example: google
QUERY PARAMETERS
locationId
string
REQUIRED
Location Id
Example: w37swmmLbA02zgqKPpxITe2
userId
string
REQUIRED
User Id
Example: u37swmmLbA02zgqKPpxITe2
page
string
Page
Example: integration
reconnect
string
Reconnect
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
CURL
NODEJS
PYTHON
PHP
JAVA
GO
RUBY
POWERSHELL
CURL
curl -L 'https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Parameters
platform — path
REQUIRED
---
google
facebook
instagram
linkedin
tiktok
tiktok-business
youtube
pinterest
locationId — query
REQUIRED
userId — query
REQUIRED
Authorization — header
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