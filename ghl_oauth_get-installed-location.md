# Get Location where app is installed

Source: https://marketplace.gohighlevel.com/docs/ghl/oauth/get-installed-location

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_oauth_get-installed-location_screenshot.png

---

OAuth 2.0OAuth 2.0Get Location where app is installed
Get Location where app is installed
GET
 https://services.leadconnectorhq.com/oauth/installedLocations
This API allows you fetch location where app is installed upon
Requirements
Scope(s)
oauth.readonly
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
QUERY PARAMETERS
skip
string
Parameter to skip the number installed locations
Default value:0
Example: 1
limit
string
Parameter to limit the number installed locations
Default value:20
Example: 10
query
string
Parameter to search for the installed location by name
Example: location name
isInstalled
boolean
Filters out location which are installed for specified app under the specified company
Example:
companyId
string
REQUIRED
Parameter to search by the companyId
Example: tDtDnQdgm2LXpyiqYvZ6
appId
string
REQUIRED
Parameter to search by the appId
Example: tDtDnQdgm2LXpyiqYvZ6
versionId
string
VersionId of the app
Example: tDtDnQdgm2LXpyiqYvZ6
onTrial
boolean
Filters out locations which are installed for specified app in trial mode
Example:
planId
string
Filters out location which are installed for specified app under the specified planId
Example:
locationId
string
locationId
Example: 1245
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
locations
object[]
count
number
Total location count under the company
Example:1231
installToFutureLocations
boolean
Boolean to control if user wants app to be automatically installed to future locations
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
curl -L 'https://services.leadconnectorhq.com/oauth/installedLocations' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
companyId — query
REQUIRED
appId — query
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