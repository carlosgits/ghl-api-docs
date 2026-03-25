# Uploads File to customFields

Source: https://marketplace.gohighlevel.com/docs/ghl/locations/upload-file-custom-fields

Screenshot: images/ghl_locations_upload-file-custom-fields_screenshot.png

---

Sub-Account (Formerly location)Custom FieldUploads File to customFields
Uploads File to customFields
POST
 https://services.leadconnectorhq.com/locations/:locationId/customFields/upload
Uploads File to customFields
Requirements
Scope(s)
locations/customFields.write
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
locationId
string
REQUIRED
MULTIPART/FORM-DATA
BODY
REQUIRED
id
string
Id(Contact Id/Opportunity Id/Custom Field Id)
Example:aWdODOBVOlH1RUFKWQke
maxFiles
string
Max number of files
Example:15
Responses
200
400
401
422
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
uploadedFiles
object
Uploaded files
Example:{"FileName.csv":"https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"}
meta
string[]
Meta data of uploaded files
Example:[{"fieldname":"FileName.csv","originalname":"FileName.csv","encoding":"7bit","mimetype":"text/csv","size":2061,"url":"https://highlevel-private-staging.storage.googleapis.com/location/Ar4JQgIyuzRsVuwD9RSK/custom-Field/UpZLmohmKEQYn0ymqplY/56e0d7fc-085c-4a07-9e1d-6d8fdac7e710.csv"}]































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
curl -L -X POST 'https://services.leadconnectorhq.com/locations/:locationId/customFields/upload' \
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
locationId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
id
maxFiles
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!