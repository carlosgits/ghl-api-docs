# Upload files to custom fields

Source: https://marketplace.gohighlevel.com/docs/ghl/forms/upload-to-custom-fields

Screenshot: images/ghl_forms_upload-to-custom-fields_screenshot.png

---

FormsFormsUpload files to custom fields
Upload files to custom fields
POST
 https://services.leadconnectorhq.com/forms/upload-custom-files
Post the necessary fields for the API to upload files. The files need to be a buffer with the key "< custom_field_id >_< file_id >".
Here custom field id is the ID of your custom field and file id is a randomly generated id (or uuid)
There is support for multiple file uploads as well. Have multiple fields in the format mentioned.
File size is limited to 50 MB.

The allowed file types are:
PDF
DOCX
DOC
JPG
JPEG
PNG
GIF
CSV
XLSX
XLS
MP4
MPEG
ZIP
RAR
TXT
SVG


The API will return the updated contact object.
Requirements
Scope(s)
forms.write
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
contactId
string
REQUIRED
Contact ID to upload the file to.
Example: dtEv6KtI27yF92YPm3Zz
locationId
string
REQUIRED
Location ID of the contact.
Example: quXmPY59n1zgGBabY1bZ
MULTIPART/FORM-DATA
BODY
REQUIRED
Responses
200
400
401
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
curl -L -X POST 'https://services.leadconnectorhq.com/forms/upload-custom-files' \
-H 'Content-Type: multipart/form-data' \
-H 'Authorization: Bearer <TOKEN>' \
-d ''
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Security Scheme
bearer
Location-Access
Bearer Token
Parameters
contactId — query
REQUIRED
locationId — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!