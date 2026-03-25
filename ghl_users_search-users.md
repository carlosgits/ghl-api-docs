# Search Users

Source: https://marketplace.gohighlevel.com/docs/ghl/users/search-users

Screenshot: images/ghl_users_search-users_screenshot.png

---

UsersSearchSearch Users
Search Users
GET
 https://services.leadconnectorhq.com/users/search
Search Users
Requirements
Scope(s)
users.readonly
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Agency Token
Sub-Account Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
QUERY PARAMETERS
companyId
string
REQUIRED
Company ID in which the search needs to be performed
Example: 5DP41231LkQsiKESj6rh
query
string
The search term for the user is matched based on the user full name, email or phone
Example: John
skip
string
No of results to be skipped before returning the result
Default value:0
Example: 1
limit
string
No of results to be limited before returning the result
Default value:25
Example: 10
locationId
string
Location ID in which the search needs to be performed
Example: 5DP41231LkQsiKESj6rh
type
string
Type of the users to be filtered in the search
Example: agency
role
string
Role of the users to be filtered in the search
Example: admin
ids
string
List of User IDs to be filtered in the search
Example: 5DP4iH6HLkQsiKESj6rh,5DP4iH6HLkQsiKESj34h
sort
string
The field on which sort is applied in which the results need to be sorted. Default is based on the first and last name
Example: dateAdded
sortDirection
string
The direction in which the results need to be sorted
Example: asc
enabled2waySync
boolean
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
users
object[]
count
number
Example:1231




















































































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
curl -L 'https://services.leadconnectorhq.com/users/search' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Security Scheme
Agency-Access
Location-Access
Bearer Token
Parameters
companyId — query
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