# Upload File into Media Storage

Source: https://marketplace.gohighlevel.com/docs/ghl/medias/upload-media-content

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_medias_upload-media-content_screenshot.png

---

Media StorageMediasUpload File into Media Storage
Upload File into Media Storage
POST
 https://services.leadconnectorhq.com/medias/upload-file
If hosted is set to true then fileUrl is required. Else file is required. If adding a file, maximum allowed is 25 MB. For video files, the maximum allowed size is 500 MB.
Requirements
Scope(s)
medias.write
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
MULTIPART/FORM-DATA
BODY
REQUIRED
file
binary
hosted
boolean
fileUrl
string
name
string
parentId
string
Responses
200
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
fileId
string
REQUIRED
ID of the uploaded file
Example:file.pdf
url
string
REQUIRED
Google Cloud Storage URL of the uploaded file
Example:https://storage.googleapis.com/bucket-name/path/to/file.pdf




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
curl -L -X POST 'https://services.leadconnectorhq.com/medias/upload-file' \
-H 'Content-Type: multipart/form-data' \
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
file
file
hosted
fileUrl
name
parentId
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!