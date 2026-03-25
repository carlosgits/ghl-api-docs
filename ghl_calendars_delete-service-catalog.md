# Delete Service

Source: https://marketplace.gohighlevel.com/docs/ghl/calendars/delete-service-catalog

Screenshot: images/ghl_calendars_delete-service-catalog_screenshot.png

---

CalendarsServicesDelete Service
Delete Service
DELETE
 https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId
Delete service by ID.
Requirements
Scope(s)
calendars.write
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
Possible values: [2021-04-15]
API Version
PATH PARAMETERS
serviceId
string
REQUIRED
Service ID
Example: 65e5f6dfacf123513228d384
Responses
200
400
401
Service deleted successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Success
Example:true
message
string
Success message
Example:Service deleted successfully













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
curl -L -X DELETE 'https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
serviceId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!