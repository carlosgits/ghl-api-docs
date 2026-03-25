# List Shipping Rates

Source: https://marketplace.gohighlevel.com/docs/ghl/store/list-shipping-rates

Screenshot: images/ghl_store_list-shipping-rates_screenshot.png

---

StoreShipping Zone RatesList Shipping Rates
List Shipping Rates
GET
 https://services.leadconnectorhq.com/store/shipping-zone/:shippingZoneId/shipping-rate
The "List Shipping Rate" API allows to retrieve a list of shipping rate.
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
QUERY PARAMETERS
altId
string
REQUIRED
Location Id or Agency Id
Example: 6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
limit
number
The maximum number of items to be included in a single page of results
Default value:0
Example: 20
offset
number
The starting index of the page, indicating the position from which the results should be retrieved.
Default value:0
Example: 0
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
total
number
REQUIRED
Total number of items
Example:20
data
object[]
REQUIRED













































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
curl -L 'https://services.leadconnectorhq.com/store/shipping-zone/:shippingZoneId/shipping-rate' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
shippingZoneId — path
REQUIRED
altId — query
REQUIRED
altType — query
REQUIRED
---
location
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!