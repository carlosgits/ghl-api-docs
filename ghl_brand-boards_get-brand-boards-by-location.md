# Get Brand Boards

Source: https://marketplace.gohighlevel.com/docs/ghl/brand-boards/get-brand-boards-by-location

Screenshot: images/ghl_brand-boards_get-brand-boards-by-location_screenshot.png

---

Brand BoardsBrand BoardsGet Brand Boards
Get Brand Boards
GET
 https://services.leadconnectorhq.com/brand-boards/:locationId
Retrieves all Brand Boards for a specific location
Requirements
Scope(s)
brand-boards/design-kit.readonly
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
locationId
string
REQUIRED
QUERY PARAMETERS
limit
number
Maximum number of brand boards to return
Default value:10
Example: 10
offset
number
Number of brand boards to skip for pagination
Default value:0
Example: 0
search
string
Search term to filter brand boards by name
Default value:
Example: brandboard
deleted
boolean
Include deleted brand boards in results
Default value:false
Responses
200
400
401
403
422
Success
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
brandBoards
object[]
REQUIRED
totalCount
number
REQUIRED
Total number of brand boards matching the query
Example:42





































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
curl -L 'https://services.leadconnectorhq.com/brand-boards/:locationId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — path
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