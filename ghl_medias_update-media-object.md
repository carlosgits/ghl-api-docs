# Update File/ Folder

Source: https://marketplace.gohighlevel.com/docs/ghl/medias/update-media-object

Screenshot: images/ghl_medias_update-media-object_screenshot.png

---

Media StorageMediasUpdate File/ Folder
Update File/ Folder
POST
 https://services.leadconnectorhq.com/medias/:id
Updates a single file or folder by ID
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
PATH PARAMETERS
id
string
REQUIRED
Unique identifier of the file or folder to update
Example: 686f9817f0d3165be9fbcef6
APPLICATION/JSON
BODY
REQUIRED
name
string
REQUIRED
New name for the file or folder
Example:Updated File Name.pdf
altType
string
REQUIRED
Type of entity that owns the file or folder
Possible values: [location]
Example:location
altId
string
REQUIRED
Location identifier that owns the file or folder
Example:sx6wyHhbFdRXh302LLNR
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
curl -L 'https://services.leadconnectorhq.com/medias/:id' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "name": "Updated File Name.pdf",
  "altType": "location",
  "altId": "sx6wyHhbFdRXh302LLNR"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
id — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "name": "Updated File Name.pdf",
  "altType": "location",
  "altId": "sx6wyHhbFdRXh302LLNR"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!