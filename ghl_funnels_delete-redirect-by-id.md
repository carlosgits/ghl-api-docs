# Delete Redirect By Id

Source: https://marketplace.gohighlevel.com/docs/ghl/funnels/delete-redirect-by-id

Screenshot: images/ghl_funnels_delete-redirect-by-id_screenshot.png

---

FunnelsRedirectDelete Redirect By Id
Delete Redirect By Id
DELETE
 https://services.leadconnectorhq.com/funnels/lookup/redirect/:id
The "Delete Redirect By Id" API Allows deletion of a URL redirect from the system using its unique identifier. Use this endpoint to delete a URL redirect with the specified ID using details provided in the request payload.
Requirements
Scope(s)
funnels/redirect.write
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
id
string
REQUIRED
QUERY PARAMETERS
locationId
string
REQUIRED
Example: 6p2RxpgtMKQwO3E6IUaT
Responses
200
422
Successful response - URL redirect deleted successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
data
object
REQUIRED
Status of the delete operation
Example:{"status":"ok"}





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
curl -L -X DELETE 'https://services.leadconnectorhq.com/funnels/lookup/redirect/:id' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
id — path
REQUIRED
locationId — query
REQUIRED
Version — header
REQUIRED
---
2021-07-28
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!