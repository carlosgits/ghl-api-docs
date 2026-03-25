# Update Rebilling

Source: https://marketplace.gohighlevel.com/docs/ghl/saas/update-rebilling-deprecated

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_saas_update-rebilling-deprecated_screenshot.png

---

SaasSaasUpdate Rebilling
Update Rebilling
POST
 https://services.leadconnectorhq.com/saas-api/public-api/update-rebilling/:companyId
DEPRECATED
This endpoint has been deprecated and may be replaced or removed in future versions of the API.
Bulk update rebilling for given locationIds
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
companyId
string
REQUIRED
Company ID to update rebilling for
Example: 5DP4iH6HLkQsiKESj6rh
APPLICATION/JSON
BODY
REQUIRED
product
string
REQUIRED
The product to update rebilling for
Possible values: [contentAI, workflow_premium_actions, workflow_ai, conversationAI, EmailNotification, whatsApp, reviewsAI, VERIFIED_CALLER_ID, WALLET_SALES_TAX, NOTIFICATION_SMS, EmailSmtp, EmailVerification, autoCompleteAddress, funnelAI, domainPurchase, Phone, Email]
Example:contentAI
locationIds
string[]
REQUIRED
Array of location IDs to update rebilling for
Example:["zzyG7A4x6bRJl5SlhQhH","Vygq7VgXCDfg3xnl8TBR"]
config
object
REQUIRED
Responses
200
400
401
404
500
Rebilling updated successfully
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
success
boolean
REQUIRED
Indicates if the rebilling update was successful
Example:true

























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
curl -L 'https://services.leadconnectorhq.com/saas-api/public-api/update-rebilling/:companyId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "product": "contentAI",
  "locationIds": [
    "zzyG7A4x6bRJl5SlhQhH",
    "Vygq7VgXCDfg3xnl8TBR"
  ],
  "config": {
    "optIn": true,
    "enabled": true,
    "markup": 5
  }
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
companyId — path
REQUIRED
Version — header
REQUIRED
---
2021-04-15
Body
 REQUIRED
{
  "product": "contentAI",
  "locationIds": [
    "zzyG7A4x6bRJl5SlhQhH",
    "Vygq7VgXCDfg3xnl8TBR"
  ],
  "config": {
    "optIn": true,
    "enabled": true,
    "markup": 5
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!