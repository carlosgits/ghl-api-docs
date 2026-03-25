# Create Custom Object

Source: https://marketplace.gohighlevel.com/docs/ghl/objects/create-custom-object-schema

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_objects_create-custom-object-schema_screenshot.png

---

ObjectsObject SchemaCreate Custom Object
Create Custom Object
POST
 https://services.leadconnectorhq.com/objects/
Allows you to create a custom object schema. To understand objects and records, please have a look at the documentation here : https://doc.clickup.com/8631005/d/h/87cpx-277156/93bf0c2e23177b0
Requirements
Scope(s)
objects/schema.write
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
Possible values: [2021-07-28]
API Version
APPLICATION/JSON
BODY
REQUIRED
labels
object
key
string
REQUIRED
key that would be used to refer the Custom Object internally (lowercase + underscore_separated). 'custom_objects.' would be added as prefix by default
Example:custom_objects.pet
description
string
Pet Object`s description
Example:These are non vaccinated pets
locationId
string
REQUIRED
Location Id
Example:ve9EPM428h8vShlRW1KT
primaryDisplayPropertyDetails
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
object
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
curl -L 'https://services.leadconnectorhq.com/objects/' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "labels": {
    "singular": "Pet",
    "plural": "Pets"
  },
  "key": "custom_objects.pet",
  "description": "These are non vaccinated pets",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "primaryDisplayPropertyDetails": {
    "key": "custom_objects.pet.name",
    "name": "Pet name",
    "dataType": "TEXT"
  }
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
  "labels": {
    "singular": "Pet",
    "plural": "Pets"
  },
  "key": "custom_objects.pet",
  "description": "These are non vaccinated pets",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "primaryDisplayPropertyDetails": {
    "key": "custom_objects.pet.name",
    "name": "Pet name",
    "dataType": "TEXT"
  }
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!