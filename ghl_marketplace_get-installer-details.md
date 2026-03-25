# Get Installer Details

Source: https://marketplace.gohighlevel.com/docs/ghl/marketplace/get-installer-details

Screenshot: images/ghl_marketplace_get-installer-details_screenshot.png

---

Developer marketplaceApp ManagementGet Installer Details
Get Installer Details
GET
 https://services.leadconnectorhq.com/marketplace/app/:appId/installations
Fetches installer details for the authenticated user. This endpoint returns information about the company, location, user, and installation details associated with the current OAuth token.
Requirements
Scope(s)
marketplace-installer-details.readonly
Auth Method(s)
OAuth Access Token
Token Type(s)
Sub-Account Token
Agency Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
PATH PARAMETERS
appId
string
REQUIRED
ID of the app to get installer details
Responses
200
400
403
Successfully retrieved installer details. Returns company, location, user, and installation information.
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
installationDetails
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
curl -L 'https://services.leadconnectorhq.com/marketplace/app/:appId/installations' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Security Scheme
Location-Access-Only
Agency-Access-Only
Bearer Token
Parameters
appId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!