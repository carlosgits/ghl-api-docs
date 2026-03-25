# Update Shipping Zone

Source: https://marketplace.gohighlevel.com/docs/ghl/store/update-shipping-zone

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_store_update-shipping-zone_screenshot.png

---

StoreShipping ZoneUpdate Shipping Zone
Update Shipping Zone
PUT
 https://services.leadconnectorhq.com/store/shipping-zone/:shippingZoneId
The "update Shipping Zone" API allows update a shipping zone to the system.
Requirements
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
PATH PARAMETERS
shippingZoneId
string
REQUIRED
ID of the item that needs to be returned
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
Name of the shipping zone
Example:North zone
countries
object[]
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
curl -L -X PUT 'https://services.leadconnectorhq.com/store/shipping-zone/:shippingZoneId' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "name": "North zone",
  "countries": [
    {
      "code": "US",
      "states": [
        {
          "code": "VA"
        }
      ]
    }
  ]
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
shippingZoneId — path
REQUIRED
Body
 REQUIRED
{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "name": "North zone",
  "countries": [
    {
      "code": "US",
      "states": [
        {
          "code": "VA"
        }
      ]
    }
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!