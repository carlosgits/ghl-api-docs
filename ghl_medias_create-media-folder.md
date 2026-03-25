# Create Folder

Source: https://marketplace.gohighlevel.com/docs/ghl/medias/create-media-folder

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_medias_create-media-folder_screenshot.png

---

Media StorageMediasCreate Folder
Create Folder
POST
 https://services.leadconnectorhq.com/medias/folder
Creates a new folder in the media storage
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
Location Id
Example:sx6wyHhbFdRXh302LLNR
altType
string
REQUIRED
Type of entity (location only)
Possible values: [location]
Example:location
name
string
REQUIRED
Name of the folder to be created
Example:New Folder
parentId
string
ID of the parent folder (optional)
Example:64af50c42d567a3b4f5989e0
Responses
200
Returns the newly created folder object
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
altId
string
REQUIRED
Location identifier that owns this folder
Example:sx6wyHhbFdRXh302LLNR
altType
string
REQUIRED
Type of entity that owns the folder
Possible values: [location]
Example:location
name
string
REQUIRED
Name of the folder
Example:New Folder
parentId
string
ID of the parent folder (null for root folders)
Example:64af50c42d567a3b4f5989e0
type
string
REQUIRED
Type of the object (always 'folder' for folders)
Example:folder
deleted
boolean
Whether the folder has been deleted
Example:false
pendingUpload
boolean
Whether there are pending uploads to this folder
Example:false
category
string
Primary category of content stored in the folder
Example:image
subCategory
string
Sub-category of content stored in the folder
Example:logo
isPrivate
boolean
Whether the folder is private and not publicly accessible
Example:false
relocatedFolder
boolean
Whether the folder has been moved from its original location
Example:false
migrationCompleted
boolean
Whether the data migration process has been completed for this folder
Example:true
appFolder
boolean
Whether this is a system-generated application folder
Example:false
isEssential
boolean
Whether the folder is essential and should not be deleted
Example:false
status
string
Current status of the folder
lastUpdatedBy
string
ID of the user who last updated the folder
Example:user-uuid-123


















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
curl -L 'https://services.leadconnectorhq.com/medias/folder' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "sx6wyHhbFdRXh302LLNR",
  "altType": "location",
  "name": "New Folder",
  "parentId": "64af50c42d567a3b4f5989e0"
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
  "name": "New Folder",
  "parentId": "64af50c42d567a3b4f5989e0"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!