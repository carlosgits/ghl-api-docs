# Upload file attachments

Source: https://marketplace.gohighlevel.com/docs/ghl/conversations/upload-file-attachments

Screenshot: images/ghl_conversations_upload-file-attachments_screenshot.png

---

ConversationsMessagesUpload file attachments
Upload file attachments
POST
 https://services.leadconnectorhq.com/conversations/messages/upload
Post the necessary fields for the API to upload files. The files need to be a buffer with the key "fileAttachment".

Note: One of conversationId or contactId must be provided.

File Size Limits:
Maximum file size: 5 MB
Maximum files per upload: 5

Allowed file types:

Images: JPG, JPEG, PNG, GIF, SVG, HEIC, AI

Videos: MP4, MPEG, 3GP

Audio: MP3, WAV, WAVE, AIFF, AIF, AIFC, GSM, ULAW, OGG, AAC, M4A, AMR

Documents: PDF, DOC, DOCX, TXT, CSV, XLS, XLSX, PPT, PPTX, ODT

Archives: ZIP, RAR

Other: VCF, VCARD (contact files), ICS (calendar files)

The API will return an object with the URLs
Requirements
Scope(s)
conversations/message.write
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
Possible values: [2021-04-15]
API Version
MULTIPART/FORM-DATA
BODY
REQUIRED
conversationId
string
Conversation Id
Example:ve9EPM428h8vShlRW1KT
contactId
string
Contact Id
Example:ve9EPM428h8vShlRW1KT
workflowId
string
Workflow Id
Example:ve9EPM428h8vShlRW1KT
campaignId
string
Campaign Id
Example:ve9EPM428h8vShlRW1KT
locationId
string
REQUIRED
attachmentUrls
string[]
REQUIRED
Responses
200
400
401
404
413
415
Uploaded the file successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
uploadedFiles
object
REQUIRED
























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
curl -L -X POST 'https://services.leadconnectorhq.com/conversations/messages/upload' \
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
2021-04-15
Body
 REQUIRED
conversationId
contactId
workflowId
campaignId
locationId
REQUIRED
attachmentUrls
REQUIRED
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!