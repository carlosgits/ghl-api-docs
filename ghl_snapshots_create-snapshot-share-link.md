# Create Snapshot Share Link

Source: https://marketplace.gohighlevel.com/docs/ghl/snapshots/create-snapshot-share-link

Screenshot: images/ghl_snapshots_create-snapshot-share-link_screenshot.png

---

SnapshotsSnapshotsCreate Snapshot Share Link
Create Snapshot Share Link
POST
 https://services.leadconnectorhq.com/snapshots/share/link
Create a share link for snapshot
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
APPLICATION/JSON
BODY
REQUIRED
snapshot_id
string
REQUIRED
id for snapshot to be shared
Example:1eM2UgkfaECOYyUdCo9Pa
share_type
string
REQUIRED
Type of share link to generate
Possible values: [link, permanent_link, agency_link, location_link]
Example:permanent_link
relationship_number
string
Comma separated Relationship number of Agencies to create agency restricted share link
Example:0-128-926,1-208-926,2-008-926
share_location_id
string
Comma separated Sub-Account ids to create sub-account restricted share link
Example:l1C08ntBrFjLS0elLIYU, U1C08ntBrFjLS0elKIYP
Responses
201
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
id
string
id for shared snapshot
Example:1eM2UgkfaECOYyUdCo9Pa
shareLink
string
Share Link for snapshot
Example:https://affiliates.gohighlevel.com/?share=1eM2UgkfaECOYyUdCo9Pa













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
curl -L 'https://services.leadconnectorhq.com/snapshots/share/link' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "snapshot_id": "1eM2UgkfaECOYyUdCo9Pa",
  "share_type": "permanent_link",
  "relationship_number": "0-128-926,1-208-926,2-008-926",
  "share_location_id": "l1C08ntBrFjLS0elLIYU, U1C08ntBrFjLS0elKIYP"
}'
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
Body
 REQUIRED
{
  "snapshot_id": "1eM2UgkfaECOYyUdCo9Pa",
  "share_type": "permanent_link",
  "relationship_number": "0-128-926,1-208-926,2-008-926",
  "share_location_id": "l1C08ntBrFjLS0elLIYU, U1C08ntBrFjLS0elKIYP"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!