# Create Redirect

Source: https://marketplace.gohighlevel.com/docs/ghl/funnels/create-redirect

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_funnels_create-redirect_screenshot.png

---

FunnelsRedirectCreate Redirect
Create Redirect
POST
 https://services.leadconnectorhq.com/funnels/lookup/redirect
The "Create Redirect" API Allows adding a new url redirect to the system. Use this endpoint to create a url redirect with the specified details. Ensure that the required information is provided in the request payload.
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
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
Example:6p2RxpgtMKQwO3E6IUaT
domain
string
REQUIRED
Example:example.com
path
string
REQUIRED
Example:/Hello
target
string
REQUIRED
Example:https://www.google.com
action
string
REQUIRED
Possible values: [funnel, website, url, all]
Example:URL
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
curl -L 'https://services.leadconnectorhq.com/funnels/lookup/redirect' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "6p2RxpgtMKQwO3E6IUaT",
  "domain": "example.com",
  "path": "/Hello",
  "target": "https://www.google.com",
  "action": "URL"
}'
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
{
  "locationId": "6p2RxpgtMKQwO3E6IUaT",
  "domain": "example.com",
  "path": "/Hello",
  "target": "https://www.google.com",
  "action": "URL"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!