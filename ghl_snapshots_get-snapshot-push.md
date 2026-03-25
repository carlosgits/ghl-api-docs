# Get Snapshot Push between Dates

Source: https://marketplace.gohighlevel.com/docs/ghl/snapshots/get-snapshot-push

Screenshot: images/ghl_snapshots_get-snapshot-push_screenshot.png

---

SnapshotsSnapshotsGet Snapshot Push between Dates
Get Snapshot Push between Dates
GET
 https://services.leadconnectorhq.com/snapshots/snapshot-status/:snapshotId
Get list of sub-accounts snapshot pushed in time period
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
QUERY PARAMETERS
companyId
string
REQUIRED
Example: 5D112kQsiKESj6rash
from
string
REQUIRED
Only accepts ISO 8601 format
Example: 2022-10-10T12:00:00Z or 2022-10-10
to
string
REQUIRED
Only accepts ISO 8601 format
Example: 2023-12-18T11:59:59Z or 2023-12-18
lastDoc
string
REQUIRED
Id for last document till what you want to skip
Example: VUJO4Sw2TrDNZ5lx4wZg
limit
string
Limit of documents to return. Default is 20
Example: 10
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
curl -L 'https://services.leadconnectorhq.com/snapshots/snapshot-status/:snapshotId' \
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
companyId — query
REQUIRED
from — query
REQUIRED
to — query
REQUIRED
lastDoc — query
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