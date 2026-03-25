# Fetch List of Funnels

Source: https://marketplace.gohighlevel.com/docs/ghl/funnels/get-funnels

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_funnels_get-funnels_screenshot.png

---

FunnelsFunnelFetch List of Funnels
Fetch List of Funnels
GET
 https://services.leadconnectorhq.com/funnels/funnel/list
Retrieves a list of all funnels based on the given query parameters.
Requirements
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
QUERY PARAMETERS
locationId
string
REQUIRED
type
string
category
string
offset
string
limit
string
parentId
string
name
string
Responses
200
Successful response - List of funnels returned
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
funnels
object
REQUIRED
Example:{"_id":"SkIDfu0S4m3NYQyvWHC6","dateAdded":"2024-04-29T15:00:05.681Z","dateUpdated":"2024-04-29T15:00:28.465Z","deleted":false,"domainId":"","locationId":"ojQjykmwNIU88vfsfzvH","name":"Chaitanya Copy","orderFormVersion":2,"originId":"hAmyh7jrJH5FfEEKAJ9z","steps":[{"id":"f5d178c0-8bbb-4cd4-927c-691c68a62c59","name":"Step 1","originId":"80b2f227-5bc8-4ca5-980d-817745ea4e8b","pages":["2IhBmBcQRx9JXV1JZsRt"],"products":[],"sequence":1,"type":"optin_funnel_page","url":"/newtestifypath"}],"type":"funnel","updatedAt":"2024-04-29T15:00:34.233Z","faviconUrl":"","globalSectionVersion":1,"globalSectionsPath":"funnel/SkIDfu0S4m3NYQyvWHC6/global-sections-1","globalSectionsUrl":"https://firebasestorage.googleapis.com/v0/b/highlevel-staging.appspot.com/o/funnel%2FSkIDfu0S4m3NYQyvWHC6%2Fglobal-sections-1?alt=media&token=9cc5c211-093b-4751-aeba-19282ac92955","isStoreActive":false,"trackingCodeBody":"","trackingCodeHead":"","url":"/chaitanya"}
count
number
REQUIRED
Example:24
traceId
string
REQUIRED
Example:03774d31-a57e-4b4f-95c7-315ce61969f1







































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
curl -L 'https://services.leadconnectorhq.com/funnels/funnel/list' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
locationId — query
REQUIRED
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!