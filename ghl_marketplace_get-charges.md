# Get all wallet charges

Source: https://marketplace.gohighlevel.com/docs/ghl/marketplace/get-charges

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_marketplace_get-charges_screenshot.png

---

Developer marketplaceWallet ChargesGet all wallet charges
Get all wallet charges
GET
 https://services.leadconnectorhq.com/marketplace/billing/charges
Get all wallet charges
Requirements
Scope(s)
charges.readonly
Auth Method(s)
OAuth Access Token
Token Type(s)
Sub-Account Token
Request
QUERY PARAMETERS
meterId
string
Billing Meter ID (you can find this on your app's pricing page on the developer portal)
eventId
string
Event ID / Transaction ID
userId
string
Filter results by User ID that your server passed via API when the charge was created
startDate
string
Filter results AFTER a specific date. Use this in combination with endDate to filter results in a specific time window.
Example: 2025-03-26
endDate
string
Filter results BEFORE a specific date. Use this in combination with startDate to filter results in a specific time window.
Example: 2025-03-26
skip
number
Number of records to skip
limit
number
Maximum number of records to return
Responses
200
422
Returns list of wallet charges
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
charges
object[]
count
number
DEPRECATED
Total number of charges
Example:100
pagination
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
curl -L 'https://services.leadconnectorhq.com/marketplace/billing/charges' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!