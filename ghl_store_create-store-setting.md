# Create/Update Store Settings

Source: https://marketplace.gohighlevel.com/docs/ghl/store/create-store-setting

Screenshot: images/ghl_store_create-store-setting_screenshot.png

---

StoreStore SettingCreate/Update Store Settings
Create/Update Store Settings
POST
 https://services.leadconnectorhq.com/store/store-setting
Create or update store settings by altId and altType.
Requirements
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
APPLICATION/JSON
BODY
REQUIRED
altId
string
REQUIRED
Location Id or Agency Id
Example:6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
shippingOrigin
object
storeOrderNotification
object
storeOrderFulfillmentNotification
object
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
status
boolean
REQUIRED
Status of api action
Example:true
message
string
Success message
Example:Successfully created
data
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
curl -L 'https://services.leadconnectorhq.com/store/store-setting' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "shippingOrigin": {
    "name": "ABC Store",
    "country": "US",
    "state": "VA",
    "city": "Tokyo",
    "street1": "Street 1",
    "street2": "Street 2",
    "zip": "674561",
    "phone": "+1-214-559-6993",
    "email": "john@deo.com"
  },
  "storeOrderNotification": {
    "enabled": true,
    "subject": "Your order is placed !",
    "emailTemplateId": "6788d542f0462ffd6bc29bb9",
    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"
  },
  "storeOrderFulfillmentNotification": {
    "enabled": true,
    "subject": "Order fulfilled",
    "emailTemplateId": "6788d542f0462ffd6bc29bb9",
    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"
  }
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Body
 REQUIRED
{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "shippingOrigin": {
    "name": "ABC Store",
    "country": "US",
    "state": "VA",
    "city": "Tokyo",
    "street1": "Street 1",
    "street2": "Street 2",
    "zip": "674561",
    "phone": "+1-214-559-6993",
    "email": "john@deo.com"
  },
  "storeOrderNotification": {
    "enabled": true,
    "subject": "Your order is placed !",
    "emailTemplateId": "6788d542f0462ffd6bc29bb9",
    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"
  },
  "storeOrderFulfillmentNotification": {
    "enabled": true,
    "subject": "Order fulfilled",
    "emailTemplateId": "6788d542f0462ffd6bc29bb9",
    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!