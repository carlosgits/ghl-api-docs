# Update a template with settings

Source: https://marketplace.gohighlevel.com/docs/ghl/emails/patch-template

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_emails_patch-template_screenshot.png

---

EmailTemplatesUpdate a template with settings
Update a template with settings
PATCH
 https://services.leadconnectorhq.com/emails/builder/:templateId
Update a template with settings
Requirements
Scope(s)
emails/builder.write
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
Example: 2021-07-28
PATH PARAMETERS
templateId
string
REQUIRED
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
Location ID where the template belongs
Example:ve9EPM428h8vShlRW1KT
updatedBy
string
User ID who is updating the template
Example:zYy3YOUuHxgomU1uYJty
editorContent
object
editorType
string
Type of editor content: "html" for HTML content, "text" for plain text content, "builder" for drag-and-drop builder content. Must be provided together with editorContent.
Possible values: [html, builder, text]
Example:html
previewText
string
Preview text shown in email clients before opening
Example:Email preview text
subjectLine
string
Email subject line
Example:Welcome to our newsletter
fromName
string
Sender name displayed in email
Example:John Doe
fromEmail
string
Sender email address
Example:john@example.com
name
string
Template name
Example:Newsletter Template
archived
boolean
Whether the template is archived
Example:false
Responses
200
400
401
404
422
Success
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
ok
boolean
REQUIRED
Indicates if the update was successful
Example:true
id
string
REQUIRED
Unique template identifier
Example:507f1f77bcf86cd799439011
name
string
REQUIRED
Template name
Example:My Email Template
archived
boolean
REQUIRED
Whether the template is archived
Example:false
builderVersion
string
REQUIRED
Builder version used for the template
Example:2
fromName
string
REQUIRED
Sender name displayed in email
Example:John Doe
fromEmail
string
REQUIRED
Sender email address
Example:john@example.com
subjectLine
string
REQUIRED
Email subject line
Example:Welcome to our newsletter
previewText
string
REQUIRED
Preview text shown in email clients
Example:Check out our latest updates
previewUrl
string
REQUIRED
URL to preview the rendered template
Example:https://example.com/preview/template123
type
string
REQUIRED
Type of template editor used
Possible values: [html, builder]
Example:builder
lastUpdated
string
REQUIRED
Timestamp of last update
Example:2024-01-15T10:30:00Z
createdAt
string
REQUIRED
Timestamp when template was created
Example:2024-01-01T08:00:00Z
isPlainText
boolean
REQUIRED
Whether the template contains plain text content (true) or HTML content (false)
Example:false
































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
curl -L -X PATCH 'https://services.leadconnectorhq.com/emails/builder/:templateId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "updatedBy": "zYy3YOUuHxgomU1uYJty",
  "editorContent": "<html><body>Hello World</body></html>",
  "editorType": "html",
  "previewText": "Email preview text",
  "subjectLine": "Welcome to our newsletter",
  "fromName": "John Doe",
  "fromEmail": "john@example.com",
  "name": "Newsletter Template",
  "archived": false
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
templateId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "updatedBy": "zYy3YOUuHxgomU1uYJty",
  "editorContent": "<html><body>Hello World</body></html>",
  "editorType": "html",
  "previewText": "Email preview text",
  "subjectLine": "Welcome to our newsletter",
  "fromName": "John Doe",
  "fromEmail": "john@example.com",
  "name": "Newsletter Template",
  "archived": false
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!