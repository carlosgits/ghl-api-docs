# Starts OAuth For Twitter Account

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/start-twitter-oauth

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_start-twitter-oauth_screenshot.png

---

Social PlannerOauth | TwitterStarts OAuth For Twitter Account
Starts OAuth For Twitter Account
GET
 https://services.leadconnectorhq.com/social-media-posting/oauth/twitter/start
DEPRECATED
This endpoint has been deprecated and may be replaced or removed in future versions of the API.
As of December 4, 2024, X (formerly Twitter) is no longer supported. We apologise for any inconvenience.
Requirements
Scope(s)
socialplanner/oauth.readonly
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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/oauth/twitter/start' \
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