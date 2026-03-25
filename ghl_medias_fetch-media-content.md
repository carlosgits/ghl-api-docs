# Get List of Files/ Folders

Source: https://marketplace.gohighlevel.com/docs/ghl/medias/fetch-media-content

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_medias_fetch-media-content_screenshot.png

---

Media StorageMediasGet List of Files/ Folders
Get List of Files/ Folders
GET
 https://services.leadconnectorhq.com/medias/files
Fetches list of files and folders from the media storage
Requirements
Scope(s)
medias.readonly
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
QUERY PARAMETERS
offset
string
Number of files to skip in listing
Example: 5
limit
string
Number of files to show in the listing
Example: 10
sortBy
string
REQUIRED
Field to sorting the file listing by
Example: createdAt
sortOrder
string
REQUIRED
Direction in which file needs to be sorted
Example: asc
type
string
REQUIRED
Type
Example: file
query
string
Query text
Example: Test file
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
parentId
string
parent id or folder id
fetchAll
string
Fetch all files or folders
Example: false
Responses
200
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
files
string[]
REQUIRED
Array of File Objects
Example:{"altId":"locationId","altType":"location","name":"file name","parentId":"parent folder id","url":"file url","path":"file path"}










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
curl -L 'https://services.leadconnectorhq.com/medias/files' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
sortBy — query
REQUIRED
sortOrder — query
REQUIRED
type — query
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
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!