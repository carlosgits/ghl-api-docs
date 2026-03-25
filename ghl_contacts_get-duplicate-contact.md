# Get Duplicate Contact

Source: https://marketplace.gohighlevel.com/docs/ghl/contacts/get-duplicate-contact

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_contacts_get-duplicate-contact_screenshot.png

---

ContactsSearchGet Duplicate Contact
Get Duplicate Contact
GET
 https://services.leadconnectorhq.com/contacts/search/duplicate
Get Duplicate Contact.

If Allow Duplicate Contact is disabled under Settings, the global unique identifier will be used for searching the contact. If the setting is enabled, first priority for search is email and the second priority will be phone.
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
QUERY PARAMETERS
locationId
string
REQUIRED
Location Id
Example: sadadya1u12basyhasd
number
string
Phone Number - Pass in URL Encoded form. i.e +1423164516 will become %2B1423164516
Example: +1423164516
email
string
Email - Pass in URL Encoded form. i.e test+abc@gmail.com will become test%2Babc%40gmail.com
Example: abc@abc.com
Responses
200
400
401









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
curl -L 'https://services.leadconnectorhq.com/contacts/search/duplicate' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
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