# Delete Contact from Workflow

Source: https://marketplace.gohighlevel.com/docs/ghl/contacts/delete-contact-from-workflow

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_contacts_delete-contact-from-workflow_screenshot.png

---

ContactsWorkflowDelete Contact from Workflow
Delete Contact from Workflow
DELETE
 https://services.leadconnectorhq.com/contacts/:contactId/workflow/:workflowId
Delete Contact from Workflow
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
workflowId
string
REQUIRED
Workflow Id
Example: sx6wyHhbFdRXh302LLNR
APPLICATION/JSON
BODY
REQUIRED
eventStartTime
string
Example:2021-06-23T03:30:00+01:00
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
succeded
boolean
Example:true



















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
curl -L -X DELETE 'https://services.leadconnectorhq.com/contacts/:contactId/workflow/:workflowId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "eventStartTime": "2021-06-23T03:30:00+01:00"
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
workflowId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "eventStartTime": "2021-06-23T03:30:00+01:00"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!