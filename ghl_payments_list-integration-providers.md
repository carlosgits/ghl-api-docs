# List White-label Integration Providers

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/list-integration-providers

Screenshot: images/ghl_payments_list-integration-providers_screenshot.png

---

PaymentsIntegrationsList White-label Integration Providers
List White-label Integration Providers
GET
 https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel
The "List White-label Integration Providers" API allows to retrieve a paginated list of integration providers. Customize your results by filtering whitelabel integration providers(which are built directly on top of Authorize.net or NMI) based on name or paginate through the list using the provided query parameters. This endpoint provides a straightforward way to explore and retrieve integration provider information.
Requirements
Scope(s)
payments/integration.readonly
Auth Method(s)
OAuth Access Token
Private Integration Token
Token Type(s)
Sub-Account Token
Request
HEADER PARAMETERS
Version
string
REQUIRED
Possible values: [2021-07-28]
API Version
QUERY PARAMETERS
altId
string
REQUIRED
location Id / company Id based on altType
Example: 6578278e879ad2646715ba9c
altType
string
REQUIRED
Possible values: [location]
Alt Type
Example: location
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
providers
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
curl -L 'https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
altId — query
REQUIRED
altType — query
REQUIRED
---
location
Version — header
REQUIRED
---
2021-07-28
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!