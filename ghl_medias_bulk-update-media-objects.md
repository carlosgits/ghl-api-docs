# Bulk Update Files/ Folders

Source: https://marketplace.gohighlevel.com/docs/ghl/medias/bulk-update-media-objects

Screenshot: images/ghl_medias_bulk-update-media-objects_screenshot.png

---

Media StorageMediasBulk Update Files/ Folders
Bulk Update Files/ Folders
PUT
 https://services.leadconnectorhq.com/medias/update-files
Updates metadata or status of multiple files and folders
Requirements
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
APPLICATION/JSON
BODY
REQUIRED
altId
string
REQUIRED
Location identifier
Example:sx6wyHhbFdRXh302LLNR
altType
string
REQUIRED
Type of entity that owns the files
Possible values: [location]
Example:location
filesToBeUpdated
object[]
REQUIRED
Responses
200
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA






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
curl -L -X PUT 'https://services.leadconnectorhq.com/medias/update-files' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "sx6wyHhbFdRXh302LLNR",
  "altType": "location",
  "filesToBeUpdated": [
    {
      "id": "686f9817f0d3165be9fbcef6",
      "name": "Updated File Name.pdf"
    }
  ]
}'
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
{
  "altId": "sx6wyHhbFdRXh302LLNR",
  "altType": "location",
  "filesToBeUpdated": [
    {
      "id": "686f9817f0d3165be9fbcef6",
      "name": "Updated File Name.pdf"
    }
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!