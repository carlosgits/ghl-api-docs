# Update SaaS subscription

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/generate-payment-link-deprecated

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_saas_generate-payment-link-deprecated_screenshot.png

---

SaasSaasUpdate SaaS subscription
Update SaaS subscription
PUT
 https://services.leadconnectorhq.com/saas-api/public-api/update-saas-subscription/:locationId
DEPRECATED
This endpoint has been deprecated and may be replaced or removed in future versions of the API.
Update SaaS subscription for given locationId and customerId
Requirements
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Agency Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-04-15]
API Version
PATH PARAMETERS
locationId
string
REQUIRED
Location ID to update subscription for
Example: AUKAtFVo0lWezBsBQ3FE
APPLICATION/JSON
BODY
REQUIRED
subscriptionId
string
REQUIRED
Subscription ID
Example:sub_1QDPY5FpU9DlKp7RQ8BXfywx
customerId
string
REQUIRED
Customer ID
Example:cus_1QDPY5FpU9DlKp7RQ8BXfywx
companyId
string
REQUIRED
Company ID
Example:companyId1
Responses
200
400
401
404
500
SaaS subscription updated successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
string
string























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
curl -L -X PUT 'https://services.leadconnectorhq.com/saas-api/public-api/update-saas-subscription/:locationId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "subscriptionId": "sub_1QDPY5FpU9DlKp7RQ8BXfywx",
  "customerId": "cus_1QDPY5FpU9DlKp7RQ8BXfywx",
  "companyId": "companyId1"
}'
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
2021-04-15
Body
 REQUIRED
{
  "subscriptionId": "sub_1QDPY5FpU9DlKp7RQ8BXfywx",
  "customerId": "cus_1QDPY5FpU9DlKp7RQ8BXfywx",
  "companyId": "companyId1"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!