# Update Object Schema By Key / Id

Source: https://marketplace.gohighlevel.com/docs/ghl/objects/update-custom-object

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_objects_update-custom-object_screenshot.png

---

ObjectsObject SchemaUpdate Object Schema By Key / Id
Update Object Schema By Key / Id
PUT
 https://services.leadconnectorhq.com/objects/:key
Update Custom Object Schema or standard object's like contact, opportunity, business searchable fields. To understand objects and records, please have a look at the documentation here : https://doc.clickup.com/8631005/d/h/87cpx-277156/93bf0c2e23177b0
Requirements
Scope(s)
objects/schema.write
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
PATH PARAMETERS
key
string
REQUIRED
key of the custom or standard object. For custom objects, the key must include the prefix “custom_objects.”. This key can be found on the Object Details page under Settings in the UI.
Example: custom_objects.pet
APPLICATION/JSON
BODY
REQUIRED
labels
object
description
string
NULLABLE
Pet Object`s description
Example:These are non vaccinated pets
locationId
string
REQUIRED
location id
Example:632c34b4c9b7da3358ac9891
searchableProperties
string[]
REQUIRED
Searchable Fields: Provide the field key of your object that you want to search on, using the format (custom_object.<object_name>.<field_key>).
Example:["custom_objects.mad.mad","custom_objects.mad.record_1","custom_objects.mad.nn"]
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
curl -L -X PUT 'https://services.leadconnectorhq.com/objects/:key' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "labels": {
    "singular": "Pet",
    "plural": "Pets"
  },
  "description": "These are non vaccinated pets",
  "locationId": "632c34b4c9b7da3358ac9891",
  "searchableProperties": [
    "custom_objects.mad.mad",
    "custom_objects.mad.record_1",
    "custom_objects.mad.nn"
  ]
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Auth
Bearer Token
Parameters
key — path
REQUIRED
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
  "description": "These are non vaccinated pets",
  "locationId": "632c34b4c9b7da3358ac9891",
  "searchableProperties": [
    "custom_objects.mad.mad",
    "custom_objects.mad.record_1",
    "custom_objects.mad.nn"
  ]
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!