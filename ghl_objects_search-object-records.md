# Search Object Records

Source: https://marketplace.gohighlevel.com/docs/ghl/objects/search-object-records

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_objects_search-object-records_screenshot.png

---

ObjectsSearch Object Records
Search Object Records
POST
 https://services.leadconnectorhq.com/objects/:schemaKey/records/search
Supported Objects are custom objects and standard objects like "business". Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-277156/93bf0c2e23177b0/87cpx-379336
Requirements
Scope(s)
objects/record.readonly
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
schemaKey
string
custom object key
Example: 632c34b4c9b7da3358ac9891
APPLICATION/JSON
BODY
REQUIRED
locationId
string
REQUIRED
Location Id
Example:ve9EPM428h8vShlRW1KT
page
number
REQUIRED
Page
Example:1
pageLimit
number
REQUIRED
Page Limit
Example:10
query
string
REQUIRED
Pass this query parameter to search using your searchable properties. For example, if you have a custom object called “Pets” and have configured “name” as a searchable property, you can pass name:Buddy to search for pets with the name “Buddy.”
Example:Buddy
searchAfter
string[]
REQUIRED
Example:["sx6wyHhbFdRXh302Lunr","sx6wyHhbFdRXh302Lunr"]
Responses
200
400
401
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
records
object[]
total
number
REQUIRED
Total Number of records
Example:20



































































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
curl -L 'https://services.leadconnectorhq.com/objects/:schemaKey/records/search' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "page": 1,
  "pageLimit": 10,
  "query": "Buddy",
  "searchAfter": [
    "sx6wyHhbFdRXh302Lunr",
    "sx6wyHhbFdRXh302Lunr"
  ]
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
Show optional parameters
Body
 REQUIRED
{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "page": 1,
  "pageLimit": 10,
  "query": "Buddy",
  "searchAfter": [
    "sx6wyHhbFdRXh302Lunr",
    "sx6wyHhbFdRXh302Lunr"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!