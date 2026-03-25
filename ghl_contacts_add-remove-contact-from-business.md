# Add/Remove Contacts From Business

Source: https://marketplace.gohighlevel.com/docs/ghl/contacts/add-remove-contact-from-business

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_contacts_add-remove-contact-from-business_screenshot.png

---

ContactsBulkAdd/Remove Contacts From Business
Add/Remove Contacts From Business
POST
 https://services.leadconnectorhq.com/contacts/bulk/business
Add/Remove Contacts From Business . Passing a null businessId will remove the businessId from the contacts
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
Example:PX8m5VwxEbcpFlzYEPVG
ids
string[]
REQUIRED
Possible values: <= 50 characters
Example:["IDqvFHGColiyK6jiatuz","pOC0uJ97VYOKH2m3fkMD"]
businessId
string
NULLABLE
REQUIRED
Example:63b7ec34ea409a9a8bd2a4ff
Responses
200
422
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Example:true
ids
string[]
REQUIRED
Example:["pOC0uJ97VYOKH2m3fkMD"]













Share your feedback
★
★
★
★
★
CURL
NODEJS
PYTHON
PHP
JAVA
GO
RUBY
POWERSHELL
CURL
curl -L 'https://services.leadconnectorhq.com/contacts/bulk/business' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-d '{
  "locationId": "PX8m5VwxEbcpFlzYEPVG",
  "ids": [
    "IDqvFHGColiyK6jiatuz",
    "pOC0uJ97VYOKH2m3fkMD"
  ],
  "businessId": "63b7ec34ea409a9a8bd2a4ff"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Parameters
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "locationId": "PX8m5VwxEbcpFlzYEPVG",
  "ids": [
    "IDqvFHGColiyK6jiatuz",
    "pOC0uJ97VYOKH2m3fkMD"
  ],
  "businessId": "63b7ec34ea409a9a8bd2a4ff"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!