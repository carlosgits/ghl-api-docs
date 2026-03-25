# Uninstall an application

Source: https://marketplace.gohighlevel.com/docs/ghl/marketplace/uninstall-application

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_marketplace_uninstall-application_screenshot.png

---

Developer marketplaceApp ManagementUninstall an application
Uninstall an application
DELETE
 https://services.leadconnectorhq.com/marketplace/app/:appId/installations
Uninstalls an application from your company or a specific location. This will remove the application`s access and stop all its functionalities
Requirements
Scope(s)
oauth.write
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
The application id which is to be uninstalled.
Example: 674587703dfd4161f1e3c557
APPLICATION/JSON
BODY
REQUIRED
companyId
string
The company id from which the application is to be uninstalled. If you pass agency token, then companyId is required. It will uninstall application from agency as well as all sub-accounts.
Example:tDtDnQdgm2LXpyiqYvZ6
locationId
string
The location id from which the application is to be uninstalled. If you pass location token, then locationId is required. It will uninstall application from that location only.
Example:tDtDnQdgm2LXpyiqYvZ6
reason
string
The reason for uninstalling the application. Reason is required if you are uninstalling the application as a developer.
Example:Application is not working as expected
Responses
200
400
401
422
Successfully uninstalled the application
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
The status of the uninstallation of the application
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/marketplace/app/:appId/installations' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "companyId": "tDtDnQdgm2LXpyiqYvZ6",
  "locationId": "tDtDnQdgm2LXpyiqYvZ6",
  "reason": "Application is not working as expected"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Security Scheme
Location-Access-Only
Agency-Access
Bearer Token
Parameters
appId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "companyId": "tDtDnQdgm2LXpyiqYvZ6",
  "locationId": "tDtDnQdgm2LXpyiqYvZ6",
  "reason": "Application is not working as expected"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!