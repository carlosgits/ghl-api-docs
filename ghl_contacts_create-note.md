# Create Note

Source: https://marketplace.gohighlevel.com/docs/ghl/contacts/create-note

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_contacts_create-note_screenshot.png

---

ContactsNotesCreate Note
Create Note
POST
 https://services.leadconnectorhq.com/contacts/:contactId/notes
Create Note
Requirements
Scope(s)
contacts.write
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
contactId
string
REQUIRED
Contact Id
Example: sx6wyHhbFdRXh302LLNR
APPLICATION/JSON
BODY
REQUIRED
userId
string
Example:GCs5KuzPqTls7vWclkEV
body
string
REQUIRED
Example:lorem ipsum
Responses
201
400
401
422
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
note
object

























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
curl -L 'https://services.leadconnectorhq.com/contacts/:contactId/notes' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "userId": "GCs5KuzPqTls7vWclkEV",
  "body": "lorem ipsum"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
contactId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "userId": "GCs5KuzPqTls7vWclkEV",
  "body": "lorem ipsum"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!