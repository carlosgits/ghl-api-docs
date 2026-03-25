# Delete Sub-Account (Formerly Location)

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/delete-location

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_locations_delete-location_screenshot.png

---

Sub-Account (Formerly location)Sub-Account (Formerly Location)Delete Sub-Account (Formerly Location)
Delete Sub-Account (Formerly Location)
DELETE
 https://services.leadconnectorhq.com/locations/:locationId
Delete a Sub-Account (Formerly Location) from the Agency
Requirements
Scope(s)
locations.internal-access-only
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Agency Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
PATH PARAMETERS
locationId
string
REQUIRED
Location Id
Example: ve9EPM428h8vShlRW1KT
QUERY PARAMETERS
deleteTwilioAccount
boolean
REQUIRED
Boolean value to indicate whether to delete Twilio Account or not
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Success status of the API
Example:true
message
string
REQUIRED
Success message of the API
Example:Deleted location with id: ve9EPM428h8vShlRW1KT













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
curl -L -X DELETE 'https://services.leadconnectorhq.com/locations/:locationId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — path
REQUIRED
deleteTwilioAccount — query
REQUIRED
---
true
false
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!