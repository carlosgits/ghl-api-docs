# Update Business

Source: https://marketplace.gohighlevel.com/docs/ghl/businesses/update-business

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_businesses_update-business_screenshot.png

---

BusinessBusinessesUpdate Business
Update Business
PUT
 https://services.leadconnectorhq.com/businesses/:businessId
Update Business
Requirements
Scope(s)
businesses.write
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
Example: 5DP4iH6HLkQsiKESj6rh
APPLICATION/JSON
BODY
REQUIRED
name
string
Example:Microsoft
phone
string
Example:+18832327657
email
string
Example:john@deo.com
postalCode
string
Example:12312312
website
string
Example:www.xyz.com
address
string
Example:street adress
state
string
Example:new york
city
string
Example:new york
country
string
Example:us
description
string
Example:business description
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
success
boolean
REQUIRED
Success Value
Example:true
buiseness
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
curl -L -X PUT 'https://services.leadconnectorhq.com/businesses/:businessId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "name": "Microsoft",
  "phone": "+18832327657",
  "email": "john@deo.com",
  "postalCode": "12312312",
  "website": "www.xyz.com",
  "address": "street adress",
  "state": "new york",
  "city": "new york",
  "country": "us",
  "description": "business description"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
businessId — path
REQUIRED
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "name": "Microsoft",
  "phone": "+18832327657",
  "email": "john@deo.com",
  "postalCode": "12312312",
  "website": "www.xyz.com",
  "address": "street adress",
  "state": "new york",
  "city": "new york",
  "country": "us",
  "description": "business description"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!