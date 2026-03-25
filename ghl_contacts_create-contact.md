# Create Contact

Source: https://marketplace.gohighlevel.com/docs/ghl/contacts/create-contact

Screenshot: images/ghl_contacts_create-contact_screenshot.png

---

ContactsContactsCreate Contact
Create Contact
POST
 https://services.leadconnectorhq.com/contacts/
Please find the list of acceptable values for the country field here
Requirements
Scope(s)
contacts.write
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
firstName
string
NULLABLE
Example:Rosan
lastName
string
NULLABLE
Example:Deo
name
string
NULLABLE
Example:Rosan Deo
email
string
NULLABLE
Example:rosan@deos.com
locationId
string
REQUIRED
Example:ve9EPM428h8vShlRW1KT
gender
string
Example:male
phone
string
NULLABLE
Example:+1 888-888-8888
address1
string
NULLABLE
Example:3535 1st St N
city
string
NULLABLE
Example:Dolomite
state
string
NULLABLE
Example:AL
postalCode
string
Example:35061
website
string
NULLABLE
Example:https://www.tesla.com
timezone
string
NULLABLE
Example:America/Chihuahua
dnd
boolean
Example:true
dndSettings
object
inboundDndSettings
object
tags
string[]
Example:["nisi sint commodo amet","consequat"]
customFields
object[]
source
string
Example:public api
dateOfBirth
object
NULLABLE
The birth date of the contact. Supported formats: YYYY/MM/DD, MM/DD/YYYY, YYYY-MM-DD, MM-DD-YYYY, YYYY.MM.DD, MM.DD.YYYY, YYYY_MM_DD, MM_DD_YYYY
Example:1990-09-25
country
string
Example:US
companyName
string
NULLABLE
Example:DGS VolMAX
assignedTo
string
User's Id
Example:y0BeYjuRIlDwsDcOHOJo
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
contact
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
curl -L 'https://services.leadconnectorhq.com/contacts/' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
--data-raw '{
  "firstName": "Rosan",
  "lastName": "Deo",
  "name": "Rosan Deo",
  "email": "rosan@deos.com",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "gender": "male",
  "phone": "+1 888-888-8888",
  "address1": "3535 1st St N",
  "city": "Dolomite",
  "state": "AL",
  "postalCode": "35061",
  "website": "https://www.tesla.com",
  "timezone": "America/Chihuahua",
  "dnd": true,
  "dndSettings": {
    "Call": {
      "status": "active",
      "message": "string",
      "code": "string"
    },
    "Email": {
      "status": "active",
      "message": "string",
      "code": "string"
    },
    "SMS": {
      "status": "active",
      "message": "string",
      "code": "string"
    },
    "WhatsApp": {
      "status": "active",
      "message": "string",
      "code": "string"
    },
    "GMB": {
      "status": "active",
      "message": "string",
      "code": "string"
    },
    "FB": {
      "status": "active",
      "message": "string",
      "code": "string"
    }
  },
  "inboundDndSettings": {
    "all": {
      "status": "active",
      "message": "string"
    }
  },
  "tags": [
    "nisi sint commodo amet",
    "consequat"
  ],
  "customFields": [
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": "My Text"
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": "My Text"
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": "My Selected Option"
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": "My Selected Option"
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": 100
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": 100.5
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": [
        "test",
        "test2"
      ]
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": [
        "test",
        "test2"
      ]
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": {
        "f31175d4-2b06-4fc6-b7bc-74cd814c68cb": {
          "meta": {
            "fieldname": "1HeGizb13P0odwgOgKSs",
            "originalname": "IMG_20231215_164412935.jpg",
            "encoding": "7bit",
            "mimetype": "image/jpeg",
            "size": 1786611,
            "uuid": "f31175d4-2b06-4fc6-b7bc-74cd814c68cb"
          },
          "url": "https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ",
          "documentId": "w2M9qTZ0ZJz8rGt02jdJ"
        }
      }
    }
  ],
  "source": "public api",
  "dateOfBirth": "1990-09-25",
  "country": "US",
  "companyName": "DGS VolMAX",
  "assignedTo": "y0BeYjuRIlDwsDcOHOJo"
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
  "firstName": "Rosan",
  "lastName": "Deo",
  "name": "Rosan Deo",
  "email": "rosan@deos.com",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "gender": "male",
  "phone": "+1 888-888-8888",
  "address1": "3535 1st St N",
  "city": "Dolomite",
  "state": "AL",
  "postalCode": "35061",
  "website": "https://www.tesla.com",
  "timezone": "America/Chihuahua",
  "dnd": true,
  "dndSettings": {
    "Call": {
      "status": "active",
      "message": "string",
      "code": "string"
    },
    "Email": {
      "status": "active",
      "message": "string",
      "code": "string"
    },
    "SMS": {
      "status": "active",
      "message": "string",
      "code": "string"
    },
    "WhatsApp": {
      "status": "active",
      "message": "string",
      "code": "string"
    },
    "GMB": {
      "status": "active",
      "message": "string",
      "code": "string"
    },
    "FB": {
      "status": "active",
      "message": "string",
      "code": "string"
    }
  },
  "inboundDndSettings": {
    "all": {
      "status": "active",
      "message": "string"
    }
  },
  "tags": [
    "nisi sint commodo amet",
    "consequat"
  ],
  "customFields": [
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": "My Text"
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": "My Text"
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": "My Selected Option"
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": "My Selected Option"
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": 100
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": 100.5
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": [
        "test",
        "test2"
      ]
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": [
        "test",
        "test2"
      ]
    },
    {
      "id": "6dvNaf7VhkQ9snc5vnjJ",
      "key": "my_custom_field",
      "field_value": {
        "f31175d4-2b06-4fc6-b7bc-74cd814c68cb": {
          "meta": {
            "fieldname": "1HeGizb13P0odwgOgKSs",
            "originalname": "IMG_20231215_164412935.jpg",
            "encoding": "7bit",
            "mimetype": "image/jpeg",
            "size": 1786611,
            "uuid": "f31175d4-2b06-4fc6-b7bc-74cd814c68cb"
          },
          "url": "https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ",
          "documentId": "w2M9qTZ0ZJz8rGt02jdJ"
        }
      }
    }
  ],
  "source": "public api",
  "dateOfBirth": "1990-09-25",
  "country": "US",
  "companyName": "DGS VolMAX",
  "assignedTo": "y0BeYjuRIlDwsDcOHOJo"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!