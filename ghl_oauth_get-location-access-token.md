# Get Location Access Token from Agency Token

Source: https://marketplace.gohighlevel.com/docs/ghl/oauth/get-location-access-token

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_oauth_get-location-access-token_screenshot.png

---

OAuth 2.0OAuth 2.0Get Location Access Token from Agency Token
Get Location Access Token from Agency Token
POST
 https://services.leadconnectorhq.com/oauth/locationToken
This API allows you to generate locationAccessToken from AgencyAccessToken
Requirements
Scope(s)
oauth.write
Auth Method(s)
OAuth Access Token
Token Type(s)
Agency Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
APPLICATION/X-WWW-FORM-URLENCODED
BODY
REQUIRED
companyId
string
REQUIRED
Company Id of location you want to request token for
locationId
string
REQUIRED
The location ID for which you want to obtain accessToken
Responses
200
400
401
422
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
access_token
string
Location access token which can be used to authenticate & authorize API under following scope
Example:ab12dc0ae1234a7898f9ff06d4f69gh
token_type
string
Example:Bearer
expires_in
number
Time in seconds remaining for token to expire
Example:86399
scope
string
Scopes the following accessToken have access to
Example:conversations/message.readonly conversations/message.write
locationId
string
Location ID - Present only for Sub-Account Access Token
Example:l1C08ntBrFjLS0elLIYU
planId
string
Plan Id of the subscribed plan in paid apps.
Example:l1C08ntBrFjLS0elLIYU
userId
string
REQUIRED
USER ID - Represent user id of person who performed installation
Example:l1C08ntBrFjLS0elLIYU
appId
string
App ID of the installed application
Example:6578278e879ad2646715ba9c
versionId
string
Version ID of the installed app version
Example:6578278e879ad2646715ba9c



























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
curl -L -X POST 'https://services.leadconnectorhq.com/oauth/locationToken' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
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
companyId
REQUIRED
locationId
REQUIRED
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!