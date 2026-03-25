# Bulk Delete / Trash Files or Folders

Source: https://marketplace.gohighlevel.com/docs/ghl/medias/bulk-delete-media-objects

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_medias_bulk-delete-media-objects_screenshot.png

---

Media StorageMediasBulk Delete / Trash Files or Folders
Bulk Delete / Trash Files or Folders
PUT
 https://services.leadconnectorhq.com/medias/delete-files
Soft-deletes or trashes multiple files and folders in a single request
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
filesToBeDeleted
object[]
REQUIRED
altType
string
REQUIRED
Type of entity that owns the files
Possible values: [location]
Example:location
altId
string
REQUIRED
Location identifier
Example:sx6wyHhbFdRXh302LLNR
status
string
REQUIRED
Status to set for the files (deleted or trashed)
Possible values: [deleted, trashed]
Example:deleted
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
curl -L -X PUT 'https://services.leadconnectorhq.com/medias/delete-files' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "filesToBeDeleted": [
    {
      "_id": "686f630df0d3166d68fbcec2"
    }
  ],
  "altType": "location",
  "altId": "sx6wyHhbFdRXh302LLNR",
  "status": "deleted"
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
  "filesToBeDeleted": [
    {
      "_id": "686f630df0d3166d68fbcec2"
    }
  ],
  "altType": "location",
  "altId": "sx6wyHhbFdRXh302LLNR",
  "status": "deleted"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!