# List active numbers

Source: https://marketplace.gohighlevel.com/docs/ghl/phone-system/active-numbers

Screenshot: images/ghl_phone-system_active-numbers_screenshot.png

---

Phone SystemPhone NumbersList active numbers
List active numbers
GET
 https://services.leadconnectorhq.com/phone-system/numbers/location/:locationId
Retrieve a paginated list of active phone numbers for a specific location. Supports filtering, pagination, and optional exclusion of number pool assignments.
Requirements
Scope(s)
phonenumbers.read
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
The unique identifier of the location
Example: ve9EPM428h8vShlRW1KT
QUERY PARAMETERS
pageSize
number
Possible values: >= 1 and <= 1000
How many resources to return in each list page. The default is 50, and the maximum is 1000.
Default value:1000
Example: 100
page
number
The page index for pagination. The default is 0.
Default value:0
Example: 0
searchFilter
string
Filter numbers by phone number pattern. Supports partial matching (e.g., "+91" to find all Indian numbers).
Example: +91
skipNumberPool
boolean
Whether to exclude numbers that are assigned to number pools. Default is true.
Default value:true
Example:
Responses
200
400
401
404
500
Successfully retrieved list of active numbers
APPLICATION/JSON
Schema
Example (auto)
successful-response
empty-response
SCHEMA
numbers
object[]
REQUIRED
isUnderGhl
boolean
REQUIRED
Whether this account is manged by LeadconnectorHQ
Example:true
pageSize
number
REQUIRED
Number of items requested per page
Possible values: >= 1 and <= 1000
Example:100
page
number
REQUIRED
Current page index (0-based)
Example:0
accountStatus
string
REQUIRED
Current status of the account
Possible values: [active, suspended, closed]
Example:active





























































































































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
curl -L 'https://services.leadconnectorhq.com/phone-system/numbers/location/:locationId' \
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