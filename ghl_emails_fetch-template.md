# Fetch email templates

Source: https://marketplace.gohighlevel.com/docs/ghl/emails/fetch-template

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_emails_fetch-template_screenshot.png

---

EmailTemplatesFetch email templates
Fetch email templates
GET
 https://services.leadconnectorhq.com/emails/builder
Fetch email templates by location id
Requirements
Scope(s)
emails/builder.readonly
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
Example: 2021-07-28
QUERY PARAMETERS
locationId
string
REQUIRED
Example: ve9EPM428h8vShlRW1KT
limit
number
Default value:10
offset
number
Default value:0
search
string
Default value:
sortByDate
string
Default value:desc
archived
boolean
Default value:false
builderVersion
string
Possible values: [1, 2]
Default value:2
name
string
Default value:
parentId
string
Default value:
originId
string
Example: ve9EPM428h8vShlRW1KT
templatesOnly
boolean
Default value:false
Responses
200
400
401
404
422
Success
APPLICATION/JSON
Schema
Example (auto)
SCHEMA
name
string
template name
Example:New Template
updatedBy
string
updated by
Example:John Doe
isPlainText
boolean
plain text based template
Example:false
lastUpdated
string
last updated
Example:2024-11-12T12:34:36.070Z
dateAdded
string
date added
Example:2024-11-12T12:34:36.070Z
previewUrl
string
preview url
Example:https://example.com
id
string
id
Example:67334b231f2fad724062f52b5
version
string
version
Example:1
templateType
string
type
Example:builder



























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
curl -L 'https://services.leadconnectorhq.com/emails/builder' \
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
Version — header
REQUIRED
---
2021-07-28
Show optional parameters
SEND API REQUEST
RESPONSE
CLEAR
Click the Send API Request button above and see the response here!