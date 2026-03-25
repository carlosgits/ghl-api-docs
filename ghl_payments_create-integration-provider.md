# Create White-label Integration Provider

Source: https://marketplace.gohighlevel.com/docs/ghl/payments/create-integration-provider

Screenshot: images/ghl_payments_create-integration-provider_screenshot.png

---

PaymentsIntegrationsCreate White-label Integration Provider
Create White-label Integration Provider
POST
 https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel
The "Create White-label Integration Provider" API allows adding a new payment provider integration to the system which is built on top of Authorize.net or NMI. Use this endpoint to create a integration provider with the specified details. Ensure that the required information is provided in the request payload. This endpoint can be only invoked using marketplace-app token
Requirements
Scope(s)
payments/integration.write
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
APPLICATION/JSON
BODY
REQUIRED
altId
string
REQUIRED
location Id / company Id based on altType
Example:6578278e879ad2646715ba9c
altType
string
REQUIRED
Alt Type
Possible values: [location]
Example:location
uniqueName
string
REQUIRED
A unique name given to the integration provider, uniqueName must start and end with a character. Only lowercase characters and hyphens (-) are supported
Example:easy-direct
title
string
REQUIRED
The title or name of the integration provider.
Example:Title
provider
string
REQUIRED
The type of payment provider associated with the integration provider.
Possible values: [authorize-net, nmi]
Example:{"AUTHORIZE_NET":"authorize-net","NMI":"nmi"}
description
string
REQUIRED
A brief description providing additional information about the integration provider.
Example:Description
imageUrl
string
REQUIRED
The URL to an image representing the integration provider. The imageUrl should start with "https://" and ensure that this URL is publicly accessible.
Example:https://example.com/image.jpg
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
_id
string
REQUIRED
The unique identifier of the integration provider.
Example:65cb47dda50f4f13ced4b870
altId
string
REQUIRED
The altId / locationId of the integration provider.
Example:Z4Bxl8J4SaPEPLq9IQ8g
altType
string
REQUIRED
The altType of the integration provider.
Example:location
title
string
REQUIRED
The title or name of the integration provider.
Example:Example
route
string
REQUIRED
The route name associated with the integration provider.
Example:epd
provider
string
REQUIRED
The payment provider associated with the integration provider.
Example:nmi
description
string
REQUIRED
A brief description providing additional information about the integration provider.
Example:Lorem
imageUrl
string
REQUIRED
The URL to an image representing the integration provider.
Example:https://example.com/assets/pmd/img/payments/nmi-logo.webp
createdAt
date-time
REQUIRED
The timestamp when the integration provider was created.
Example:2024-02-13T10:43:41.026Z
updatedAt
date-time
REQUIRED
The timestamp when the integration provider was last updated.
Example:2024-02-13T10:43:41.026Z




























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
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "uniqueName": "easy-direct",
  "title": "Title",
  "provider": {
    "AUTHORIZE_NET": "authorize-net",
    "NMI": "nmi"
  },
  "description": "Description",
  "imageUrl": "https://example.com/image.jpg"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "uniqueName": "easy-direct",
  "title": "Title",
  "provider": {
    "AUTHORIZE_NET": "authorize-net",
    "NMI": "nmi"
  },
  "description": "Description",
  "imageUrl": "https://example.com/image.jpg"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!