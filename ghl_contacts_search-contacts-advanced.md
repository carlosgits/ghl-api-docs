# Search Contacts

Source: https://marketplace.gohighlevel.com/docs/ghl/contacts/search-contacts-advanced

Screenshot: images/ghl_contacts_search-contacts-advanced_screenshot.png

---

ContactsSearchSearch Contacts
Search Contacts
POST
 https://services.leadconnectorhq.com/contacts/search
Search contacts based on combinations of advanced filters. Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-158396/6e629989abe7fad
Requirements
Scope(s)
contacts.readonly
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
object
Responses
200
400
401
Success
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
curl -L 'https://services.leadconnectorhq.com/contacts/search' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{}'
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
{}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!