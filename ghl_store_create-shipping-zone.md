# Create Shipping Zone

Source: https://marketplace.gohighlevel.com/docs/ghl/store/create-shipping-zone

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_store_create-shipping-zone_screenshot.png

---

StoreShipping ZoneCreate Shipping Zone
Create Shipping Zone
POST
 https://services.leadconnectorhq.com/store/shipping-zone
The "Create Shipping Zone" API allows adding a new shipping zone.
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
Name of the shipping zone
Example:North zone
countries
object[]
REQUIRED
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
curl -L 'https://services.leadconnectorhq.com/store/shipping-zone' \
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