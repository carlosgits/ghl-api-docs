# Get Social Media Statistics

Source: https://marketplace.gohighlevel.com/docs/ghl/social-planner/get-statistics

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_social-planner_get-statistics_screenshot.png

---

Social PlannerStatisticsGet Social Media Statistics
Get Social Media Statistics
POST
 https://services.leadconnectorhq.com/social-media-posting/statistics
Retrieve analytics data for multiple social media accounts. Provides metrics for the last 7 days with comparison to the previous 7 days. Supports filtering by platforms and specific connected accounts.
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
Location ID
Example: w37swmmLbA02zgqKPpxITe2
APPLICATION/JSON
BODY
profileIds
string[]
REQUIRED
Array of connected social media account IDs to fetch analytics for. This can be found as 'profileId' in /accounts api.
Possible values: >= 1
Example:["67a5a9aa776c837de4aa5b12"]
platforms
string[]
Array of social media platforms to filter analytics by. If not provided, all platforms will be included. NOTE: Linkedin (PAGE only) and Tiktok (BUSINESS only) are supported.
Possible values: [facebook, instagram, linkedin, google, pinterest, youtube, tiktok]
Example:["facebook","instagram"]
Responses
201
400
401
422
Successfully retrieved analytics data
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
results
object
message
string
Example:Analytics Built Successfully
traceId
string
Example:42fc8dd8-d55b-475f-944f-9efb90d77564































































































































































































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
curl -L 'https://services.leadconnectorhq.com/social-media-posting/statistics' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-d '{
  "profileIds": [
    "67a5a9aa776c837de4aa5b12"
  ],
  "platforms": [
    "facebook",
    "instagram"
  ]
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Parameters
locationId — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
{
  "profileIds": [
    "67a5a9aa776c837de4aa5b12"
  ],
  "platforms": [
    "facebook",
    "instagram"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!