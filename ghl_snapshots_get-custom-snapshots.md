# Get Snapshots

Source: https://marketplace.gohighlevel.com/docs/ghl/snapshots/get-custom-snapshots

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_snapshots_get-custom-snapshots_screenshot.png

---

SnapshotsSnapshotsGet Snapshots
Get Snapshots
GET
 https://services.leadconnectorhq.com/snapshots/
Get a list of all own and imported Snapshots
Requirements
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
QUERY PARAMETERS
companyId
string
REQUIRED
Company Id
Example: 5D112kQsiKESj6rash
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
snapshots
object[]


















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
curl -L 'https://services.leadconnectorhq.com/snapshots/' \
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
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!