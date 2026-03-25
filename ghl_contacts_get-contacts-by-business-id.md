# Get Contacts By BusinessId

Source: https://marketplace.gohighlevel.com/docs/ghl/contacts/get-contacts-by-business-id

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_contacts_get-contacts-by-business-id_screenshot.png

---

ContactsContactsGet Contacts By BusinessId
Get Contacts By BusinessId
GET
 https://services.leadconnectorhq.com/contacts/business/:businessId
Get Contacts By BusinessId
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
PATH PARAMETERS
businessId
string
REQUIRED
QUERY PARAMETERS
limit
string
Default value:25
Example: 10
locationId
string
REQUIRED
Example: 5DP4iH6HLkQsiKESj6rh
skip
string
Default value:0
Example: 10
query
string
Example: contact name
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
contacts
object[]
count
number
Example:10
































































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
curl -L 'https://services.leadconnectorhq.com/contacts/business/:businessId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
businessId — path
REQUIRED
locationId — query
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