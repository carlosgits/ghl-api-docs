# Get Last Snapshot Push

Source: https://marketplace.gohighlevel.com/docs/ghl/snapshots/get-latest-snapshot-push

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_snapshots_get-latest-snapshot-push_screenshot.png

---

SnapshotsSnapshotsGet Last Snapshot Push
Get Last Snapshot Push
GET
 https://services.leadconnectorhq.com/snapshots/snapshot-status/:snapshotId/location/:locationId
Get Latest Snapshot Push Status for a location id
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
PATH PARAMETERS
snapshotId
string
REQUIRED
Example: 39It2BFz7EkNaNBALPif
locationId
string
REQUIRED
Example: IIRGHCgxSINdPT79M75P
QUERY PARAMETERS
companyId
string
REQUIRED
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
data
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
curl -L 'https://services.leadconnectorhq.com/snapshots/snapshot-status/:snapshotId/location/:locationId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
snapshotId — path
REQUIRED
locationId — path
REQUIRED
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