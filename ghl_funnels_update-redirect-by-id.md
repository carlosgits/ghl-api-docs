# Update Redirect By Id

Source: https://marketplace.gohighlevel.com/docs/ghl/funnels/update-redirect-by-id

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_funnels_update-redirect-by-id_screenshot.png

---

FunnelsRedirectUpdate Redirect By Id
Update Redirect By Id
PATCH
 https://services.leadconnectorhq.com/funnels/lookup/redirect/:id
The "Update Redirect By Id" API Allows updating an existing URL redirect in the system. Use this endpoint to modify a URL redirect with the specified ID using details provided in the request payload.
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
APPLICATION/JSON
BODY
REQUIRED
target
string
REQUIRED
Example:https://www.google.com
action
string
REQUIRED
Possible values: [funnel, website, url, all]
Example:URL
locationId
string
REQUIRED
Example:6p2RxpgtMKQwO3E6IUaT
Responses
200
422
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
data
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
curl -L -X PATCH 'https://services.leadconnectorhq.com/funnels/lookup/redirect/:id' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "target": "https://www.google.com",
  "action": "URL",
  "locationId": "6p2RxpgtMKQwO3E6IUaT"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
id — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "target": "https://www.google.com",
  "action": "URL",
  "locationId": "6p2RxpgtMKQwO3E6IUaT"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!