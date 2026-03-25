# Update Contacts Tags

Source: https://marketplace.gohighlevel.com/docs/ghl/contacts/create-association

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_contacts_create-association_screenshot.png

---

ContactsBulkUpdate Contacts Tags
Update Contacts Tags
POST
 https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type
Allows you to update tags to multiple contacts at once, you can add or remove tags from the contacts
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
contacts
string[]
REQUIRED
list of contact ids to be processed
Example:["qFSqySFkVvNzOSqgGqFi","abcdef","qFSqySFkVvNzOSqgGqFi","3ualbhnV7j3n3a9r2moD"]
tags
string[]
REQUIRED
list of tags to be added or removed
Example:["tag-1","tag-2"]
locationId
string
REQUIRED
location id from where the bulk request is executed
Example:asdrwHvLUxlfw5SqKVCN
removeAllTags
boolean
Option to implement remove all tags. if true, all tags will be removed from the contacts. Can only be used with remove type.
Example:false
Responses
201
400
422
Successful response
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
succeded
boolean
REQUIRED
Indicates if the operation was successful
Example:true
errorCount
number
REQUIRED
Number of errors encountered during the operation
Example:0
responses
string[]
REQUIRED
Responses for each contact processed
Example:[{"contactId":"qFSqySFkVvNzOSqgGqFi","message":"Tags updated","type":"success","oldTags":["tag-1","tag-2"],"tagsAdded":[],"tagsRemoved":[]},{"contactId":"abcdef","message":"contact id is not a valid firebase id","type":"error"},{"contactId":"qFSqySFkVvNzOSqgGqFi","message":"contact is deleted","type":"error"},{"contactId":"3ualbhnV7j3n3a9r2moD","message":"contact does not belong to location","type":"error"}]











































Share your feedback
★
★
★
★
★
CURL
NODEJS
PYTHON
PHP
JAVA
GO
RUBY
POWERSHELL
CURL
curl -L 'https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-d '{
  "contacts": [
    "qFSqySFkVvNzOSqgGqFi",
    "abcdef",
    "qFSqySFkVvNzOSqgGqFi",
    "3ualbhnV7j3n3a9r2moD"
  ],
  "tags": [
    "tag-1",
    "tag-2"
  ],
  "locationId": "asdrwHvLUxlfw5SqKVCN",
  "removeAllTags": "false"
}'
REQUEST
COLLAPSE ALL
Base URL
https://services.leadconnectorhq.com
Parameters
Version — header
REQUIRED
---
2021-07-28
Body
 REQUIRED
{
  "contacts": [
    "qFSqySFkVvNzOSqgGqFi",
    "abcdef",
    "qFSqySFkVvNzOSqgGqFi",
    "3ualbhnV7j3n3a9r2moD"
  ],
  "tags": [
    "tag-1",
    "tag-2"
  ],
  "locationId": "asdrwHvLUxlfw5SqKVCN",
  "removeAllTags": "false"
}
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!