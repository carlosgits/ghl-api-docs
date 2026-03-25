# Create Business

Source: https://marketplace.gohighlevel.com/docs/ghl/businesses/create-business

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_businesses_create-business_screenshot.png

---

BusinessBusinessesCreate Business
Create Business
POST
 https://services.leadconnectorhq.com/businesses/
Create Business
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
APPLICATION/JSON
BODY
REQUIRED
name
string
REQUIRED
Example:Microsoft
locationId
string
REQUIRED
Example:5DP4iH6HLkQsiKESj6rh
phone
string
Example:+18832327657
email
string
Example:john@deo.com
website
string
Example:www.xyz.com
address
string
Example:street adress
city
string
Example:new york
postalCode
string
Example:12312312
state
string
Example:new york
country
string
Example:us
description
string
Example:business description
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
curl -L 'https://services.leadconnectorhq.com/businesses/' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "name": "Microsoft",
  "locationId": "5DP4iH6HLkQsiKESj6rh",
  "phone": "+18832327657",
  "email": "john@deo.com",
  "website": "www.xyz.com",
  "address": "street adress",
  "city": "new york",
  "postalCode": "12312312",
  "state": "new york",
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
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "name": "Microsoft",
  "locationId": "5DP4iH6HLkQsiKESj6rh",
  "phone": "+18832327657",
  "email": "john@deo.com",
  "website": "www.xyz.com",
  "address": "street adress",
  "city": "new york",
  "postalCode": "12312312",
  "state": "new york",
  "country": "us",
  "description": "business description"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!