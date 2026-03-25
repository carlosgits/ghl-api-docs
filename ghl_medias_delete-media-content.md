# Delete File or Folder

Source: https://marketplace.gohighlevel.com/docs/ghl/medias/delete-media-content

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_medias_delete-media-content_screenshot.png

---

Media StorageMediasDelete File or Folder
Delete File or Folder
DELETE
 https://services.leadconnectorhq.com/medias/:id
Deletes specific file or folder from the media storage
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
PATH PARAMETERS
id
string
REQUIRED
QUERY PARAMETERS
altType
string
REQUIRED
Possible values: [location]
AltType
Example: location
altId
string
REQUIRED
location Id
Responses
200
Successful response
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
curl -L -X DELETE 'https://services.leadconnectorhq.com/medias/:id' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
id — path
REQUIRED
altType — query
REQUIRED
---
location
altId — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!