# Get Access Token

Source: https://marketplace.gohighlevel.com/docs/ghl/oauth/get-access-token

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_oauth_get-access-token_screenshot.png

---

OAuth 2.0OAuth 2.0Get Access Token
Get Access Token
POST
 https://services.leadconnectorhq.com/oauth/token
Use Access Tokens to access GoHighLevel resources on behalf of an authenticated location/company.
Request
APPLICATION/X-WWW-FORM-URLENCODED
BODY
REQUIRED
client_id
string
REQUIRED
The ID provided by GHL for your integration
client_secret
string
REQUIRED
grant_type
string
REQUIRED
Possible values: [authorization_code, refresh_token, client_credentials]
code
string
refresh_token
string
user_type
string
The type of token to be requested
Possible values: [Company, Location]
Example:Location
redirect_uri
string
The redirect URI for your application
Example:https://myapp.com/oauth/callback/gohighlevel
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
Example:ab12dc0ae1234a7898f9ff06d4f69gh
token_type
string
Example:Bearer
expires_in
number
Example:86399
refresh_token
string
Example:xy34dc0ae1234a4858f9ff06d4f66ba
scope
string
Example:conversations/message.readonly conversations/message.write
userType
string
Example:Location
locationId
string
Location ID - Present only for Sub-Account Access Token
Example:l1C08ntBrFjLS0elLIYU
companyId
string
Company ID
Example:l1C08ntBrFjLS0elLIYU
approvedLocations
string[]
Approved locations to generate location access token
Example:["l1C08ntBrFjLS0elLIYU"]
userId
string
REQUIRED
USER ID - Represent user id of person who performed installation
Example:l1C08ntBrFjLS0elLIYU
planId
string
Plan Id of the subscribed plan in paid apps.
Example:l1C08ntBrFjLS0elLIYU
isBulkInstallation
boolean
Example:Bearer
installToFutureLocations
boolean
Boolean to control if user wants app to be automatically installed to future locations (only for company tokens)
Example:true
approveAllLocations
boolean
Boolean indicating if user approved all locations during bulk installation (only for company tokens)
Example:true


































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
curl -L -X POST 'https://services.leadconnectorhq.com/oauth/token' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-H 'Accept: application/json'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Body
 REQUIRED
client_id
REQUIRED
client_secret
REQUIRED
grant_type
REQUIRED
---
authorization_code
refresh_token
client_credentials
code
refresh_token
user_type
---
Company
Location
redirect_uri
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!