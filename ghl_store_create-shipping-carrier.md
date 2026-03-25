# Create Shipping Carrier

Source: https://marketplace.gohighlevel.com/docs/ghl/store/create-shipping-carrier

Screenshot: images/ghl_store_create-shipping-carrier_screenshot.png

---

StoreShipping CarrierCreate Shipping Carrier
Create Shipping Carrier
POST
 https://services.leadconnectorhq.com/store/shipping-carrier
The "Create Shipping Carrier" API allows adding a new shipping carrier.
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
name
string
REQUIRED
Name of the shipping carrier
Example:FedEx
callbackUrl
string
REQUIRED
The URL endpoint that GHL needs to retrieve shipping rates. This must be a public URL.
Example:https://example.com/get-shipping-rates
services
object[]
allowsMultipleServiceSelection
boolean
The seller can choose multiple services while creating shipping rates if this is true.
Example:true
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
curl -L 'https://services.leadconnectorhq.com/store/shipping-carrier' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "name": "FedEx",
  "callbackUrl": "https://example.com/get-shipping-rates",
  "services": [
    {
      "name": "Priority Mail Express International",
      "value": "PriorityMailExpressInternational"
    }
  ],
  "allowsMultipleServiceSelection": true
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
  "name": "FedEx",
  "callbackUrl": "https://example.com/get-shipping-rates",
  "services": [
    {
      "name": "Priority Mail Express International",
      "value": "PriorityMailExpressInternational"
    }
  ],
  "allowsMultipleServiceSelection": true
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!