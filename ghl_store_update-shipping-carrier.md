# Update Shipping Carrier

Source: https://marketplace.gohighlevel.com/docs/ghl/store/update-shipping-carrier

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_store_update-shipping-carrier_screenshot.png

---

StoreShipping CarrierUpdate Shipping Carrier
Update Shipping Carrier
PUT
 https://services.leadconnectorhq.com/store/shipping-carrier/:shippingCarrierId
The "update Shipping Carrier" API allows update a shipping carrier to the system.
Requirements
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
PATH PARAMETERS
shippingCarrierId
string
REQUIRED
ID of the shipping carrier that needs to be returned
Example: 6578278e879ad2646715ba9c
APPLICATION/JSON
BODY
REQUIRED
altId
string
Location Id or Agency Id
Example:6578278e879ad2646715ba9c
altType
string
Possible values: [location]
name
string
Name of the shipping carrier
Example:FedEx
callbackUrl
string
The URL endpoint that GHL needs to retrieve shipping rates. This must be a public URL.
Example:https://example.com/get-shipping-rates
services
object[]
allowsMultipleServiceSelection
boolean
The seller can choose multiple services while creating shipping rates if this is true.
Example:true
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
curl -L -X PUT 'https://services.leadconnectorhq.com/store/shipping-carrier/:shippingCarrierId' \
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
Parameters
shippingCarrierId — path
REQUIRED
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