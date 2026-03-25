# Get Contacts

Source: https://marketplace.gohighlevel.com/docs/ghl/contacts/get-contacts

Screenshot: images/ghl_contacts_get-contacts_screenshot.png

---

ContactsContactsGet Contacts
Get Contacts
GET
 https://services.leadconnectorhq.com/contacts/
DEPRECATED
This endpoint has been deprecated and may be replaced or removed in future versions of the API.
Get Contacts
Note: This API endpoint is deprecated. Please use the Search Contacts endpoint instead.
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
Example: ve9EPM428h8vShlRW1KT
startAfterId
string
Start After Id
Example: UIaE1WjAwWKdlyD7osQI
startAfter
number
Start Afte
Example: 1603870249758
query
string
Contact Query
Example: John
limit
number
Limit Per Page records count. will allow maximum up to 100 and default will be 20
Default value:20
Example: 20
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
curl -L 'https://services.leadconnectorhq.com/contacts/' \
-H 'Accept: application/json' \
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